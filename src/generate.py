import json
import random


def main():
    with open('./src/config.json') as config:
        data = json.load(config)

    sounds = data['sounds']
    patterns = data['patterns']

    sounds = {
        sound: sounds[sound].split(' ') for sound in sounds
    }

    for pattern in patterns:
        pattern.setdefault('label', 'no label')
        pattern.setdefault('count', 5)

        print(f'Pattern name: {pattern["label"]}')
        print(f'Pattern: x{pattern["count"]} {pattern["syllable"]}')

        for _ in range(pattern['count']):
            words = ''.join([
                random.choice(sounds[sound]) for sound in pattern['syllable']
            ])

            print((words), end=', ')

        print('\n')


if __name__ == '__main__':
    main()
