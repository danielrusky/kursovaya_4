from abc import ABC, abstractmethod

import requests

from vacancy import Vacancy


class APIInteraction(ABC):
    @abstractmethod
    def request(self):
        """
    Создаем метод для получения страницы со списком вакансий.
        """
        pass
