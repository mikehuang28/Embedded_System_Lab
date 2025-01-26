import os
import sys
import datetime

import jetson.inference
import jetson.utils

import threading

import cv2 #camera
import pyimgur #upload photo
#import pygsheets #fetch data from google sheet
from openpyxl import load_workbook #excel
from openpyxl import Workbook

from argparse import ArgumentParser
from datetime import datetime
from glob import glob
from time import sleep

from flask import Flask, request, abort, Response, send_from_directory
from linebot import (
    LineBotApi, WebhookHandler 
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
channel_secret = "2c5958918a34c00a0ccd046d2ac34bc6"
channel_access_token = "wWc7YMXxvxILzxreW6fzHA1BOh8usaeeWI4iy2GQpbpvGn4XIK8s1jF2F3cSaCpOCLLS9ZP5LYZWTkXPHXfSlMMmc7ChziFzkKfjPiPsBh9LULr3PE5q1+VSdk9ngp+79RhHB9lJIBd4LGc5uU/L/QdB04t89/1O/w1cDnyilFU="

if channel_secret == "":
    print("Please specify LINE_CHANNEL_SECRET.")
    sys.exit(1)
if channel_access_token == "":
    print("Please specify LINE_CHANNEL_ACCESS_TOKEN.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

#push message to one user
line_bot_api.push_message('Ua274c7efa252b179fcd96746b2d7b610', 
    TextSendMessage(text='您與確診者有接觸,請盡快撥打1922,與疫調單位取得聯繫,謝謝!'))


@app.route("/callback", methods=["POST"])
def callback():
    # get X-Line-Signature header value
    signature = request.headers["X-Line-Signature"]

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return "OK"







