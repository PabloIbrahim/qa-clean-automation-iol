from dataclasses import dataclass


@dataclass(frozen=True)
class Credentials:
    """
    Modelo de dominio para credenciales.
    """

    username: str
    password: str