# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.

import subprocess

args = (['ping', 'yandex.ru'], ['ping', 'youtube.com'])
for arg in args:
    subproc = subprocess.Popen(arg, stdout=subprocess.PIPE)

    for line in subproc.stdout:
        print(line.decode('cp866'))