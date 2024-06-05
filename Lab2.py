#Tusk 1
import datetime

class Person:
    def __init__(self, surname, first_name, nickname=None, birth_date=None):
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        self.birth_date = self._parse_birth_date(birth_date)

    def _parse_birth_date(self, birth_date_str):
        if birth_date_str:
            year, month, day = map(int, birth_date_str.split('-'))
            return datetime.date(year, month, day)
        else:
            return None

    def get_age(self):
        if self.birth_date:
            today = datetime.date.today()
            age = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
            return str(age)
        else:
            return "Unknown"

    def get_fullname(self):
        return f"{self.surname} {self.first_name}"

# Приклад використання:
person1 = Person(surname="Блінда", first_name="Анатолій", birth_date="2005-01-31")
print(f"Повне ім'я: {person1.get_fullname()}")
print(f"Вік: {person1.get_age()} років")

