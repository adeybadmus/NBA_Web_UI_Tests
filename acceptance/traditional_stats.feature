Feature: Traditional_Stats_Page_Feature
  As a fan
  I want to interact with the traditional stats filsters
  In order get valid stats of teams

  Background:
	 Given I am on the "Tradition Stats" page

  Scenario Outline: Free_Agent_Tracker_01 Test Player Availability
    When click "Players" on the menu
    And I click on "Fire Agent Tracker"
    And I select the "<text>" for Availability
    Then the New Team detail must be displayed for "<text>" and they should not change
    Examples:
    |text|
    |Signed|
    |Unsigned|