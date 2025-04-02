import random

def main():
    draw_things = []
    draw_range = input("Podaj zakres losowania: ")
    draw_range = int(draw_range)
    for i in range(0, draw_range):
        draw_things.append(input("Podaj losowane nazwy/rzeczy: "))
    print(f"Wylosowana nazwa/rzecz to: {draw_things[random.randint(0,draw_range-1)]}")
main()