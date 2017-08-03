from PIL import ImageGrab
import os
import time
import win32api, win32con
import win32gui
import win32ui
from ctypes import windll
 
branco = (255,255,255)
azul = (0,0,255)
cinza_escuro = (123,123,123)
preto = (0,0,0)
verde = (0,123,0)
vermelho = (255,0,0)
azul_escuro = (0,0,123)
violeta = (123,0,0)
verde_agua = (0,123,123)
 
x_inicial = 381 #549
y_inicial = 174 #174
 
 
altura = 16 #16
largula = 30 #30
 
dc = windll.user32.GetDC(0)
 
completos = []
 
#Funcao para posicionar mouse
def mousePos(x,y):
    win32api.SetCursorPos((x,y))
 
 
#Funcao de click esquerdo
def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
 
 
#Funcao de click direito
def RightClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
 
 
#Funcao para clicar nos botoes com botao esquerdo
def click_square_volta(x,y):
    global im
    if im.getpixel((x + 9,y)) == branco and im.getpixel((x + 16,y)) != preto and x != 1013:
        mousePos(x+16,y)
        leftClick()
        im = ImageGrab.grab()   
    if im.getpixel((x - 9,y)) == cinza_escuro and im.getpixel((x - 16,y)) != preto and x != 549:
        mousePos(x-16,y)
        leftClick()
        im = ImageGrab.grab()
    if im.getpixel((x,y+9)) == branco and im.getpixel((x,y+16)) != preto and y != 414:
        mousePos(x,y+16)
        leftClick()
        im = ImageGrab.grab()
    if im.getpixel((x,y-9)) == cinza_escuro and im.getpixel((x,y-16)) != preto and y != 174:
        mousePos(x,y-16)
        leftClick()
        im = ImageGrab.grab()
    if im.getpixel((x+9,y+9)) == branco and im.getpixel((x+16,y+16)) != preto and x != 1013 and y != 414:
        mousePos(x + 16,y+16)
        leftClick()
        im = ImageGrab.grab()
    if im.getpixel((x+9,y-9)) == cinza_escuro and im.getpixel((x+16,y-16)) != preto and x != 1013 and y != 174:
        mousePos(x + 16,y-16)
        leftClick()
        im = ImageGrab.grab()
    if im.getpixel((x-9,y+9)) == cinza_escuro and im.getpixel((x-16,y+16)) != preto and x != 549 and y != 414:
        mousePos(x-16,y+16)
        leftClick()
        im = ImageGrab.grab()
    if im.getpixel((x-9,y-9)) == cinza_escuro and im.getpixel((x-16,y-16)) != preto and x != 549 and y != 174: 
        mousePos(x-16,y-16)
        leftClick()
        im = ImageGrab.grab()
    im = ImageGrab.grab()
    return im
 
#Funcao para marcar bombas
def check_square_volta(x,y):
    global im
    im = ImageGrab.grab()
    if im.getpixel((x + 9,y)) == branco and im.getpixel((x + 16,y)) != preto and x != 1013:
        mousePos(x+16,y)
        RightClick()
        im = ImageGrab.grab()
    if im.getpixel((x - 9,y)) == cinza_escuro and im.getpixel((x - 16,y)) != preto and x != 549:
        mousePos(x-16,y)
        RightClick()
        im = ImageGrab.grab()
    if im.getpixel((x,y+9)) == branco and im.getpixel((x,y+16)) != preto and y != 414 :
        mousePos(x,y+16)
        RightClick()
        im = ImageGrab.grab()
    if im.getpixel((x,y-9)) == cinza_escuro and im.getpixel((x,y-16)) != preto and y != 174:
        mousePos(x,y-16)
        RightClick()
        im = ImageGrab.grab()
    if im.getpixel((x+9,y+9)) == branco and im.getpixel((x+16,y+16)) != preto and x != 1013 and y != 414:
        mousePos(x + 16,y+16)
        RightClick()
        im = ImageGrab.grab()
    if im.getpixel((x+9,y-9)) == cinza_escuro and im.getpixel((x+16,y-16)) != preto and x != 1013 and y != 174:
        mousePos(x + 16,y-16)
        RightClick()
        im = ImageGrab.grab()
    if im.getpixel((x-9,y+9)) == cinza_escuro and im.getpixel((x-16,y+16)) != preto and x != 549 and y != 414:
        mousePos(x-16,y+16)
        RightClick()
        im = ImageGrab.grab()
    if im.getpixel((x-9,y-9)) == cinza_escuro and im.getpixel((x-16,y-16)) != preto and x != 549 and y != 174: 
        mousePos(x-16,y-16)
        RightClick()
        im = ImageGrab.grab()
    return im
 
