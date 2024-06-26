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

@app.get("/on", status_code=200)
def turn_on(response: Response):
    lamp.set_all(255, 255, 255)
    lamp.show()

    return {"status": "on"}

@app.get("/off", status_code=200)
def turn_off(response: Response):
    lamp.off()

    return {"status": "off"}


@app.get("/change-color", status_code=200)
def change_color(r: str, g:str, b:str, response: Response):
    red = int(r)
    green = int(g)
    blue = int(b)
    lamp.set_all(red,green,blue)
    lamp.show()

    return {"status": "on"}

@app.get("/change-brightness", status_code=200)
def change_brightness(b:str, response: Response):
    brightness = float(b)
    lamp.brightness(brightness)
    lamp.show()

    return {"status": "on"}

# @app.get("/toggle", status_code=200)
# def toggle(response: Response):
#     status = None
#     print(lamp.get_pixel(0,0))
#     if lamp.get_pixel(0,0) == 0 or lamp.get_pixel(0,0) == None:
#         lamp.set_all(255, 255, 255)
#         lamp.show()
#         status = "on"
#     else:
#         lamp.off()
#         status: "off"

#     return {"status": status}