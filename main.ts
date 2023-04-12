let ultrasonico = 0
basic.forever(function on_forever() {
    
    ultrasonico = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.Centimeters)
    basic.pause(100)
    //  Si detecta un obstaculo se movera a la derecha y seguira adelante
    if (ultrasonico < 20) {
        robotbit.MotorRunDual(robotbit.Motors.M1A, 255, robotbit.Motors.M2B, -255)
        basic.pause(250)
    } else {
        robotbit.MotorRunDual(robotbit.Motors.M1A, 90, robotbit.Motors.M2B, 80)
    }
    
})
