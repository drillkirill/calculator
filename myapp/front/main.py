from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.config import Config


SAVE_INPUT = ''


class CalculatorApp(App):

    def build(self):
        root = BoxLayout(orientation='vertical', padding=5)

        self.result = TextInput(
            text='', readonly=True, font_size=70,
            size_hint=[1, .50], background_color=[1, 1, 1, .8])
        root.add_widget(self.result)

        all_buttons = GridLayout(cols=5)

        all_buttons.add_widget(
            Button(text='7', font_size=25, on_press=self.calc))
        all_buttons.add_widget(
            Button(text='8', font_size=25, on_press=self.calc))
        all_buttons.add_widget(
            Button(text='9', font_size=25, on_press=self.calc))
        all_buttons.add_widget(
            Button(text='+', font_size=25, on_press=self.calc))
        all_buttons.add_widget(
            Button(text='del', font_size=25, on_press=self.calc))

        all_buttons.add_widget(
            Button(text='4', font_size=25, on_press=self.calc))
        all_buttons.add_widget(
            Button(text='5', font_size=25, on_press=self.calc))
        all_buttons.add_widget(
            Button(text='6', font_size=25, on_press=self.calc))
        all_buttons.add_widget(
            Button(text='-', font_size=25, on_press=self.calc))
        all_buttons.add_widget(
            Button(text='(', font_size=25, on_press=self.calc))

        all_buttons.add_widget(
            Button(text='1', font_size=25, on_press=self.calc))
        all_buttons.add_widget(
            Button(text='2', font_size=25, on_press=self.calc))
        all_buttons.add_widget(
            Button(text='3', font_size=25, on_press=self.calc))
        all_buttons.add_widget(
            Button(text='*', font_size=25, on_press=self.calc))
        all_buttons.add_widget(
            Button(text=')', font_size=25, on_press=self.calc))

        all_buttons.add_widget(
            Button(text='0', font_size=25, on_press=self.calc))
        all_buttons.add_widget(
            Button(text='.', font_size=25, on_press=self.calc))
        all_buttons.add_widget(
            Button(text='=', font_size=25, on_press=self.calc))
        all_buttons.add_widget(
            Button(text='/', font_size=25, on_press=self.calc))
        all_buttons.add_widget(
            Button(text='%', font_size=25, on_press=self.calc))

        root.add_widget(all_buttons)
        return root

    def calc(self, symbol):
        global SAVE_INPUT

        if symbol.text is 'del':
            SAVE_INPUT = self.result.text = ''
        elif symbol.text is not '=':
            self.result.text += symbol.text
            SAVE_INPUT += symbol.text
        else:
            try:
                SAVE_INPUT = self.result.text = str(eval(SAVE_INPUT))
            except:
                SAVE_INPUT = self.result.text = ''


if __name__ == '__main__':
    CalculatorApp().run()
