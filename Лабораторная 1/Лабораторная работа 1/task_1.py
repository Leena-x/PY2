# TODO Написать 3 класса с документацией и аннотацией типов


class Cat:
    def __init__(self, breed: str, weight: (float, int)):
        """
        Создание и подготовка к работе объекта кот
        :param breed: порода кошки
        :param weight: вес кошки
        """
        if not isinstance(breed, str):
            raise TypeError("Порода кошки должна быть типа str")
        self.breed = breed

        if not isinstance(weight, (float, int)):
            raise TypeError("Вес кошки должен быть типа float или int")
        if weight <= 0:
            raise ValueError("Вес не может быть равно нулю или быть отрицательной")
        self.weight = weight

    def cat_in(self) -> None:
        """ впустить кошку """
        ...

    def cat_out(self) -> None:
        """
        выпустить кошку
        Примеры:
        >>> cat1 = Cat("Toyger", 4700)
        >>> cat1.cat_in()
        """
        ...


class Safe:
    def __init__(self, color: str, alive: bool, volume: (float, int)):
        """
               Создание и подготовка к работе безопасного объекта
               :param color: цвет безопасного объекта
               :param alive: объект живое или нет
               """
        if not isinstance(color, str):
            raise TypeError("Цвет безопасного объекта должен быть типа str")
        self.color = color

        if not isinstance(alive, bool):
            raise TypeError("Жизнеспособность безопасного объекта должна быть типа bool")
        self.alive = alive

        if not isinstance(volume, (float, int)):
            raise TypeError("Объем безопасного объекта должен быть типа float или int")
        if volume < 0:
            raise ValueError("Объем безопасного объекта должен быть неотрицательным")
        self.volume = volume

    def object_out(self) -> None:
        """Положили безопасный объект в коробку"""
        ...

    def object_in(self, volume_box: float) -> None:
        """
        Добавляем безопасный объект в коробку
        :param volume_box: объем коробки
        >>>safe_object = Safe("белый", False, 5)
        >>>safe_object.object_in(5)
        """
        if not isinstance(volume_box, (float, int)):
            raise TypeError("Объем коробки должен быть типа float или int")
        if volume_box <= 0:
            raise ValueError("Объем коробки не должен быть неположительным")
        ...


class StudyGroup:
    def __init__(self, name: str, number: int):
        """
         Создание и подготовка к работе объекта учебная группа, который создает список учебной группы
         :param name: Имя студента
         :param number: Номер студента в списке группы
         """
        if not isinstance(name, str):
            raise TypeError("Имя студента должно быть типа str")
        self.name = name

        if not isinstance(number, int):
            raise TypeError("Номер студента в списке группы должно быть типа str ")
        if number < 0:
            raise ValueError("Номер не может быть отрицательным")
        self.number = number

    def add_student(self, name: str, number: int) -> None:
        """
        Добавление нового студента в список группы
        :param name: Имя нового студента
        :param number: Номер в списке нового студента
        >>> group1 = StudyGroup("Иван", 1)
        >>> group1.add_student("Игорь", 2)
        """
        if not isinstance(name, str):
            raise TypeError("Имя студента должно быть типа str")
        self.name = name

        if not isinstance(number, int):
            raise TypeError("Номер студента в списке группы должно быть типа str ")
        if number < 0:
            raise ValueError("Номер не может быть отрицательным")
        self.number = number
        ...


    def delete_student(self, name: str, number: int) -> None:
        """
        удаление студента из списка группы
        :param name: Имя студента, которого нужно убрать из списка
        :param number: Номер студенда, которого нужно убрать из списка
        """
        if not isinstance(name, str):
            raise TypeError("Имя студента должно быть типа str")
        self.name = name

        if not isinstance(number, int):
            raise TypeError("Номер студента в списке группы должно быть типа str ")
        if number < 0:
            raise ValueError("Номер не может быть отрицательным")
        self.number = number
        ...

    # TODO работоспособность экземпляров класса проверить с помощью doctest

import doctest
if __name__ == "__main__":
     doctest.testmod()
