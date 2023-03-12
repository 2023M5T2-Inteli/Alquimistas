from flask import Flask, render_template, redirect
#import requests
from Dobot import Dobot
import asyncio
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

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
    return render_template('iniciate.html')

@app.route('/status')
def conection():
    return render_template('status.html')

@app.route('/routine')
async def routine():
    arm = Dobot(225, 3, 140, 0)

    arm.moveHome()

    arm.pickToggle()
    arm.moveArmXY(189, 183, 151, 41)
    arm.drawLine(200, 183, -10, 41, -150)
    arm.moveArmXY(189, 183, 151, 41)
    arm.moveHome()
    arm.drawLine(302, 0, -10, 0, -100)
    arm.rotateTool(90)
    arm.moveHome()
    arm.moveArmXY(128, -195, 14, 0)
    # arm.pickToggle()

    return render_template('index.html')

@app.route('/on')
async def control_on():
    try:
        response = await requests.get('http://10.128.64.164/ON')
        return render_template('end.html')
    except Exception as e:
        print(e)
        await routine()
        return render_template('end.html')
    
@app.route('/off')
async def control_off():
    try:
        response = await requests.get('http://10.128.64.164/OFF')
        return render_template('iniciate.html')
    except:
        return render_template('iniciate.html')
    
@app.route('/stop')
async def control_stop():
    try:
        response = await requests.get('http://10.128.64.164/STOP')
        return render_template('iniciate.html')
    except:
        return render_template('iniciate.html')

@app.route('/report')
def report():
    return render_template('report.html')
<<<<<<< HEAD
    
=======

<<<<<<< HEAD
@app.route('/end')
def end():
    return render_template('end.html')
=======
>>>>>>> dev

>>>>>>> dev
app.run(host = '0.0.0.0', port=3000, debug=True)