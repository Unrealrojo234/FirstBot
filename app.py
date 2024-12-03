from flask import Flask
import requests
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()


app = Flask(__name__)

CORS(app)

@app.route("/")
def root():
    return "<h1 style='text-align:center;color:teal;'>WhatsApp Chat Bot Made using Green API</h1>"


@app.route("/send/<phone>/<msg>")
def send(msg=None, phone=None):
    url = os.getenv("API_URL")

    payload = {
        "chatId": f"{phone}@c.us",
        "message": f"{msg}",
    }
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload, headers=headers)

    print(response.text.encode("utf8"))
    return response.json()


@app.route("/contacts")
def contacts():

    url = os.getenv("API_URL2")

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text.encode("utf8"))

    return response.json()


@app.route("/avator/<phone>")
def avator(phone=None):

    url = os.getenv("API_URL3")

    payload = {"chatId": f"{phone}@c.us"}
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=payload)

    print(response.text.encode("utf8"))

    return response.json()
