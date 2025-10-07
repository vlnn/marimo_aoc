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
def _(mo, part):
    mo.md(f"""## AOC 2015, Day {part}""")
    return


@app.cell
def _(mo, part):
    mo.md(f"""## Part {part}""")
    return


@app.cell
def _(part):
    def show_a_star():
        return f"Part {part}: *"

    res1 = show_a_star()
    return (res1,)


@app.cell
def _(mo, res1):
    mo.md(rf"""Result: {res1}""")
    return


if __name__ == "__main__":
    app.run()
