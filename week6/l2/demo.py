
def read_until_charracter():
    chapter = ''
    first_row = True
    with open('b001.txt', 'r') as file:
        for line in file:
            if '#' in line:
                yield chapter
            else:
                chapter += line
        yield chapter

chapter = read_until_charracter()
def foo(chapter):
    chapters = []
    print(chapter)
    return chapters
print(foo(chapter))

