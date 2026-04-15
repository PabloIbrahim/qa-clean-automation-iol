class LoginUseCase:

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.open()

    def login(self, credentials):
        self.page.login(credentials)

    def is_logged(self):
        return self.page.is_logged()

    def has_login_error(self):
        return self.page.is_error_message_visible()

    def get_login_error(self):
        return self.page.get_error_message()