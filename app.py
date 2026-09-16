from fastapi import FastAPI, HTTPException

app = FastAPI()

readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

def average_temp(devices):
    #returns the average temperature

    sum = 0
    i=0

    for device in devices:
        sum += device["temp"]
        i += 1

    return sum/i


@app.get("/devices")
def list_devices():
    return readings

@app.get("/devices/hottest")
def hottest():
    #return the whole dictionary of the hottest device
    max_idx = 0
    i=0

    for device in readings:
        if device["temp"] > readings[max_idx]["temp"]: max_idx = i
        i+=1

    return readings[max_idx]

@app.get("/devices/online")
def list_online_devices():
    online_devices = []
    for device in readings:
        if device["online"] == True: online_devices.append(device)
    return online_devices