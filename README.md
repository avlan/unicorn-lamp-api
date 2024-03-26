# Simple lamp API

⚠️ **You should have unicornhat already installed to properly use this. Otherwise this API won't work**

Just an API for turning a unicorn hat on and off. Default color is white and default brightness is 1

## Installing dependencies

```bash
sudo pip3 install -r requirements.txt
```

## Running

### Locally

```bash
sudo venv/bin/uvicorn main:app --host=0.0.0.0
```

### As a demon

```bash
sudo gunicorn -b 0.0.0.0:8000 -w 3 -k uvicorn.workers.UvicornH11Worker main:app --daemon
```

### With systemd

Move content of `unicorn-lamp-api.service` file to `/etc/systemd/system/unicorn-lamp-api.service`

```bash
sudo systemctl start unicorn-lamp-api
sudo systemctl enable unicorn-lamp-api
```

TODO: Add authentication
TODO: Research about supervisord
