from abc import ABC, abstractmethod
from src.domain.models.credentials import Credentials


class LoginPagePort(ABC):
    """
    Interfaz del dominio para la página de login.
    Define QUÉ se puede hacer, no CÓMO.
    """

    @abstractmethod
    def open(self) -> None:
        """Abre la página de login"""
        pass

    @abstractmethod
    def login(self, credentials: Credentials) -> None:
        """Realiza el login"""
        pass

    @abstractmethod
    def is_logged(self) -> bool:
        """Verifica si el usuario está logueado"""
        pass

    @abstractmethod
    def is_error_message_visible(self) -> bool:
        pass

    @abstractmethod
    def get_error_message(self) -> str:
        pass