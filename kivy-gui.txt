from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class main_grid(GridLayout):
    def __init__(self, **args):
        super(main_grid, self).__init__(**args)

        self.cols = 1

        self.inside = GridLayout()
        self.inside.cols = 2

        self.fnlabel = Label(text = "First Name:", font_size = 30)
        self.inside.add_widget(self.fnlabel)
        self.fninput = TextInput(font_size = 30)
        self.inside.add_widget(self.fninput)

        self.lnlabel = Label(text="Last Name:", font_size=30)
        self.inside.add_widget(self.lnlabel)
        self.lninput = TextInput(font_size=30)
        self.inside.add_widget(self.lninput)

        self.mnlabel = Label(text="Middle Name:", font_size=30)
        self.inside.add_widget(self.mnlabel)
        self.mninput = TextInput(font_size=30)
        self.inside.add_widget(self.mninput)

        self.add_widget(self.inside)

        self.btn = Button(text="Click Me",font_size = 60)
        self.btn.bind(on_press = self.clicked)
        self.add_widget(self.btn)

    def clicked(self, args):
        fn = self.fninput.text
        mn = self.mninput.text
        ln = self.lninput.text
        fullname = fn +" "+mn+", "+ln
        print(fullname)
        self.add_widget(Label(text = fullname, font_size = 60))

class main(App):
    def build(self):
        return main_grid()

if __name__ == "__main__":
    main().run()