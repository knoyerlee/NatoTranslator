class NATOTranslator:
    def __init__(self):
        self.natodictionary = {
            'a': 'alpha',
            'b': 'bravo',
            'c': 'charlie',
            'd': 'delta',
            'e': 'echo',
            'f': 'foxtrot',
            'g': 'golf',
            'h': 'hotel',
            'i': 'india',
            'j': 'juliett',
            'k': 'kilo',
            'l': 'lima',
            'm': 'mike',
            'n': 'november',
            'o': 'oscar',
            'p': 'papa',
            'q': 'quebec',
            'r': 'romeo',
            's': 'sierra',
            't': 'tango',
            'u': 'uniform',
            'v': 'victor',
            'w': 'whiskey',
            'x': 'xray',
            'y': 'yankee',
            'z': 'zulu'
            }
        self.user_letter = ''

    def exit_info(self):
        print("\nTo close this program type exit and hit enter at anytime: ")

    def prompt_user(self):
        self.user_letter = input(f"Please enter the letter you would like translated: ")
        return self.user_letter.lower()

    def translate_letter(self, user_letter):
        for letter, translation in self.natodictionary.items():
            if(user_letter == letter):
                return translation.title()



    