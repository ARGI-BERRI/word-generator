import json
import random


def main():
    with open('./src/config.json') as config:
        data = json.load(config)

    sounds = data['sounds']
    patterns = data['patterns']

    for sound in sounds:
        sounds[sound] = sounds[sound].split(' ')

    for pattern in patterns:
        for _ in range(pattern['count']):
            words: list[str] = list()

            for sound in pattern['syllable']:
                words.append(random.choice(sounds[sound]))

            print(''.join(words))


if __name__ == '__main__':
    main()
