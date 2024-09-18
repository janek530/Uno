class Card:
    type = ''
    number = ''
    color = ''

    def __init__(self, number, color=None, type='normal'):
        self.number = number
        self.color = color
        self.type = type

    def __str__(self):
        if self.type == 'normal':
            return self.number + ' ' + self.color
        else:
            return self.number
