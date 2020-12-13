from fastapi import FastAPI, Response, status
from lamps.lamp import Lamp

app = FastAPI()
lamp = Lamp()


@app.get("/")
def read_root():
    return {"version": "0.0.1"}


@app.get("/switch", status_code=200)
def turn_switch(v: str, response: Response):
    if v == "on":
        lamp.set_all(255, 255, 255)
        lamp.show()
    elif v == "off":
        lamp.clear()
        lamp.show()
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        v = "unknown"

    return {"status": v}
