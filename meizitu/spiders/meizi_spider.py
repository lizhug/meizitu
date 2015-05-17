#!/usr/bin/python  
# -*- coding: utf-8 -*-  
#coding=utf-8 
import scrapy
import os
import urllib
import hashlib

savePath = os.path.abspath("../image")

class MeiziSpider(scrapy.Spider):
    name = "meizi"
    allowed_domains = ["meizitu.com"]
    start_urls = []

    ### 页码1 到 5000   可自行调整
    for i in range(400,401):
        start_urls.append("http://www.meizitu.com/a/%d.html" % i)

    def parse(self, response):
        for sel in response.xpath("//div[@class='postContent']//img"):
        
            imageUrl = sel.xpath("@src").extract()

            m = hashlib.md5()
            m.update(imageUrl[0])
            filename = m.hexdigest() + ".jpg"
            dist = os.path.join(savePath, filename) 

            urllib.urlretrieve(imageUrl[0], dist, None)
            
