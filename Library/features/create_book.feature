Feature: Register Book
  Given Exists a user "username" with password "password"

Scenario: Register just book title
  Given I login as user "username" with password "password"
  When  I register book
    | title | author | summary | isbn | genre | language | date_published |
    | The 100 | Roger Jenkins | Survival apocalipse world | 891-874-845-X | Aventura | Castellano | 10/05/2019 |
  Then There are 1 book