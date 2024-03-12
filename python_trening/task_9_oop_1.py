class Input:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

search = Input('Input', '#Input')

print(search.loc)

print('\n')

print(search.text)

class Button:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

button = Button('Home', '#Home')

print(button.loc)

print('\n')

print(button.text)

class Title:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

title = Title('Title', '#Title')

print(title.loc)

print('\n')

print(title.text)

class Link:

    def __init__(self, text, loc):
        self.text = text
        self.loc = loc

link = Link('Link', '#Link')

print(link.loc)

print('\n')

print(link.text)