#Funcao que retorna numero de quadrados livres em volta
def check_num_square_volta(x,y):
    global im
    check_numero = 0
    if im.getpixel((x + 9,y)) == branco:
        check_numero += 1
    if im.getpixel((x - 9,y)) == cinza_escuro:
        check_numero += 1
    if im.getpixel((x,y+9)) == branco:
        check_numero += 1
    if im.getpixel((x,y-9)) == cinza_escuro:
        check_numero += 1
    if im.getpixel((x+9,y+9)) == branco:
        check_numero += 1
    if im.getpixel((x+9,y-9)) == cinza_escuro:
        check_numero += 1
    if im.getpixel((x-9,y+9)) == cinza_escuro:
        check_numero += 1
    if im.getpixel((x-9,y-9)) == cinza_escuro:
        check_numero += 1
    return check_numero
 
#Funcao que retorna numero de bandeiras em volta
def check_bandeira(x,y):
    global im
    numero = 0
    if im.getpixel((x+16,y)) == preto:
        numero += 1
    if im.getpixel((x-16,y)) == preto:
        numero += 1
    if im.getpixel((x,y+16)) == preto:
        numero += 1
    if im.getpixel((x,y-16)) == preto:
        numero += 1
    if im.getpixel((x+16,y+16)) == preto:
        numero += 1
    if im.getpixel((x+16,y-16)) == preto:
        numero += 1
    if im.getpixel((x-16,y+16)) == preto:
        numero += 1
    if im.getpixel((x-16,y-16)) == preto:
        numero += 1
    return numero
#Funcao principal
def main():
    global im, completos
    k = 0
    for i in range(30):
        k += 1
        for j in range(16):
            x_pixel = 549 + 16*(i)
            y_pixel = 174 + 16*(j)
            if im.getpixel((x_pixel,y_pixel)) == azul and k not in completos:
                if check_num_square_volta(x_pixel,y_pixel) == 1:
                    im = check_square_volta(x_pixel,y_pixel)
                if check_bandeira(x_pixel,y_pixel) == 1:
                    im = click_square_volta(x_pixel,y_pixel)
                if check_num_square_volta(x_pixel,y_pixel) - check_bandeira(x_pixel,y_pixel) == 0:
                    completos.append(k)
            elif im.getpixel((x_pixel,y_pixel)) == verde and k not in completos:
                if check_num_square_volta(x_pixel,y_pixel) == 2 :
                    im = check_square_volta(x_pixel,y_pixel)
                if check_bandeira(x_pixel,y_pixel) == 2:
                    im = click_square_volta(x_pixel,y_pixel)
                if check_num_square_volta(x_pixel,y_pixel) - check_bandeira(x_pixel,y_pixel) == 0:
                    completos.append(k)
            elif im.getpixel((x_pixel,y_pixel)) == vermelho and k not in completos:
                if check_num_square_volta(x_pixel,y_pixel) == 3:
                    im = check_square_volta(x_pixel,y_pixel)
                if check_bandeira(x_pixel,y_pixel) == 3:
                    im = click_square_volta(x_pixel,y_pixel)
                if check_num_square_volta(x_pixel,y_pixel) - check_bandeira(x_pixel,y_pixel) == 0:
                    completos.append(k)
            elif im.getpixel((x_pixel,y_pixel)) == azul_escuro and k not in completos:
                if check_num_square_volta(x_pixel,y_pixel) == 4:
                    im = check_square_volta(x_pixel,y_pixel)
                if check_bandeira(x_pixel,y_pixel) == 4:
                    im = click_square_volta(x_pixel,y_pixel)
                if check_num_square_volta(x_pixel,y_pixel) - check_bandeira(x_pixel,y_pixel) == 0:
                    completos.append(k)
            elif im.getpixel((x_pixel,y_pixel)) == violeta :
                if check_num_square_volta(x_pixel,y_pixel) == 5 and k not in completos:
                    im = check_square_volta(x_pixel,y_pixel)
                if check_bandeira(x_pixel,y_pixel) == 5:
                    im = click_square_volta(x_pixel,y_pixel)
                if check_num_square_volta(x_pixel,y_pixel) - check_bandeira(x_pixel,y_pixel) == 0:
                    completos.append(k)
            elif im.getpixel((x_pixel,y_pixel)) == violeta:
                if check_num_square_volta(x_pixel,y_pixel) == 6 and k not in completos:
                    im = check_square_volta(x_pixel,y_pixel)
                if check_bandeira(x_pixel,y_pixel) == 6:
                    im = click_square_volta(x_pixel,y_pixel)
                if check_num_square_volta(x_pixel,y_pixel) - check_bandeira(x_pixel,y_pixel) == 0:
                    completos.append(k)
            k +=1
 
 
 
 
if __name__ == '__main__':
    mousePos(708,322)
    leftClick()
    time.sleep(0.15)
    im = ImageGrab.grab()
    while True:
        main()