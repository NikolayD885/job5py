# Напишите программу, удаляющую из текста все слова, содержащие ""абв""

listA = list(map(str, input('Введите текст: ').split()))

def deleteWord(x):
  if "а" not in x and "б" not in x and "в" not in x:
    return True
  else:
    return False

res = ' '.join(list(filter(deleteWord, listA)))
print(res)