#Code written by - Eng. Mohammed Jassim 
# QMR-KWT telemetry data visualizer v0.1 2021
# Thie code will visualize the telemtry data received from the QMR-KWT using
# using flask server, bootstrap framework and data visualization scripts.

from flask import Flask, request, jsonify, render_template, Response, json, send_from_directory, redirect, url_for, session
from flask_cors import CORS
import os.path
import os
import csv

# Get the relative path to this app
FILE_PATH = os.path.dirname(os.path.realpath(__file__))

telemetryData = {}

# Create App
app = Flask(__name__, static_url_path='/static')
CORS(app, support_credentials=True)
app.secret_key = 'jhjhggsashju576'

def readTelemetry():
    with open('telemetry.csv', 'r') as data:
        i = 0    
        for line in csv.DictReader(data): 
            telemetryData[i] = line
            i = i + 1
        i = 0
    return telemetryData

@app.route('/')
def index():
    
    return render_template("index.html",telemetryData=readTelemetry())

@app.route('/charts')
def charts():
        
    return render_template("charts.html")

@app.route('/map')
def map():
        
    return render_template("map.html")
    
# * -------------------- RUN SERVER -------------------- *
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)



