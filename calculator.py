from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
    

class Touch(BoxLayout):
    pass

class CalculatorApp(App):
    def build(self):
        return Touch()

if __name__ == '__main__':
    CalculatorApp().run()