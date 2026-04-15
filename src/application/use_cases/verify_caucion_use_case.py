class VerifyCaucionUseCase:

    def __init__(self, page):
        self.page = page

    def execute(self):
        return self.page.get_title()