class Settings:
    """
    Configuración global del framework
    """

    BASE_URL = "https://micuenta.invertironline.com/Ingresar"

    HEADLESS = False  # True para CI/CD

    BROWSER = "chromium"

    TIMEOUT = 60000