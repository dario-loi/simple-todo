# Simple TODO

The app is a trivial, mostly AI generated, Single Page Application that uses FastAPI, TailwindCSS, and SQLite.

It allows you to create TODO items, mark them as done, and delete them, and nothing else!

## Hosting the app

The app can be launched on your local network using the following command:

```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

You can then access the app at `http://127.0.0.1:8000`. You can access the app from your
phone by replacing `127.0.0.1` with your computer's local IP address (which you can find
by running `ipconfig` on Windows or `ifconfig` on Linux).

Be sure to open your firewall to allow incoming TCP connections to port 8000!