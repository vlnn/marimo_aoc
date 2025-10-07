import marimo

__generated_with = "0.16.5"
app = marimo.App(width="medium")


@app.cell(hide_code=True)
def _():
    import marimo as mo
    from pathlib import Path
    return Path, mo


@app.cell(hide_code=True)
def _(Path):
    aoc_dirs = [d for d in Path(".").glob("aoc_*") if d.is_dir()]

    year_day_pairs = []
    for aoc_dir in aoc_dirs:
        year = aoc_dir.name.split("_")[1]
        for notebook in aoc_dir.glob("*.py"):
            stem = notebook.stem
            if "day" in stem.lower():
                _, day = stem.split("_")
                year_day_pairs.append((year, day, str(notebook)))

    available_years = sorted(set(y for y, _, _ in year_day_pairs))
    year_to_days = {y: sorted(set(d for yr, d, _ in year_day_pairs if yr == y), key=lambda x: int(x)) for y in available_years}
    year_day_to_path = {(y, d): p for y, d, p in year_day_pairs}
    return available_years, year_day_to_path, year_to_days


@app.cell(hide_code=True)
def _(available_years, mo):
    year_dropdown = mo.ui.dropdown(
        options=available_years,
        value=available_years[0] if available_years else None,
        label="Year"
    )
    return (year_dropdown,)


@app.cell(hide_code=True)
def _(mo, year_dropdown, year_to_days):
    available_days = year_to_days.get(year_dropdown.value, []) # RRR: can't use year_dropdown value from same cell

    day_dropdown = mo.ui.dropdown(
        options=available_days,
        value=available_days[0] if available_days else None,
        label="Day"
    )

    mo.hstack([year_dropdown, day_dropdown], justify="start")
    return (day_dropdown,)


@app.cell(hide_code=True)
def _(day_dropdown, year_day_to_path, year_dropdown):
    selected_year = year_dropdown.value
    selected_day = day_dropdown.value

    notebook_path = year_day_to_path.get((selected_year, selected_day)) if selected_year and selected_day else None
    return selected_day, selected_year


@app.cell(hide_code=True)
def dynamic_import(selected_day, selected_year):
    import importlib
    parent = importlib.import_module(f"aoc_{selected_year}")
    module = importlib.import_module(f"aoc_{selected_year}.day_{selected_day}")
    app = module.app # RRR no await.app.embed() possible -- interactivity will be broken.
    return (app,)


@app.cell
async def show_results(app):
    result = await app.embed()
    result.output
    return


if __name__ == "__main__":
    app.run()
