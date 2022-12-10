from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
    

class MainScreen(BoxLayout):
    pass

class CalculatorApp(App):
    operation = StringProperty("")
    resultat = StringProperty("")
    
    def on_click_button(self, *args):
        pass
    
    def calculate(self, *args):
        pass
        
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    CalculatorApp().run()