# Overview

# GPA Calculator

This Python script calculates your new GPA based on your current GPA, total credits, the grade you received in a new course, and the credit hours of the new course. It also shows how much your GPA will increase or drop after adding the new grade.

```markdown
## Requirements

Before running the script, make sure you have Python 3 installed on your machine. You can check your Python version by running:

```
python --version
```

If you don't have Python installed, you can download and install it from the official website: https://www.python.org/downloads/.

## How to Run

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/Cyang18/CollegeCalculator.git
   ```

2. Navigate to the project directory: 

   ```
   cd CollegeCalculator
   ```

3. Run the Python script:

   ```
   python gpa_calculator.py
   ```

4. The script will prompt you for the following inputs:
   - Your current GPA (a value between 0.0 and 4.0)
   - Your total credit hours
   - The new grade you received (case-sensitive: A, A-, B+, B, B-, C+, C, C-, D, F)
   - The credit hours for the new course

   After you input these values, the script will calculate and display your new GPA and the GPA change (increase or drop).

## Case Sensitivity

Please note that the grade input is **case-sensitive**. For example, entering `a` or `b+` instead of `A` or `B+` will result in an error. Ensure that the grade is typed exactly as one of the following options:

- A, A-, B+, B, B-, C+, C, C-, D, F

## Example

```
Enter your current GPA (0.0 - 4.0): 3.5

Enter your total credit hours: 60

Enter the new grade (A, A-, B+, B, B-, C+, C, C-, D, F): A

Enter the credit hours for the new class: 3

Your new GPA will be: 3.57

Your GPA will increase by: 0.07 points
```

## Notes

- The GPA calculation is based on the standard 4.0 grading scale.
- If you input an invalid grade or an incorrect GPA, the script will prompt an error message and ask you to try again.


