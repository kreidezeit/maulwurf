Maulwurf = 0
Punkte = 0

def on_forever():
    global Maulwurf, Punkte
    basic.turn_rgb_led_off()
    basic.show_leds("""
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        """)
    Maulwurf = randint(0, 1)
    if Maulwurf == 0:
        basic.show_leds("""
            . . # . .
            . . # . .
            # . # . .
            . . # . .
            . . # . .
            """)
        basic.pause(100)
        if input.button_is_pressed(Button.A):
            basic.show_leds("""
                . . . . .
                . . . . #
                . . . # .
                # . # . .
                . # . . .
                """)
            Punkte += 1
            basic.set_led_color(0xffff00)
    else:
        basic.show_leds("""
            . . # . .
            . . # . .
            . . # . #
            . . # . .
            . . # . .
            """)
        basic.pause(100)
        if input.button_is_pressed(Button.B):
            basic.show_leds("""
                . . . . .
                . # . # .
                . . # . .
                # . . . #
                . # # # .
                """)
            Punkte += 1
    basic.pause(500)
    basic.show_string("" + str((Punkte)))
basic.forever(on_forever)
