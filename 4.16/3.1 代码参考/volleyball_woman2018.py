# -*- coding: utf-8 -*-
"""
Crawler
@author: Dazhuang
"""
import re
import requests
def crawler(url):
    try:
        r = requests.get(url)
    except requests.exceptions.RequestException as err:
        return err
    r.encoding = r.apparent_encoding
    pattern = re.compile('href="/en/vnl/2018/women/teams/.*?">(.*?)</a></figcaption>\s+</figure>\s+</td>\s+<td>(.*?)</td>\s+<td class="table-td-bold">(.*?)</td>\s+<td class="table-td-rightborder">(.*?)</td>')
    p = re.findall(pattern, r.text)
    return p

if __name__ == "__main__":
    url = 'http://www.volleyball.world/en/vnl/2018/women/results-and-ranking/round1'
    result = crawler(url)
    print(result)


