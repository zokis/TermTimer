#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Desenvolvido por: Marcelo Fonseca Tambalo - https://gist.github.com/3493575
import os


class FonteASCIIArt(object):
    colors = {'n_red': '\033[01;31m',
        'red': '\033[31m', 'green': '\033[32m',
        'n_green': '\033[01;32m', 'blue': '\033[34m',
        'n_blue': '\033[01;34m',
        'default': '\033[00;00m',
        'n_green__gray': '\033[01;40m'}
    lines = 0
    character_list = tuple()
    character_map = {}

    def __init__(self):
        self.__dict__.update(self.colors)

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
