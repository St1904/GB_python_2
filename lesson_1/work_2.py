# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность
# кодов (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

s1 = b'class'
s2 = b'function'
s3 = b'method'

print(type(s1), s1, len(s1))
print(type(s2), s2, len(s2))
print(type(s3), s3, len(s3))