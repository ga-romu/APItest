from fastapi import FastAPI

import random

import importlib
importlib.reload(af)

app = FastAPI()

@app.get('/')
async def root():
    return {'example': 'Hello friend', 'data': 0}