Feature: showing off behave

  Scenario Outline: Retrieve tokens
  Login using plain credentials and retrieve authentication data
    Given Endpoint page '<Endpoint>'
    When Open page with predefined endpoint
    Then Take screenshot of page

    @qa-instance
    Examples:
      | Endpoint           |
      | https://playwright.dev/docs/ci-intro |

