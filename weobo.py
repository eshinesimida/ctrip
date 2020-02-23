# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 09:35:12 2019

@author: Administrator
"""

#动态加载
import requests
import re
import time

import pandas as pd
import requests
import csv
import numpy as np

from urllib.parse import urlencode
base_url = 'https://m.weibo.cn/api/container/getIndex?'

#
head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
def get_page(con_id,page):
    parames = {
                "containerid" : con_id,
                "page_type" : "03",
                "page" : page
                
                }
        #print(base_url + urlencode(parames))
    time.sleep(2)
    response = requests.get(base_url + urlencode(parames), headers = head)
        #print(response.json())
    return response.json()




########3
x = []
m = 0
for page in range(1601, 2000):
    try:
        m =  m+1
        print(m)
        con_id = '1076031618051664'
        res_json = get_page(con_id,page)
        weibo_num = res_json['data']['cardlistInfo']['total']
        id1 = res_json['data']['cards'][0]['mblog']['user']['id']
        name = res_json['data']['cards'][0]['mblog']['user']['screen_name']
        
        follow = res_json['data']['cards'][0]['mblog']['user']['follow_count']
        follower = res_json['data']['cards'][0]['mblog']['user']['followers_count']
        len1 = len(res_json['data']['cards'])
        for i in range(len1):
            
            id_tiezi = res_json['data']['cards'][i]['mblog']['id']
            time1 = res_json['data']['cards'][i]['mblog']['created_at']
            data = res_json['data']['cards'][i]['mblog']['text']
            hanzi = ''.join(re.findall('[\u4e00-\u9fa5]', data))
            
            comment_num = res_json['data']['cards'][i]['mblog']['comments_count']
            zan = res_json['data']['cards'][i]['mblog']['attitudes_count'] 
            zhuanfa = res_json['data']['cards'][i]['mblog']['reposts_count']
            #print(id1, name, id_tiezi,time,hanzi, comment_num,zan, zhuanfa)
            print(name,time1)
            x.append([id1, name,weibo_num,follow,follower, id_tiezi,time1,hanzi, comment_num,zan, zhuanfa])
           # with open('weibo.txt', 'a') as ff:
              # ff.write(id1 + '\t' + name +'\t'+id_tiezi+'\t'+time+'\t'+hanzi+'\t'+c)
    except:
        None
    c = pd.DataFrame(x)
    c.columns = ['id1', 'name','weibo_num','follow','follower', 'id_tiezi', 'time','hanzi','comment_num','zan','zhuanfa']
    c.to_csv('toutiaoxinwen4.csv')


