from flask import Flask, render_template, redirect, request

from Dobot import Dobot
from pdf import PDF
import asyncio
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.report import Report

IP ="10.128.66.31"

PDF_WIDTH = 210
PDF_HEIGHT = 297

app = Flask(__name__)
header = []
engine = create_engine("sqlite+pysqlite:///reports.db", echo=True)
Session = sessionmaker(bind = engine)
session = Session()

Base.metadata.create_all(engine)

@app.route('/')
def index():
    return render_template('report.html')

@app.route('/report')
def report():
    return render_template('index.html')


@app.route('/routine')
async def routine():
    arm = Dobot(225, 3, 140, 0)

    arm.moveHome()

    arm.pickToggle()
    arm.moveArmXY(189, 183, 151, 41)
    arm.drawLine(200, 183, -10, 41, -150)
    arm.rotateTool(360)
    arm.moveHome()
    arm.drawLine(302, 0, -10, 0, -100)
    arm.rotateTool(180)
    arm.moveHome()
    arm.moveArmXY(189, -183, 151, 41)
    arm.drawLine(200, -183, -10, 41, -150)
    arm.rotateTool(720)

@app.route('/on')
async def control_on():
    try:
        # request.args.get('http://${IP}/on')
        await routine()
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
    except  Exception as e:
        print("error")
        return e

@app.route('/off')
async def control_off():
    try:
        #await request.args.get('http://${IP}/off')
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

    r1 = Report(project=request.form['projeto'], client=request.form['cliente'], sample=request.form['amostra'], operator=request.form['operador'], cycles=request.form['ciclos'], liquid_initial_mass=request.form['peso solido'], solid_initial_mass=request.form['peso solido'])

    session.add(r1)
    session.commit()
    return render_template('index.html', project=request.form['projeto'], client=request.form['cliente'], sample=request.form['amostra'])

@app.route('/pdf')
async def generatePDF():
    pdf = PDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.header()
    a = [10,10]
    side = True
    for i in header:
        pdf.element(i[0] + ': ' + i[1], a, side)
        a[1] += 5 if(not side) else 0
        side = not side 
    pdf.generate(datetime.now().strftime("%d-%m-%Y-%H%M%S"))
    return redirect('/')


app.run(host = '0.0.0.0', port=3000, debug=True)