from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class cuadricula(GridLayout):
    def __init__(self, **kwargs):
        super(cuadricula, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password = TextInput(password=True, multiline=False)
        self.add_widget(self.password)





        #return Button(text="hola", background_color=(155,0,0,80))
class kivyHola(App):

    def build(self):

        return  cuadricula()

if __name__ == '__main__':
    kivyHola().run()