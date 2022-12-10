from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
    

class MainScreen(BoxLayout):
    pass

class CalculatorApp(App):
    array = []
    operation = StringProperty("")
    resultat = StringProperty("")
    
    def on_click_buttonon_click_numeric_button(self,id,*args):
        self.array.append(id.text)
        self.operation = ''.join(map(str,self.array))# ==> 'salut'
    
    def delete(self,*args):
        if self.array:
            self.resultat = ""
            self.array.pop()
            self.operation = ''.join(map(str,self.array))
    
    def delete_all(self,*args):
        self.array.clear()
        self.operation = ""
        self.resultat = ""
        
    def calculate(self,*args):
        try:
            self.resultat = str(eval(self.operation))
        except:
            self.resultat = "Syntax error"
                
    def build(self):
        return MainScreen()

if __name__ == '__main__':
    CalculatorApp().run()