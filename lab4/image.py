import pygame

# После импорта библиотеки, необходимо её инициализировать:
pygame.init()


def foo(a, b=1):
    """
    Складывает числа
    
    :param a: первое слагаемое
    :param b: второе слагаемое
    :return: сумма
    """
    return a + b


# И создать окно:
screen = pygame.display.set_mode((300, 200))

# здесь будут рисоваться фигуры
# ...
foo(10, 15)
# после чего, чтобы они отобразились на экране, экран нужно обновить:
pygame.display.update()
# Эту же команду нужно будет повторять, если на экране происходят изменения.

# Наконец, нужно создать основной цикл, в котором будут отслеживаться
# происходящие события.
# Пока единственное событие, которое нас интересует - выход из программы.
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
