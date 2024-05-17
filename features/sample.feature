Feature: showing off behave

  Scenario: run a simple test
    Given we have behave installed
    When we implement a test
    And we implement a test
    Then behave will test it for us!

  Scenario Outline: Retrieve tokens
  Login using plain credentials and retrieve authentication data
    Given Endpoint page '<Endpoint>'
    When Open page with predefined endpoint
    Then Take screenshot of page

    @qa-instance
    Examples:
      | Endpoint           |
      | https://playwright.dev/docs/ci-intro |


  Scenario: run a simple test 1
    Given we have behave installed
    When we implement a test
    And we implement a fail test
    Then behave will test it for us!