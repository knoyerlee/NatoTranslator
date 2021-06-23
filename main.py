from translator import NATOTranslator as nt

translator = nt()

while(True):
    translator.exit_info()
    letter = translator.prompt_user()
    if(letter == 'exit'):
        break
    else:
        translation = translator.translate_letter(letter)
        print(f"\nThe letter {letter.title()} translates to: {translation}")

