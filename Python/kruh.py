import matplotlib.pyplot as plt
import math

volba = input('Vyber si či chceš počítať O alebo S ')

if volba.lower() == 'o':
    r = float(input('Zadaj hodnotu polomeru'))
    x = [r * math.cos(i / 10 * math.pi * 2) for i in range(101)]
    y = [r * math.sin(i / 10 * math.pi * 2) for i in range(101)]
    plt.plot(x, y)
    plt.axis('equal')
    plt.show()
elif volba.lower() == 's':
    r = float(input('Zadaj hodnotu polomeru'))
    x = [r * math.cos(i / 10 * math.pi * 2) for i in range(101)]
    y = [r * math.sin(i / 10 * math.pi * 2) for i in range(101)]
    plt.plot(x, y)
    plt.axis('equal')
    plt.show()
else:
    print('Neplatná volba.')
    
