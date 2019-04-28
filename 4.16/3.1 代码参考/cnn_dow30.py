# -*- coding: utf-8 -*-
"""
Get dji stock data
@author: Dazhuang
"""

import requests
import re

def retrieve_dji_list():
    try:
        r = requests.get('http://money.cnn.com/data/dow30/')
    except Exception as err:
        print(err)
    search_pattern = re.compile('class="wsod_symbol">(.*?)<\/a>.*?<span.*?">(.*?)<\/span>.*?\n.*?class="wsod_stream">(.*?)<\/span>')
    dji_list_in_text = re.findall(search_pattern, r.text)
    return dji_list_in_text

dji_list = retrieve_dji_list()
print(dji_list)

