Feature: Login Functionality

  @login
  Scenario: Login with valid credentials
    Given I navigated to login page
    When I enter valid email address and valid password into the fields
    And I click on login button
    Then I should get logged in

  @login
  Scenario: Login with invalid email and valid password
    Given I navigated to login page
    When I enter invalid email address and valid password into the fields
    And I click on login button
    Then I should get a proper warning message

  @login
  Scenario: Login with valid email and invalid password
    Given I navigated to login page
    When I enter valid email address and invalid password into the fields
    And I click on login button
    Then I should get a proper warning message

  @login
  Scenario: Login with invalid email and invalid password
    Given I navigated to login page
    When I enter invalid email address and invalid password into the fields
    And I click on login button
    Then I should get a proper warning message

  @login
  Scenario: Login without entering any credentials
    Given I navigated to login page
    When I dont enter anything into email and password fields
    And I click on login button
    Then I should get a proper warning message