def colorize(s=0, c=0, bg=0):
    s = str(s).zfill(2)
    c = str(c).zfill(2)
    bg = str(bg).zfill(2)
    base = '\x1b[%s;%s;%sm' % (s, c, bg)
    return base

if __name__ == '__main__':
    for x in range(100, 108):
        for y in range(1, 5):
            for z in range(30, 38):
                print colorize(x, y, z) + ":: %s %s %s ::" % (x, y, z)
