import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    part_dropdown = mo.ui.dropdown(
        options=[1,2],
        value=1,
        label="Part"
    )
    return (part_dropdown,)


@app.cell
def _(part_dropdown):
    part_dropdown
    return


@app.cell
def _(part_dropdown):
    part = part_dropdown.value
    return (part,)


@app.cell
def _():
    from itertools import accumulate
    def read_input(_,_1):
        return "(())(())((((()()))))))"

    def solve_part1(directions) -> int:
        lefts = directions.count("(")
        rights = directions.count(")")

        return lefts - rights


    def parse_as_ints(directions) -> list[int]:
        ints = [1 if c == "(" else -1 for c in directions]
        return ints


    def solve_part2(directions) -> int:
        ints = parse_as_ints(directions)
        accs = list(accumulate(ints))
        return accs.index(-1) + 1


    def part1() -> int:
        raw_input = read_input(2015, 1)
        return solve_part1(raw_input)


    def part2() -> int | None:
        raw_input = read_input(2015, 1)
        return solve_part2(raw_input)
    return part1, part2


@app.cell
def _(part, part1, part2):
    if part == 1:
        res = part1()
    else:
        res = part2()

    res
    return


if __name__ == "__main__":
    app.run()
