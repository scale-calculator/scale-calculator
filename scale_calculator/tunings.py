import tomllib
from importlib import resources

import typer
from rich import print
from rich.table import Table

app = typer.Typer()


class Tuning:
    def __init__(self, short_name, name, notes):
        self.short_name = short_name
        self.name = name
        self.notes = notes

    @classmethod
    def from_file(cls, file_):
        with file_.open(mode="rb") as f:
            parsed = tomllib.load(f)
            return cls(file_.stem, parsed["name"], parsed["tuning"]["notes"])


class UnknownTuningError(Exception):
    pass


def get_all():
    tunings_dir = resources.files("scale_calculator.data") / "tunings"
    return [Tuning.from_file(f) for f in tunings_dir.glob("*.toml")]


TUNINGS = {tuning.short_name: tuning for tuning in get_all()}


def get(name):
    try:
        return TUNINGS[name]
    except KeyError:
        raise UnknownTuningError(name)


@app.command()
def list():
    grid = Table.grid(expand=True)
    grid.add_column()
    grid.add_column()
    for tuning in get_all():
        grid.add_row(tuning.short_name, tuning.name)
    print(grid)


@app.command()
def show(tuning):
    pass
