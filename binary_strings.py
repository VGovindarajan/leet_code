import logging
l = 4
a = ['x' for _ in range(0, l)]
_logger = logging.getLogger("log")

def binary_strings(n):
    _logger.info(f"In n={n}, n-1={n-1}, {a}")
    #print(a)
    if n <= 0:
        print(a)
        _logger.info(f"Cnadidate n={n}, n-1={n - 1}, {a}")
        return
    a[n-1] = 0
    _logger.info(f"after 0, n={n}, n-1={n - 1}, {a}")
    binary_strings(n-1)
    a[n - 1] = 1
    _logger.info(f"after 1, n={n}, n-1={n - 1}, {a}")
    binary_strings(n - 1)


def main():
    logging.basicConfig(filename='binary_strings.log', format='%(levelname)s:%(message)s', level=logging.DEBUG)
    binary_strings(len(a))

if __name__ == "__main__":
    main()
