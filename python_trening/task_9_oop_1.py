
from task_9_cheks import Checks

class Input(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc

search = Input('Input', '#Input')


print(search.check_text())

class Button(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc

button = Button('Home', '#Home')

print(button.check_text())

class Title(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc

title = Title('Title', '#Title')


print(title.check_text())

class Link(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc

link = Link('Link', '#Link')


print(link.check_text())