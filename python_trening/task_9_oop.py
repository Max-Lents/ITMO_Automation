class Button:

    def __init__(self, text, link):
        self.text = text
        self.link = link

# экземпляры класса
home = Button('Домой', '/home')
catalog_msk = Button('Каталог', '/msk/catalog')

# доступ к атрибутам
print(home.text)
print('Кнопка ' + home.text + ' имеет ссылку ' + home.link)

print('\n')

print(catalog_msk.text)
print('Кнопка ' + catalog_msk.text + ' имеет ссылку ' + catalog_msk.link)


class ButtonTwo:
    pass


class ButtonTwo:

    def __init__(self, text, link, loc):
        self.text = text
        self.link = link
        self.loc = loc

    def click(self):
        return "Клик по локатору - {}".format(self.loc)

    # экземпляр класса
    home_two = ButtonTwo('Домой', '/home', 'button#home')

    # вызываем метод
    print(home_two.click())

