import time


def performance(file):

    def smth_hvy(func):
        start = time.time()

        def real_func():
            with open(file, 'a') as f:
                print(func())
                end = time.time()
                f.write('{} was called and took {} seconds to complete \n'.format(func.__name__, end - start))
                f.write('\n')
        return real_func
    return smth_hvy


@performance('log.txt')
def something_heavy():
    time.sleep(2)
    return "I am done!"


something_heavy()
