import random
import lorem


def create_chapter(lenght):
    chapter = ''
    while True:
        if len(chapter) >= lenght:
            yield chapter[:lenght]
            chapter = ''
        else:
            chapter += lorem.text()
            lenght = random.randint(100, 1000)


def safe_to_file(count, lenght):
    chapter = create_chapter(lenght)
    with open('book1.txt', 'a') as file:
        for i in range(count + 1):
            file.write(f'#CHAPTER {i}\n')
            file.write('\n')
            cur_chapter = next(chapter)
            if cur_chapter[-1] != '.':
                cur_chapter = cur_chapter[:-1] + '.'
            file.write(cur_chapter)
            file.write('\n')


def main():
    open('book1.txt', 'w').close()
    count = random.randint(1, 500)
    lenght = random.randint(100, 10000)
    safe_to_file(count, lenght)


if __name__ == '__main__':
    main()
