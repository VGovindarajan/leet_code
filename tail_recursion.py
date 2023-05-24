import logging
import timeit

def fact(n):
    if n <= 1:
        return 1
    return n * fact(n-1)

def tailed_fact(n, result=1):
    if n <= 1:
        return result
    return tailed_fact(n-1, n * result)

def main():
    logging.basicConfig(filename="tailed_recursion.txt", format='%(asctime)s, %(levelname)s: %(message)s', level=logging.DEBUG)
    _logger = logging.getLogger('timed_recursion')
    n = 100
    count = 10000
    fact_result = fact(n)
    tailed_fact_result = tailed_fact(n, 1)
    rec_time = timeit.timeit(lambda: fact(n), globals=globals(), number=count)
    tailed_recur_time = timeit.timeit(lambda: tailed_fact(n, 1), globals=globals(), number=count)

    _logger.info(f'fact_result= {fact_result}')
    _logger.info(f'tailed_fact_result= {tailed_fact_result}')
    _logger.info(f'Ran {count} times, fact = {rec_time/count}, tailed_fact = {tailed_recur_time/count}')


if __name__ == "__main__":
    main()