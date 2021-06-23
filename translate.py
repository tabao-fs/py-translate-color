WHITESPACE = ' '

colors_en = [
    'beige',
    'blue',
    'brown',
    'yellow',
    'gold',
    'gray',
    'green',
    'purple',
    'multicolored',
    'orange',
    'pink',
    'red',
    'black',
    'silver',
    'transparent',
    'turquoise',
    'white',
]

colors_de = {
    'beige': 'beige',
    'blau': 'blue',
    'braun': 'brown',
    'gelb': 'yellow',
    'gold': 'gold',
    'grau': 'gray',
    'grün': 'green',
    'lila': 'purple',
    'mehrfarbig': 'multicolored',
    'orange': 'orange',
    'rosa': 'pink',
    'rot': 'red',
    'schwarz': 'black',
    'silber': 'silver',
    'transparent': 'transparent',
    'türkis': 'turquoise',
    'weiß': 'white',
}

def main(word):
    if word in colors_en:
        return word
    elif word in colors_de:
        return colors_de[word]

    if WHITESPACE in word:
        words = word.split()
        result = ''
        for w in words:
            if w in colors_en:
                result += w + WHITESPACE
            elif w in colors_de:
                result += colors_de[w] + WHITESPACE

        return result

    return None

if __name__ == "__main__":
    word_input = input('Input: ')
    result = main(word_input)
    print(f'Output: {result}')
