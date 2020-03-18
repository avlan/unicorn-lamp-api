# Simple lamp API

⚠️ **You should have unicornhat already installed to properly use this. Otherwise this API won't work**

Just an API for turning a unicorn hat on and off. Default color is white and default brightness is 1

# Installing dependencies

```bash
sudo pip3 install -r requirements.txt
```

# Running

## Locally

```bash
sudo uvicorn main:app --host=0.0.0.0
```

## As a demon

```bash
sudo gunicorn -w 4 -k uvicorn.workers.UvicornH11Worker main:app --daemon
```

TODO: Try/catch importing unicornhat
TODO: Add authentication
TODO: Add capacity to change colors
TODO: Add capacity to change brightness
