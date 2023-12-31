import typer

from scale_calculator import tunings

# ==|==0==1==2==3==4==5
# E4|------------------
# B3|------------------
# G3|------------------
# D3|--7-----1---------
# A2|--4-----5--6-----7
# E2|--1-----2--3-----4-----5--6-----7-----1-----2--3-----4-----5--6-----7------1
# ==|==0==1==2==3==4==5==6==7==8==9==10=11=12=13=14=15=16=17=18=19=20=21=22=23=24

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
    tuning: str = typer.Option(
        "e_standard", help="Гитарная настройка. Например, e_standard."
    ),
    scale: str = typer.Option(..., help="Музыкальная шкала. Например, minor."),
    root: str = typer.Option(..., help="Корневая нота. Например, E."),
    # открытая струна или закрытые струны,
    # fretboard: list = typer.Option(
    #     ..., help="Диапазон грифа. Например, лады 0-5.")
    num_frets: int = typer.Option(..., help="Количество ладов. Например, 4"),
):
    typer.echo(f"Вы выбрали: {tuning}, {scale}, {root} и {num_frets} ладов!")

    try:
        tuning = tunings.get(tuning)
    except tunings.UnknownTuningError:
        print(f"Неизвестный строй {tuning}!")
        raise typer.Exit(code=1)

    string_notes = tuning.notes

    # корневая нота на открытой струне
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
    # ---

    # 1
    # положения первой струны
    new_value = f"{note}|" + string_position[:num_hyphens]
    lines[index_to_replace] = new_value

    # положения второй струны
    new_value = (
        f"{note}|" + string_position[num_hyphens + 3 : num_hyphens + 3 + num_hyphens]
    )
    lines[index_to_replace - 1] = new_value

    # положения третьей струны
    new_value = (
        f"{note}|" + string_position[num_hyphens + 3 + num_hyphens + 3 :] + "-" * 9
    )
    lines[index_to_replace - 2] = new_value

    # 2
    # for i in range(3):
    #     current_note = string_notes[i]
    #     new_value = f"{current_note}|" + string_position[i * (num_hyphens + 3):(i + 1) * (num_hyphens + 3)]
    #     lines[index_to_replace - i] = new_value

    # --
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
