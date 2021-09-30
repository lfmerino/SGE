from pynput import keyboard
# The event listener will be running in this block
def pulsaESC():
    with keyboard.Events() as events:
        for event in events:
            if event.key == keyboard.Key.esc:
                return True
                
            else:
                return False              
i=0
while True:
   print(i)
   i=i+1
   if pulsaESC():
       break
   else:
       print("Hola")