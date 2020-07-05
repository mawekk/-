import pygame
import random
import sys

pygame.init()

screen_width, screen_height = 600, 800
size = (screen_width, screen_height)
screen = pygame.display.set_mode(size)

pygame.display.set_caption('memory&attention')
img = pygame.image.load('data\\icon.jpg')
pygame.display.set_icon(img)
menu_background = pygame.image.load('data\\background1.png')

grey = (240, 240, 240)
white = (255, 255, 255)
purple = (178, 127, 176)
blue = (52, 78, 110)
light_blue = (54, 193, 203)
pink = (255, 78, 132)


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.color = light_blue
        self.color_t = blue
        self.color_t_active = white

    def draw(self, x, y, text, text_size=25):
        mouse = pygame.mouse.get_pos()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(screen, self.color, (x, y, self.width, self.height))
            print_text(text, x + 10, y + 10, self.color_t_active, text_size)
        else:
            pygame.draw.rect(screen, self.color, (x, y, self.width, self.height), 2)
            print_text(text, x + 10, y + 10, self.color_t, text_size)


def draw_cell(x, y, cell_size, digit, a=45, b=35, c=30, text_size=40):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    pygame.draw.rect(screen, white, (x, y, cell_size, cell_size))
    if digit < 10:
        print_text(str(digit), x + a, y + c, blue, text_size)
    else:
        print_text(str(digit), x + b, y + c, blue, text_size)

    if x < mouse[0] < x + cell_size and y < mouse[1] < y + cell_size:
        pygame.draw.rect(screen, grey, (x, y, cell_size, cell_size))
        if click[0] == 1:
            if digit < 10:
                print_text(str(digit), x + a, y + c, pink, text_size)
            else:
                print_text(str(digit), x + b, y + c, pink, text_size)
        else:
            if digit < 10:
                print_text(str(digit), x + a, y + c, blue, text_size)
            else:
                print_text(str(digit), x + b, y + c, blue, text_size)


def print_text(text, x, y, font_color, font_size=27, bold=True):
    if bold:
        font = pygame.font.Font('data\\fonts\\montb.ttf', font_size)
    else:
        font = pygame.font.Font('data\\fonts\\mont.ttf', font_size)
    text = font.render(text, True, font_color)
    screen.blit(text, (x, y))


