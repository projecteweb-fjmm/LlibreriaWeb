Feature: Edit Book
  In order to keep updated my previos registers about book
  As a user
  I wan t to edit a book register I created

  Background: There are registered users and a book by one of them
    Given Exists a user "username" with password "password"
    And Exists book registered by "username"
      | title                        |
      | El gato que quiso volar alto |

    Scenario: Edit owned book registry title
      Given I login as user "username" with password "password"
      When I view the details for book "title"
      And I edit the current book
        | title                           | author | user |
        |  El gato que quiso volar alto 2 | Jose Cañas | username |
      Then I will view the details page for book
        | title                        |
        | El gato que quiso volar alto 2 |

    Scenario: Try to edit dish but not logged in
      Given I'm not logged in
      When I view the details for book
      Then There is no "edit" link available

    Scenario: Try to edit book but not the owner
      Given I login as user "username" with password "password"
      When I view the details for book
      Then There is no "edit" link available

    Scenario: Delete a Book
      Then I can delete Book




