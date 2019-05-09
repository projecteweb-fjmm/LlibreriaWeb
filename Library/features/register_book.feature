Feature: User Adds Book
  In order to provide content to my users
  As an user
  I want to register a Book with all it's information

  Background: There is a registered user and book
    Given Exists an admin "admin" with password "admin"
    And No Exists Book registered

  Scenario: Register a Book with all info
    Given I login as admin "admin" with password "admin"
    And
    When I register the Book
      | title                     | author | summary | isb | genre | language |
      | El gato que quiso volar   | Jose Canas | Un gato quiero volar, para ello usa perico |  4444444489102| Drogadiccion | Castellano |
    Then I'm viewing the details page for the Degree
      | title                     | author | summary | isb | genre | language |
      | El gato que quiso volar   | Jose Canas | Un gato quiero volar, para ello usa perico |  4444444489102| Drogadiccion | Castellano |
    And There is 1 Book