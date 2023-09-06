import typer


# def main():
#     print(
#         """
# ==|==0==1==2==3==4==5
# E4|------------------
# B3|------------------
# G3|------------------
# D3|--7-----1---------
# A2|--4-----5--6------
# E2|--1-----2--3------
# ==|==0==1==2==3==4==5
# """
#     )

#     print(
#         """
# e|-0-------
# B|-0-1---3-
# G|-0-2-----
# D|-0-2---4-
# A|-0-2-3---
# E|-0-2-3---
# """
#     )

def main(
    # guitar_type: str = typer.Option(
    #     ..., help="Тип гитары. Например, гитара или бас-гитара"),
    # num_strings: str = typer.Option(
    #     ..., help="Количество струн на гитаре. Например, 6."),
    tuning: str = typer.Option(
        ..., help="Гитарная настройка. Например, e_standard."),
    scale: str = typer.Option(
        ..., help="Музыкальная шкала. Например, minor."),
    root: str = typer.Option(
         ..., help="Корневая нота. Например, e."),
    # neck_range: str = typer.Option(
    #     ..., help="Диапазон грифа. Например, ноты E2-E4 или лады 1-12."),
):
    typer.echo(f"Вы выбрали {tuning}, {scale}, {root}")


if __name__ == "__main__":
    typer.run(main)
