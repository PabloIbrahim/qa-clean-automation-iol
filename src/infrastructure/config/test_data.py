from src.domain.models.credentials import Credentials


class TestData:
    """
    Datos reutilizables para testing
    """

    VALID_CREDENTIALS = Credentials(
        username="ibrahimpablo@gmail.com",
        password="NNNNNNNNNNNN"
    )

    INVALID_USER = Credentials(
        username="usuario_invalido@test.com",
        password="Password123"
    )

    INVALID_PASSWORD = Credentials(
        username="ibrahimpablo@gmail.com",
        password="PasswordIncorrecta"
    )