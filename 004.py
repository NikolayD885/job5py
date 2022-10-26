# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример: aaaaaaabbbbbbccccccccc => 7a6b9c и 11a3b7c => aaaaaaaaaaabbbccccccc

with open('encoding.txt', 'r') as data:
    string = data.readline()

def encode(s):
    encoding = ''
    i = 0
    while i < len(s):
        count = 1

        while i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
            i = i + 1
        encoding += str(count) + s[i]
        i = i + 1
    return encoding


def decode(s):
    decoding = ''
    zip = ''
    for i in s:
        if i.isdigit():
            zip += i
        else:
            decoding += int(zip) * i
            zip = ''
    return decoding


print(f'Входные данные:          {string}')
print(f'Сжатые данные:           {encode(string)}')
print(f'Восстановленные данные:  {decode(encode(string))}')

with open(r'decoding.txt', 'w') as data:
    data.write(decode(encode(string)))
    data.close