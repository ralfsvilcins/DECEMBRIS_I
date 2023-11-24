import time

# dabut pašreizējo stundu
pašreizējā_stunda = time.time.now().hour

# atkariba no laika ievadit atbilstošu sveicienu
if 6 <= pašreizējā_stunda < 12:
    print("Labrīt!")
if 12 <= pašreizējā_stunda < 18:
    print("Labdien!")
else:
    print("Labvakar!")
