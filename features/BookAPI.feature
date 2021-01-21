Feature: Verify add book is successful or not
  @library
  Scenario: verify add book API functionality
    Given The book details added to library
    When We execute add book Post method
    Then Book should add successfully

  @library
  Scenario Outline: verify add book API functionality
    Given The book details added with "<isbn>" and "<aisle>"
    When We execute add book Post method
    Then Book should add successfully
    Examples:
      | isbn    |aisle  |
      | hvhvh       |12395  |
      | gyfyg       |1279  |