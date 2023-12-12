Feature: Free_Agent_Tracker_Feature
  As a fan
  In order to compare stats of players
  I want to interact with the advanced filter function

  Background:
	Given that Nba website is loaded

#  Scenario Outline: Free_Agent_Tracker_01 Test Player Availability
#    When click "Players" on the menu
#    And I click on "Fire Agent Tracker"
#    And I select the "<text>" for Availability
#    Then the New Team detail must be displayed for "<text>" and they should not change
#    Examples:
#    |text|
#    |Signed|
#    |Unsigned|

  Scenario Outline: Free_Agent_Tracker_02 Test Name Search Box
    When click "Players" on the menu
    And I click on "Fire Agent Tracker"
    And I search a valid the a "<player_name>"
   # Then I should see the record for "<player_name>" player name displayed and they should not change
    Examples:
    |player_name|
    |valid|
    |invalid|
