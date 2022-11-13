Feature: login to namshi website

  Scenario Outline: login with email and password
    Given I launch chrome browser
    When I provide website url
    And Enter username "<username>" and password "<password>"
    And Click on login button
    And Check dashboard page
    Then User must login to website

    Examples:
      | username                | password |
      | gowithpriyank@gmail.com | Test@777 |






