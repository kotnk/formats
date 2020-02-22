import json
import xml.etree.ElementTree as ET


def extension_check(file):
    if file[-4:] == 'json':
        return 'json'
    elif file[-3:] == 'xml':
        return 'xml'
    else:
        return 'unknown'


def reader(file, extension):
    words = []
    if extension == 'xml':
        print(f'> Получили {file}, работаем с библиотекой xml')
        root = ET.parse(file).getroot()
        news = root.findall(r'channel/item')
        for item in news:
            line = item.find('description').text.split()
            for word in line:
                word = word.lower()
                words.append(word)
        counter(words)
    elif extension == 'json':
        print(f'> Получили {file}, работаем с библиотекой json.')
        with open(file, encoding='utf8') as text:
            data = json.load(text)
        for items in data['rss']['channel']['items']:
            line = items['description'].split()
            for word in line:
                word = word.lower()
                words.append(word)
        counter(words)


def counter(words):
    print('Попали в счетчик, пересчет слов может занять некоторое время...\n')
    glob_counter = {}
    for item in words:
        if len(item) >= 6:
            count = words.count(item)
            temp_dict = {item: count}
            glob_counter.update(temp_dict)
    candidates = sorted(glob_counter.items(), key=lambda x: x[1], reverse=True)
    for x in range(10):
        print(f'{x + 1} место: слово "{candidates[x][0]}" встречается {candidates[x][1]} раз(а)')


def main():
    user_choice = input('Введите название файла, который надо открыть: ')
    extension = extension_check(user_choice)
    if extension == 'unknown':
        print('С такими файлами программа работать не может.')
    else:
        print(f'Тип файла: {extension}')
        reader(user_choice, extension)


main()
