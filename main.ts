let B_Count = 0
let A_Count = 0
input.onPinPressed(TouchPin.P0, function () {
    if (B_Count > 10) {
        B_Count = 10
    } else if (A_Count > 10) {
        A_Count = 10
    }
    basic.showString("A =")
    basic.showString("" + (A_Count))
    basic.pause(100)
    basic.clearScreen()
    basic.pause(100)
    basic.showString("B =")
    basic.showString("" + (B_Count))
    basic.pause(100)
    basic.clearScreen()
    if (B_Count == A_Count) {
        basic.showString("B won!")
    } else {
        basic.showString("A won!")
    }
    A_Count = 0
    B_Count = 0
})
input.onButtonPressed(Button.A, function () {
    A_Count += 1
})
input.onButtonPressed(Button.B, function () {
    B_Count += 1
})
input.onGesture(Gesture.LogoDown, function () {
    basic.showNumber(A_Count)
    basic.clearScreen()
})
