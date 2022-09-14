## CodedEnum

**Description:**

Extends availability of enumerations creation lik vocabulary, codifiers and 
etc. (code -> value format)


**Using:**

```python
import CodedEnum


class WeekDays(CodedEnum):
    MONDAY = 1, "Monday"
    TUESDAY = 2, "Tuesday"
    WEDNESDAY = 3, "Wednesday"
    THURSDAY = 4, "Thursday"
    FRIDAY = 5, "Friday"
    SATURDAY = 6, "Saturday"
    SUNDAY = 7, "Sunday"
```

Appealing to enumeration elements:
```shell
>> WeekDays.THURSDAY.name
'THURSDAY'
>> WeekDays.THURSDAY.value
4
>> WeekDays.THURSDAY.term
'Thursday'
```

Checking of value existing:
```shell
>> 4 in WeekDays
True
>> 8 in WeekDays
False
>> "Wednesday" in WeekDays
True
>> "January" in WeekDays
False
```

Getting element by string value:
```shell
>> friday = WeekDays["Friday"]
>> type(friday)
<enum 'WeekDays'>
>> friday.name
'FRIDAY'
```
Getting element by code value:
```shell
>> tuesday = WeekDays[2]
>> type(tuesday)
<enum 'WeekDays'>
>> tuesday.name
'TUESDAY'
```
Getting of missed element:
```shell
>> missed_element = WeekDays["Март"]
>> type(missed_element)
<class 'NoneType'>
```


Comparison of enumeration elements, including with other objects:<br>
__Only equal comparison available for string elements. 
For integers available all comparison types.__
```shell
>> "Friday" == WeekDays.FRIDAY
True
>> "Thursday" == WeekDays.FRIDAY
False
>> "Thursday" < WeekDays.FRIDAY
TypeError("Cannot compare with type <class 'str'>")
>> 5 >= WeekDays.FRIDAY
True
>> 4 >= WeekDays.FRIDAY
False
```

Cast:
```shell
>> sunday_str = str(WeekDays.SUNDAY)
>> type(sunday_str)
<class 'str'>
>> sunday_str
'7'
```
```shell
>> monday_int = int(WeekDays.MONDAY)
>> type(monday_int)
<class 'int'>
>> monday_int
1
```

Additional cast methods:
* `as_dict` &ndash; to dict with saving key names
```shell
>> WeekDays.WEDNESDAY.as_dict
{'value': 3, 'term': 'Thursday'}
```
* `to_frontend` &ndash; to dict for frontend as fall down list
```shell
>> WeekDays.WEDNESDAY.to_frontend
{'id': 3, 'name': 'Thursday'}
```