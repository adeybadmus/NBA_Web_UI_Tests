Feature: Traditional_Stats_Page_Feature
  As a fan
  I want to interact with the traditional stats filsters
  In order get valid stats of teams

  Background:
	 Given I am on the "Traditional Stats" page

  Scenario: Tradition_Stats_Feature_01 Test Season Filter
    When I filter by season "season" value "2018-19"
    Then I should see the Pills value equal to the correct value "2018-19"


  Scenario: Tradition_Stats_Feature_02 Test Season Type Filter
    When I filter by season_type "season_type" value "Playoffs"
    Then I should see the Pills value equal to the correct value "Playoffs"



  Scenario: Tradition_Stats_Feature_03 Test Per Mode Filter
    When I filter by per_mode "per_mode" value "Per 1 Minute"
    Then I should see the Pills value equal to the correct value "Per 1 Minute"



  Scenario: Tradition_Stats_Feature_04 Test Season Segment Filter
    When I filter by season_segment "season_segment" value "Pre All-Star"
    Then I should see the Pills value equal to the correct value "Pre All-Star"


  Scenario Outline: Tradition_Stats_Feature_05 Test Multiple Filters - Per Mode and Season Segment
    When I filter by "<filter1>>" value "<value1>" and "<filter2>" value "<value2>"
    Then I should see the Pills values equal to the correct values "<value1>" and "<value2>"
    Examples:
    |filter1|value1|filter2|value2|
    |season |2020-21|season_type|In-Season Tournament|
    |season_type|Playoffs|per_mode|Per 1 Play|
    |season     |2007-08  |season_segment|Last 10 Games|
    |season_type    |All Star  |per_mode|Per Game|