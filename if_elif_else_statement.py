"""Grade Classification Program

This script prompts the user for a numeric grade, determines the corresponding letter grade,
and displays the result. It includes input validation and follows best practices for Python programming.
"""

def get_numeric_grade() -> int:
    """
    Prompts the user to enter a numeric grade, validates input, and returns the grade as an integer.
    
    Returns:
        int: The numeric grade entered by the user.
    """
    while True:
        try:
            grade = int(input("Enter your numeric grade: "))
            if 0 <= grade <= 100:
                return grade
            print("Error: Please enter a grade between 0 and 100.")
        except ValueError:
            print("Error: Invalid input. Please enter an integer.")

def determine_letter_grade(grade: int) -> str:
    """
    Determines the letter grade based on the given numeric grade.
    
    Args:
        grade (int): The numeric grade to evaluate.
    
    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    if grade >= 90:
        return "A"
    if grade >= 80:
        return "B"
    if grade >= 70:
        return "C"
    if grade >= 60:
        return "D"
    return "F"

def main() -> None:
    """Main function that runs the grade classification program."""
    grade = get_numeric_grade()
    letter_grade = determine_letter_grade(grade)
    print(f"Your grade is: {letter_grade}")

if __name__ == "__main__":
    main()
