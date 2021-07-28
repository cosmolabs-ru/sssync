#!/usr/bin/python
from flask import Flask
from json import dumps
from datetime import datetime
from math import floor

app = Flask(__name__)


@app.route('/')
def index():
    dt = datetime.utcnow().timetuple()
    hour = dt.tm_hour-2
    if hour < 0:
        hour = 24+hour
    ss = (hour * 3600 + dt.tm_min * 60 + dt.tm_sec)*(1000/864)
    sstime = {"year": dt.tm_year-1, "month": floor(dt.tm_yday / 73), "date": dt.tm_yday % 73 - 1, "ss": ss}
    return dumps(sstime)


app.run(host="0.0.0.0", port=864)
