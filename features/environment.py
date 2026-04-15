import allure
from src.infrastructure.playwright.browser.browser_manager import BrowserManager

from src.infrastructure.playwright.pages.login_page import LoginPage
from src.infrastructure.playwright.pages.deposit_page import DepositPage
from src.infrastructure.playwright.pages.caucion_page import CaucionPage
from src.infrastructure.playwright.pages.simulator_page import SimulatorPage

from src.application.use_cases.login_use_case import LoginUseCase
from src.application.use_cases.navigate_to_deposit_use_case import NavigateToDepositUseCase
from src.application.use_cases.verify_deposit_page_use_case import VerifyDepositPageUseCase
from src.application.use_cases.navigate_to_caucion_use_case import NavigateToCaucionUseCase
from src.application.use_cases.simulate_caucion_use_case import SimulateCaucionUseCase
from src.application.use_cases.verify_caucion_use_case import VerifyCaucionUseCase
from src.application.use_cases.navigate_to_simulator_use_case import NavigateToSimulatorUseCase
from src.application.use_cases.click_buy_use_case import ClickBuyUseCase
from src.application.use_cases.verify_simulator_use_case import VerifySimulatorUseCase
from src.infrastructure.playwright.pages.deposit_page import DepositPage

def before_all(context):
    print("🔵 Inicio ejecución")


def before_scenario(context, scenario):
    print(f"🚀 Escenario: {scenario.name}")

    context.browser_manager = BrowserManager()
    page = context.browser_manager.start()
    context.page = page



    login_page = LoginPage(page)
    deposit_page = DepositPage(page)
    caucion_page = CaucionPage(page)
    simulator_page = SimulatorPage(page)

    # 👉 GUARDAR EN CONTEXT (CLAVE)
    context.deposit_page = deposit_page

    # Use Cases
    context.login_use_case = LoginUseCase(login_page)

    context.navigate_to_deposit = NavigateToDepositUseCase(deposit_page)
    context.verify_deposit = VerifyDepositPageUseCase(deposit_page)

    context.navigate_to_caucion = NavigateToCaucionUseCase(caucion_page)
    context.simulate_caucion = SimulateCaucionUseCase(caucion_page)
    context.verify_caucion = VerifyCaucionUseCase(caucion_page)

    context.navigate_to_simulator = NavigateToSimulatorUseCase(simulator_page)
    context.click_buy = ClickBuyUseCase(simulator_page)
    context.verify_simulator = VerifySimulatorUseCase(simulator_page)


def after_scenario(context, scenario):
    try:
        screenshot = context.page.screenshot(full_page=True)
        allure.attach(screenshot, name=scenario.name, attachment_type=allure.attachment_type.PNG)

        allure.attach(
            f"Resultado: {scenario.status}",
            name="Resultado",
            attachment_type=allure.attachment_type.TEXT
        )
    finally:
        context.browser_manager.stop()

def after_step(context, step):

    # cerrar popup SIEMPRE después de cada paso
    try:
        if hasattr(context, "page"):
            from src.infrastructure.playwright.pages.base_page import BasePage
            BasePage(context.page).close_popup_if_present()
    except:
        pass

    if step.status == "failed":
        screenshot = context.page.screenshot(full_page=True)
        allure.attach(screenshot, name=step.name, attachment_type=allure.attachment_type.PNG)

