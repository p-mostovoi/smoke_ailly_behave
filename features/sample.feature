Feature: showing off behave

  Scenario: run a simple test
    Given we have behave installed
    When we implement a test
    And we implement a test
    Then behave will test it for us!


  Scenario: run a simple test 1
    Given we have behave installed
    When we implement a test
    And we implement a fail test
    Then behave will test it for us!