import pyautogui as pag
from coords import *

def click_secondary_btn():
    print("Secondary Button Clicked")
    pag.moveTo(*BTN_BELOW_TICKET)
    pag.click()

def move_ticket_to_line():
    print("Move to ticket")
    pag.moveTo(*TICKET) # ticket
    print("Drag ticket over to line")
    pag.drag(-700, -300)
    
def move_ticket_to_main():
    print("Drag ticket over")
    pag.moveTo(*TICKET_LINE_1)
    pag.drag(700, 300)

def handle_pizza_baking_1():
    print("Move to cutting")
    pag.moveTo(*PIZZA_BAKING_1)
    pag.click()

def handle_pizza_horizontal_cut():
    print("Horizonal Cut")
    pag.moveTo(*PIZZA_HORIZONAL_CUT)
    pag.drag(450, 0)

def handle_pizza_vertical_cut():
    print("Vertical Cut")
    pag.moveTo(*PIZZA_VERTICAL_CUT)
    pag.drag(0, 415)

def handle_top_button(btn_string):
    if btn_string == "topping":
        print("Move to toppings")
        pag.moveTo(*TOP_BTN_TOPPINGS) # topping
        pag.click()