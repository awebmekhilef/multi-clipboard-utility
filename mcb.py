#! python3
# mcb.py - Saves and loads pieces of text to the clipboard.
# Usage: mcb.py save <keyword> - Saves clipboard to keyword.
#        mcb.py <keyword> - Loads keyword to clipboard.

import pyperclip
import os
import sys

# TODO: Serialize to file
messages = {
    'agree': 'Yes, I agree. That sounds fine to me.',
    'busy': 'Sorry, can we do this later this week or next week'
}


def main():
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        messages[sys.argv[2]] = pyperclip.paste()
    elif len(sys.argv) == 2:
        keyword = sys.argv[1].lower()

        if keyword in messages:
            pyperclip.copy(messages[keyword])
        else:
            print(f'There is no message saved for \'{keyword}\'.')
    else:
        print('Incorrect format. Usage: \n\tmcb.py <keyword>\tLoads keyword to clipboard\n\tmcb.py save <keyword>\tSaves clipboard to keyword.')


if __name__ == '__main__':
    main()
    print(messages)
