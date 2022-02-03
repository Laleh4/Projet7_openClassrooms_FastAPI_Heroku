# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 15:28:50 2022

@author: laleh
"""

from pydantic import BaseModel
class Client(BaseModel):
    Number: int
    