from project.task import Task


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
