# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 20:38:01 2022

@author: Adarsha Chatterjee
"""
story="Once upon a time there was a boy named as Adarsha who used to code in python"

#String functions
print("The length of the story is: ",len(story))
print(story.endswith("python"))#This will print as true
print(story.count("c"))
print(story.capitalize())
print(story.find("upon"))#it will tell the index of the first occurances.
print(story.replace("Adarsha","Deep"))