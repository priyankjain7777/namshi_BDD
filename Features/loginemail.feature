Feature: login to namshi website

  Scenario Outline: login with email and password
    Given I launch chrome browser
    When I provide website url
    And Enter username "<user>" and password "<pwd>"
    And Click on login button
    And Check dashboard page
    Then logout to website

    Examples:
      | user                | pwd |
      | gowithpriyank@gmail.com | Test@777 |






