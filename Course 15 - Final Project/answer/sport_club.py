class SportClub:
    def __init__(self, data):
        """
        Initialize the SportClub with member data.
        
        :param data: List of dictionaries containing member data
        """
        self.data = data

    def view_all_members(self):
        """
        Print all member data to the console.
        """
        for member in self.data:
            print(member)

    def add_member(self):
        """
        Add a new member to the club.
        - Prompt the user for member details.
        - Append the new member to the data list.
        """
        new_member = {}
        new_member['ID'] = input("Enter ID: ")
        new_member['Name'] = input("Enter name: ")
        new_member['Age'] = input("Enter age: ")
        new_member['Sport'] = input("Enter sport: ")
        new_member['Membership Duration'] = input("Enter membership duration: ")
        new_member['Satisfaction Score'] = input("Enter satisfaction score: ")
        self.data.append(new_member)
        print("New member added successfully.")

    def remove_member(self):
        """
        Remove a member from the club.
        - Prompt the user for the ID of the member to remove.
        - Remove the member with the matching ID from the data list.
        """
        member_id = input("Enter the ID of the member to remove: ")
        self.data = [member for member in self.data if member['ID'] != member_id]
        print("Member removed successfully.")

    def update_member(self):
        """
        Update information for an existing member.
        - Prompt the user for the ID of the member to update.
        - Update the details of the member with the matching ID.
        """
        member_id = input("Enter the ID of the member to update: ")
        for member in self.data:
            if member['ID'] == member_id:
                member['Name'] = input("Enter new name: ")
                member['Age'] = input("Enter new age: ")
                member['Sport'] = input("Enter new sport: ")
                member['Membership Duration'] = input("Enter new membership duration: ")
                member['Satisfaction Score'] = input("Enter new satisfaction score: ")
                print("Member updated successfully.")
                return
        print("Member not found.")

    def sort_members(self):
        """
        Sort members based on a specified attribute.
        - Prompt the user for the attribute to sort by.
        - Sort the data list by the specified attribute.
        """
        sort_by = input("Enter the attribute to sort by (ID, Name, Age, Sport, Membership Duration, Satisfaction Score): ")
        self.data = sorted(self.data, key=lambda x: x[sort_by])
        print(f"Members sorted by {sort_by}.")

    def filter_members(self):
        """
        Filter members based on a specified attribute and value.
        - Prompt the user for the attribute and value to filter by.
        - Print the filtered members to the console.
        """
        filter_by = input("Enter the attribute to filter by (Age, Sport, Membership Duration, Satisfaction Score): ")
        filter_value = input(f"Enter the value to filter {filter_by} by: ")
        filtered_members = [member for member in self.data if member[filter_by] == filter_value]
        for member in filtered_members:
            print(member)

    def view_statistics(self):
        """
        View statistics of the club members.
        - Calculate and print total members and average satisfaction score.
        """
        total_members = len(self.data)
        avg_satisfaction = sum(float(member['Satisfaction Score']) for member in self.data) / total_members
        print(f"Total Members: {total_members}")
        print(f"Average Satisfaction Score: {avg_satisfaction:.2f}")

    def get_members_data(self):
        """
        Get the current member data.
        
        :return: List of dictionaries containing the current member data
        """
        return self.data
