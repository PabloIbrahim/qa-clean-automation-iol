class BasePage:
    """
    Clase base para todas las páginas.
    Encapsula acciones comunes de Playwright.
    """

    def __init__(self, page):
        self.page = page

    def navigate(self, url: str) -> None:
        self.page.goto(url)

    def click(self, selector: str) -> None:
        self.page.locator(selector).click()

    def fill(self, selector: str, value: str) -> None:
        self.page.locator(selector).fill(value)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()

    def is_visible(self, selector: str) -> bool:
        return self.page.locator(selector).is_visible()

    def wait_for(self, selector: str) -> None:
        self.page.wait_for_selector(selector)

    def get_current_url(self) -> str:
        return self.page.url

    def close_popup_if_present(self):
        """
        Cierra el popup de IOL si aparece.
        No rompe si no existe.
        """

        try:
            close_button = self.page.locator("button:has-text('×'), .close, [aria-label='Close']")

            if close_button.is_visible(timeout=2000):
                close_button.click()
                print("🟡 Popup cerrado")

        except Exception:
            # No existe popup → seguimos normal
            pass