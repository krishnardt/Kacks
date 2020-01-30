# -*- coding: utf-8 -*-
"""
Created on Sat Dec 28 13:10:56 2019

@author: hp
"""





def NRCS(s):
    if len(s) == 0:
        return len(s)
    substr = ''
    max_str = ''
    #print(len(subsets))
    for ch in s:
        if ch in substr:
            ind = substr.index(ch)
            #subsets.append(substr)
            #print(subsets, substr)
            if len(max_str) < len(substr):
                max_str = substr
            if substr[-1] == substr[ind]:
                substr = ''
            else:
                substr = substr[ind+1:]
        substr = substr+ch
    #print(subsets, substr)
    if len(max_str) < len(substr):
        max_str = substr
        
    #subsets.append(substr)
    #max_str = max(subsets, key=len)
    #print(max_str)
    #print(len(max_str))
    #print(subsets)
    #print(len(subsets))
    print(max_str, len(max_str))
    return max_str, len(max_str)

NRCS('geeksforgeeks')
NRCS('sss')
NRCS('abcabcbb')
NRCS('au')
NRCS('pwwkew')
NRCS('dvdf')
NRCS('')
                    
                    
                