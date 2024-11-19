# Real Estate Price Estimator

## Project Level: Beginner  
This project is designed for beginners practicing Python fundamentals. It estimates the price of a property based on its size (in square feet) and location (city or suburb).

---

## Features
- **User Input**: Collects property size in square feet and location (city or suburb).  
- **Conditional Logic**: Determines price per square foot based on location.  
- **Calculations**: Estimates the property price using basic arithmetic.  
- **String Handling**: Ensures location input is case-insensitive using `.lower()`.  
- **Testing**: Uses Robot Framework to validate functionality with a simple test script.

---

## How It Works
1. The program prompts the user to enter the size of the property in square feet.  
2. The user inputs either "city" or "suburb" for the location.  
   - **City**: Price per square foot is $250.  
   - **Suburb**: Price per square foot is $150.  
3. The program calculates the estimated property price and displays the result.

---

## Example Output
Enter the size of the property in square feet: 1000 
<br>Enter the location (city/suburb): city 
<br>The estimated price of the property is $250000.



---

## Robot Framework Test Example
This project is tested using the Robot Framework. Below is an example test script:

```robot
*** Settings ***
Documentation    First time using robot framework, utilized on simple python script
Library           Process

*** Test Cases ***
Test Valid Input For City
    [Documentation]    Test calculation for city property type
    ${result}    Run Process    python3    REPE.py    stdin=1000\ncity
    Should Contain    ${result.stdout}    The estimated price for a 1000sq ft property in the city is: $250000