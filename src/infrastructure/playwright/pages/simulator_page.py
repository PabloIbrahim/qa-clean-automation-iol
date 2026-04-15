class SimulatorPage:

    def __init__(self, page):
        self.page = page

    def go_to_simulator(self):
        self.page.click("text=Herramientas")
        self.page.click("text=Simulador")

    def click_buy(self):
        self.page.click("text=Comprar")

    def get_title(self):
        return self.page.locator("h1").inner_text()