class SimulateCaucionUseCase:

    def __init__(self, page):
        self.page = page

    def execute(self, amount):
        self.page.set_amount(amount)