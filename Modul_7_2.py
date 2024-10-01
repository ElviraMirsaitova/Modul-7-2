def custom_write(file_name, strings):
    dict1 = {}
    file = open(file_name, 'w', encoding='utf-8')

    for nomer, stroka in enumerate(strings, start=1):
        x = file.tell()
        file.write(stroka + '\n')
        dict1[(nomer, x)] = stroka
    file.close()
    return dict1


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('text.txt', info)
for i in result.items():
    print(i)