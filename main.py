import logging


def init():
    logging.basicConfig(level=logging.INFO)

def main():
    logging.info('hello world')



if __name__ == '__main__':
    init()
    main()

