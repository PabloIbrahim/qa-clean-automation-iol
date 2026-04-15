class ClickBuyUseCase:

    def __init__(self, page):
        self.page = page

    def execute(self):
        self.page.click_buy()