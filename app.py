from flask import Flask
import os

app = Flask(__name__)

@app.get("/")
def home():
    return f"Hello from Kubernetes! Version: {os.getenv('VERSION', 'dev')}\n"

@app.get("/healthz")
def health():
    return "ok"