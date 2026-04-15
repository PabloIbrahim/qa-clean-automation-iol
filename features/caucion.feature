@caucion

Feature: Caución colocadora

  Scenario: Simular caución
    Given el usuario logueado en IOL
    When navega a Caución Colocadora
    #And ingresa monto 5000
    Then se visualiza el título "Cauciones"