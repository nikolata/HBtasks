import pyglet
from pyglet.window import key
# keyboard.add_hotkey('space', lambda: keyboard.write('foobar'))
window = pyglet.window.Window()


def read_until_charracter():
    chapter = ''
    with open('book1.txt', 'r') as file:
        for line in file:
            if '#' in line:
                yield chapter
            else:
                chapter += line


chapter = read_until_charracter()


def printt(i):
    chapters = []
    for k in chapter:
        chapters.append(k)
    if i == 0:
        print(chapters[i])
    else:
        print(chapters[i].replace(chapters[i - 1], ''))


@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.SPACE:
        try:
            print(next(chapter))
        except Exception:
            print('END OF BOOK')
            pyglet.app.exit()


pyglet.app.run()
