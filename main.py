
import json
import amino
import requests
from flask import Flask, request, jsonify
from time import time as timestamp
from json_minify import json_minify
import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import ast
import urllib.parse
import threading

app = Flask(__name__)

dictlist=[{"email":"adoringPretzels4183d@gmail.com","password":"LsuaaIsGay1234%","device":"19F8388287B60BFD494E0E79512F2D28A87A1B19F3CF42070F313D186B68C61CB520359BF170448968"},{"email":"anxiousTeal3cc5a@gmail.com","password":"LsuaaIsGay1234%","device":"190EF76F45620E3A3CFBB6C2A601A58CB5A68694254489CE63395201125BAED9A6A7779A7569878158"},{"email":"wrathfulMallard33dc5@gmail.com","password":"LsuaaIsGay1234%","device":"19796AD9D8A08E38B6F47B41FE4FCCB8C1A71BEBCDC2F6E3C52CDF3EF9FCE1883CD4993DA22EE7BC8B"},{"_id":"653b32dfb7ff417f700b5050","email":"gleefulAntelope8710e@gmail.com","password":"LsuaaIsGay1234%","device":"19A6440EE1A3D77206A3F0A3AB9C982D3E1184C092AF3AA796DF97B5C787812792027BE65B2B4A98DE"},{"email":"boredPolenta4d15f@gmail.com","password":"LsuaaIsGay1234%","device":"19DCDEA94A9DB0FB15C5C5D205FBE1ACE71682D9807332A9324883DD0097ADA68F0B47FFA924061FA4"},{"email":"obsessedRaisins3d185@gmail.com","password":"LsuaaIsGay1234%","device":"1913437454867FF85955B5FABF56CE52572EEEA6235263E02AE30EF66A1A596367498C97F75C8B275B"},{"email":"importedSeahorse3e2de@gmail.com","password":"LsuaaIsGay1234%","device":"19EED5021809E4C9AF68FC20295EC675E89294225D378C8610B7093A2D1A62BE3082B1E91AD51E4010"},{"email":"affectedChile5957e@gmail.com","password":"LsuaaIsGay1234%","device":"1979648C636F3F3B36B0B8E95A9A719BA3514C665CB037456A4BF29127CD46E2E44FEC0DBEE624CC66"},{"email":"fondBuzzard2612d@gmail.com","password":"LsuaaIsGay1234%","device":"19BC89F2D15811B7DC140D0104EE54AC4027DB97BFF12E43E618035D8F3183D235A25510BB29D14D5D"},{"email":"solidZebra48f7b@gmail.com","password":"LsuaaIsGay1234%","device":"1916D013223B53C7B4D4546B2A9C81CED2CFB0B061D7334087F808D7756AF5968356FC4C4D9FB5F779"},{"email":"blissfulWigeon92dbd@gmail.com","password":"LsuaaIsGay1234%","device":"19D0860185E165BB3B4CA09C93092B09CD3833C4D2631EFF84D322ACDD418B9614D640E2D4A962349C"},{"email":"selfishTacos3535f@gmail.com","password":"LsuaaIsGay1234%","device":"1917B5C4FB09838BDA0DE2FECB212C236F3C1A142C03E8D654E7BB6CAB42BB0A789471C46AC8DAEA6B"},{"email":"panickyToucan90e41@gmail.com","password":"LsuaaIsGay1234%","device":"1962762EA528CC4AD4221168C9C84D7A1F5EBC87FC7DF16F4083DEB380CDFBBC69BD20C27E6A1DE209"},{"email":"panickyCheese82678@gmail.com","password":"LsuaaIsGay1234%","device":"191B9BE67BBABACD44DBD0EE479479BCE2FE0D0866CA5323DBBE2488AFBBDEE3193FCA9EF735C93F82"},{"email":"shamefulOryx33723@gmail.com","password":"LsuaaIsGay1234%","device":"193915C1E94EF7210588CD4C282250DC7A73A3A1B8A321EDD058CB45EB5E88AB3D59FA70519256F5A4"},{"email":"tautTermite5e12c@gmail.com","password":"LsuaaIsGay1234%","device":"19BBBA386A76BDC3718AE45D1DBDB28AAD87C9AFF0C3908CA99B95FAE4D7004AB9EC3DC4A7024DE6FF"},{"email":"gleefulGelding27147@gmail.com","password":"LsuaaIsGay1234%","device":"193F1EAB2C12EFCE11772F6050773F9AE4009DA932E10969327106B3AEF3A5536760CAC1190AECF346"},{"email":"dejectedCur737ba@gmail.com","password":"LsuaaIsGay1234%","device":"19F0900B9214D44F0E49FC594445577197F2BD21898140FD3B5C98D0D79947263A6BB9B2EFD7F3AF98"},{"email":"euphoricPudding10ebe@gmail.com","password":"LsuaaIsGay1234%","device":"195A6306D2ADA2AC3A54203EAB8C474BDE42BB8CA3A5CBE3FC47523AB5CCDCFD6B5A884F1D6C3A68A3"},{"email":"finickyBustard57899@gmail.com","password":"LsuaaIsGay1234%","device":"19C59EDD8C9C92CFCFF5CA17A0ADD6BCDAD25053E2A96576B8DBFF64ABBC4046F8BA6ECD6BA6EC429B"},{"email":"pluckySmelt6da30@gmail.com","password":"LsuaaIsGay1234%","device":"19A7CFC5F310C43657335D5A7431E5764AD87789EA7B667CCA71C791D503F786612F96BF423C13C408"}]

def ut(cli,id,cid):
    cli.join_screen_room(comId=comId,chatId=chatId)

def summon(chatId,comId):
#    id=chatId
    #cid=coomId
    for s in dictlist:
        try:
            email=s["email"]
            password=s["password"]
            device=s["device"]
            cli=amino.Client(device)
            cli.login(email, password)
            cli.join_community(comId)
            print(comId , chatId)
            threading.Thread(target=ut,args=(cli,chatId,comId)).start()
        except Exception:
            pass

@app.route('/sig-gen/', methods=['POST'])
def post_something():
    param = request.form.get('data')
    #print(param)
    f=json.loads(param)
    chatId=f["chatId"]
    comId=f["comId"]
    sig=summon(chatId,comId)
    return sig

@app.route('/')
def index():
    return "<h1>Summon bot</h1>"

if __name__ == '__main__':
    app.run("0.0.0.0",5000)