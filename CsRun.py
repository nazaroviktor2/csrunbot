import pyautogui as pg
import time
from mss import mss
import numpy as np
import vk_api
import random
from vk_api.utils import get_random_id
import sys, traceback


def get_color_rgb(x, y):
    # Проба цвета с координат
    m = mss()

    monitor = {
        "left": x,
        "top": y,
        "width": 1,
        "height": 1,
    }
    img = m.grab(monitor)
    # Преобразуем этот пиксель в матрицу
    img_arr = np.array(img)

    item = img_arr[0][0]

    r = item[2]
    g = item[1]
    b = item[0]

    return [r, g, b]


def get_color_crash(x, y):
    # Проба цвета с координат
    m = mss()

    monitor = {
        "left": x,
        "top": y,
        "width": 1,
        "height": 1,
    }
    img = m.grab(monitor)
    # Преобразуем этот пиксель в матрицу
    img_arr = np.array(img)

    item = img_arr[0][0]

    r = item[2]
    g = item[1]
    b = item[0]

    return [r, g, b]


def get_color(item):
    color = "Color"
    r = item[0]
    g = item[1]
    b = item[2]

    if 160 < r < 168 and 40 < g < 48 and 60 < b < 66:
        color = "red"  # 1 - 1.2
    elif 110 < r < 120 and 80 < g < 90 and 158 < b < 166:
        color = "purple"  # 1.2 - 1.99
    elif 242 < r < 253 and 20 < g < 26 and 240 < b < 248:
        color = "pink"  # 2x - 3x
    elif 65 < r < 78 and 170 < g < 185 and 118 < b < 127:
        color = "green"  # 3x - 6x
    elif 250 < r < 260 and 250 < g < 260 and 0 <= b <= 5:
        color = "gold"  # 6x-25x
    # elif 218 < r < 228 and 169 < g < 179 and 108 < b < 118:
    #   color = "gold" # 100x
    elif 9 < r < 19 and 190 < g < 205 and 220 < b < 235:
        color = "blue"  # 30x
    return color


def send_mess(user_id, mess):
    vk.messages.send(
        user_id=user_id,
        random_id=get_random_id(),
        message=mess
    )


def set_gun(x, y):
    item = get_color_rgb(x, y)
    r = item[0]
    g = item[1]
    b = item[2]

    if 15 < r < 25 and 205 < g < 220 and 227 < b < 237:
        return False
    else:
        return True


def crash():
    item = get_color_crash(crash_x_y[0], crash_x_y[1])

    r = item[0]
    g = item[1]
    b = item[2]
    if 142 < r < 240 and 32 < g < 57 and 56 < b < 68:
        return False
    else:
        return True


def get_random(start, stop):
    num = random.uniform(start, stop)
    num = float('{:.2f}'.format(num))
    return num


def trade():
    if set_gun(set_gun_x_y[0], set_gun_x_y[1]):
        pg.click(set_gun_x_y[0], set_gun_x_y[1])
    else:
        pass
    time.sleep(0.1)
    pg.click(trade_x_y[0], trade_x_y[1])
    time.sleep(0.3)
    pg.click(trade_price_x_y[0], trade_price_x_y[1])
    time.sleep(0.3)
    pg.press('backspace')
    pg.press('backspace')
    pg.press('backspace')
    pg.press('backspace')
    pg.press('backspace')
    pg.press('backspace')
    pg.write(str(trade_buy_price))
    pg.press('enter')

    time.sleep(0.3)
    pg.click(trade_weapon_x_y[0], trade_weapon_x_y[1])
    time.sleep(0.3)
    pg.click(trade_accept_x_y[0], trade_accept_x_y[1])
    time.sleep(0.1)
    pg.click(trade_exit[0], trade_exit[1])


