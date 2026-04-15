@deposito
Feature: Ingreso de dinero

  Scenario: Validar acceso a ingresar dinero
    Given el usuario logueado en IOL
    When navega a Ingresar Dinero
    Then se observa el título "¿Cómo ingresar dinero?"