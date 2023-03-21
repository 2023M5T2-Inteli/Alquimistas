from flask import Flask, render_template, redirect, request

from Dobot import Dobot
import asyncio
from flask_sqlalchemy import SQLAlchemy
IP ="10.128.66.31"

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
    return render_template('index.html')

@app.route('/report')
def report():
    return render_template('report.html')


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

    return redirect('/')

@app.route('/on')
async def control_on():
    try:
        request.args.get('http://${IP}/on')
        await routine()
        return redirect('/')
    except Exception as e:
        print("error")
        return e
    
@app.route('/stop')
async def control_stop():
    try:
        request.args.get('http://${IP}/stop')
        return redirect('/')
    except  Exception as e:
        print("error")
        return e

@app.route('/off')
async def control_off():
    try:
        await request.args.get('http://${IP}/off')
        return redirect('/')
    except Exception as e:
        print("error")
        return e


app.run(host = '0.0.0.0', port=3000, debug=True)