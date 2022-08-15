#! python3
# mcb.py - Saves and loads pieces of text to the clipboard.
# Usage: mcb.py save <keyword> - Saves clipboard to keyword.
#        mcb.py <keyword> - Loads keyword to clipboard.

import pyperclip
import os
import sys
import json

# TODO: Clean up file name references
# TODO: Save file to APPDATA

def main():
    # Prep the messages.json file
    if not os.path.exists('./messages.json') or not os.path.getsize('./messages.json') > 0:
        with open('./messages.json', 'w') as file:
            file.write('{}')

    # Saving a new message from clipboard
    if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
        with open('./messages.json', 'r+') as file:
            messages = json.load(file)
            messages[sys.argv[2]] = pyperclip.paste()

            # Rewind to beginning.
            # No need to truncate as new data will be bigger than previous.
            file.seek(0)
            json.dump(messages, file)

    # Loading a saved message to the clipboard
    elif len(sys.argv) == 2:
        keyword = sys.argv[1].lower()

        with open('./messages.json', 'r') as file:
            messages = json.load(file)

            if keyword in messages:
                pyperclip.copy(messages[keyword])
            else:
                print(f'There is no message saved for \'{keyword}\'.')
    # Incorrect argument format
    else:
        print('Incorrect format. Usage: \n\tmcb.py <keyword>\tLoads keyword to clipboard\n\tmcb.py save <keyword>\tSaves clipboard to keyword.')


if __name__ == '__main__':
    main()
