from flask import Flask, render_template, redirect, request

from Dobot import Dobot
from pdf import PDF
import asyncio
from datetime import datetime
from sqlalchemy import create_engine, delete
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.report import Report
from models.cycle import Cycle
from threading import Thread
import threading
from time import sleep
import json

import plotly
import plotly.graph_objs as go

IP = "10.128.66.31"

PDF_WIDTH = 210
PDF_HEIGHT = 297
process = None

app = Flask(__name__)
header = []
engine = create_engine("sqlite+pysqlite:///reports.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

# session.query(Report).delete()
# session.query(Cycle).delete()
# session.commit()

# cycle = Cycle(magnetic_field=100, speed=20, cycle_mass=31, cycle_duration=150, report_id=1)
# cycle2 = Cycle(magnetic_field=200, speed=12, cycle_mass=20, cycle_duration=150, report_id=1)
# cycle3 = Cycle(magnetic_field=300, speed=24, cycle_mass=18, cycle_duration=150, report_id=1)
# cycle4 = Cycle(magnetic_field=400, speed=55, cycle_mass=19, cycle_duration=150, report_id=1)
# cycle5 = Cycle(magnetic_field=500, speed=4, cycle_mass=5, cycle_duration=150, report_id=1)
# cycle6 = Cycle(magnetic_field=600, speed=30, cycle_mass=1, cycle_duration=150, report_id=1)
# cycle7 = Cycle(magnetic_field=100, speed=20, cycle_mass=31, cycle_duration=150, report_id=2)

# session.add(cycle)
# session.add(cycle2)
# session.add(cycle3)
# session.add(cycle4)
# session.add(cycle5)
# session.add(cycle6)
# session.add(cycle7)

# session.commit()


@app.route('/')
def index():
    return render_template('about.html')


@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/report')
def report():
    return render_template('report.html')


def routine():
    arm = Dobot(225, 3, 140, 0)
    arm.moveHome()
    arm.pickToggle()

    # #bandeja 1
    arm.moveArmXY(174, 222, 77, 51)

    arm.moveArmXY(265, 175, -11, 32)
    arm.moveArmXY(64, 169, -11, 67)
    arm.moveArmXY(276, 202, -11, 35)
    arm.moveArmXY(66, 195, -11, 69)
    arm.moveArmXY(268, 241, -11, 41)
    arm.moveArmXY(64, 271, -11, 75)
    arm.moveArmXY(260, 266, -11, 44)

    arm.moveArmXY(174, 222, 77, 51)

    # #bandeja 2
    arm.moveHome()
    arm.moveArmXY(325, -36, -8, -7)
    arm.rotateTool(-90)
    arm.moveArmXY(181, -18, -8, -6)
    arm.moveArmXY(313, 52, -8, 8)
    arm.rotateTool(-80)
    arm.moveArmXY(177, 43, -8, 12)
    arm.moveHome()

    # #bandeja 3
    arm.moveArmXY(185, -229, 77, -51)
    arm.moveArmXY(185, -229, -10, -51)
    sleep(2)


@app.route('/on')
async def control_on():
    global process
    try:
        # request.args.get('http://${IP}/on')
        process = Thread(target=routine, args=())
        process.start()
        process.join()
        return redirect('/')
    except Exception as e:
        print("error")
        return e


@app.route('/stop')
async def control_stop():
    try:
        # request.args.get('http://${IP}/stop')
        # arm = Dobot(225,3,140,0)
        return redirect('/')
    except Exception as e:
        print("error")
        return e


@app.route('/off')
async def control_off():
    try:
        # await request.args.get('http://${IP}/off')
        return redirect('/')
    except Exception as e:
        print("error")
        return e


@app.route('/post', methods=["POST"])
async def postForm():
    print(request.form)
    header.clear()
    for i in request.form:
        header.append((i.capitalize(), request.form[i]))

    r1 = Report(project=request.form['projeto'], client=request.form['cliente'], sample=request.form['amostra'], operator=request.form['operador'],
                cycle_number=request.form['ciclos'], liquid_initial_mass=request.form['peso solido'], solid_initial_mass=request.form['peso solido'])

    session.add(r1)
    session.commit()
    return render_template('index.html', project=request.form['projeto'], client=request.form['cliente'], sample=request.form['amostra'])


@app.route('/pdf')
async def generatePDF():
    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.header()
    a = [10, 10]
    side = True
    for i in header:
        pdf.element(i[0] + ': ' + i[1], a, side)
        a[1] += 5 if (not side) else 0
        side = not side
    pdf.generate(datetime.now().strftime("%d-%m-%Y-%H%M%S"))
    return render_template("index.html")


@app.route('/dashboard')
def dashboard():
    query = session.query(Report).all()

    label = []
    data = []
    for report in query:
        for cycle in report.children:
            label.append(cycle.id)
            data.append(cycle.cycle_mass)

    json_string = json.dumps([{'label': label, 'data': data}
                             for label, data in zip(label, data)], indent=1)
    json_object = json.loads(json_string)
    print(json_object)

    return render_template("dashboard.html", data=json_object, title=report.project)


app.run(host='0.0.0.0', port=3000, debug=True)
