Feature: Verify add book is successful or not

  Scenario: verify add book API functionality

    Given The book details added to library
    When We execute add book Post method
    Then Book should add successfully