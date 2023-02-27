import pyautogui as pag
import time
from movement import *

# ─── Main ─────────────────────────────────────────────────────────────────────

click_secondary_btn()

time.sleep(8)

move_ticket_to_line()

time.sleep(1)
handle_top_button("topping")

time.sleep(1)
move_ticket_to_main()

time.sleep(2)
click_secondary_btn()


time.sleep(1)
print("Moving toppings")
pag.moveTo(*TOPPING_1)
pag.drag(159, -194)


pag.moveTo(*TOPPING_1)
pag.drag(116, -108)

pag.moveTo(*TOPPING_1)
pag.drag(159, -35)

pag.moveTo(*TOPPING_1)
pag.drag(195, 42)

time.sleep(1)

click_secondary_btn()


time.sleep(6)

move_ticket_to_line()


time.sleep(1)
move_ticket_to_main()

time.sleep(15.5)
handle_pizza_baking_1()

time.sleep(2)

handle_pizza_horizontal_cut()

time.sleep(2)

handle_pizza_vertical_cut()

time.sleep(2)

click_secondary_btn()

