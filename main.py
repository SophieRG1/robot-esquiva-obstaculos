ultrasonico = 0

def on_forever():
    global ultrasonico
    ultrasonico = sonar.ping(DigitalPin.P1, DigitalPin.P2, PingUnit.CENTIMETERS)
    basic.pause(100)
    # Si detecta un obstaculo se movera a la derecha y seguira adelante
    if ultrasonico < 20:
        robotbit.motor_run_dual(robotbit.Motors.M1A, 255, robotbit.Motors.M2B, -255)
        basic.pause(250)
    else:
        robotbit.motor_run_dual(robotbit.Motors.M1A, 90, robotbit.Motors.M2B, 80)
basic.forever(on_forever)
