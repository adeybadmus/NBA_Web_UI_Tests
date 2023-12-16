Feature: Navigation between  pages
	As a fan
	In order to check mt team's performance
	I want to view stats on the NBA stats pages

Background:
	Given that Nba website is loaded


	Scenario: Navigation_01_Verify that user can navigate to standings page
		When I am on the HomePage
		And click "Standings" on the menu
		Then I should see overall information for all teams in the current regular season


	Scenario Outline: Navigation_02_Navigate homepage menus
		When I am on the HomePage
		And click on "<item>" on the menu
		Then I should navigate to the correct page for "<item>"
		Examples:
			|item|
			|  Games  	|
			|   Schedule |
			|Watch       |
			|News        |
			|In-Season Tournament|
			|Stats               |
			|Standings           |
			|Teams               |
			|Players             |
			|Future Starts Now   |
			|NBA Fitness         |