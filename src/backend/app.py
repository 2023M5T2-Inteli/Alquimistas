from flask import Flask, render_template, redirect, request

from Dobot import Dobot
from pdf import PDF
import asyncio
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
IP ="10.128.66.31"

PDF_WIDTH = 210
PDF_HEIGHT = 297

header = []

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
db.init_app(app)


class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    produto = db.Column(db.String(100))
    amostra = db.Column(db.String(100))
    data = db.Column(db.Date)
    material = db.Column(db.String(100))
    massa = db.Column(db.Float)

@app.cli.command()
def createdb():
    db.create_all()

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