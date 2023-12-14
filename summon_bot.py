import json
import random
import os
import sys
import time
from time import time as timestamp
from time import sleep
import names
from hashlib import sha1
from functools import reduce
from base64 import b85decode, b64decode
import random
import requests
import hmac
import platform,socket,re,uuid
import base64
import  threading
from uuid import uuid4
import aminos
from flask import Flask, jsonify, request, render_template
def r():
    s = requests.Session()
    return s.headers['User-Agent']
def sigg(data):
        key='EAB4F1B9E3340CD1631EDE3B587CC3EBEDF1AFA9'
        mac = hmac.new(bytes.fromhex(key), data.encode("utf-8"), sha1)
        digest = bytes.fromhex("52") + mac.digest()
        return base64.b64encode(digest).decode("utf-8")
def dev():
    hw=(names.get_full_name()+str(random.randint(0,10000000))+platform.version()+platform.machine()+names.get_first_name()+socket.gethostbyname(socket.gethostname())+':'.join(re.findall('..', '%012x' % uuid.getnode()))+platform.processor())
    identifier=sha1(hw.encode('utf-8')).digest()
    key='AE49550458D8E7C51D566916B04888BFB8B3CA7D'
    mac = hmac.new(bytes.fromhex(key), b"\x52" + identifier, sha1)
    return (f"52{identifier.hex()}{mac.hexdigest()}").upper()

def live(sid,comId,chatId):
    header = {
    "NDCAUTH": f"sid={sid}",
    "NDCDEVICEID":dev()
    }
    ws = aminos.Wss(header)
    ws.launch()
    wsClient = ws.getClient()
    wsClient.joinVideoChatAsSpectator(comId,chatId)
app = Flask(__name__)

@app.route("/")
def home():
  return "ready"

@app.route("/vc", methods=['POST'])
def home_post():
  param= request.form['data']
  data=json.loads(param)
  sids= data['list']
  comId= data['comId']
  chatId= data['chatId']
  
  for sid in sids:
      live(sid,comId,chatId)
  
  return "Done"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
