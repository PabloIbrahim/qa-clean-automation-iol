from src.infrastructure.config.settings import Settings

class LoginPage:

    def __init__(self, page):
        self.page = page

        self.username_input = page.locator("#usuario")
        self.password_input = page.locator("#password")
        self.submit_button = page.locator("button[type='submit']")

        self.error_message = page.locator(".validation-summary-errors li")

    def open(self):
        self.page.goto("https://micuenta.invertironline.com/Ingresar")

    def login(self, credentials):

        # escribir como humano
        self.page.fill("#usuario", credentials.username)
        self.page.wait_for_timeout(500)

        self.page.fill("#password", credentials.password)
        self.page.wait_for_timeout(500)

        self.page.click("button[type='submit']")

        # esperar que aparezca algo de usuario logueado
        self.page.wait_for_selector("text=Mi cuenta", timeout=15000)

        # cerrar popup si aparece
        try:
            self.page.locator("button:has-text('×')").click(timeout=3000)
        except:
            pass

    def is_logged(self):
        return self.page.locator("text=Mi cuenta").is_visible()

    def is_error_message_visible(self) -> bool:
        return self.error_message.is_visible()

    def get_error_message(self) -> str:
        return self.error_message.inner_text()