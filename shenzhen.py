# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:23:37 2020

@author: a4546
"""

import requests
import re
import time

import pandas as pd
import requests
import csv
import numpy as np
from tqdm import tqdm
import datetime

from lxml import etree
from urllib.parse import urlencode
base_url = 'http://tocc.jtys.sz.gov.cn/req//earlyWarning/getRoadStatus'

head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}


    



def run(interval, command):  
   
    while True:  
        try:  
             
              
            #print("Starting command.")  
            # execute the command  
            
            response = requests.get(base_url, headers = head)
            
            html = response.json()
            data = html['data']
            
            time1 = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            speed = []
            status = []
            name = []
            direction = []
            time2 = []
            ID = []
            for item in data:
                speed.append(item['SPEED'])
                status.append(item['CONSTATUS'])
                name.append(item['NAMEN'])
                direction.append(item['DIR'])
                time2.append(time1)
                ID.append(item['NAMEN']+'_'+time1)
                print(item['NAMEN'])
            
            pf = pd.DataFrame({'ID':ID, 'name':name, 'status':status, 'direction':direction,
                       'speed':speed,'time':time1})
            A = time1.split(' ')
            time10 = A[0]+'_'+A[1].split(':')[0]
            pf.to_csv(time10+".csv", encoding="utf-8-sig", header=True, index=False)
            time.sleep(interval)
            
            
        except:  
            pass  
if __name__=="__main__":  
    interval = 3600  
    command = r"ls"  
    run(interval, command)  
