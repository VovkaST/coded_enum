from enum import Enum, EnumMeta
from typing import Union


class CodedEnumMeta(EnumMeta):
    """
    Мета-класс перечислений для реализации функционала работы
    с классом CodedValue.
    """

    def __new__(mcs, cls, bases, classdict, **kwds):
        enum_class = super().__new__(mcs, cls, bases, classdict, **kwds)
        # Составим заново карту значений и элементов перечисления
        enum_class._value2member_map_ = {}
        for member_name in enum_class.__members__:
            member_instance = getattr(enum_class, member_name)
            # Добавим ссылки на элемент по его ключу и значению.
            item_map = {
                member_instance.value: member_instance,
                member_instance.term: member_instance,
            }
            # Преобразуем коды (числа в виде строк) в действительные числа
            # и также добавим в карту
            if (
                isinstance(member_instance.value, str)
                and member_instance.value.isdigit()
            ):
                item_map.update({int(member_instance.value): member_instance})
            # Преобразуем коды (целые числа) в строки и также добавим в карту
            elif isinstance(member_instance.value, int):
                item_map.update({str(member_instance.value): member_instance})
            enum_class._value2member_map_.update(item_map)
        return enum_class

    def __call__(
        cls,
        value,
        names=None,
        *,
        module=None,
        qualname=None,
        type=None,
        start=1,
    ):
        if isinstance(value, tuple):
            value, *_ = value
        return cls.__new__(cls, value)

    def __getitem__(self, item):
        if item in self._value2member_map_:
            return self._value2member_map_[item]

    def __contains__(cls, item):
        for value_instance in cls._member_map_.values():
            if item in value_instance:
                return True
        return False


COMPARE_ERROR_TEMPLATE = "Cannot compare with type {}"


class CodedValue(Enum):
    """
    Класс элемента кодифицированного перечисления. На вход в качестве кода
    может принимать число в виде строки. Оно будет преобразовано к целому
    числу.
    """

    def __init__(self, value: Union[int, str], term: str):
        if isinstance(value, str) and value.isdigit():
            # Приведем число, переданное в виде строки, к целому
            value = int(value)
        self._value = value
        self._term = term

    def __int__(self):
        return self.value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f"{self.value}: {self.term}"

    @property
    def value(self) -> int:
        return self._value

    @property
    def term(self) -> str:
        return self._term

    @property
    def as_dict(self):
        return {
            "value": self.value,
            "term": self.term,
        }

    @property
    def to_frontend(self):
        return {
            "id": self.value,
            "name": self.term,
        }

    def __hash__(self):
        return self._value.__hash__()

    def __contains__(self, item):
        return item in [self.value, self.term]

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other
        if isinstance(other, str) or other is None:
            return self.term == other
        if isinstance(other, self.__class__):
            return self.value == other.value
        return TypeError(COMPARE_ERROR_TEMPLATE.format(type(other)))

    def __ne__(self, other):
        if isinstance(other, int):
            return self.value != other
        if isinstance(other, str):
            return self.term != other
        if isinstance(other, self.__class__):
            return self.value != other.value
        return TypeError(COMPARE_ERROR_TEMPLATE.format(type(other)))

    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other
        if isinstance(other, self.__class__):
            return self.value < other.value
        return TypeError(COMPARE_ERROR_TEMPLATE.format(type(other)))

    def __gt__(self, other):
        if isinstance(other, int):
            return self.value > other
        if isinstance(other, self.__class__):
            return self.value > other.value
        return TypeError(COMPARE_ERROR_TEMPLATE.format(type(other)))

    def __le__(self, other):
        if isinstance(other, int):
            return self.value <= other
        if isinstance(other, self.__class__):
            return self.value <= other.value
        return TypeError(COMPARE_ERROR_TEMPLATE.format(type(other)))

    def __ge__(self, other):
        if isinstance(other, int):
            return self.value >= other
        if isinstance(other, self.__class__):
            return self.value >= other.value
        return TypeError(COMPARE_ERROR_TEMPLATE.format(type(other)))


class CodedEnum(CodedValue, metaclass=CodedEnumMeta):
    """Реализация класса кодифицированного перечисления.
    Для создания перечисления необходимо создать класс, унаследованный
    от CodedEnum и объявить его элементы в виде кортежа, где первый элемент
    является числом (кодом значения), второй - строкой (строковым
    представлением), например::

        class WeekDays(CodedEnum):
            MONDAY = 1, "Понедельник"
            TUESDAY = 2, "Вторник"
            WEDNESDAY = 3, "Среда"
            THURSDAY = 4, "Четверг"
            FRIDAY = 5, "Пятница"
            SATURDAY = 6, "Суббота"
            SUNDAY = 7, "Воскресенье"
    """

    pass
