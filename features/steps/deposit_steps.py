from behave import when, then

@when('navega a Ingresar Dinero')
def step_navigate_deposit(context):
    context.navigate_to_deposit.execute()

@then('se observa el título "{title}"')
def step_verify_title(context, title):
    result = context.verify_deposit.execute()

    assert title.lower() in result.lower(), \
        f"Se esperaba '{title}' pero se obtuvo '{result}'"