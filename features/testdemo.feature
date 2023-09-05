Feature: Library Information System GUI test

  Scenario Outline: Logon Screen
     Given the logon page <username>
     And the logon <password>
     When click on logon
     Then the logon is <status>
    Examples:
       |  username      |     password         | status         |
       |  correct       |    correct           | OK             |
       |  not_existed   |    abc               | failed         |
