# 2025-ITELEC2-LAB010
Week 04 - Conditional Statements

Laboratory # 10 - Guided Coding Exercise: if...elif...else Statement in Python

## **Instructions**

### **Step 1.1: Accept the Assignment**

   1. Click on the assignment link provided by your instructor.
   2. GitHub Classroom will create a **private repository** under your GitHub account.
   3. After the repository is created, click **"Go to Repository"** to view your assignment.

---

### **Step 1.2: Setup your Git Environment**
Only perform this if this is the first time you will setup your Git Environment

   1. Create a GitHub Account:
   ```bash
   https://github.com/signup?source=login
   ```
      
   2. Download and Install Git on your Laptop/Desktop:
   ```bash
   https://git-scm.com/downloads
   ```
   
   3. Create a Folder in your Laptop/Desktop
   4. Right-click anywhere in the created folder and select "Open Git Bash Here".
   5. In the Git Bash Terminal, set your git name, perform command:
   ```bash
   git config --global user.name "Your Name"
   ```
   
   6. In the Git Bash Terminal, set your git email, perform command:
   ```bash
   git config --global user.email "your.email@example.com"
   ```
   
   7. Create your SSH Key, just follow the instructions, no need to provide filename and passphrase. In the Git Bash Terminal, perform command:
   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```
   
   8. Copy your SSH Keys into clipboard. In the Git Bash Terminal, perform command:
   ```bash
   clip < ~/.ssh/id_rsa.pub
   ```
   
   9. Log in to your GitHub account.
   10. In the upper-right corner of GitHub, click your profile picture and select Settings.
   11. In the left sidebar, click on SSH and GPG keys.
   12. Click the New SSH key button.
   13. In the Title field, give the key a recognizable name (e.g., "My Windows Laptop").
   14. In the Key field, CTRL + V or paste the keys copied into your clipboard. Save the key.
   15. Go Back to terminal, use command:
   ```bash
   ssh -T git@github.com
   ```

### **Step 2: Clone the Repository to Your Local Machine**

   1. On your repository page, click the green **"Code"** button.
   2. Copy the repository URL (choose HTTPS for simplicity).
   3. Open your terminal (or Git Bash, Command Prompt, or PowerShell) and run:
   
   ```bash
   git clone <git_repo_url>
   ```
   
   4. Navigate into the cloned folder:
   
   ```bash
   cd <git_cloned_folder>
   ```

### **Step 3: Complete the Assignment**

**Laboratory # 10 - Guided Coding Exercise: if...elif...else Statement in Python**

   **Objective:**
   - Learn how to handle multiple conditions using if...elif...else.
   - Understand how the program chooses the first true condition and skips the rest.
   - Practice using comparison operators for range checking.
   - Reinforce input handling and type conversion.

   **Desired Output (Example 1):**
   ```bash
   Enter your numeric grade: 92
   Your grade is: A
   
   ```
   **Desired Output (Example 2):**
   ```bash
   Enter your numeric grade: 75
   Your grade is: C
   
   ```
   **Desired Output (Example 3):**
   ```bash
   Enter your numeric grade: 55
   Your grade is: F
   
   ```
      
   **Notable Observations (to be discussed after completing the exercise):**
   - The conditions in an if...elif...else chain are evaluated in order. The code block associated with the first True condition is executed, and the rest of the conditions are skipped.
   - The else block acts as a "catch-all" and executes only if none of the preceding conditions are True.
   - if...elif...else is useful for handling situations with multiple, mutually exclusive possibilities.

   **Python Best Practices**
   - Order Conditions (Most Specific to Least Specific): Arrange your conditions from the most specific to the least specific. This ensures that the correct block of code is executed. For example, if you checked grade >= 70 before grade >= 80, a grade of 85 would incorrectly be assigned a "C" instead of a "B".
   - Comprehensive else: Ensure that your final else block covers all remaining cases. This makes your code more robust.
   - Input Validation (Recommended): Use try-except blocks to handle potential errors if the user enters non-numerical input.
   - Descriptive Variable Names: Use clear and descriptive variable names (e.g., grade instead of g).
   - Comments: Add comments to explain your logic, especially for more complex grading schemes.
   - Consistent Indentation: Maintain consistent indentation (4 spaces per level is standard).
   - Test Thoroughly: Test your code with various inputs, including edge cases (e.g., grades of 0, 60, 70, 80, 90, 100) to ensure it works correctly for all valid grades and handles invalid input gracefully.

   **Step-by-Step Instructions:**

   1. Setting up: Open your preferred Python environment or Text Editor, and create a Python Script.
      - Required Filename: `if_elif_else_statement.py`
      
   2.  Get input from the user:
      - Use the input() function to prompt the user to enter their numeric grade. Store the returned string in a variable.
```python
user_input = input("Enter your numeric grade: ")
```
      
   3. Convert input to an integer:
```python
grade = int(user_input)
```

   4. Determine the letter grade (using if...elif...else):
      - Use an if statement to check if the grade is greater than or equal to 90. If it is, assign the letter grade "A".
      - Use elif statements for the other grade ranges (80-89, 70-79, 60-69). Remember to order them from most specific to least specific.
      - Use an else block for grades below 60, assigning the letter grade "F".
```python
if grade >= 90:
    letter_grade = "A"
elif grade >= 80:
    letter_grade = "B"
elif grade >= 70:
    letter_grade = "C"
elif grade >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
```

   5. Print the letter grade:
      - Use the print() function to display the calculated letter grade.
```python
print("Your grade is:", letter_grade)
```

   6. Complete Code: Combine the steps above to form the complete program.

   7. Run the code: Execute your Python code.
   8. Observe the output: Enter different grades and observe the output.
   9. (Optional) Input Validation: Add a try-except block to handle ValueError if the user enters non-integer input.
```python
try:
    #your code here
except ValueError:
    print("Invalid input. Please enter an integer.")
```

   **Conclusion**
   This exercise demonstrated the use of the if...elif...else statement to handle multiple conditions. You learned how the program evaluates conditions in order and executes the code block associated with the first true condition. You also practiced using comparison operators for range checking and (optionally) improved the program's robustness with input validation. The if...elif...else statement is a powerful tool for creating programs that can handle complex decision-making scenarios.

### **Step 4: Push Changes to GitHub**
Once you've completed your changes, follow these steps to upload your work to your GitHub repository.

1. Check the status of your changes:
   Open the terminal and run:
   
```bash
git status
```
   This command shows any modified or new files.
   
2. Stage the changes:
   Add all modified files to staging:
   
```bash
git add .
```
   
3. Commit your changes:
   Write a meaningful commit message:
   
```bash
git commit -m "Submitting Python Week 04 - Laboratory # 10"
```
   
4. Push your changes to GitHub:
   Upload your changes to your remote repository:
   
```bash
git push origin main
```
