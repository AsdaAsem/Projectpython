Feature: saucedemo Login

  Scenario: check site is loaded successfully
    Given I launch Chrome browser
    When I open SWAGLABS Homepage
    Then login form must be available
    And close the bowser

  Scenario: Check login/logout
    Given I launch Chrome browser
    When I open SWAGLABS Homepage
    Given Enter username "standard_user" and password "secret_sauce"
    And Click on login button
    Then User must succesfully login to Dashboard page
    When User click on logout
    Then user must be successully logout

  Scenario: Check login functionality using valid parameters
    Given I launch Chrome browser
    When I open SWAGLABS Homepage
    Given Enter username "standard_user" and password "secret_sauce"
    And Click on login button
    Then User must succesfully login to Dashboard page

  Scenario Outline: Check login functionality with valid parameters
    Given I launch Chrome browser
    When I open SWAGLABS Homepage
    Given Enter username "<name>" and password "<password>"
    And Click on login button
    Then User must succesfully login to Dashboard page

    Examples: Credentials
      | name          | password     |
      | standard_user | secret_sauce |

  Scenario Outline: Item addition
    Given I launch Chrome browser
    When I open SWAGLABS Homepage
    Given Enter username "standard_user" and password "secret_sauce"
    And Click on login button
    Then User must succesfully login to Dashboard page
    And Adding all carts
    And  shoping cart
    And Checkout
    And Enter "<FirstName>","<LastName>" And "<PostalCode>"
    Then click on Continue
    Examples:
      | FirstName | LastName | PostalCode |
      | Asem      | empty    | empty      |
      | Asem      | Asda     | empty      |
      | Asem      | empty    | 12345      |
      | empty     | Asda     | empty      |
      | empty     | Asda     | 12345      |
      | empty     | empty    | 12345      |
      | Asem      | Asda     | 12345      |


  Scenario: Check login functionality using invalid parameters
    Given I launch Chrome browser
    When I open SWAGLABS Homepage
    Given Enter username "standard_user" and password "empty"
    And Click on login button
    Then User must not succesfully login to Dashboard page

  Scenario Outline: Check login functionality with invalid parameters
    Given I launch Chrome browser
    When I open SWAGLABS Homepage
    Given Enter username "<name>" and password "<password>"
    And Click on login button
    Then User must not succesfully login to Dashboard page

    Examples: Credentials
      | name            | password     |
      | standard_user   | empty        |
      | locked_out_user | secret_sauce |
      | problem_user    |54352         |

