def calculate_total(test1, test2, assignment):
    """
    Calculate weighted internal marks.
    Test 1 = 30%, Test 2 = 30%, Assignment = 40%.
    Each input must be between 0 and 100.
    """
    marks = [test1, test2, assignment]

    for mark in marks:
        if not isinstance(mark, (int, float)) or isinstance(mark, bool):
            raise ValueError("Marks must be numbers.")
        if mark < 0 or mark > 100:
            raise ValueError("Each mark must be between 0 and 100.")

    total = (test1 * 0.30) + (test2 * 0.30) + (assignment * 0.40)
    return total


def assign_grade(total):
    """Return a grade based on the weighted total."""
    if not isinstance(total, (int, float)) or isinstance(total, bool):
        raise ValueError("Total marks must be a number.")
    if total < 0 or total > 100:
        raise ValueError("Total marks must be between 0 and 100.")

    if total >= 90:
        return "A"
    elif total >= 80:
        return "B"
    elif total >= 70:
        return "C"
    elif total >= 60:
        return "D"
    elif total >= 40:
        return "E"
    else:
        return "F"


def check_pass_status(total):
    """Check whether the student has passed (minimum 40 marks)."""
    if not isinstance(total, (int, float)) or isinstance(total, bool):
        raise ValueError("Total marks must be a number.")
    if total < 0 or total > 100:
        raise ValueError("Total marks must be between 0 and 100.")

    return total >= 40
