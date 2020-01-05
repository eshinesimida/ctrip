# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 18:57:23 2020

@author: a4546
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 17:00:46 2020

@author: lenovo
"""

import re
import requests
import json
import time


import pandas as pd
import pymysql

from lxml import etree


head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'} 

postUrl="https://sec-m.ctrip.com/restapi/soa2/12530/json/viewCommentList"
        
urls = [
        ['107540','广州塔'],
        ['6802','长隆野生动物世界']
               
        
        ]


for data in urls:
    
    data_1={
				"pageid": "10650000804",
			    "viewid": data[0],
			    "tagid": "0",
			    "pagenum": "1",
			    "pagesize": "50",
			    "contentType": "json",
                "SortType":"1",
			    "head": {
			        "appid": "100013776",
			        "cid": "09031037211035410190",
			        "ctok": "",
			        "cver": "1.0",
			        "lang": "01",
			        "sid": "8888",
			        "syscode": "09",
			        "auth": "",
			        "extension": [
			            {
			                "name": "protocal",
			                "value": "https"
			            }
			        ]
			    },
			    "ver": "7.10.3.0319180000"
            }
    
    
    html=requests.post(postUrl,data=json.dumps(data_1)).text
    html=json.loads(html)
    jingqu = data[1]
    #comments = html['data']['comments']
    pages = html['data']['totalpage']
    datas = []
    for j in range(pages):
        
        data1={
				"pageid": "10650000804",
			    "viewid": data[0],
			    "tagid": "0",
			    "pagenum": str(j+1),
			    "pagesize": "50",
			    "contentType": "json",
                "SortType":"1",
			    "head": {
			        "appid": "100013776",
			        "cid": "09031037211035410190",
			        "ctok": "",
			        "cver": "1.0",
			        "lang": "01",
			        "sid": "8888",
			        "syscode": "09",
			        "auth": "",
			        "extension": [
			            {
			                "name": "protocal",
			                "value": "https"
			            }
			        ]
			    },
			    "ver": "7.10.3.0319180000"
			}
        datas.append(data1)
    
    for k in datas:
        print('正在抓取第'+k['pagenum']+"页")
        time.sleep(3)
        html1=requests.post(postUrl,data=json.dumps(k)).text
        html1=json.loads(html1)
        comments = html1['data']['comments']
        
       
        for i in comments:
            ID = i['id']
            name = i['uid']
            content = i['content']
            content = re.sub("&#x20;", "", content)
            
            time1 = i['date']
            print(ID,jingqu,name,content,time1)
            
           
