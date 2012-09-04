#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Timer in Terminal
# Desenvolvido por: Marcelo Fonseca Tambalo - https://github.com/zokis/TermTimer

import time as timer
import os
import sys
import optparse
import platform

EXIT = 0
ERROR = 2
SUCSSES = 1

from fonte import FonteZokis


class TermTimer(object):
    def __init__(self, time=None, notnow=True, c='m'):
        self.font = FonteZokis()
        self.timing = 5
        self.cls = self.font.cls
        if time:
            self.timing = time
            if c == 'm':
                self.timing = int(self.timing * 60)

            if notnow:
                raw_input("Press Enter")
        else:
            self.in_set_time()

    def in_set_time(self):
        try:
            print "%sEnter time to time" % self.font.n_green
            print "0 to %sexit" % self.font.n_blue
            print "%snothing to %s5 %sminutes" % (self.font.n_green, self.font.n_blue, self.font.n_green)
            timing = raw_input("%s>> %s" % (self.font.n_red, self.font.n_green))
        except:
            sys.exit(ERROR)
        if timing == '0':
            sys.exit(EXIT)
        try:
            if timing:
                timing = float(timing)
            else:
                timing = 5
        except:
            sys.exit(ERROR)
        if timing < 0:
            timing *= -1
        self.timing = int(timing * 60)

    def end(self):
        str_fim = ' Time Out! ' * 5
        self.cls()
        if platform.system() == 'Linux':
            os.system("notify-send '%s'" % str_fim)
        else:
            print "%s" % str_fim
        timer.sleep(0.5)
        self.cls()
        self.restart()

    def restart(self):
        self.cls()
        print "%s" % self.font.n_green
        self.cls()
        op = raw_input("%sTiming again? %s(y/n)%s: " % (self.font.n_green,
            self.font.n_blue, self.font.n_green))
        if op in ("y", "Y"):
            self.clocking()
        elif op in ("n", "N"):
            print "%s" % self.font.default
            self.cls()
            sys.exit(EXIT)
        else:
            self.restart()

    def clocking(self):
        print "%s" % self.font.n_green__gray
        for i in range(self.timing, -1, -1):
            self.cls()
            print self.font.text_renderer("%0.2d" % (i / 60) + ":" + "%0.2d" % (i % 60))
            timer.sleep(1.0)
        self.end()


def main(argv):
    opar = optparse.OptionParser()
    opar.add_option("-s", "--sec", dest="sec", help="time in seconds", type="int", default=None)
    opar.add_option("-m", "--min", dest="min", help="time in minutes", type="float", default=None)
    opar.add_option("-n", "--notnow", dest="notnow", help="the timer does not start now", default=False, action="store_true")

    options, args = opar.parse_args(argv)

    if options.sec:
        tc = TermTimer(options.sec, options.notnow, 's')
    elif options.min:
        tc = TermTimer(options.min, options.notnow, 'm')
    else:
        tc = TermTimer()
    tc.clocking()
    sys.exit(SUCSSES)

if __name__ == '__main__':
    main(sys.argv[1:])
