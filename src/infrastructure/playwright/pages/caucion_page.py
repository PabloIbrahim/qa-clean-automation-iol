class CaucionPage:

    def __init__(self, page):
        self.page = page

    def go_to_caucion(self):
        self.page.click("text=Operar")
        self.page.click("text=Caucionar")
        self.page.click("text=Caución Colocadora")

    def set_amount(self, amount):
        self.page.fill("#amount", str(amount))

    def get_title(self):
        return self.page.locator("h1").inner_text()