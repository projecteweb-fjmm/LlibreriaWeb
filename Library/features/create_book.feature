Feature: Register Book

  Background: There is a registered user and book
    Given Exists a user "username" with password "password"


  Scenario: Register a Book
    Given I login as user "username" with password "username"
    When I register book
      | title |
      | The 100 |
    Then Im viewing the details page for book
      | title |
      | The 100 |
    And There are 1 book
