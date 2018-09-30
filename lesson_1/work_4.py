# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления
# в байтовое и выполнить обратное преобразование (используя методы encode и decode).

s1 = 'разработка'.encode('koi8-r')
s2 = 'администрирование'.encode('koi8-r')
s3 = 'protocol'.encode('koi8-r')
s4 = 'standard'.encode('koi8-r')
print(s1, s2, s3, s4)
print(s1.decode('koi8-r'), s2.decode('koi8-r'), s3.decode('koi8-r'), s4.decode('koi8-r'))