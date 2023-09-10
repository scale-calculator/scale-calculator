import typer

from scale_calculator import tunings

# ==|==0==1==2==3==4==5
# E4|------------------
# B3|------------------
# G3|------------------
# D3|--7-----1---------
# A2|--4-----5--6-----7
# E2|--1-----2--3-----4-----5--6-----7
# ==|==0==1==2==3==4==5==6==7==8==9==10

"""
C-D-E-F-G-A-B-C
 2 2 1 2 2 2 1

C C# D D# E F F# G G# A A# B C


"""

# e|-0-------
# B|-0-1---3-
# G|-0-2-----
# D|-0-2---4-
# A|-0-2-3---
# E|-0-2-3---

app = typer.Typer()
app.add_typer(tunings.app, name="tunings")


@app.command()
def calc(
    # guitar_type: str = typer.Option(
    #     ..., help="Тип гитары. Например, гитара или бас-гитара"),
    # num_strings: str = typer.Option(
    #     ..., help="Количество струн на гитаре. Например, 6."),
    tuning: str = typer.Option(..., help="Гитарная настройка. Например, e_standard."),
    scale: str = typer.Option(..., help="Музыкальная шкала. Например, minor."),
    root: str = typer.Option(..., help="Корневая нота. Например, E."),
    # fretboard: list = typer.Option(
    #     ..., help="Диапазон грифа. Например, лады 0-5.")
    num_frets: int = typer.Option(..., help="Количество ладов. Например, 4"),
):
    typer.echo(f"Вы выбрали: {tuning}, {scale}, {root} и {num_frets} ладов!")

    if tuning == "e_standart":
        string_notes = ["E2", "A2", "D3", "G3", "B3", "E4"]

    if scale == "minor":
        string_position = "--1-----2--3-----4-----5--6-----7"

    print("Нотация:")
    print(draw_notation(string_notes, string_position, num_frets, root))
    print("Табулатура:")
    print(draw_tablature(string_notes, num_frets))


def draw_notation(string_notes, string_position, num_frets, root):
    num_hyphens = num_frets * 3

    # верхняя горизонтальная линия
    notation = "==|==" + "==".join(str(i) for i in range(num_frets))

    lines = []

    # скелет грифа гитары
    for note in reversed(string_notes):
        line = f"{note}|"
        line += "-" * num_hyphens
        lines.append(line)

    # определение первой струны
    for index, line in enumerate(reversed(lines)):
        if line.startswith(root):
            index_to_replace = len(lines) - 1 - index
            break

    # положения первой струны
    new_value = f"{note}|" + string_position[:num_hyphens]
    lines[index_to_replace] = new_value

    # гриф гитары
    notation += "\n" + "\n".join(lines)

    # нижняя горизонтальная линия
    notation += "\n" + "==|==" + "==".join(str(i) for i in range(num_frets))

    return notation


def draw_tablature(string_notes, num_frets):
    tablature = f"{string_notes[0][0]}|"
    tablature += "-" * 9

    for note in string_notes[1:]:
        tablature += f"\n{note[0]}|"
        tablature += "-" * 9

    return tablature


if __name__ == "__main__":
    app()
