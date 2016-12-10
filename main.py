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
    """Class for FloatLayout - main layout that houses the app."""
    # Class Variables - called as root.variable_name.
    text = StringProperty()
    main_color = 0.3215, 0.5333, 0.8588, 1  # Colors are RGBA.
    sub_color = 0.7725, 0.7725, 0.7725, 1

    def __init__(self):
        """Initiate Class variables and create popup display."""
        # Class Variables (not accessible for thoughtbox.kv)
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
        """Get data from JSON file (self.filename).

        Returns:
            dict: JSON data.
        """
        with open(self.filename) as f:
            f = json.load(f)
        return f

    def set_json(self, text_input):
        """Set text_input to JSON data and 'saves' it.

        Args:
            text_input (TextInput): User-entered text.
        """
        json_data = self.get_json()
        if text_input.text:
            json_data["Thoughts"].append(text_input.text)

        with open(self.filename, "r+") as f:
            json.dump(json_data, f, indent=4)

        # Closes Popup display
        self.popup.dismiss()

    def change_text(self):
        """Change on-screen text to a random user-entered value."""
        json_data = self.get_json().values()
        self.text = choice(json_data[0])

    def add_thought(self):
        """Open Popup for a user to enter a thought."""
        self.popup.open()


class ThoughtBoxApp(App):
    """Class for building app."""
    def build(self):
        """Build MyFloatLayout()."""
        return MyFloatLayout()

if __name__ == "__main__":
    ThoughtBoxApp().run()
