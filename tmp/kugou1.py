#!/usr/bin/env python
# coding=utf-8

import requests

url = 'https://complexsearch.kugou.com/v2/search/song?callback=callback123&srcappid=2919&clientver=1000&clienttime=1672664456483&mid=c93a792b0e652a4f4d9d3c15fa269de0&uuid=c93a792b0e652a4f4d9d3c15fa269de0&dfid=34d0e417TotG0Iydip4Q2345&keyword=%E5%A4%A7%E9%B1%BC&page=1&pagesize=30&bitrate=0&isfuzzy=0&inputtype=0&platform=WebFilter&userid=0&iscorrection=1&privilege_filter=0&filter=10&token=&appid=1014&signature=4a20ca240d6376177421e50bac843eb2'
param = url.split('?')[1]
list1 = param.split('&')
print(list1)
param_dic = {}
for i in list1:
    param_dic[i.split('=')[0]] = i.split('=')[1]
print(param_dic)
param  = {'callback': 'callback123', 'srcappid': '2919', 'clientver': '1000', 'clienttime': '1672664456483', 'mid': 'c93a792b0e652a4f4d9d3c15fa269de0', 'uuid': 'c93a792b0e652a4f4d9d3c15fa269de0', 'dfid': '34d0e417TotG0Iydip4Q2345', 'keyword': '%E5%A4%A7%E9%B1%BC', 'page': '1', 'pagesize': '30', 'bitrate': '0', 'isfuzzy': '0', 'inputtype': '0', 'platform': 'WebFilter', 'userid': 
'0', 'iscorrection': '1', 'privilege_filter': '0', 'filter': '10', 'token': '', 'appid': '1014', 'signature': '4a20ca240d6376177421e50bac843eb2'}