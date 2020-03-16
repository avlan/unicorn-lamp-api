from fastapi import FastAPI, Response, status


app = FastAPI()


@app.get("/")
def read_root():
    return {"version": "0.0.1"}


@app.get("/switch", status_code=200)
def turn_switch(v: str, response: Response):
    if v == "on":
        # TODO: Turn on the lights
        print("it is on!")
    elif v == "off":
        # TODO: Turn off the lights
        print("it is off! ):")
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        v = "unknown"

    return {"status": v}
