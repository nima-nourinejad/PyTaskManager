from datetime import datetime

class To_Do_List:
    """
    A class representing a to-do list.

    Attributes:
    - tasks: A list containing dictionaries representing tasks. Each dictionary contains the following keys:
        - "ID": An integer representing the task's unique identifier.
        - "Date": A string representing the date when the task was added.
        - "Description": A string representing the task's description.
        - "Status": A string representing the task's completion status ("Not_Complete" or "Complete").
    """

    def __init__(self):
        """Initialize an empty list of tasks."""
        self.tasks = []

    def __repr__(self):
        """
        Return a string representation of the to-do list.

        This method overrides the default __repr__ method to provide a formatted string
        containing the ID, Description, and Status of each task in the list.
        """
        all_lst = "\n" + "ID" + "\t" + "Desc." + "\t" + "Status" + "\n"
        for task in self.tasks:
            all_lst += str(task["ID"]) + "\t" + task["Description"] + "\t" + task["Status"] + "\n"
        return all_lst  

    def add_task(self, description):
        """
        Add a new task to the to-do list.

        Args:
        - description: A string representing the description of the task.
        """
        id = len(self.tasks) + 1
        date = datetime.now().date().strftime("%b %d, %Y")
        new_task = {"ID": id, "Date": date, "Description": description, "Status": "Not_Complete"}
        self.tasks.append(new_task)
        print(f"The task has been added with the id of {id}")

    def complete_task(self, id):
        """
        Mark a task as complete.

        Args:
        - id: An integer representing the ID of the task to be marked as complete.
        """
        for task in self.tasks:
            if task["ID"] == id:
                task["Status"] = "Complete"
                print(f"The task with the id of {id} marked as complete")
                return
        print(f"There is no task with the id of {id}")

    def delete_task(self, id):
        """
        Delete a task from the to-do list.

        Args:
        - id: An integer representing the ID of the task to be deleted.
        """
        for task in self.tasks:
            if task["ID"] == id:
                self.tasks.remove(task)
                print(f"The task with the id of {id} has been deleted")
                return
        print(f"There is no task with the id of {id}")


# Test your To_Do_List class
to_do_list = To_Do_List()
print(to_do_list)
to_do_list.add_task("new")
print(to_do_list)
to_do_list.complete_task(1)
print(to_do_list)
to_do_list.complete_task(2)
to_do_list.delete_task(2)
to_do_list.delete_task(2)
to_do_list.delete_task(1)
print(to_do_list)
