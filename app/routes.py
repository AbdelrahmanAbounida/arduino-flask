from flask import render_template, session, Response
from flask_jsonpify import jsonpify
from app import app
import pandas as pd
import serial
import os


def arduino_sensor_event(df):
    ser = serial.Serial(port="/dev/ttyACM0", baudrate=9600,timeout=0.2)

    counter = 0
    while True:
        data = ser.readline()

        try:
            data = int(ser.readline().decode().strip())
        except:
            print("error")
            data = 1
        
        if data == 0:
            if counter == len(df)-1:
                counter = 0
            else:
                counter += 1

            yield df.iloc[counter:counter+1,:6].to_string(index=False)
        yield ""

@app.route('/')
def index():
    session['sensor_data_csv_file'] = os.path.join(app.config['UPLOAD_FOLDER'],'sensors.csv')
    data_file_path = session.get('sensor_data_csv_file', None)

    # taking data from arduino
    df = pd.read_csv(data_file_path)
    counter = 1
    # print(len(df))
    for i in arduino_sensor_event():
        if counter > len(df):
            counter = 1
        if int(i) == 0:
            current_df = df.iloc[0:counter,:]
            
            out_html_table = current_df.to_html()
            yield render_template('index.html',data=out_html_table)
            

    out_html_table = df.to_html()
    return render_template('index.html',data=out_html_table)


@app.route('/arduino')
def arduino():
    ser = serial.Serial(port='/dev/ttyACM0',baudrate=9600,timeout=0.2)
    data = ser.readline().decode().strip()
    print(ser.readline())
    print(data)
    # try:
    #     data = int(data)
    # except:
    #     data = 1
    # print(data)

    session['sensor_data_csv_file'] = os.path.join(app.config['UPLOAD_FOLDER'],'sensors.csv')
    data_file_path = session.get('sensor_data_csv_file', None)
    df = pd.read_csv(data_file_path)
    newSensorResponse = Response(arduino_sensor_event(df),mimetype="text/event-stream")
    newSensorResponse.headers.add('Access-Control-Allow-Origin', '*')
    newSensorResponse.headers.add('Cache-Control', 'no-cache')
    return newSensorResponse
