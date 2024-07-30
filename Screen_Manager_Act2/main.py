from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


class AddTaskScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        self.task_input = TextInput(multiline=False)
        layout.add_widget(self.task_input)

        add_button = Button(text='Add Task')
        add_button.bind(on_release=self.add_task)
        layout.add_widget(add_button)

        self.add_widget(layout)

    def add_task(self, _):
        task_text = self.task_input.text
        if task_text:
            app = App.get_running_app()
            app.tasks.append(task_text)
            self.task_input.text = ''
            app.update_task_list()
            app.screen_manager.current = 'task_list'


class TaskListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical')
        self.task_list = BoxLayout(orientation='vertical')
        layout.add_widget(self.task_list)

        back_button = Button(text='Back')
        back_button.bind(on_release=self.go_to_add_task)
        layout.add_widget(back_button)

        self.add_widget(layout)

    def go_to_add_task(self, _):
        app = App.get_running_app()
        app.screen_manager.current = 'add_task'


class TaskManager(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tasks = []
        self.screen_manager = ScreenManager()

    def build(self):
        self.screen_manager.add_widget(AddTaskScreen(name='add_task'))
        self.screen_manager.add_widget(TaskListScreen(name='task_list'))
        self.screen_manager.current = 'add_task'
        return self.screen_manager

    def delete_task(self, task_text):
        self.tasks.remove(task_text)
        self.update_task_list()

    def complete_task(self, task_text):
        self.tasks.remove(task_text)
        self.tasks.append(f'[DONE] {task_text}')
        self.update_task_list()

    def update_task_list(self):
        task_list_screen = self.screen_manager.get_screen('task_list')
        task_list_screen.task_list.clear_widgets()
        for task in self.tasks:
            task_label = Label(text=task)
            delete_button = Button(text='Delete')
            delete_button.bind(on_release=lambda btn, text=task: self.delete_task(text))
            task_label.bind(on_touch_down=lambda label, touch, text=task: self.complete_task(text))
            task_list_screen.task_list.add_widget(task_label)
            task_list_screen.task_list.add_widget(delete_button)


if __name__ == '__main__':
    TaskManager().run()
