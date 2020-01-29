# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 17:22:26 2020

@author: hp
"""


class DLL:
    
    def __init__(self):
        self.head = {}
        self.tail = {}
    
    def insert(self, v):
        #print(len(self.head))
        if len(self.head) == 0:
            self.head[v] = {'prev':None, 'next':None}
        else:
            key = list(self.head.keys())[0]
            #print(key)
            temp = self.head
            while temp[key]['next'] is not None:
                #temp = temp[key]
                key = temp[key]['next']
                
            temp[key]['next'] = v
            temp[v] = {'prev':key, 'next':None}
    
    def print(self):
        #print(self.head)
        key = list(self.head.keys())[0]
        temp = self.head
        while key is not None:
            print(key, temp[key])
            key = temp[key]['next']


dl = DLL()
dl.insert(10)
dl.insert(20)
dl.insert(30)
dl.insert(40)
dl.insert(50)
dl.insert(60)
dl.print()
        
                
                