def timer(start, now, x, y, timer_color=blue, timer_size=35, print_time=False):
    sec = (now - start) // 1000
    minute = str(sec // 60)
    sec %= 60
    if sec < 10:
        sec = '0' + str(sec)
    else:
        sec = str(sec)
    time = minute + ':' + sec
    if print_time:
        print_text(time, x, y, timer_color, timer_size)
    else:
        return time


def terminate():
    pygame.quit()
    sys.exit()


def result(score, name):
    new_record = False
    with open('data\\records\\record_' + name + '.txt', 'r') as f:
        record = f.read()
    if name == 'shulte':
        if record == '':
            record = 100000
            record = timer(0, int(record), 0, 0)
        if record > score:
            new_record = True
            with open('data\\records\\record_' + name + '.txt', 'w') as f:
                f.write(str(score))
            record = score
    else:
        if record == '':
            record = 0
        record = int(record)
        if record < score:
            new_record = True
            with open('data\\records\\record_' + name + '.txt', 'w') as f:
                f.write(str(score))
            record = score
    return record, new_record


def game_over(score, name):
    back_button_game_over = Button(130, 55)
    again_button = Button(130, 55)
    x_back, y_back = 235, 580
    x_again, y_again = 235, 510
    y = 120
    best, new_record = result(score, name)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if x_back < mouse[0] < x_back + 150 and y_back < mouse[1] < y_back + 55:
                    return False
                if x_again < mouse[0] < x_again + 150 and y_again < mouse[1] < y_again + 55:
                    return True

        screen.blit(menu_background, (0, 0))
        print_text('Ваш результат:', 20, y, blue, 50)
        print_text('Лучший результат:', 20, y + 160, blue, 50)
        print_text(str(score), 20, y + 60, pink, 80)
        print_text(str(best), 20, y + 220, pink, 80)
        if new_record:
            print_text('Новый рекорд!', 20, y + 310, pink, 40)
        back_button_game_over.draw(x_back, y_back, 'В меню')
        again_button.draw(x_again, y_again, 'Ещё раз')

        pygame.display.update()
        clock.tick(FPS)


def menu():
    b1 = Button(400, 55)
    b2 = Button(400, 55)
    b3 = Button(400, 55)
    b4 = Button(400, 55)
    b5 = Button(400, 55)
    help_button = Button(145, 55)
    records_button = Button(145, 55)
    button_mas = [b1, b2, b3, b4, b5]
    actions = [shulte, summa, circles, strup, matrix]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                x, y = 20, 130
                for i in range(5):
                    if x < mouse[0] < x + 400 and y < mouse[1] < y + 55:
                        return actions[i]
                    y += 70
                if 20 < mouse[0] < 165 and 620 < mouse[1] < 675:
                    return help_
                elif 20 < mouse[0] < 165 and 550 < mouse[1] < 605:
                    return records

        screen.blit(menu_background, (0, 0))
        print_text('Тренировка памяти', 20, 10, pink, 40)
        print_text('и внимания', 20, 50, pink, 40)
        x, y = 20, 130
        for i in range(5):
            button_mas[i].draw(x, y, headers[i])
            y += 70
        records_button.draw(20, 550, 'Рекорды')
        help_button.draw(20, 620, 'Помощь')
        pygame.display.update()
        clock.tick(FPS)


def help_():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if x_back < mouse[0] < x_back + 105 and y_back < mouse[1] < y_back + 55:
                    return False

        screen.blit(menu_background, (0, 0))
        print_text('Что нужно делать?', 20, 10, pink, 40)
        x, y = 20, 130
        for i in range(5):
            print_text(headers[i] + descriptions[i * 2], x, y, blue, 20)
            print_text(descriptions[i * 2 + 1], x, y + 35, blue, 20)
            y += 70
        x_back, y_back = x, y + 30
        back_button.draw(x_back, y_back, 'В меню')
        pygame.display.update()
        clock.tick(FPS)


def records():
    names = ['shulte', 'summa', 'circles', 'strup', 'matrix']
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if x_back < mouse[0] < x_back + 105 and y_back < mouse[1] < y_back + 55:
                    return False

        screen.blit(menu_background, (0, 0))
        print_text('Ваши рекорды:', 20, 10, pink, 40)
        x, y = 20, 130
        for i in range(5):
            print_text(headers[i], x, y, blue, 30)
            with open('data\\records\\record_' + names[i] + '.txt', 'r') as f:
                record = f.read()
                if record == '':
                    print_text('—', x + 400, y, pink, 30)
                else:
                    print_text(record, x + 400, y, pink, 30)
            y += 70
        pygame.draw.line(screen, light_blue, (x + 360, 110), (x + 360, y - 10), 3)
        x_back, y_back = x, y + 30
        back_button.draw(x_back, y_back, 'В меню')
        pygame.display.update()
        clock.tick(FPS)


def shulte():
    table = [[0] * 5 for _ in range(5)]
    numbers = [i for i in range(1, 26)]
    random.shuffle(numbers)
    q = 0
    for i in range(5):
        for k in range(5):
            table[i][k] = numbers[q]
            q += 1

    block = 114
    margin = 5
    number = 1
    time_start = pygame.time.get_ticks()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                col = mouse[0] // (block + margin)
                row = (mouse[1] - 200) // (block + margin)
                if table[row][col] == number:
                    time_end = pygame.time.get_ticks()
                    if number < 25:
                        number += 1
                    else:
                        return timer(time_start, time_end, 210, 160), 'shulte'

        screen.fill(white)
        x, y = 0, 200
        pygame.draw.rect(screen, light_blue, (x, y, 600, 600))
        for row in range(5):
            for col in range(5):
                x = col * block + (col + 1) * margin
                y = 200 + row * block + (row + 1) * margin
                draw_cell(x, y, block, table[row][col])

        timer(time_start, pygame.time.get_ticks(), 50, 70, blue, 35, True)

        print_text('Найдите:', 225, 60, blue, 50)
        print_text(str(number), 490, 50, pink, 70)

        pygame.display.update()
        clock.tick(FPS)


def circles():
    level = 1
    new_level = True
    wrong = False
    coords = []
    x, y = random.randint(50, 550), random.randint(50, 750)
    radius = random.randint(10, 45)
    coords.append((x, y, radius))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if (mouse[0] - x) ** 2 + (mouse[1] - y) ** 2 <= radius ** 2:
                    x, y = random.randint(50, 550), random.randint(50, 750)
                    radius = random.randint(10, 45)
                    k = 0
                    while k != len(coords):
                        for i in range(len(coords)):
                            x1, y1, r = coords[i][0], coords[i][1], coords[i][2]
                            d = ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
                            if d <= r + radius:
                                x, y = random.randint(50, 550), random.randint(50, 750)
                                k = 0
                                break
                            else:
                                k += 1
                    coords.append((x, y, radius))
                    level += 1
                    new_level = True
                else:
                    for i in range(len(coords) - 1):
                        x1, y1, r = coords[i][0], coords[i][1], coords[i][2]
                        if (mouse[0] - x1) ** 2 + (mouse[1] - y1) ** 2 <= r ** 2:
                            wrong = True
                            break

        if new_level:
            screen.fill(white)
            last = pygame.time.get_ticks()
            now = pygame.time.get_ticks()
            print_text('Уровень', 160, 300, blue, 50)
            print_text(str(level), 410, 300, pink, 50)
            pygame.display.update()
            while now - last < 1000:
                now = pygame.time.get_ticks()
            screen.fill(white)
            new_level = False

        if wrong:
            last = pygame.time.get_ticks()
            now = pygame.time.get_ticks()
            pygame.draw.circle(screen, pink, (x, y), radius)
            pygame.display.update()
            while now - last < 1000:
                now = pygame.time.get_ticks()
            return (level - 1) * 100, 'circles'

        for i in range(len(coords)):
            x1, y1, r = coords[i][0], coords[i][1], coords[i][2]
            pygame.draw.circle(screen, light_blue, (x1, y1), r)

        pygame.display.update()
        clock.tick(FPS)


def summa():
    def print_summa(ans_1, ans_2, summ, text=False):
        print_text('+', 210, 240, pink, 70)
        print_text('= ' + str(summ), 370, 240, pink, 70)
        x1 = 130
        x2 = 290
        if ans_1 != '?':
            if 9 < ans_1 < 100:
                x1 = 110
            elif 99 < ans_1 < 1000:
                x1 = 90
        if ans_2 != '?':
            if 9 < ans_2 < 100:
                x2 = 270
            elif 99 < ans_2 < 1000:
                x2 = 240
        print_text(str(ans_1), x1, 240, blue, 70)
        print_text(str(ans_2), x2, 240, blue, 70)
        if text:
            if text == 'Ошибка!':
                print_text(text, 160, 350, blue, 60)
                print_text('+', 210, 450, pink, 70)
                print_text('= ' + str(ans_1 + ans_2), 370, 450, pink, 70)
                print_text(str(ans_1), x1, 450, blue, 70)
                print_text(str(ans_2), x2, 450, blue, 70)
            else:
                print_text(text, 185, 350, blue, 60)

    level = 1
    a, b = 0, 5
    terms = [0] * 3
    indexes = []

    time = 91000
    start = pygame.time.get_ticks()
    now = pygame.time.get_ticks()
    track = 0

    f_size = 55
    a1, b1, c1 = 45, 35, 30
    margin = 5
    block = 130

    new_level = True
    wrong = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if y < mouse[1] < (y + 2 * margin + block):
                    index = (mouse[0] - x) // (block + margin)
                    if index in indexes:
                        if ans_2 == '?':
                            ans_1 = ans_2
                        else:
                            ans_2 = '?'
                        indexes.remove(index)
                    else:
                        indexes.append(index)
                        if ans_1 == '?':
                            ans_1 = terms[index]
                        else:
                            ans_2 = terms[index]
                            if ans_1 + ans_2 == summ:
                                level += 1
                                new_level = True
                            else:
                                wrong = True

        screen.blit(menu_background, (0, 0))
        print_text('Уровень', 220, 30, blue)
        print_text(str(level), 355, 27, pink, 30)
        print_text('Подберите верные слагаемые', 50, 80, blue, 30)
        timer(now, time + start, 260, 130, blue, 30, True)
        if timer(now, time + start, 260, 130, blue, 30) == '0:00':
            return (level - 1) * 100, 'summa'
        now = pygame.time.get_ticks()

        if new_level:
            if level > 1:
                print_summa(ans_1, ans_2, summ, 'Верно!')
                pygame.display.update()
                last = pygame.time.get_ticks()
                now = pygame.time.get_ticks()
                while now - last < 1000:
                    now = pygame.time.get_ticks()

            track +=1
            a += 5
            b += 5
            if track == 4:
                terms.append(0)
                margin = 6
                block = 90
                f_size = 40
                a1, b1, c1 = 33, 25, 20
            elif track == 7:
                terms = [0] * 3
                margin = 5
                block = 130
                f_size = 55
                a1, b1, c1 = 45, 35, 30
                track = 0
            if level % 5 == 0:
                time += 1000

            indexes = []
            summ = random.randint(a, b)
            terms[0] = summ - random.randint(1, summ - 1)
            terms[1] = summ - terms[0]
            for i in range(2, len(terms)):
                test = random.randint(1, summ - 1)
                while test in terms:
                    test = random.randint(1, summ - 1)
                terms[i] = test

            random.shuffle(terms)
            ans_1, ans_2 = '?', '?'

            new_level = False

        if wrong:
            print_summa(ans_1, ans_2, summ, 'Ошибка!')
            pygame.display.update()
            last = pygame.time.get_ticks()
            now = pygame.time.get_ticks()
            while now - last < 1500:
                now = pygame.time.get_ticks()
            return (level - 1) * 100, 'summa'

        print_summa(ans_1, ans_2, summ)
        x, y = 100, 450
        pygame.draw.rect(screen, light_blue,
                         (x - margin, y - margin, (len(terms) + 1) * margin + len(terms) * block, 2 * margin + block))
        for i in range(len(terms)):
            draw_cell(x, y, block, terms[i], a1, b1, c1, f_size)
            x += block + margin

        pygame.display.update()
        clock.tick(FPS)


def strup():
    level = 1
    span = 2
    new_level = True
    last_word = ''

    button_1 = Button(200, 55)
    button_2 = Button(200, 55)

    time = 91000
    start = pygame.time.get_ticks()
    now = pygame.time.get_ticks()

    words = ['Синий', 'Красный', 'Зелёный', 'Оранжевый', 'Чёрный', 'Розовый', 'Фиолетовый']
    colors = [(55, 81, 203), (203, 55, 69), (55, 203, 104), (255, 152, 80), (0, 0, 0), pink, (157, 55, 203)]
    xs = [180, 145, 145, 80, 160, 150, 70]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                pressed_button = 0
                if x_1 < mouse[0] < x_1 + 200 and y_1 < mouse[1] < y_1 + 55:
                    pressed_button = 1
                elif x_2 < mouse[0] < x_2 + 200 and y_2 < mouse[1] < y_2 + 55:
                    pressed_button = 2
                if pressed_button != 0:
                    if true_button == pressed_button:
                        level += 1
                        new_level = True
                    else:
                        return (level - 1) * 100, 'strup'

        screen.blit(menu_background, (0, 0))
        print_text('Уровень', 220, 30, blue)
        print_text(str(level), 355, 27, pink, 30)
        print_text('Каким цветом написано слово?', 40, 80, blue, 30)
        timer(now, time + start, 260, 130, blue, 30, True)
        if timer(now, time + start, 260, 130, blue, 30) == '0:00':
            return (level - 1) * 100, 'strup'
        now = pygame.time.get_ticks()

        if new_level:
            if level % 7 == 0 and span < 6:
                span += 1
            i_word = random.randint(0, span)
            word = words[i_word]
            while last_word == word:
                i_word = random.randint(0, span)
                word = words[i_word]
            last_word = word
            i_color = random.randint(0, span)
            color = colors[i_color]
            text = ['', '']
            text[0] = words[i_color]
            text[1] = word
            while text[1] == text[0]:
                text[1] = words[random.randint(0, span)]
            random.shuffle(text)
            if text[0] == words[i_color]:
                true_button = 1
            else:
                true_button = 2

            new_level = False

        print_text(word, xs[i_word], 300, color, 70, False)
        x_1, y_1 = 200, 500
        x_2, y_2 = 200, 570
        button_1.draw(x_1, y_1, text[0])
        button_2.draw(x_2, y_2, text[1])

        pygame.display.update()
        clock.tick(FPS)


def matrix():
    def draw_matrix():
        pygame.draw.rect(screen, blue, (0, 200, 600, 600))
        for row in range(blocks):
            for col in range(blocks):
                x = col * block + (col + 1) * margin
                y = 200 + row * block + (row + 1) * margin
                if (row, col) not in matrix_check:
                    pygame.draw.rect(screen, white, (x, y, block, block))
                else:
                    pygame.draw.rect(screen, light_blue, (x, y, block, block))
        pygame.display.update()


    level = 1
    new_level = True
    wrong = False

    cells = 3
    blocks = 3
    block = 196
    margin = 3

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 200 <= mouse[1] <= 800:
                    col = int(mouse[0] // (block + margin))
                    row = int((mouse[1] - 200) // (block + margin))
                    if (row, col) in matrix_check:
                        matrix_check.remove((row, col))
                    else:
                        matrix_check.append((row, col))
                    if len(matrix_check) == cells:
                        matrix_check.sort()
                        if matrix_check == matrix_cells:
                            level += 1
                            new_level = True
                        else:
                            wrong = True



        if new_level:
            if level > 1:
                draw_matrix()
                last = pygame.time.get_ticks()
                now = pygame.time.get_ticks()
                while now - last < 500:
                    now = pygame.time.get_ticks()
            screen.fill(white)
            last = pygame.time.get_ticks()
            now = pygame.time.get_ticks()
            print_text('Уровень', 160, 300, blue, 50)
            print_text(str(level), 410, 300, pink, 50)
            pygame.display.update()
            while now - last < 500:
                now = pygame.time.get_ticks()

            if level > 1:
                cells += 1
                if level % 2 != 0:
                    blocks += 1
                    block = (screen_width - margin * (blocks + 1)) // blocks

            matrix_cells = []
            matrix_check = []
            for i in range(cells):
                row, col = random.randint(0, blocks - 1), random.randint(0, blocks - 1)
                while (row, col) in matrix_cells:
                    row, col = random.randint(0, blocks - 1), random.randint(0, blocks - 1)
                matrix_cells.append((row, col))
            matrix_cells.sort()

            screen.fill(white)

        screen.fill(white)
        print_text('Счёт:', 50, 80, blue, 30)
        print_text(str((level - 1) * 100), 150, 80, pink, 30)
        print_text('Ячейки:', 350, 80, blue, 30)
        print_text(str(cells), 500, 80, pink, 30)
        draw_matrix()

        if new_level:
            for row in range(blocks):
                for col in range(blocks):
                    x = col * block + (col + 1) * margin
                    y = 200 + row * block + (row + 1) * margin
                    if (row, col) in matrix_cells:
                        pygame.draw.rect(screen, light_blue, (x, y, block, block))
            pygame.display.update()
            new_level = False
            last = pygame.time.get_ticks()
            now = pygame.time.get_ticks()
            while now - last < 1000:
                now = pygame.time.get_ticks()

        if wrong:
            last = pygame.time.get_ticks()
            now = pygame.time.get_ticks()
            for row in range(blocks):
                for col in range(blocks):
                    x = col * block + (col + 1) * margin
                    y = 200 + row * block + (row + 1) * margin
                    if (row, col) in matrix_cells:
                        pygame.draw.rect(screen, light_blue, (x, y, block, block))
                    elif (row, col) in matrix_check and (row, col) not in matrix_cells:
                        pygame.draw.rect(screen, pink, (x, y, block, block))
            pygame.display.update()
            while now - last < 1500:
                now = pygame.time.get_ticks()
            return (level - 1) * 100, 'matrix'

        pygame.display.update()
        clock.tick(FPS)


clock = pygame.time.Clock()
FPS = 60
headers = ['Таблица Шульте', 'Быстрое сложение', 'Круги ', 'Задача Струпа', 'Матрицы памяти']
descriptions = [' — найдите все числа от 1 до 25 как', 'можно быстрее.',
                ' — выберите такие два числа, ', 'сумма которых будет равна указанной.',
                ' — запоминайте расположение кругов на ', 'экране и правильно отмечайте новый.',
                ' — посмотрите на слово на экране и',  'определите, каким цветом оно написано.',
                ' — запомните рисунок на экране', 'и постарайтесь повторить его.']
back_button = Button(120, 55)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()

    game = menu()
    if game is not None:
        while True:
            end = game()
            if end:
                again = game_over(end[0], end[1])
                if not again:
                    break
            else:
                break

    pygame.display.update()
    clock.tick(FPS)
