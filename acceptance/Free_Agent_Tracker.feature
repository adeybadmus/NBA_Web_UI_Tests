Feature: Free_Agent_Tracker_Feature
  As a fan
  In order to compare stats of players
  I want to interact with the advanced filter function

  Background:
	 Given I am on the "Players" page

  Scenario Outline: Free_Agent_Tracker_01 Test Player Availability
    When click "Players" on the menu
    And I click on "Fire Agent Tracker"
    And I select the "<text>" for Availability
    Then the New Team detail must be displayed for "<text>" and they should not change
    Examples:
    |text|
    |Signed|
    |Unsigned|


  Scenario Outline: Free_Agent_Tracker_02 Test Name Search Box
    When I click on "Fire Agent Tracker"
    And I search a "<player_name>" player name
    Then I should see the record for "<player_name>" player name displayed and they should not change
    Examples:
    |player_name|
    |valid|
    #|invalid|


  Scenario: Free_Agent_Tracker_03 Test Old Team Filter
    When I click on "Fire Agent Tracker"
    And I filter by Old team values "Chicago Bulls"
    Then I should see the correct stats displayed for "Chicago Bulls" and they should not change


  Scenario: Free_Agent_Tracker_04 Test New Team Filter
    When I click on "Fire Agent Tracker"
    And I filter by New team values "LA Clippers"
    Then I should see the correct stats displayed for "LA Clippers" and they should not change


  Scenario: Free_Agent_Tracker_05 Test Position Filter
    When I click on "Fire Agent Tracker"
    And I filter by Position values "Guard"
    Then I should see the correct stats displayed for "G" and they should not change