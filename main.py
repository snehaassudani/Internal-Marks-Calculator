from marks_pkg import calculate_total, assign_grade, check_pass_status


def main():
    print("INTERNAL MARKS CALCULATOR")
    print("Enter marks out of 100.\n")

    try:
        test1 = float(input("Enter Test 1 marks: "))
        test2 = float(input("Enter Test 2 marks: "))
        assignment = float(input("Enter Assignment marks: "))

        total = calculate_total(test1, test2, assignment)
        grade = assign_grade(total)
        passed = check_pass_status(total)

        print("\n----- RESULT -----")
        print(f"Weighted Internal Marks: {total:.2f}/100")
        print(f"Grade: {grade}")
        print("Status:", "Pass" if passed else "Fail")

    except ValueError as error:
        print("Invalid input:", error)


if __name__ == "__main__":
    main()
