from behave import when, then

@when("navega a Caución Colocadora")
def step_nav(context):
    context.navigate_to_caucion.execute()

#@when("ingresa monto 5000")
#def step_amount(context):
#    context.simulate_caucion.execute(5000)

@then('se visualiza el título "{title}"')
def step_verify(context, title):
    result = context.verify_caucion.execute()
    assert title in result