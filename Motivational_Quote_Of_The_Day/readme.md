# Motivational Quote of the Day

## Project Level: Intermediate

### Project Description
This project is designed to help you practice and enhance your Python programming skills. The program reads a list of motivational quotes from a text file and displays one every Monday (or any day the program is run). Using Python's date handling capabilities, the program ensures a new quote is shown each time you run it.

---

### **Expected Output**
#### A) Scenario 1: If Monday  
The program checks the current day. If it is Monday, it displays a special message and picks a motivational quote from the `quotes.txt` file.  

**Example Output**:  
> "Happy Monday! Here’s your motivational quote to start the week:  
> *'The way to get started is to quit talking and begin doing.' - Walt Disney*"

#### B) Scenario 2: If Not Monday  
If it is not Monday, the program displays a different message while still providing a motivational quote.  

**Example Output**:  
> "Here’s your motivational quote to brighten your day:  
> *'Success is not the key to happiness. Happiness is the key to success.' - Albert Schweitzer*"

---

### **Learning Benefits**
This project helps reinforce key programming concepts:
1. **File Handling**  
   - Practice reading and processing data from a text file.  
   - Build a foundation for working with external resources like databases or logs.  

2. **Randomization**  
   - Use Python’s `random` module to select a random quote.  
   - Understand randomization for applications like recommendations or creative tools.

3. **String Processing**  
   - Parse and manipulate strings (e.g., slicing, trimming whitespace, and formatting).  
   - Practice text presentation techniques for better readability.

4. **Control Flow**  
   - Practice decision-making using `if-else` statements.  
   - Enhance skills in creating interactive and logic-driven programs.

5. **Output Formatting**  
   - Create user-friendly and engaging console outputs.  
   - Learn to structure your program's output for an improved user experience.

---

### **How to Run**
1. Ensure you have Python installed on your system.
2. Create a text file named `quotes.txt` in the same directory as the script.  
   - Add motivational quotes to this file, with one quote per line.
3. Run the Python script:
   ```bash
   python motivational_quote_of_the_day.py
