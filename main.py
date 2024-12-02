def calculate_new_gpa(current_gpa, total_credits, new_grade, new_credits):
    grade_points = {
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D': 1.0,
        'F': 0.0
    }
    
    if not (0.0 <= current_gpa <= 4.0):
        return "Invalid current GPA. Must be between 0.0 and 4.0."
    if total_credits < 0:
        return "Total credits cannot be negative."
    if new_credits <= 0:
        return "New credits must be a positive value."
    if new_grade not in grade_points:
        return "Invalid grade entered."
    
    # Calculate current quality points
    current_quality_points = current_gpa * total_credits
    
    # Calculate new quality points from the new grade
    new_quality_points = grade_points[new_grade] * new_credits
    
    # Calculate new total quality points and total credits
    new_total_quality_points = current_quality_points + new_quality_points
    new_total_credits = total_credits + new_credits
    
    # Calculate new GPA
    new_gpa = new_total_quality_points / new_total_credits
    
    # Calculate GPA change (could be drop or increase)
    gpa_change = current_gpa - new_gpa
    
    return new_gpa, gpa_change

try:
    current_gpa = float(input("Enter your current GPA (0.0 - 4.0): "))
    total_credits = int(input("Enter your total credit hours: "))
    new_grade = input("Enter the new grade (A, A-, B+, B, B-, C+, C, C-, D, F): ").strip()
    new_credits = int(input("Enter the credit hours for the new class: "))
    
    result = calculate_new_gpa(current_gpa, total_credits, new_grade, new_credits)
    if isinstance(result, str):
        print(result) 
    else:
        new_gpa, gpa_change = result
        change_type = "drop" if gpa_change > 0 else "increase"
        print(f"Your new GPA will be: {new_gpa:.2f}")
        print(f"Your GPA will {change_type} by: {abs(gpa_change):.2f} points")
except ValueError:
    print("Invalid input! Please enter numeric values for GPA and credit hours.")
