Feature: Traditional_Stats_Page_Feature
  As a fan
  I want to interact with the traditional stats filsters
  In order get valid stats of teams

  Background:
	 Given I am on the "Traditional" page

  Scenario: Tradition_Stats_Feature_01 Test Season Filter
    When I filter by season values "2018-19"
    Then I should see the Pills value equal to the correct season value selected

