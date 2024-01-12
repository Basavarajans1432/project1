# main.py
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class CalculatorApp(App):
    def build(self):
        self.icon = 'icon.png'
        self.title = 'Calculator'
        self.root = CalculatorLayout()
        return self.root

class CalculatorLayout(GridLayout):
    def __init__(self, **kwargs):
        super(CalculatorLayout, self).__init__(**kwargs)
        self.cols = 5
        self.rows = 4

        # Background Image
        self.background = 'back.jpy'

        # Display Label
        self.display = Label(text='', font_size=32, halign='right', valign='middle', size_hint_y=None, height=100)
        self.add_widget(self.display)

        # Calculator Buttons
        buttons = [
            '1', '2', '3', 
            '4', '5', '6', 
            '7', '8', '9', 
            '0', 'C', '=', 
            '+', '-', '/',
            '*', '%', '√','+-',
        ]

        for button in buttons:
            btn = Button(text=button, font_size=24)
            btn.bind(on_press=self.on_button_press)
            self.add_widget(btn)

    def on_button_press(self, instance):
        current_text = self.display.text

        if instance.text == 'C':
            self.display.text = ''
        elif instance.text == '=':
            try:
                self.display.text = str(eval(current_text))
            except:
                self.display.text = 'Error'
        else:
            self.display.text += instance.text

if __name__ == '__main__':
    CalculatorApp().run()
