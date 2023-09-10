from importlib import resources

import typer
import tomllib

app = typer.Typer()


class Tuning:
    def __init__(self, name, notes):
        self.name = name
        self.notes = notes

    @classmethod
    def from_file(cls, file_):
        with file_.open(mode="rb") as f:
            parsed = tomllib.load(f)
            return cls(file_.stem, parsed["tuning"]["notes"])


class UnknownTuningError(Exception):
    pass


def get_all():
    tunings_dir = resources.files("scale_calculator.data") / "tunings"
    return [Tuning.from_file(f) for f in tunings_dir.glob("*.toml")]


TUNINGS = {tuning.name: tuning for tuning in get_all()}


def get(name):
    try:
        return TUNINGS[name]
    except KeyError:
        raise UnknownTuningError(name)


@app.command()
def list():
    for tuning in get_all():
        print(tuning.name)


@app.command()
def show(tuning):
    pass
