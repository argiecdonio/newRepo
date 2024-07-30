from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen


class TaskManager(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.tasks = []

    def build(self):
        self.screen_manager = ScreenManager()
        self.task_screen = TaskScreen(name='task_screen', task_manager=self)
        self.task_list_screen = TaskListScreen(name='task_list_screen', task_manager=self)

        self.screen_manager.add_widget(self.task_screen)
        self.screen_manager.add_widget(self.task_list_screen)

        return self.screen_manager


class TaskScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical')

        self.task_input = TextInput(multiline=False)
        self.layout.add_widget(self.task_input)

        add_button = Button(text='Add Task')
        add_button.bind(on_release=self.add_task)
        self.layout.add_widget(add_button)

        self.add_widget(self.layout)

    def add_task(self, _):
        task_text = self.task_input.text
        if task_text:
            self.task_manager.tasks.append(task_text)
            self.task_input.text = ''
            self.task_manager.task_list_screen.update_task_list()
            self.task_manager.screen_manager.current = 'task_list_screen'


class TaskListScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.layout = BoxLayout(orientation='vertical')

        self.task_list = BoxLayout(orientation='vertical')
        self.layout.add_widget(self.task_list)

        back_button = Button(text='Back')
        back_button.bind(on_release=self.go_to_task_screen)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)

    def update_task_list(self):
        self.task_list.clear_widgets()
        for task in self.task_manager.tasks:
            task_label = Label(text=task)
            delete_button = Button(text='Delete')
            delete_button.bind(on_release=lambda btn, text=task: self.delete_task(text))
            task_label.bind(on_touch_down=lambda label, touch, text=task: self.complete_task(text))
            self.task_list.add_widget(task_label)
            self.task_list.add_widget(delete_button)

    def delete_task(self, task_text):
        self.task_manager.tasks.remove(task_text)
        self.update_task_list()

    def complete_task(self, task_text):
        self.task_manager.tasks.remove(task_text)
        self.task_manager.tasks.append(f'[DONE] {task_text}')
        self.update_task_list()

    def go_to_task_screen(self, _):
        self.task_manager.screen_manager.current = 'task_screen'


if __name__ == '__main__':
    TaskManager().run()
