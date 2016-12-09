# ThoughtBox - Johnathon Kwisses (Kwistech)
import json

from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput

from random import choice


class MyFloatLayout(FloatLayout):
    text = StringProperty()
    main_color = 0.3215, 0.5333, 0.8588, 1
    sub_color = 0.7725, 0.7725, 0.7725, 1

    def __init__(self):
        # Class Variables
        super(FloatLayout, self).__init__()
        self.filename = "box.json"
        self.text = "ThoughtBox"

        # Popup Init
        box_layout = BoxLayout(orientation='vertical')
        text_input = TextInput(font_size=25, multiline=False, padding_y=25)
        button = Button(text="Add", background_color=self.sub_color)
        button.bind(on_press=lambda x: self.set_json(text_input))
        box_layout.add_widget(text_input)
        box_layout.add_widget(button)

        self.popup = Popup(title="Enter Thought Below:",
                           content=box_layout,
                           size_hint=(.4, .4))

    def get_json(self):
        with open(self.filename) as f:
            f = json.load(f)
        return f

    def set_json(self, text_input):
        json_data = self.get_json()
        if text_input.text:
            json_data["Thoughts"].append(text_input.text)

        with open(self.filename, "r+") as f:
            json.dump(json_data, f, indent=4)

        self.popup.dismiss()

    def change_text(self):
        json_data = self.get_json().values()
        self.text = choice(json_data[0])

    def add_thought(self):
        self.popup.open()


class ThoughtBoxApp(App):
    def build(self):
        return MyFloatLayout()

if __name__ == "__main__":
    ThoughtBoxApp().run()
