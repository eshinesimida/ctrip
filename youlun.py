# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 09:54:07 2020

@author: a4546
"""

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
from tqdm import tqdm

from lxml import etree


head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'} 

import pymysql

connect = pymysql.Connect(
    host='****',
    port=3306,
    user='root',
    passwd='******',
    db='*******',
    use_unicode=1,
    charset='utf8'
)


cursor = connect.cursor()


import time
import execjs

encrypt_fun = execjs.compile("""
function hash33(s) {
    s.replace(/Date\([\d+]+\)/, function(a) { eval('d = new '+a) });
    
    return d
    
}
""")

for j in range(11,200):
    print('j=',j)
    url = 'https://sec-m.ctrip.com/restapi/soa2/12431/GetComments?_fxpcqlniredt=09031132210327115579&__gw_appid=99999999&__gw_ver=1.0&__gw_from=10320606451&__gw_platform=H5&ShipId=59&PageIndex='+str(j)+'&PageSize=200'
    #url = 'https://sec-m.ctrip.com/restapi/soa2/12431/GetComments?_fxpcqlniredt=09031132210327115579&__gw_appid=99999999&__gw_ver=1.0&__gw_from=10320606451&__gw_platform=H5&ShipId=0&PageIdex=7&PageSize=25'
    html = requests.get(url, headers =head)
    time.sleep(5)
    youlun = html.json()
    B = youlun['data']['Comments']
    for i in tqdm(range(len(B))):
        ID = B[i]['Id']
        name = B[i]['UserId']
        score = B[i]['Score']
        content = B[i]['Content']
        time1 = B[i]['CommentDate']
        time2 = encrypt_fun.call('hash33',time1)
        time2 = re.sub('T',' ', time2)
        time2 = re.sub('Z','', time2)
        print(ID,name,score,content, time2)
        sql = "INSERT IGNORE INTO you_haiyang(ID,name,score,content, time) VALUES ( '%s', '%s', '%s', '%s', '%s')"
        data1 = (ID,name,score,content, time2)
    
        try:
            cursor.execute(sql % data1)
        except:
            print(ID)
    
        connect.commit()





           
