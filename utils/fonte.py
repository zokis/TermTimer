#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Desenvolvido por: Marcelo Fonseca Tambalo - https://gist.github.com/3493575
import os


class FonteASCIIArt(object):
    codes = {'': '', 'yellow': '\x1b[33;01m', 'blink': '\x1b[05m', 'lightgray': '\x1b[37m', 'bg_gray': '\x1b[01;40m',
        'underline': '\x1b[04m', 'darkyellow': '\x1b[33m', 'blue': '\x1b[34;01m', 'darkblue': '\x1b[34m', 'faint': '\x1b[02m',
        'fuchsia': '\x1b[35;01m', 'black': '\x1b[30m', 'white': '\x1b[01m', 'red': '\x1b[31;01m',
        'brown': '\x1b[33m', 'turquoise': '\x1b[36;01m', 'bold': '\x1b[01m', 'darkred': '\x1b[31m', 'darkgreen': '\x1b[32m',
        'reset': '\x1b[39;49;00m', 'standout': '\x1b[03m', 'darkteal': '\x1b[36;01m', 'darkgray': '\x1b[30;01m',
        'overline': '\x1b[06m', 'purple': '\x1b[35m', 'green': '\x1b[32;01m', 'teal': '\x1b[36m', 'fuscia': '\x1b[35;01m'}

    lines = 0
    character_list = tuple()
    character_map = {}

    def reset(self):
        print "%s" % self.codes['reset']

    def colorize(self, color_key, text):
        return self.codes[color_key] + text + self.codes["reset"]

    def add_color(self, name, value):
        if name not in self.__dict__:
            self.__dict__[name] = value
        else:
            raise ""

    def update_color(self, name, value):
        if name in self.__dict__:
            self.__dict__[name] = value
        else:
            raise ""

    def cls(self):
        os.system(['clear', 'cls'][os.name == 'nt'])

    def text_renderer(self, text):
        rendered_text = ''
        for line in range(self.lines):
            for letter in text:
                if letter in self.character_list:
                    rendered_text += self.character_map[letter][line]
                elif line == self.lines - 1:
                    rendered_text += letter
            rendered_text += '\n'
        return rendered_text


class FonteZokis(FonteASCIIArt):
    lines = 6
    character_list = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ':', ' ', '.')
    um = ('  __  ', ' /_ | ', '  | | ', '  | | ', '  | | ', '  |_| ')
    dois = ('  ___   ', ' |__ \  ', '    ) | ', '   / /  ', '  / /_  ', ' |____| ')
    tres = ('  ____   ', ' |___ \  ', '   __) | ', '  |__ <  ', '  ___) | ', ' |____/  ')
    quatro = ('  _  _   ', ' | || |  ', ' | || |_ ', ' |__   _|', '    | |  ', '    |_|  ')
    cinco = ('  _____  ', ' | ____| ', ' | |__   ', ' |___ \  ', '  ___) | ', ' |____/  ')
    seis = ('    __   ', '   / /   ', '  / /_   ', ' | \'_ \  ', ' | (_) | ', '  \___/  ')
    sete = ('  ______ ', ' |____  |', '     / / ', '    / /  ', '   / /   ', '  /_/    ')
    oito = ('   ___   ',  '  / _ \  ', ' | (_) | ', '  > _ <  ', ' | (_) | ', '  \___/  ')
    nove = ('   ___   ', '  / _ \  ', ' | (_) | ', '  \__, | ', '    / /  ', '   /_/   ')
    zero = ('   ___   ', '  / _ \  ', ' | | | | ', ' | | | | ', ' | |_| | ', '  \___/  ')
    espaco = ('  ', '  ', '  ', '  ', '  ', '__')
    ponto = ('   ', '   ', '   ', '   ', '   ', ' 0 ')
    dois_pontos = ('     ', '  0  ', '  0  ', '     ', '  0  ', '  0  ')

    character_map = {'1': um, '2': dois, '3': tres, '4': quatro, '5': cinco, '6': seis,
        '7': sete, '8': oito, '9': nove, '0': zero, ':': dois_pontos, ' ': espaco, '.': ponto}

def main():
    f = FonteASCIIArt()
    for color in f.codes.keys():
        print f.colorize(color, color)

if __name__ == '__main__':
    main()
