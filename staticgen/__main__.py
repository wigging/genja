import multiprocessing as mp
from pathlib import Path
from parse_markdown import parse_markdown


def main():
    path = Path('content')
    for file in path.iterdir():
        parse_markdown(file)


def main_parallel():
    path = Path('content')
    n = mp.cpu_count()
    with mp.Pool(n) as p:
        p.map(parse_markdown, path.iterdir())


if __name__ == '__main__':
    # main()
    main_parallel()