def bet(game1_bet, game2_bet, game3_bet):
    if game1_bet == "red" and game2_bet == "red":  # условия ставки
        bet_x = get_random(bet_start, bet_stop)
        print(bet_x)
        pg.click(bet_x_y)
        pg.press('backspace')
        pg.press('backspace')
        pg.press('backspace')
        pg.press('backspace')
        pg.press('backspace')
        pg.write(str(bet_x))

        if set_gun(set_gun_x_y[0], set_gun_x_y[1]):
            pg.click(set_gun_x_y[0], set_gun_x_y[1])

        else:
            pass

        time.sleep(0.5)
        pg.click(start_crash_x_y[0], start_crash_x_y[1])

        print("Ставка csrun")

        try:
            send_mess(vk_user_id, ("Ставка csrun была сделана, кеф: " + bet_x))

        except:
            print("Ошибка")

        while crash():
            time.sleep(3)
        time.sleep(3)
        new_game = get_color(get_color_rgb(game1_x_y[0], game1_x_y[1]))

        if new_game == "red":
            loss_mess = "Проигрышь, выпало " + new_game
            print(loss_mess)
            send_mess(vk_user_id, loss_mess)
            trade()
            return False

        else:
            win_mess = "Вы выиграли, выпало " + new_game
            print(win_mess)
            send_mess(vk_user_id, win_mess)
            return True

        print(get_color_rgb(game1_x_y[0], game1_x_y[1]), new_game)
        print(get_color_rgb(game2_x_y[0], game2_x_y[1]), game1_bet)
        print(get_color_rgb(game3_x_y[0], game3_x_y[1]), game2_bet)
        print("--------------------")


vk_session = vk_api.VkApi(token='31898d8c62e3f714c006a383a1ea80c7cf4e02f939c21c7db9e748ac6c0b49b44f6cf4f7ef942b22af068')
vk = vk_session.get_api()
vk_user_id = '299659864'
# send_mess(vk_user_id, "test")

crash_x_y = [301, 302]  # кординаты габена при падении
set_gun_x_y = [26, 394]  # кординаты обвотки оружия
start_crash_x_y = [843, 280]  # корадинаты кнопки начать
# кординаты игр по верхней линии
game1_x_y = [16, 336]
game2_x_y = [68, 336]
game3_x_y = [125, 336]

bet_max = 6  # количетсво ставок за круг  P.S 13 ставок на 1,2  = 10x
bet_start = 1.15  # минимальное значение
bet_stop = 1.20  # максимальное значения x
bet_x_y = [790, 280]  # окно авто сбора

trade_x_y = [70, 1000]  # кнопка магазин скинов
trade_weapon_x_y = [370, 740]  # оружия на которое будет менятся
trade_price_x_y = [440, 680]  # окно для вода цены
trade_buy_price = 0.25  # цена покупки предмета
trade_accept_x_y = [560, 640]  # кнопка потвердить
trade_exit = [643, 594]
# bet("red", "red", "gold")
# trade()
# while True:
#    print(crash())

# print(set_gun(set_gun_x_y[0], set_gun_x_y[1]))


# game1 = get_color(get_color_rgb(game1_x_y[0], game1_x_y[1]))
# game2 = get_color(get_color_rgb(game2_x_y[0], game2_x_y[1]))
# game3 = get_color(get_color_rgb(game3_x_y[0], game3_x_y[1]))
# print(get_color_rgb(game1_x_y[0], game1_x_y[1]), game1)
# print(get_color_rgb(game2_x_y[0], game2_x_y[1]), game2)
# print(get_color_rgb(game3_x_y[0], game3_x_y[1]), game3)

while True:
    i = 0
    try:
        while i < bet_max:
            while crash():
                time.sleep(0.5)

            print(i)

            time.sleep(3)
            game1 = get_color(get_color_rgb(game1_x_y[0], game1_x_y[1]))
            game2 = get_color(get_color_rgb(game2_x_y[0], game2_x_y[1]))
            game3 = get_color(get_color_rgb(game3_x_y[0], game3_x_y[1]))
            print(get_color_rgb(game1_x_y[0], game1_x_y[1]), game1)
            print(get_color_rgb(game2_x_y[0], game2_x_y[1]), game2)
            print(get_color_rgb(game3_x_y[0], game3_x_y[1]), game3)
            print("--------------------")
            if bet(game1, game2, game3):
                i += 1
                send_mess("Осталось ставок до круга " + bet_max - i + 1)
            else:
                i = 0
            time.sleep(5)
        trade()
        send_mess(vk_user_id, "Был выполнен круг")
    except Exception:
        send_mess(vk_user_id, " Произошла ошибка, повтор через 2 минуты")
        print(" Произошла ошибка, повтор через 2 минуты")
        time.sleep(120)
    else:
        pass

'''
71 177 123 green 
164 43 63 red
115 85 162 purple 
28 28 40
255 252 0 gold 
247 23 244 pink 
14 197 229 blue


22 214 231



162, 31, 56
'''
