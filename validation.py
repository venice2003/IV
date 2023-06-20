from db import db 
from texts import mainWindowTexts, emergencyScreenTexts,medicHistoryTexts
columns = [*mainWindowTexts,*emergencyScreenTexts,*medicHistoryTexts]
database = db()
databaseName = "medicalforms"
tableName = "formdata"
database.connect("localhost","root","",databaseName)
def validate (data : dict):  
    database.create(columns,list(data.values()),tableName)
    # code here