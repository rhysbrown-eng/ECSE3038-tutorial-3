from fastapi import FastAPI, HTTPException

app = FastAPI()

readings = [
    {"name": "front-door", "room": "hall",    "temp": 27.4, "online": True},
    {"name": "hall-lamp",  "room": "hall",    "temp": 26.1, "online": True},
    {"name": "attic",      "room": "attic",   "temp": 31.9, "online": True},
    {"name": "fridge",     "room": "kitchen", "temp": 4.2,  "online": False},
    {"name": "patio",      "room": "outside", "temp": 29.8, "online": True},
]

def hottest(devices):
    #return the whole dictionary of the hottest device
    max_idx = 0
    i=0

    for device in devices:
        if device["temp"] > devices[max_idx]["temp"]: max_idx = i
        i+=1

    return devices[max_idx]


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