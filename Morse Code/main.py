from machine import Pin
import utime


CODE_TO_MORSE = {'0': '-----', '1': '.----', '2': '..---', '3': '...--',
                '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                '8': '---..', '9': '----.'}

def code_to_morse(message):
    morse = []
    for num in message:
        if num in CODE_TO_MORSE:
            morse.append(CODE_TO_MORSE[num])
    return " ".join(morse)

def morse_to_led(morse):
    led = Pin(16, Pin.OUT)
    for sig in morse:
        if sig == ".":
            led.toggle()
            utime.sleep(0.3)
            led.toggle()
            utime.sleep(0.3)
        if sig == "-":
            led.toggle()
            utime.sleep(0.9)
            led.toggle()
            utime.sleep(0.3)
        if sig == " ":
            utime.sleep(0.3)
            
def main ():
    lock_code = "513"
    morse = code_to_morse(lock_code)
    print(morse)
    morse_to_led(morse)
    
if __name__ == "__main__":
    main()