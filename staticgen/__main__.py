import multiprocessing as mp
import time
from pathlib import Path
from parse_markdown import parse_markdown


def main():
    path = Path('mdcontent')
    for file in path.iterdir():
        parse_markdown(file)


def main_parallel():
    path = Path('mdcontent')
    n = mp.cpu_count()
    with mp.Pool(n) as p:
        p.map(parse_markdown, path.iterdir())


if __name__ == '__main__':
    tic = time.perf_counter()
    main()
    # main_parallel()
    toc = time.perf_counter()
    print('elapsed time', toc - tic)
