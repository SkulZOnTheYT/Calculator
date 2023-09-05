from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class CalculatorApp(App):
    def build(self):
        return Calculator()

class Calculator(BoxLayout):
    pass

if __name__ == '__main__':
    CalculatorApp().run()
  
