Feature: Login
  In order to access to my personal workspace
  As a user
  I want to login in the system

  Background: There is a registered user
    Given Exists a user "username" with password "password"


  Scenario: Registered user wants to login to the system
    Given I login as user "username" with password "password"
    Then I'm viewing user "username" home page