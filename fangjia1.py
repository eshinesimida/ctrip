# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 09:56:19 2020

@author: a4546
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:29:32 2020

@author: a4546
"""
import requests
import re
import time

import pandas as pd
# import requests
import csv
import numpy as np
import math
import pymysql
import json
from tqdm import tqdm
from lxml import etree
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from scrapy.http import HtmlResponse
import datetime
import re
import time



def crawlFangjia():
    loopNum = 0
    ifHandle = False
    pageNum = 2800
    while (pageNum >= 1):

        loopNum = loopNum + 1
        if (len(re.findall(u'下一页', driver.page_source)) == 0):
            break
        target = driver.find_element_by_class_name(
            'page')
        y = target.location['y']
        y = y - 100
        print(y)
        js = "var q=document.documentElement.scrollTop=" + str(y)
        driver.execute_script(js)
        time.sleep(3)
        if u"下一页" in driver.page_source:

            if ifHandle == False:
                crawllianjie(driver.page_source)

                ifHandle = True
                try:
                    # print u"下一页" in self.driver.page_source
                    if u"下一页" in driver.page_source:
                        pageNum = pageNum - 1

                        driver.find_element_by_partial_link_text("下一页").click()
                        # self.driver.find_element_by_xpath("//div[@class='weiboitem active']/div[@class='comment_ctrip']/div[@class='ttd_pager cf']/div[@class='pager_v1']/a[@class='nextpage']").click()
                        ifHandle = False
                        loopNum = 0

                        time.sleep(3)
                        print("页数：" + str(pageNum))

                        num1 = 2800 - pageNum + 1
                        print('num1 = ' + str(num1))


                except:
                    pageNum = pageNum + 1
    return False if pageNum > 1 else True


def crawllianjie(page_source):
    response1 = HtmlResponse(url="my HTML string", body=page_source, encoding="utf-8")

    tweet_nodes = response1.xpath('//div[@class="nl_con clearfix"]/ul/li')
    city = response1.xpath('//div[@class="fl"]/a/text()').extract()[0]
    for tweet_node in tweet_nodes:
        
        try:
            ID = tweet_node.xpath('@id').extract()[0]
            name = tweet_node.xpath('div/div[@class="nlc_details"]/div[1]/div/a/text()').extract()
            names = []
            for i in name:
                i = i.strip()
                if(i):
                    names.append(i)
                
                
            names = names[0]
            
            huxing = tweet_node.xpath('div/div[@class="nlc_details"]/div[2]/a/text()').extract()
            huxing = ','.join(huxing)
            area = tweet_node.xpath('div/div[@class="nlc_details"]/div[2]/text()').extract()
            for j in area:
                j = j.strip()
                if(j):
                    areas = j
            areas = areas.split('\t')[-1]
            
            
            
            
            address = tweet_node.xpath('div/div[@class="nlc_details"]/div[3]/div/a/@title').extract()[0]
            #quyu = tweet_node.xpath('div/div[@class="nlc_details"]/div[3]/div/a/span/text()').extract()[0]
            try:
                quyu = tweet_node.xpath('div/div[@class="nlc_details"]/div[3]/div/a/text()').extract()[0]
                quyu = quyu.strip()
                quyu = quyu.split('\t')[0]
                m = re.findall('[\u4e00-\u9fa5]+', quyu)[0]
            except:
                quyu = tweet_node.xpath('div/div[@class="nlc_details"]/div[3]/div/a/span/text()').extract()[0]
                quyu = quyu.strip()
                quyu = quyu.split('\t')[0]
                m = re.findall('[\u4e00-\u9fa5]+', quyu)[0]
            
            
            
            
            
            category = tweet_node.xpath('div/div[@class="nlc_details"]/div[4]/a/text()').extract()
            A = []
            for i in category:
                i = i.strip()
                A.append(i)
            Category1 = ','.join(A)
            
            price = tweet_node.xpath('div/div[@class="nlc_details"]/div[5]/span/text()').extract()[0]
            print(ID,names,address,Category1,huxing,areas,city,price,m)
            
        except:
            pass
            
        


if __name__ == '__main__':
    url = 'https://hf.newhouse.fang.com/house/s/a9%BA%CF%B7%CA/'
    driver = webdriver.Chrome()
    driver.get(url)
    crawlFangjia()
