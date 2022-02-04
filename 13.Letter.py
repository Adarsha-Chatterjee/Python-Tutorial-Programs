# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 00:41:20 2022

@author: Adarsha
"""
letter='''Dear <|Name|>,
                You are Selected!
         <|Date|>'''
name=input("Enter the name:")
date=input("Enter the date:")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)