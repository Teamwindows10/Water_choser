import random

def main():
    draw_things = []
    draw_range = input("Podaj zakres losowania: ")
    draw_range = int(draw_range)
    for i in range(0, draw_range):
        draw_things.append(input("Podaj losowane nazwy/rzeczy: "))
    random_num = random.randint(0,draw_range-1)
    print(f"Wylosowana nazwa/rzecz to: {draw_things[random_num]}")
    print(f"Wylosowana nazwa/rzecz odwrócona to: {draw_things[random_num][::-1]}")
main()

print("f_wheel")