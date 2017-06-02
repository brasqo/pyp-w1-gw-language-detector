#!/usr/bin/python
# -*- coding: utf-8 -*-
from collections import defaultdict
import operator



"""This is the entry point of the program."""

def detect_language(text, languages):
    """Returns the detected language of given text."""
    # implement your solution here
    
    # create dictionary with same keys as languages
    result_languages = defaultdict(int)
    

    
   
   
    for word in text.split():
        for lang in languages:
            if word in lang['common_words']:
                result_languages[lang['name']] += 1     
                #if so increase count for language
              
                
    # for result in result_languages:
    #     if lang['name'] count save count number and name
    
    result = max(result_languages, key=result_languages.get)


    return result 
    # return name
    
    
