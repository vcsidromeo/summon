from os import system
system("pip install flask")
system("pip install -U websocket")
system("pip install -U websocket-client==1.5.1")
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
        key='DFA5ED192DDA6E88A12FE12130DC6206B1251E44'
        mac = hmac.new(bytes.fromhex(key), data.encode("utf-8"), sha1)
        digest = bytes.fromhex("19") + mac.digest()
        return base64.b64encode(digest).decode("utf-8")
def dev():
    hw=(names.get_full_name()+str(random.randint(0,10000000))+platform.version()+platform.machine()+names.get_first_name()+socket.gethostbyname(socket.gethostname())+':'.join(re.findall('..', '%012x' % uuid.getnode()))+platform.processor())
    identifier=sha1(hw.encode('utf-8')).digest()
    key='E7309ECC0953C6FA60005B2765F99DBBC965C8E9'
    mac = hmac.new(bytes.fromhex(key), b"\x19" + identifier, sha1)
    return (f"19{identifier.hex()}{mac.hexdigest()}").upper()

def reset(l):
  #data.subClient.send_message(data.chatId,"done")
  sleep(2)
  sys.argv
  sys.executable
  print("restart now")
  os.execv(sys.executable, ['python'] + sys.argv)

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

@app.get('/restart')
def res():
    threading.Thread(target=reset,args=[""]).start()
    return "restart"

@app.route("/")
def home():
  return "summon bot"

@app.route("/vc", methods=['POST'])
def home_post():
  param= request.form['data']
  data=json.loads(param)
  sids= data['list']
  comId= data['comId']
  chatId= data['chatId']
  
  for sid in sids:
      #print(sid)
      live(sid,comId,chatId)
  
  return "finished"
#port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
    app.run(host='0.0.0.0')

def Root():
    j = 0
    while True:
        if j >= 1800:
            sys.argv
            sys.executable
            print("restarting")
            os.execv(sys.executable, ['python'] + sys.argv)
            j = 0
        j += 1
        time.sleep(1)
Root()