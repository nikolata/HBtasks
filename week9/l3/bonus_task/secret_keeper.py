from utls import (check,
                  get_last_word_from_db,
                  create_CipherBreaker,
                  create_table_for_result,
                  get_info_from_result
                  )


def main():
    create_CipherBreaker()
    create_table_for_result()
    last_word = get_last_word_from_db()
    check(last_word)
    print(get_info_from_result())


if __name__ == '__main__':
    main()
