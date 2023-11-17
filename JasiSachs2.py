def calculate_grades(scores):
    best_score = max(scores)
    grades = []
    for score in scores:
        if score >= best_score - 10:
            grades.append('A')
        elif score >= best_score - 20:
            grades.append('B')
        elif score >= best_score - 30:
            grades.append('C')
        elif score >= best_score - 40:
            grades.append('D')
        else:
            grades.append('F')
    return grades

def main():
    while True:
        total_students = int(input("Total number of students: "))

        try:
            scores = list(map(int, input(f"Enter {total_students} score(s): ").split()))
            if len(scores) == total_students:
                break
            else:
                print(f"Please enter exactly {total_students} scores.")
        except ValueError:
            print("Invalid input. Please enter integers only.")

    grades = calculate_grades(scores)

    print("\nGrading Report:")
    for i, grade in enumerate(grades):
        print(f"Student {i + 1} score is {scores[i]} and grade is {grade}")

if __name__ == "__main__":
    main()
