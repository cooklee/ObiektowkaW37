class Option:

    def __init__(self, name, funk):
        self.name = name
        self.funk = funk

    def execute(self):
        self.funk()

    def __str__(self):
        return self.name
class Menu:

    def __init__(self, *options, intend=""):
        self.intend = intend
        self.options = {}
        for id, option in enumerate(options):
            self.options[id+1] = option

    def __str__(self):
        s = ""
        for key, value in self.options.items():
            s+= f"{self.intend} {key} {value}\n"
        s+= f"{self.intend} q - wyjscie"
        return s

    def start(self):
        while True:
            action = input(f"{self}")
            if action == 'q':
                break
            action = int(action)
            self[action].execute()


    def __getitem__(self, key):
        return self.options[key]


