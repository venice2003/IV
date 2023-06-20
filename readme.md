# How to read the data inside the forms:

The data structure of the file will look like this :

```json
{
    14
  'lastName': '',
  'firstName': '',
  'middleInitial': '',
  'age': '',
  'contact': '',
  'month': '',
  'day': '',
  'year': '',
  'sex': '',
  'academicYear': '',
  'course': '',
  'section': '',
  'gName': '',
  'gAddress': '',
   10
  'dtMonth': '',
  'dtDay': '',
  'dtYear': '',
  'bp': '',
  'rr': '',
  'height': '',
  'weight': '',
  'bmi': '',
  'lmp': '',
  'impression': '',

  'hi': False,
  'ep': False,
  'enp': False,
  'asthma': False,
  'tb': False,
  'old': False,
  'hd': False,
  'hypertension': False,
  'ulcer': False,
  'kp': False,
  'fse': False,
  'dtd': False,
  'std': False,
  'ldh': False,
  'cc': False,

  'hiDetails': '',
  'epDetails': '',
  'enpDetails': '',
  'asthmaDetails': '',
  'tbDetails': '',
  'oldDetails': '',
  'hdDetails': '',
  'hypertensionDetails': '',
  'ulcerDetails': '',
  'kpDetails': '',
  'fseDetails': '',
  'dtdDetails': '',
  'stdDetails': '',
  'ldhDetails': '',
  'ccDetails': ''}
```

to read the data in python just simply add [] plus the key:

```python
sex = data['sex']
print(sex) #prints Female
```

[documentation](https://www.w3schools.com/python/python_dictionaries.asp)

## Adding data to the database.

mas lalo ko ng pinadali yung buhay niyo na ISANG file na lang ang i eedit niyo (baka kung ano ano pa buksan niyo),
to add the data to the data base,
just open the `validation.py` and ENTER YOUR CODE INSIDE THE ONE AND ONLY FUNCTION/METHOD na meron ang file nayon. sobrang dali diba?
1
