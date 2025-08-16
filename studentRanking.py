def calculate_average(scores):
    """
    Calculate the average of a list of scores.
    
    Args:
        scores (list): List of numeric scores
        
    Returns:
        float: Average score rounded to 2 decimal places
    """
    if not scores:
        return 0.0
    
    return round(sum(scores) / len(scores), 2)

def rank_students(students_dict):
    """
    Rank students by average score, breaking ties alphabetically.
    
    Args:
        students_dict (dict): Dictionary with student names as keys and score lists as values
        
    Returns:
        list: List of tuples (name, average) sorted by rank
    """
    # Calculate averages for each student
    student_averages = []
    for name, scores in students_dict.items():
        average = calculate_average(scores)
        student_averages.append((name, average))
    
    # Sort by average (descending) then by name (ascending) for ties
    # Using negative average for descending sort, name for ascending alphabetical sort
    ranked_students = sorted(student_averages, key=lambda x: (-x[1], x[0]))
    
    return ranked_students

def rank_students_detailed(students_dict):
    """
    Rank students with detailed breakdown of the ranking process.
    
    Args:
        students_dict (dict): Dictionary with student names as keys and score lists as values
        
    Returns:
        list: List of tuples (name, average) sorted by rank
    """
    print("DETAILED RANKING PROCESS")
    print("=" * 50)
    
    print("\n1. Calculate Averages:")
    student_averages = []
    for name, scores in students_dict.items():
        average = calculate_average(scores)
        student_averages.append((name, average))
        total = sum(scores)
        count = len(scores)
        print(f"  {name}: {scores} → {total}/{count} = {average}")
    
    print(f"\n2. Before Sorting: {student_averages}")
    
    # Sort with detailed explanation
    ranked_students = sorted(student_averages, key=lambda x: (-x[1], x[0]))
    
    print(f"\n3. After Sorting: {ranked_students}")
    print("   Sort key: (-average, name)")
    print("   - Negative average for descending order (highest first)")
    print("   - Name for ascending alphabetical order (ties)")
    
    return ranked_students

def display_ranking_table(ranked_students):
    """
    Display ranking results in a formatted table.
    
    Args:
        ranked_students (list): List of tuples (name, average)
    """
    print("\nRANKING TABLE")
    print("=" * 30)
    print(f"{'Rank':<6} {'Name':<12} {'Average':<8}")
    print("-" * 30)
    
    current_rank = 1
    prev_average = None
    
    for i, (name, average) in enumerate(ranked_students):
        # Handle tied ranks
        if prev_average is not None and average != prev_average:
            current_rank = i + 1
        
        print(f"{current_rank:<6} {name:<12} {average:<8}")
        prev_average = average

def find_top_students(students_dict, top_n=3):
    """
    Find the top N students by average score.
    
    Args:
        students_dict (dict): Dictionary with student names and scores
        top_n (int): Number of top students to return
        
    Returns:
        list: Top N students as tuples (name, average)
    """
    ranked = rank_students(students_dict)
    return ranked[:top_n]

def get_students_by_grade_range(students_dict, min_avg=0, max_avg=100):
    """
    Get students within a specific average grade range.
    
    Args:
        students_dict (dict): Dictionary with student names and scores
        min_avg (float): Minimum average score
        max_avg (float): Maximum average score
        
    Returns:
        list: Students within the grade range
    """
    ranked = rank_students(students_dict)
    return [(name, avg) for name, avg in ranked if min_avg <= avg <= max_avg]

def analyze_class_performance(students_dict):
    """
    Provide comprehensive analysis of class performance.
    
    Args:
        students_dict (dict): Dictionary with student names and scores
    """
    print("\nCLASS PERFORMANCE ANALYSIS")
    print("=" * 50)
    
    # Calculate all averages
    averages = [calculate_average(scores) for scores in students_dict.values()]
    
    if not averages:
        print("No student data available.")
        return
    
    # Statistics
    class_average = round(sum(averages) / len(averages), 2)
    highest_avg = max(averages)
    lowest_avg = min(averages)
    
    print(f"Class Average: {class_average}")
    print(f"Highest Average: {highest_avg}")
    print(f"Lowest Average: {lowest_avg}")
    print(f"Range: {highest_avg - lowest_avg}")
    print(f"Number of Students: {len(students_dict)}")
    
    # Grade distribution
    a_students = len([avg for avg in averages if avg >= 90])
    b_students = len([avg for avg in averages if 80 <= avg < 90])
    c_students = len([avg for avg in averages if 70 <= avg < 80])
    d_students = len([avg for avg in averages if 60 <= avg < 70])
    f_students = len([avg for avg in averages if avg < 60])
    
    print(f"\nGrade Distribution:")
    print(f"  A (90-100): {a_students} students")
    print(f"  B (80-89):  {b_students} students")
    print(f"  C (70-79):  {c_students} students")
    print(f"  D (60-69):  {d_students} students")
    print(f"  F (0-59):   {f_students} students")

