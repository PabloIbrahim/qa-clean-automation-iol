from behave import when, then

@when("navega al simulador")
def step_nav(context):
    context.navigate_to_simulator.execute()

#@when("presiona comprar")
#def step_buy(context):
#    context.click_buy.execute()

@then('se visualiza "{title}"')
def step_verify(context, title):
    result = context.verify_simulator.execute()
    assert title in result