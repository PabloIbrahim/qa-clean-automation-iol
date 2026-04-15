from playwright.sync_api import sync_playwright
from src.infrastructure.config.settings import Settings


class BrowserManager:
    """
    Maneja el ciclo de vida del navegador
    """

    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def start(self):

        self.playwright = sync_playwright().start()

        # 1. Lanzar navegador con anti-detección
        self.browser = self.playwright.chromium.launch(
            headless=Settings.HEADLESS,
            args=["--disable-blink-features=AutomationControlled"]
        )

        # 2. Crear contexto más "humano"
        context = self.browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36",
            viewport={"width": 1366, "height": 768}
        )

        # 3. Crear página
        self.page = context.new_page()

        # 4. Ocultar Playwright (MUY IMPORTANTE)
        self.page.add_init_script("""
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """)

        # 5. Timeout global
        self.page.set_default_timeout(Settings.TIMEOUT)

        return self.page

    def stop(self):
        """
        Cierra navegador y libera recursos
        """

        if self.page:
            self.page.close()

        if self.browser:
            self.browser.close()

        if self.playwright:
            self.playwright.stop()