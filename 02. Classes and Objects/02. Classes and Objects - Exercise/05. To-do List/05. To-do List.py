class Task:

    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name: str):
        if new_name != self.name:
            self.name = new_name
            return self.name

        return "Name cannot be the same."

    def change_due_date(self, new_due_date: str):
        if new_due_date != self.due_date:
            self.due_date = new_due_date
            return self.due_date

        return "Date cannot be the same."

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if comment_number in range(len(self.comments)):
            self.comments[comment_number] = new_comment
            return ", ".join(self.comments)

        return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


class Section:

    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task in self.tasks:
            return f"Task is already in the section {self.name}"

        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        if task_name not in list(map(lambda task: task.name, self.tasks)):
            return f"Could not find task with the name {task_name}"

        for tazk in self.tasks:
            if tazk.name == task_name:
                tazk.completed = True

        return f"Completed task {task_name}"

    def clean_section(self):
        completed = [x.name for x in self.tasks if x.completed]
        self.tasks = list(filter(lambda x: not x.completed, self.tasks))
        return f'Cleared {len(completed)} tasks.'

    def view_section(self):
        return f'Section {self.name}:\n' + '\n'.join([x.details() for x in self.tasks])


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())

section = Section("Daily tasks")
section_new = Section('New section')
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
print(section.complete_task(second_task.name))
print(section.complete_task(task.name))
print(section.clean_section())
print(section.view_section())

section_new.add_task(second_task)
print(section_new.view_section())