class SportClub:
    def __init__(self, data):
        """
        Initialize the SportClub with member data.
        
        :param data: List of dictionaries containing member data
        """
        # TODO: Implement the __init__ method
        pass

    def view_all_members(self):
        """
        Print all member data to the console.
        """
        # TODO: Implement the view_all_members method
        pass

    def add_member(self):
        """
        Add a new member to the club.
        - Prompt the user for member details.
        - Check if the ID is unique before adding the new member.
            - If the ID is not unique, print a message indicating the ID already exists and prompt for a new ID.
        - Remember to generate input prompt messages for each attribute:
            - ID
            - Name
            - Age
            - Sport
            - Membership Duration
            - Satisfaction Score
        - Append the new member to the data list.
        - Print a message indicating the member was added successfully.
        """
        # TODO: Implement the add_member method
        pass

    def remove_member(self):
        """
        Remove a member from the club.
        - Prompt the ID of the member to remove (using input()).
            - Remember to generate a input prompt message.
        - Remove the member with the matching ID from the data list.
        - Print a message indicating the member was removed successfully.
        """
        # TODO: Implement the remove_member method
        pass

    def update_member(self):
        """
        Update information for an existing member.
        - Prompt the user for the ID of the member to update.
            - Remember to generate a input prompt message.
        - Update the details of the member with the matching ID.
        - Print a message indicating the member was updated successfully, quit the function after updating the member.
        - If the member is not found, print a message indicating the member was not found.
        """
        # TODO: Implement the update_member method
        pass

    def sort_members(self):
        """
        Sort members based on a specified attribute.
        - Sort the data list by the specified attribute.
        - Print a message indicating the members were sorted by the specified attribute.
        """
        # TODO: Implement the sort_members method
        sort_by = input("Enter the attribute to sort by (ID, Name, Age, Sport, Membership Duration, Satisfaction Score): ")
        pass

    def filter_members(self):
        """
        Filter members based on a specified attribute and value.
        - Prompt the user for the attribute and value to filter by.
        - Print the filtered members to the console.
        """
        # TODO: Implement the filter_members method
        filter_by = input("Enter the attribute to filter by (Age, Sport, Membership Duration, Satisfaction Score): ")
        filter_value = input(f"Enter the value to filter {filter_by} by: ")
        pass

    def view_statistics(self):
        """
        View statistics of the club members.
        - Calculate and print total members and average satisfaction score.
        - Print format: "Total Members: {total_members}"
        - Print format: "Average Satisfaction Score: {average_satisfaction}" (rounded to 2 decimal places)
        """
        # TODO: Implement the view_statistics method
        pass

    def get_members_data(self):
        """
        Get the current member data.
        
        :return: List of dictionaries containing the current member data
        """
        # TODO: Implement the get_members_data method
        pass
