from fastapi import FastAPI, Response, status
# import unicornhat as unicorn
# unicorn.brightness(1)

app = FastAPI()


@app.get("/")
def read_root():
    return {"version": "0.0.1"}


@app.get("/switch", status_code=200)
def turn_switch(v: str, response: Response):
    if v == "on":
        # unicorn.set_all(255, 255, 255)
        # unicorn.show()

        print("it is on!")
    elif v == "off":
        # unicorn.clear()
        # unicorn.show()

        print("it is off!")
    else:
        response.status_code = status.HTTP_404_NOT_FOUND
        v = "unknown"

    return {"status": v}
