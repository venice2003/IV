# How to read the data inside the forms:

The data structure of the file will look like this :

```json
{
 'lastName': 'asdas',
 'firstName': 'asdasdasd',
 'middleInitial': 'asda',
 'age': 'asdasdasddasd',
 'contact': 'dasdasd',
 'month': 'Febuary',
 'day': 'asdasd',
 'year': 'asdas',
 'sex': 'Female',
 'academicYear': 'asdasd',
 'gName': 'asdasd',
 'gAddress': 'asdasdsdasd',
 'bp': 'asdasdasd',
 'rr': 'asd',
 'height': 'asdasd',
 'weight': 'HIUHIUH',
 'bmi': 'uyguy',
 'lmp': 'asda',
 'impression': 'sdasdasd',
 'hi': True,
 'ep': True,
 'enp': True,
 'tb': True,
 'old': True,
 'hd': True,
 'hypertension': True,
 'ulcer': False,
 'kp': False,
 'fse': False,
 'dtd': False,
 'std': False,
 'ldh': False,
 'cc': False,
 'hiDetails': 'asda',
 'epDetails': '55646',
 'enpDetails': '654564',
 'tbDetails': '654564',
 'oldDetails': '654654',
 'hdDetails': '64654',
 'hypertensionDetails': '654564',
 'ulcerDetails': '6546',
 'kpDetails': '4654654',
 'fseDetails': '654654',
 'dtdDetails': '654654',
 'stdDetails': '654654',
 'ldhDetails': '654654',
 'ccDetails': '654654'
 }
```

to read the data in python just simply add [] plus the key:

```python
sex = data['sex']
print(sex) #prints Female
```

[documentation](https://www.w3schools.com/python/python_dictionaries.asp)

## Adding data to the database.

mas lalo ko ng pinadali yung buhay niyo na ISANG file na lang ang i eedit niyo (baka kung ano ano pa buksan niyo), to add the data to the data base, just open the `validation.py` and ENTER YOUR CODE INSIDE THE ONE AND ONLY FUNCTION/METHOD na meron ang file nayon. sobrang dali diba?
