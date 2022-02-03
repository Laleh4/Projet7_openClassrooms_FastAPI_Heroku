# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 09:43:41 2022

@author: laleh
"""

from fastapi import FastAPI
import uvicorn
import pickle
from Clients import Client
import pandas as pd
import numpy as np



app=FastAPI()




f=open('data_Milestone3.pkl', 'rb')
val_final=pickle.load(f)
seuil_final=pickle.load(f)
seuil_final=seuil_final[0,0]
rf_grid=pickle.load(f)
rf_model = rf_grid.best_estimator_
f.close()


X_valids=pd.read_csv("X_valid.csv")
X_valids=X_valids.iloc[:,1:]

@app.get("/")
def greet():
    return {"Hello World!"}


"""
@app.post("/predict")
def predictx(req: Client):
    
    i_client=req.Number
    """
    preg=req.pregnacies
    glucose=req.glucose
    bp=req.bp
    skinthickness=req.skinthickness
    insulin=req.insulin
    bmi=req.bmi
    dpf=req.dpf
    age=req.age
    features=list([preg,glucose,bp,skinthickness, insulin,bmi,dpf,age])
    """
    predict=rf_model.predict(X_valids.loc[[i_client]])
    probab=rf_model.predict_proba(X_valids.loc[[i_client]])
    if (predict==1):
        return {"ans":"Your credit is approuved with {} probability".format(probab[0][1])}
    else:
        return {"ans":"Your credit is rejected with {} probability".format(probab[0][0])}
 """   
    

    
    
    

