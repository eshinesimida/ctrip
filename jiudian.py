# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:10:25 2020

@author: a4546
"""

from urllib import request
import json
import requests

def getResponse(url):

    data = {"hotelId":5209137,"pageIndex":1,"tagId":0,"pageSize":10,"groupTypeBitMap":2,"needStatisticInfo":0,"order":0,"basicRoomName":"","travelType":-1,"head":{"cid":"09031144211504567945","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":"","extension":[]}}
    data = json.dumps(data).encode(encoding='utf-8')
    
    
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}

    url_request = request.Request(url=url,data=data,headers=header_dict)
    print("这个对象的方法是：",url_request.get_method())

    url_response = request.urlopen(url_request)
    
    return url_response

http_response = getResponse("http://m.ctrip.com/restapi/soa2/16765/gethotelcomment?_fxpcqlniredt=09031144211504567945")

data = http_response.read().decode('utf-8')
print(data)


#############
#another method
data = {"hotelId":5209137,"pageIndex":1,"tagId":0,"pageSize":10,"groupTypeBitMap":2,"needStatisticInfo":0,"order":0,"basicRoomName":"","travelType":-1,"head":{"cid":"09031144211504567945","ctok":"","cver":"1.0","lang":"01","sid":"8888","syscode":"09","auth":"","extension":[]}}
data = json.dumps(data).encode(encoding='utf-8')
url = 'http://m.ctrip.com/restapi/soa2/16765/gethotelcomment?_fxpcqlniredt=09031144211504567945'

header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',"Content-Type": "application/json"}
html = requests.post(url=url,data=data,headers= header_dict)
html = html.json()
item = html['othersCommentList']

for i in item:
    ID = i['id']
    RoomID = i['baseRoomId']
    RoomName = i['baseRoomName']
    checkInDate = i['checkInDate']
    postDate = i['postDate']
    comment = i['content']
    score = i['ratingPoint']
    name = i['userNickName']
    print(RoomID, name, RoomName, checkInDate, postDate, comment, score)
    
    

