class NavigateToDepositUseCase:

    def __init__(self, page):
        self.page = page

    def execute(self):
        self.page.go_to_deposit()