def test_student_ranking():
    """Test the student ranking with the provided example"""
    
    print("STUDENT RANKING TEST")
    print("=" * 50)
    
    # Test case from the problem
    students = {
        'Alice': [90, 85, 88], 
        'Bob': [90, 85, 88], 
        'Charlie': [95, 80, 85]
    }
    expected = [('Alice', 87.67), ('Bob', 87.67), ('Charlie', 86.67)]
    
    print(f"Input: {students}")
    print(f"Expected: {expected}")
    
    # Test the ranking function
    result = rank_students(students)
    print(f"Result: {result}")
    
    # Verify the result
    success = result == expected
    print(f"Test Status: {'PASS' if success else 'FAIL'}")
    
    if not success:
        print("\nDifferences found:")
        for i, ((exp_name, exp_avg), (res_name, res_avg)) in enumerate(zip(expected, result)):
            if exp_name != res_name or abs(exp_avg - res_avg) > 0.01:
                print(f"  Position {i}: Expected {(exp_name, exp_avg)}, Got {(res_name, res_avg)}")
    
    # Display detailed ranking
    print("\n")
    rank_students_detailed(students)
    
    # Display formatted table
    display_ranking_table(result)
    
    return result

def run_comprehensive_tests():
    """Run comprehensive test cases"""
    
    print("\n" + "=" * 60)
    print("COMPREHENSIVE TEST CASES")
    print("=" * 60)
    
    test_cases = [
        {
            'name': 'Basic tie-breaking',
            'input': {'Alice': [90, 85, 88], 'Bob': [90, 85, 88], 'Charlie': [95, 80, 85]},
            'expected': [('Alice', 87.67), ('Bob', 87.67), ('Charlie', 86.67)]
        },
        {
            'name': 'No ties',
            'input': {'Alice': [95, 90, 85], 'Bob': [80, 75, 70], 'Charlie': [85, 80, 75]},
            'expected': [('Alice', 90.0), ('Charlie', 80.0), ('Bob', 75.0)]
        },
        {
            'name': 'All same scores',
            'input': {'Zoe': [85, 85, 85], 'Alice': [85, 85, 85], 'Mike': [85, 85, 85]},
            'expected': [('Alice', 85.0), ('Mike', 85.0), ('Zoe', 85.0)]
        },
        {
            'name': 'Single scores',
            'input': {'Student1': [100], 'Student2': [95], 'Student3': [90]},
            'expected': [('Student1', 100.0), ('Student2', 95.0), ('Student3', 90.0)]
        },
        {
            'name': 'Large numbers',
            'input': {'Anna': [98, 97, 99, 96], 'Ben': [95, 94, 96, 97], 'Cat': [98, 97, 99, 96]},
            'expected': [('Anna', 97.5), ('Cat', 97.5), ('Ben', 95.5)]
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\nTest Case {i}: {test['name']}")
        print(f"Input: {test['input']}")
        
        result = rank_students(test['input'])
        expected = test['expected']
        
        print(f"Result: {result}")
        print(f"Expected: {expected}")
        
        # Check if results match (accounting for floating point precision)
        success = True
        if len(result) != len(expected):
            success = False
        else:
            for (r_name, r_avg), (e_name, e_avg) in zip(result, expected):
                if r_name != e_name or abs(r_avg - e_avg) > 0.01:
                    success = False
                    break
        
        print(f"Status: {'PASS' if success else 'FAIL'}")

def interactive_demo():
    """Interactive demonstration with various scenarios"""
    
    print("\n" + "=" * 50)
    print("INTERACTIVE DEMO")
    print("=" * 50)
    
    # Demo with a larger class
    demo_students = {
        'Emma': [92, 88, 91, 89],
        'Liam': [85, 87, 84, 86],
        'Olivia': [95, 93, 94, 96],
        'Noah': [78, 82, 80, 79],
        'Ava': [92, 88, 91, 89],  # Same as Emma - tie scenario
        'Oliver': [88, 90, 87, 85],
        'Sophia': [96, 94, 95, 97],
        'Elijah': [75, 77, 76, 78]
    }
    
    print("Demo Class Data:")
    for name, scores in demo_students.items():
        avg = calculate_average(scores)
        print(f"  {name}: {scores} (avg: {avg})")
    
    print("\n" + "-" * 50)
    
    # Full ranking
    ranked = rank_students(demo_students)
    display_ranking_table(ranked)
    
    # Class analysis
    analyze_class_performance(demo_students)
    
    # Top students
    print(f"\nTop 3 Students: {find_top_students(demo_students, 3)}")
    
    # Students in A range
    a_students = get_students_by_grade_range(demo_students, 90, 100)
    print(f"A Students (90-100): {a_students}")

if __name__ == "__main__":
    # Run main test
    test_student_ranking()
    
    # Run comprehensive tests
    run_comprehensive_tests()
    
    # Interactive demo
    interactive_demo()
    
    # Edge case testing
    print("\n" + "=" * 50)
    print("EDGE CASE TESTING")
    print("=" * 50)
    
    edge_cases = [
        {'name': 'Empty scores', 'data': {'Student': []}},
        {'name': 'Single student', 'data': {'OnlyStudent': [85, 90, 95]}},
        {'name': 'Decimal scores', 'data': {'A': [85.5, 90.3, 88.7], 'B': [86.1, 89.9, 88.0]}}
    ]
    
    for case in edge_cases:
        print(f"\nEdge Case: {case['name']}")
        try:
            result = rank_students(case['data'])
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")