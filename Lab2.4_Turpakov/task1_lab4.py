class IoTDevice:
    """
    Базовый класс для устройств Интернета вещей (IoT).
    Атрибуты:
        device_id (str): Уникальный идентификатор устройства.
        status (bool): Статус устройства (включено/выключено).
        _firmware_version (str): Непубличная версия прошивки устройства.
    Методы:
        __init__(self, device_id: str, firmware_version: str):
            Конструктор класса IoTDevice.
        __str__(self) -> str:
            Возвращает строковое представление объекта.
        __repr__(self) -> str:
            Возвращает строковое представление для разработчиков.
        _check_firmware_update(self) -> bool:
            Проверяет наличие обновлений прошивки (непубличный метод).
    """

    def __init__(self, device_id: str, firmware_version: str):
        self.device_id = device_id
        self.status = False
        self._firmware_version = firmware_version

    def __str__(self) -> str:
        return f"IoTDevice {self.device_id} (Status: {'On' if self.status else 'Off'})"

    def __repr__(self) -> str:
        return f"IoTDevice(device_id={self.device_id}, status={self.status}, firmware_version={self._firmware_version})"

    def _check_firmware_update(self) -> bool:
        pass


class SmartHome(IoTDevice):
    """
    Класс для умного дома, наследуемый от IoTDevice.
    Атрибуты:
        device_id (str): Уникальный идентификатор устройства.
        status (bool): Статус устройства (включено/выключено).
        _firmware_version (str): Непубличная версия прошивки устройства.
        rooms (list): Список комнат в умном доме.
    Методы:
        __init__(self, device_id: str, firmware_version: str, rooms: list):
            Конструктор класса SmartHome.
        __str__(self) -> str:
            Возвращает строковое представление объекта.
        __repr__(self) -> str:
            Возвращает строковое представление для разработчиков.
        control_room_lights(self, room_name: str, turn_on: bool):
            Управляет освещением в указанной комнате.
        _check_firmware_update(self) -> bool:
            Перегруженный метод для проверки обновлений прошивки.
    """

    def __init__(self, device_id: str, firmware_version: str, rooms: list):
        super().__init__(device_id, firmware_version)
        self.rooms = rooms

    def __str__(self) -> str:
        return super().__str__() + f", Rooms: {len(self.rooms)}"

    def __repr__(self) -> str:
        return super().__repr__()[:-1] + f", rooms={self.rooms})"

    def control_room_lights(self, room_name: str, turn_on: bool):
        """
        Управляет освещением в указанной комнате.
        Аргументы:
            room_name (str): Название комнаты.
            turn_on (bool): Включить ли освещение.
        Возвращает:
            None
        """
        if room_name in self.rooms:
            pass

    def _check_firmware_update(self) -> bool:
        """
        Перегруженный метод для проверки обновлений прошивки.
        Причина перегрузки:
            Для умного дома может быть специфическая логика проверки обновлений, отличная от базового устройства IoT.
        """
        pass


class SmartCar(IoTDevice):
    """
    Класс для умного автомобиля, наследуемый от IoTDevice.
    Атрибуты:
        device_id (str): Уникальный идентификатор устройства.
        status (bool): Статус устройства (включено/выключено).
        _firmware_version (str): Непубличная версия прошивки устройства.
        model (str): Модель автомобиля.
        _engine_status (bool): Непубличный статус двигателя.
    Методы:
        __init__(self, device_id: str, firmware_version: str, model: str):
            Расширенный конструктор класса SmartCar.
        __str__(self) -> str:
            Перегружает строковое представление объекта.
        __repr__(self) -> str:
            Перегружает строковое представление для разработчиков.
        start_engine(self):
            Запускает двигатель автомобиля.
        _check_firmware_update(self) -> bool:
            Перегруженный метод для проверки обновлений прошивки.
    """

    def __init__(self, device_id: str, firmware_version: str, model: str):
        super().__init__(device_id, firmware_version)
        self.model = model
        self._engine_status = False

    def __str__(self) -> str:
        return f"SmartCar {self.model} (Status: {'On' if self.status else 'Off'})"

    def __repr__(self) -> str:
        return f"SmartCar(device_id={self.device_id}, status={self.status}, firmware_version={self._firmware_version}, model={self.model})"

    def start_engine(self):
        """Запускает двигатель автомобиля."""
        self._engine_status = True

    def _check_firmware_update(self) -> bool:
        """
        Перегруженный метод для проверки обновлений прошивки.
        Причина перегрузки:
            Умные автомобили могут иметь специфическую логику проверки обновлений, отличную от других устройств IoT.
        """
        pass