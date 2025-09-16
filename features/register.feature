Feature: Register Account Functionality

  @register
  Scenario: Register with mandatory fields
    Given I navigate to register page
    When I enter details into mandatory fields
    And I select privacy policy option
    And I click on continue button
    Then account should get created

  @register
  Scenario: Register with all fields
    Given I navigate to register page
    When I enter details into all fields
    And I select privacy policy option
    And I click on continue button
    Then account should be created

  @register
  Scenario: Register with a duplicate email address
    Given I navigate to register page
    When I enter details into all fields except email field
    And I enter existing accounts email into email field
    And I select privacy policy option
    And I click on continue button
    Then Proper warning message informing about duplicate account should be displayed

  @register
  Scenario: Register without providing any details
    Given I navigate to register page
    When I dont enter anything into the fields
    And I click on continue button
    Then Proper warning messages for every mandatory fields should be displayed