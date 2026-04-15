@login

Feature: Login IOL

  Scenario: Login exitoso
    Given el usuario abre la página de login de IOL
    When ingresa credenciales válidas
    Then el login es exitoso

  Scenario: Usuario inválido
    Given el usuario abre la página de login de IOL
    When ingresa usuario inválido
    Then se muestra mensaje de error de login

  Scenario: Contraseña inválida
    Given el usuario abre la página de login de IOL
    When ingresa contraseña inválida
    Then se muestra mensaje de error de login