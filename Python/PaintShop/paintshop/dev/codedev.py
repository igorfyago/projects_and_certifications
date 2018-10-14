from collections import namedtuple

Color = namedtuple('Preferences', ['hue', 'saturation', 'luminosity'])

p = Color(170, 0.1, 0.6)

print(p.hue, p.saturation, p.luminosity, p)

