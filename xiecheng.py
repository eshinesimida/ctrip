#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author：albert time:2020/4/17

import re
import requests
import json
import time
import pandas as pd

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}

postUrl = "https://sec-m.ctrip.com/restapi/soa2/12530/json/viewCommentList"

urls = [
    ['8979', '黄鹤楼'],

]

for data in urls:

    data_1 = {
        "pageid": "10650000804",
        "viewid": data[0],
        "tagid": "0",
        "pagenum": "1",
        "pagesize": "50",
        "contentType": "json",
        "SortType": "1",
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

    html = requests.post(postUrl, data=json.dumps(data_1)).text
    html = json.loads(html)
    jingqu = data[1]
    # comments = html['data']['comments']
    pages = html['data']['totalpage']
    datas = []
    for j in range(pages):
        data1 = {
            "pageid": "10650000804",
            "viewid": data[0],
            "tagid": "0",
            "pagenum": str(j + 1),
            "pagesize": "50",
            "contentType": "json",
            "SortType": "1",
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

    IDs = []
    jingqus = []
    names = []
    scores = []
    contents = []
    times1 = []
    for k in datas:
        print('正在抓取第' + k['pagenum'] + "页")
        time.sleep(3)
        html1 = requests.post(postUrl, data=json.dumps(k)).text
        html1 = json.loads(html1)
        comments = html1['data']['comments']
        
        for i in comments:
            ID = i['id']
            name = i['uid']
            score = i['score']
            content = i['content']
            content = re.sub("&#x20;", "", content)

            time1 = i['date']
            
            IDs.append(ID)
            jingqus.append(jingqu)
            names.append(name)
            scores.append(score)
            contents.append(content)
            times1.append(time1)
            
            print(ID,jingqu,name,score,content,time1)
    pf = pd.DataFrame({'IDs':IDs, 'jingqus':jingqus, 'names':names, 'scores':scores,
                       'contents':contents,'times1':times1})
    pf.to_csv("pinglun.csv", encoding="utf-8-sig", header=False, index=False)
