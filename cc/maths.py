WIDTH = 800
HEIGHT = 800
ORIGINAL = 900

def scale_x(w, original=ORIGINAL, target=WIDTH):
    return int(w / original * target)

def scale_y(h, original=ORIGINAL, target=HEIGHT):
    return int(h / original * target)
