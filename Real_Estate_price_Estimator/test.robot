*** Settings ***
Documentation    First time using robot framework, utilized on simple python script
Library           Process

*** Test Cases ***
Test Valid Input For City
    [Documentation]    Test calculation for city property type
    ${result}    Run Process    python3    REPE.py    stdin=1000\ncity
    Should Contain    ${result.stdout}    The estimated price for a 1000sq ft property in the city is: $250000
Test Valid Input For Suburb
    [Documentation]    Test calculation for city property type
    ${result}    Run Process    python3    REPE.py    stdin=1000\nsuburb
    Should Contain    ${result.stdout}    The estimated price for a 1000sq ft property in the suburb is: $150000

Test Invalid City type
    [Documentation]    Test calculation for city property type
    ${result}    Run Process    python3    REPE.py    stdin=1000\ninvalid
    Should Contain    ${result.stdout}    Error with type, only 2 valid types city and suburb

