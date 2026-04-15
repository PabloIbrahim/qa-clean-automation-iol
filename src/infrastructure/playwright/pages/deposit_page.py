from src.infrastructure.playwright.pages.base_page import BasePage

class DepositPage(BasePage):
    # SELECTORES
    DEPOSIT_BUTTON = "#btn-ecc-ingresar-dinero"
    TITLE = "h2.iol-font-title"

    def go_to_deposit(self):
        self.page.click("text=Mi Cuenta")
        self.page.click("text=Ingresar / Retirar dinero")
        self.page.click("text=Ingresar Dinero")

        self.page.wait_for_selector(self.TITLE, timeout=15000)

    def get_title(self):
        self.page.wait_for_selector(self.TITLE, timeout=15000)
        return self.page.locator(self.TITLE).inner_text().strip()

