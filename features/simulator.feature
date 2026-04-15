@simulador

Feature: Simulador

  Scenario: Probar simulador
    Given el usuario logueado en IOL
    When navega al simulador
    #And presiona comprar
    #Then se visualiza "Simulador de Inversiones - Comprar"
    Then se visualiza "Simulador de Inversiones"