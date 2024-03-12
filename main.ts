let Maulwurf = 0
let Punkte = 0
basic.forever(function () {
    basic.turnRgbLedOff()
    basic.showLeds(`
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        . . # . .
        `)
    Maulwurf = randint(0, 1)
    if (Maulwurf == 0) {
        basic.showLeds(`
            . . # . .
            . . # . .
            # . # . .
            . . # . .
            . . # . .
            `)
        basic.pause(100)
        if (input.buttonIsPressed(Button.A)) {
            basic.showLeds(`
                . . . . .
                . . . . #
                . . . # .
                # . # . .
                . # . . .
                `)
            Punkte += 1
            basic.setLedColor(0xffff00)
        }
    } else {
        basic.showLeds(`
            . . # . .
            . . # . .
            . . # . #
            . . # . .
            . . # . .
            `)
        basic.pause(100)
        if (input.buttonIsPressed(Button.B)) {
            basic.showLeds(`
                . . . . .
                . # . # .
                . . # . .
                # . . . #
                . # # # .
                `)
            Punkte += 1
        }
    }
    basic.pause(500)
    basic.showString("" + Punkte)
})
