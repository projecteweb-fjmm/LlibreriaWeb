Feature: Register Book
  In order to keep track of the books I visit
  As a user
  I want to register a book together with its location and contact details

  Background: There is a registered user
    Given Exists a user "admin" with password "admin"

  Scenario: Register just book title
    Given I login as user "admin" with password "admin"
    When I register book
      | title        |
      | The Tavern  |
    Then I'm viewing the details page for book by "admin"
      | title        |
      | The Tavern  |
    And There are 1 book

  Scenario: Register just book name and
    Given I login as user "admin" with password "admin"
    When I register book
      | title        | author      | isbn   |
      | The Tavern  | Josep Lladanosa    | England   |
    Then I'm viewing the details page for book by "admin"
      | title        | author      | isbn   |
      | The Tavern  | Josep Lladanosa   | England   |
    And There are 1 book

  Scenario: Try to register book but not logged in
    Given I'm not logged in
    When I register book
      | title        |
      | The Tavern  |
    Then I'm redirected to the login form
    And There are 0 book