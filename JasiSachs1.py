def vote_menu():
    while True:
        print("VOTE MENU")
        print("v: Vote")
        print("x: Exit")
        option = input("Option: ").strip().lower()
        if option in ['v', 'x']:
            return option
        else:
            print("Invalid option. Please choose 'v' to vote or 'x' to exit.")


def candidate_menu():
    print("CANDIDATE MENU")
    print("1: John")
    print("2: Jane")
    while True:
        choice = input("Select a candidate (1/2): ").strip()
        if choice in ['1', '2']:
            return choice
        else:
            print("Invalid choice. Please select 1 for John or 2 for Jane.")


def main():
    john_votes = 0
    jane_votes = 0

    while True:
        option = vote_menu()

        if option == 'x':
            print(f"John {john_votes}, Jane {jane_votes}, Total {john_votes + jane_votes}")
            break

        if option == 'v':
            candidate_choice = candidate_menu()

            if candidate_choice == '1':
                john_votes += 1
            else:
                jane_votes += 1


if __name__ == "__main__":
    main()