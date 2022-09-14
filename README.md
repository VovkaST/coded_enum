## CodedEnum

**Описание:**

Расширяет возможности создания перечислений в виде кодификаторов (словарей, 
справочников и т.п.).

```python
import CodedEnum


class WeekDays(CodedEnum):
    MONDAY = 1, "Понедельник"
    TUESDAY = 2, "Вторник"
    WEDNESDAY = 3, "Среда"
    THURSDAY = 4, "Четверг"
    FRIDAY = 5, "Пятница"
    SATURDAY = 6, "Суббота"
    SUNDAY = 7, "Воскресенье"
```

Обращение к элементам перечисления:
```shell
>> WeekDays.THURSDAY.name
'THURSDAY'
>> WeekDays.THURSDAY.value
4
>> WeekDays.THURSDAY.term
'Четверг'
```

Проверка наличия значения в перечислении:
```shell
>> 4 in WeekDays
True
>> 8 in WeekDays
False
>> "Среда" in WeekDays
True
>> "Январь" in WeekDays
False
```

Получение элемента по строковому представлению:
```shell
>> friday = WeekDays["Пятница"]
>> type(friday)
<enum 'WeekDays'>
>> friday.name
'FRIDAY'
```
Получение элемента по числовому представлению:
```shell
>> tuesday = WeekDays[2]
>> type(tuesday)
<enum 'WeekDays'>
>> tuesday.name
'TUESDAY'
```
Получение отсутствующего элемента:
```shell
>> missed_element = WeekDays["Март"]
>> type(missed_element)
<class 'NoneType'>
```

Сравнение элементов перечисления, в т.ч. с другими объектами:<br>
__Строки возможно сравнить только на эквивалентность элементу перечисления. 
Для чисел доступны все виды сравнения.__
```shell
>> "Пятница" == WeekDays.FRIDAY
True
>> "Четверг" == WeekDays.FRIDAY
False
>> "Четверг" < WeekDays.FRIDAY
TypeError("Cannot compare with type <class 'str'>")
>> 5 >= WeekDays.FRIDAY
True
>> 4 >= WeekDays.FRIDAY
False
```

Приведение типов:
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

Дополнительные методы преобразования:
* `as_dict` &ndash; к словарю с сохранением имен ключей
```shell
>> WeekDays.WEDNESDAY.as_dict
{'value': 3, 'term': 'Среда'}
```
* `to_frontend` &ndash; к словарю для фронт-енда в виде элемента выпадающего 
списка
```shell
>> WeekDays.WEDNESDAY.to_frontend
{'id': 3, 'name': 'Среда'}
```