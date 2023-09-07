import typer

# ==|==0==1==2==3==4==5
# E4|------------------
# B3|------------------
# G3|------------------
# D3|--7-----1---------
# A2|--4-----5--6------
# E2|--1-----2--3------
# ==|==0==1==2==3==4==5

# e|-0-------
# B|-0-1---3-
# G|-0-2-----
# D|-0-2---4-
# A|-0-2-3---
# E|-0-2-3---


def main(
    # guitar_type: str = typer.Option(
    #     ..., help="Тип гитары. Например, гитара или бас-гитара"),
    # num_strings: str = typer.Option(
    #     ..., help="Количество струн на гитаре. Например, 6."),
    tuning: str = typer.Option(
        ..., help="Гитарная настройка. Например, e_standard."),
    # scale: str = typer.Option(
    #     ..., help="Музыкальная шкала. Например, minor."),
    # root: str = typer.Option(
    #      ..., help="Корневая нота. Например, e."),
    # fretboard: list = typer.Option(
    #     ..., help="Диапазон грифа. Например, лады 0-5.")
    num_frets: int = typer.Option(
        ..., help="Количество ладов. Например, 6"),
):
    typer.echo(f"Вы выбрали {tuning} и {num_frets} ладов!")

    if tuning == "e_standart":
        string_notes = ["E2", "A2", "D3", "G3", "B3", "E4"]

    print("Нотация:")
    print(draw_notation(string_notes, num_frets))
    print("Табулатура:")
    print(draw_tablature(string_notes, num_frets))


def draw_notation(string_notes, num_frets):

    num_hyphens = num_frets * 3

    # верхняя горизонтальная линия
    notation = "==|==" + "==".join([str(i) for i in range(num_frets)])

    # гриф гитары
    for note in reversed(string_notes):
        notation += f"\n{note}|"
        notation += "-" * num_hyphens

    # нижняя горизонтальная линия
    notation += "\n" + "==|==" + "==".join([str(i) for i in range(num_frets)])

    return notation


def draw_tablature(string_notes, num_frets):
    tablature = f"{string_notes[0][0]}|"
    tablature += "-" * 9

    for note in string_notes[1:]:
        tablature += f"\n{note[0]}|"
        tablature += "-" * 9

    return tablature


if __name__ == "__main__":
    typer.run(main)
