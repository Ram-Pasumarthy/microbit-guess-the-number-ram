B_Count = 0
A_Count = 0

def on_pin_pressed_p0():
    global B_Count, A_Count
    if B_Count > 10:
        B_Count = 10
    elif A_Count > 10:
        A_Count = 10
    basic.show_string("A =")
    basic.show_string("" + str((A_Count)))
    basic.pause(100)
    basic.clear_screen()
    basic.pause(100)
    basic.show_string("B =")
    basic.show_string("" + str((B_Count)))
    basic.pause(100)
    basic.clear_screen()
    if B_Count == A_Count:
        basic.show_string("You won!")
    else:
        basic.show_string("You lost!")
    A_Count = 0
    B_Count = 0
input.on_pin_pressed(TouchPin.P0, on_pin_pressed_p0)

def on_button_pressed_a():
    global A_Count
    A_Count += 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global B_Count
    B_Count += 1
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    pass
basic.forever(on_forever)
