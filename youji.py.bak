# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:45:01 2020

@author: lenovo
"""

import re

import time
import urllib.request
import requests
from bs4 import BeautifulSoup
import pymysql
from tqdm import tqdm


user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36"
headers = {
	'User-Agent': user_agent, 
	"Upgrade-Insecure-Requests": str(1),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Accept-Language": "zh-CN,zh;q=0.8,en;q=0.6",
    "Cache-Control": "no-cache"
    }

connect = pymysql.Connect(
    host='rm-wz988to0p0a7js870o.mysql.rds.aliyuncs.com',
    port=3306,
    user='root',
    passwd='zd45+3=48',
    db='ctrip_gengxin',
    use_unicode=1,
    charset='utf8'
)
def get_articles():
    total_page = 400
    index = 1
    

    for i in tqdm(range(index, total_page+1)):
        #counter = 1

        json_url = "https://you.ctrip.com/searchsite/travels/?query=广州&isRecommended=1&PageNo=" + str(i)
        city = re.findall('[\u4e00-\u9fa5]+', json_url)[0]
        time.sleep(2)
        res = requests.get(json_url, headers=headers)

        res_soup = BeautifulSoup(res.text, "html.parser")
        main_contain = res_soup.find_all("li", class_="cf")
        cursor = connect.cursor()
        for each in main_contain:
            articles_info = each.find_all("a")
            #tag = str(index) + "-" + str(counter)
            #data[tag] = {}
            url = "https://you.ctrip.com" + articles_info[1]["href"]
            title = articles_info[1].text
            date = re.findall(r"[0-9]+-[0-9]+-[0-9]+", str(articles_info[2].next_sibling))
            name = articles_info[-1].text
            #print("Progress: %d # %d" % (int(index), int(counter)))
            time.sleep(3)    
            res = requests.get(url, headers=headers)
            #res.text
            soup = BeautifulSoup(res.text, 'html.parser')
            content = soup.find_all("div", class_=re.compile("^ctd_content[\sa-z_]*"))
            
            contents = []
            for text in content:
                for p in text.find_all("p"):
                    valid_content = p.get_text().replace(" ", "").replace("\n", "")
                    valid_content = valid_content.strip()
                    contents.append(valid_content)
            
            youji = ','.join(contents)
            #counter += 1
            #print(title,date,youji)
            
            
            sql = "INSERT IGNORE INTO youji_guangzhou(URL, title, name, time, content,city) VALUES ( '%s', '%s', '%s', '%s', '%s' ,'%s')"
            data = (url, title, name, date[0], youji,city)
            try:
                cursor.execute(sql % data)
            except:
                print(url)
    
            connect.commit()

if __name__ == '__main__':
    get_articles()
    
        

  
