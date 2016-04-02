# ДЗ по курсу Инфопоиск (Техносфера)

## Дано: дамп lenta.ru (10k документов)

Документы доступны по адресу: https://cloud.mail.ru/public/FnMq/qCNif6bFG/dataset

Для чтения документов используем docreader.py

Используем поля .url и .text


## Необходимо:
- Создать индекс
- Реализовать булев поиск

### А конкретно

#### На оценку 8:
- имплементировать кодирование varbyte
- создать словарь термов
- разобрать текстовый запрос простого формата (см. далее)
- Вывести подходящие под булев запрос URL-ы

#### На оценку 12:
Дополнительно к предыдущему:
- имплементировать метод Simple9

#### На оценку 15:
Дополнительно к предыдущему:
- реализовать текстовый запрос полного формата (см. далее)

#### На оценку 20:
Дополнительно к предыдущему:
- потоковая обработка дерева запроса
- обязательно: индекс в бинарном виде
- обязательно: словарь в бинарном виде (см. 2ю лекцию)

### Состав пакета

Ваш пакет должен быть разделен на 3 .sh-файла:

- index.sh (varbyte|simple9) path/to/\*.gz
- make\_dict.sh
- search.sh


Вывод подразумевается только от утилиты поиска.
Вывод должен происходить на stdout

### Формат ввода

На stdin searcher.sh будет дана последовательность запросов в виде

запрос #1  
запрос #2  
...

Форматы запросов:

#### простой
присутствуют только термы и конъюнкция ("&")
Пример: власти & бельгии

#### полный
Формат каждого запроса - булево выражение содержашее слова и операторы: "(", ")", "&", "|", "!"
Пример: власти & (бельгии | парижа) & сообщили

*Гарантируется что запрос валидный*


### Формат вывода:
ИСХОДНЫЙ ЗАПРОС  
КОЛ-ВО результатов  
URL1  
URL2  
...

Пример:
Путин & Медведев
2
https://lenta.ru/news/2015/08/30/putin/  
https://lenta.ru/photo/2015/08/30/medput/


## Куда отправлять код

Код запакованный в .tgz отправляйте на ts2016idx@mail.ru

В теме письма обязательно указывайте вариант (баллы).
Формат: [Ir-ts] [idx] ДЗ-3, Иван Иванов (var: 20)

## Как будет происходить проверка

Для проверки будет использоваться набор документов lenta.ru в 10 и 50 раз больше данного.
Ограничение по RAM: 2Gb

Из-за необходимости проверки реализации, оценка НЕ БУДЕТ автоматической.
