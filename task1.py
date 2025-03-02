# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
import doctest


class Steel:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Кастрюля"

        :param capacity_volume: Объем кастрюли
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> steel = Steel(700, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем кастрюли должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем кастрюли должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_steel(self) -> bool:
        """
        Функция которая проверяет является ли кастрюля пустым

        :return: Является ли кастрюля пустым

        Примеры:
        >>> steel = Steel(700, 0)
        >>> steel.is_empty_steel()
        """
        ...

    def add_water_to_steel(self, water: float) -> None:
        """
        Добавление воды в кастрюлю.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в кастрюле, то вызываем ошибку

        Примеры:
        >>> steel = Steel(700, 0)
        >>> steel.add_water_to_steel(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        ...

    def remove_water_from_steel(self, estimate_water: float) -> None:
        """
        Извлечение воды из кастрюли.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в кастрюле,
        то возвращается ошибка.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> steel = Steel(700, 700)
        >>> steel.remove_water_from_steel(200)
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    import doctest

class Wood:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Ложка"

        :param capacity_volume: Объем ложки
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> wood = Wood(200, 0)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем ложки должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем ложки должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_wood(self) -> bool:
        """
        Функция которая проверяет является ли ложка пустым

        :return: Является ли ложка пустым

        Примеры:
        >>> wood = Wood(200, 0)
        >>> wood.is_empty_wood ()
        """
        ...

    def add_water_to_wood(self, water: float) -> None:
        """
        Добавление воды в ложку.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в ложке, то вызываем ошибку

        Примеры:
        >>> wood = Wood(200, 0)
        >>> wood.add_water_to_wood(40)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        ...

    def remove_water_from_wood(self, estimate_water: float) -> None:
        """
        Извлечение воды из ложки.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в ложке,
        то возвращается ошибка.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> wood = Wood(200, 10)
        >>> wood.remove_water_from_wood(40)
        """
        ...







