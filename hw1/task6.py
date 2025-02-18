from pathlib import Path

rootdir = Path(__file__).parent
textfile = rootdir / 'task6_read_me.txt'

def wordcount():
    with open(textfile, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)