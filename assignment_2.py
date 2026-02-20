import timeit

from math49emodule import get_files_path


def solve_problem_67() -> None:
    with open(get_files_path() / "0067_triangle.txt") as file:
        print(file.read())


if __name__ == "__main__":
    begin = timeit.timeit()
    solve_problem_67()
    end = timeit.timeit()
    print(f"Finished in {end - begin} seconds.")
