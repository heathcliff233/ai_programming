#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 09:11:52 2019

@author: apple
"""
import pandas as pd
data1 = pd.DataFrame(pd.read_table('u.data',sep='\t'))
data2 = pd.DataFrame(pd.read_table('u.user',sep='|'))
whole = pd.merge(data1 , data2)
useful = pd.DataFrame()
useful['gender'] = whole['gender']
useful['iterm_id'] = whole['item_id']
useful['rating'] = whole['rating']
output = pd.pivot_table(useful , index = ['gender','''"user_id"'''] ,  values = 'rating' , aggfunc = 'var')
output
# gender_tabel.groupby('gender').apply(np.std) #or pd.Seties.std
