# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 09:43:41 2022

@author: laleh
"""

from fastapi import FastAPI
import uvicorn
import pickle
from BankNotes import BankNote
import pandas



app=FastAPI()

f=open('data_Milestone3.pkl', 'rb')
val_final=pickle.load(f)
seuil_final=pickle.load(f)
seuil_final=seuil_final[0,0]
rf_grid=pickle.load(f)
rf_model = rf_grid.best_estimator_
f.close()

X_valids=pandas.read_csv("X_valid.csv")
X_valids=pandas.X_valids.iloc[:,1:]


model=pickle.load(open('Model_LR2.pkl', 'rb'))



@app.get("/")
def greet():
    return {"Hello World!"}



@app.post("/predict")
def predictx(req: BankNote):
    

    preg=req.pregnacies
    glucose=req.glucose
    bp=req.bp
    skinthickness=req.skinthickness
    insulin=req.insulin
    bmi=req.bmi
    dpf=req.dpf
    age=req.age
    features=list([preg,glucose,bp,skinthickness, insulin,bmi,dpf,age])
    
    predict=model.predict([features])
    probab=model.predict_proba([features])
    if (predict==1):
        return {"ans":"You have benn tested positive with {} probability".format(probab[0][1])}
    else:
        return {"ans":"You have benn tested negative with {} probability".format(probab[0][0])}
    
    

    
    
    

