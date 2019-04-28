#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 08:15:05 2019

@author: apple
"""

import pandas as pd
def line_prepender(filename, line):
    with open(filename, 'r+') as f:
        content = f.read()
        f.seek(0, 0)
        f.write(line.rstrip('\r\n') + '\n' + content)
line_prepender('u.data','user_id\titem_id\trating\ttimestamp')
line_prepender('u.user','user_id|age|gender|occupation|zip_code')

data1 = pd.DataFrame(pd.read_table('u.data',sep='\t'))
data2 = pd.DataFrame(pd.read_table('u.user',sep='|'))
print(data1)
print(data2)
