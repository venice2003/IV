#medical.py

#yan yung ilalagay mo sa loob ng medical records.
from db import db # import _mysql_connector
tableName = 'tabletest'
database = db()


# Connecting the database. YOU MUST do this before doing everything below.
# just a comment na pakibasa ulit yung nasa taas ng comment na to
database.connect(host="localhost",username="root",password="",databaseName="testdatabase")
# testing of creating a db
val = 0
while val <3: # di heart yan ha.            
    result = database.create(column_names=['field1','field2'],data=[f'value{val}',f'value{val+1}'],tableName=tableName)
    
    # preplanning
    val += 1
# testing of reading the database
result = database.read(tableName=tableName,column_names="*",condition="field1='value1'")


# either the one above, or this works, up to you.
result2 = database.read(tableName,"*","field1='value1'")
print(result)
print(result2)
# testing of update
#special note : yung field1 and field 2 is a column name. pakibasa ulit to ng mga 300 times. 
#special note 2: yung "bagong update" at "nadamay lang to" is yung new value ng field 1 and two
update = database.update(tableName, {
    "field1": "bagong update",
    "field2": "ano ba gagawin",

},"field1='value1'")

# if di mo na gets kung ano yung mga parameters(yung nasa loob ng parentesis ng mga yan), 
# just hover them tas yung nasa loob ng parenthesis nila, ayun yung mga need mo para gumana
# if may tanong pa, mag sabi na lang sakin

def addTwoNumber(number1,nubmer2):
    

    return number1+ nubmer2
add = addTwoNumber(1,2)
add2 = addTwoNumber(1,3)
