# Python Port of the TMS WEB Core Shoelace Demo

This folder contains a lightweight FastAPI application that mirrors the original Delphi/TMS WEB Core UI interactions:

- Clicking the button shows an alert with the clicked element's `id`.
- Toggling the switch shows an alert indicating whether it is ON or OFF.
- Adjusting the color picker updates the color label with the current value (including all custom swatches/tooltips from the Delphi code).
- The Shoelace image comparer is included with the same source images.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload --port 8000
```

Then open http://localhost:8000/ in a browser.

## Structure

- `app.py` – FastAPI entrypoint that serves the template and a simple health endpoint.
- `templates/index.html` – Recreates the Delphi form using Shoelace components and JavaScript handlers.
- `requirements.txt` – Runtime dependencies (FastAPI, Uvicorn, Jinja2).
