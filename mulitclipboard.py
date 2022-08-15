import pyperclip
import sys

# TODO: Serialize to file
messages = {
    'agree': 'Yes, I agree. That sounds fine to me.',
    'busy': 'Sorry, can we do this later this week or next week'
}

def main():
    if len(sys.argv) < 2:
        print('Incorrect format. Usage: multiclipboard.py <keyword> [message]')
        sys.exit()

    # TODO: Case insensitivity
    keyword = sys.argv[1]

    if keyword in messages:
        pyperclip.copy(messages[keyword])
    else:
        print(f'There is no text for {keyword}.')


if __name__ == '__main__':
    main()
