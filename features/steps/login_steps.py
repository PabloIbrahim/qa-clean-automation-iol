from behave import given, when, then
from src.infrastructure.config.test_data import TestData

@given("el usuario abre la página de login de IOL")
def step_open(context):
    context.login_use_case.open()

@when("ingresa credenciales válidas")
def step_login(context):
    context.login_use_case.login(TestData.VALID_CREDENTIALS)

@then("el login es exitoso")
def step_verify(context):
    assert context.login_use_case.is_logged()

@given("el usuario logueado en IOL")
def step_user_logged(context):
    context.login_use_case.open()
    context.login_use_case.login(TestData.VALID_CREDENTIALS)

@when("ingresa usuario inválido")
def step_invalid_user(context):
    context.login_use_case.login(TestData.INVALID_USER)


@when("ingresa contraseña inválida")
def step_invalid_password(context):
    context.login_use_case.login(TestData.INVALID_PASSWORD)


@then("se muestra mensaje de error de login")
def step_verify_error(context):

    assert context.login_use_case.has_login_error(), \
        "No se visualiza mensaje de error"

    error_text = context.login_use_case.get_login_error()

    assert "no coinciden" in error_text.lower(), \
        f"Mensaje inesperado: {error_text}"

