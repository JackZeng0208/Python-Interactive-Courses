from read import read_csv
from write import write_csv
from sport_club import SportClub

def display_menu():
    """
    Given code
    Display the main menu for the Sport Club Membership Management System.
    """
    print("\nSport Club Membership Management System")
    print("1. View all members")
    print("2. Add a new member")
    print("3. Remove an existing member")
    print("4. Update member information")
    print("5. Sort members")
    print("6. Filter members")
    print("7. View membership statistics")
    print("8. Exit")

def main():
    """
    The main function to run the Sport Club Membership Management System.
    - Read data from the CSV file.
    - Create an instance of the SportClub class.
    - Display the menu and handle user choices.
    - Save changes to the CSV file after each operation.

    There are 8 menu options:
    1. View all members
    2. Add a new member
    3. Remove an existing member
    4. Update member information
    5. Sort members
    6. Filter members
    7. View membership statistics
    8. Exit
    """
    # Read data from CSV file
    data = read_csv('/Users/yixiaozeng/Python-Interactive-Courses/Course 15 - Final Project/answer/survey_database.csv')
    
    # Create a SportClub instance
    club = SportClub(data)

    while True:
        # Display menu options
        display_menu()
        
        # Get user choice
        choice = input("Enter your choice: ")

        # Handle each menu option
        if choice == '1':
            club.view_all_members()
        elif choice == '2':
            club.add_member()
        elif choice == '3':
            club.remove_member()
        elif choice == '4':
            club.update_member()
        elif choice == '5':
            club.sort_members()
        elif choice == '6':
            club.filter_members()
        elif choice == '7':
            club.view_statistics()
        elif choice == '8':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
        # Save changes after each operation
        write_csv('/Users/yixiaozeng/Python-Interactive-Courses/Course 15 - Final Project/answer/survey_database.csv', club.get_members_data())

if __name__ == '__main__':
    main()
