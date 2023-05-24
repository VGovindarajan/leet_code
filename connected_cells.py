import logging

_logger = logging.getLogger(None)


def connected_cells():
    pass


def main():
    logging.basicConfig(filename='connected_cells.log', format='%(levelname)s:%(message)s', level=logging.DEBUG)
    connected_cells()


if __name__ == "__main__":
    main()
