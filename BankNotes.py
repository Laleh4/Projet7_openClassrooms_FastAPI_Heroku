# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 15:28:50 2022

@author: laleh
"""

from pydantic import BaseModel
class BankNote(BaseModel):
    pregnacies: float
    glucose:  float
    bp :  float
    skinthickness :  float
    insulin :  float
    bmi :  float
    dpf:  float
    age:  float