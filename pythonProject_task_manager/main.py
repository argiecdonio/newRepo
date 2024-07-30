from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class TaskManager(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tasks = []

    def build(self):
        layout = BoxLayout(orientation='vertical')

        self.task_input = TextInput(multiline=False)
        layout.add_widget(self.task_input)

        add_button = Button(text='Add Task')
        add_button.bind(on_release=self.add_task)
        layout.add_widget(add_button)

        self.task_list = BoxLayout(orientation='vertical')
        layout.add_widget(self.task_list)

        return layout

    def add_task(self, _):
        task_text = self.task_input.text
        if task_text:
            self.tasks.append(task_text)
            self.task_input.text = ''
            self.update_task_list()

    def delete_task(self, task_text):
        self.tasks.remove(task_text)
        self.update_task_list()

    def complete_task(self, task_text):
        self.tasks.remove(task_text)
        self.tasks.append(f'[DONE] {task_text}')
        self.update_task_list()

    def update_task_list(self):
        self.task_list.clear_widgets()
        for task in self.tasks:
            task_label = Label(text=task)
            delete_button = Button(text='Delete')
            delete_button.bind(on_release=lambda btn, text=task: self.delete_task(text))
            task_label.bind(on_touch_down=lambda label, touch, text=task: self.complete_task(text))
            self.task_list.add_widget(task_label)
            self.task_list.add_widget(delete_button)


if __name__ == '__main__':
    TaskManager().run()

