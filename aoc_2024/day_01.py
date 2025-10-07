import marimo

app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    return (mo,)


@app.cell
def _(mo):
    mo.md("""## AOC 2024, Day 01""")
    return


@app.cell
def _(mo):
    mo.md("""## Part 1""")
    return


@app.cell
def _():
    def show_a_star():
        return "*"

    res1 = show_a_star()
    return (res1,)


@app.cell
def _(mo, res1):
    mo.md(rf"""Result: {res1}""")
    return


if __name__ == "__main__":
    app.run()
