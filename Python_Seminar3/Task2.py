# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

import re
from collections import Counter

def top_10_words(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return Counter(words).most_common(10)

text = """«Скита́лец» (англ. The World's Desire, — «Мечта мира»[Прим. 1]) — приключенческий роман с элементами 
мистики (может также характеризоваться как фэнтези) в трёх книгах, 27 главах. Написан в 1888—1889 годах 
совместно романистом Генри Райдером Хаггардом и поэтом и учёным-филологом Эндрю Лэнгом; первое произведение 
Хаггарда, написанное в соавторстве, Лэнг разработал общую фабулу, и написал первые четыре главы и финал. Роман 
изначально планировалось назвать «Скиталец», но это название было занято стихотворением лорда Булвера; рабочим 
названием Хаггарда была «Песнь о луке».
Сюжет — вольная фантазия на тему приключений Одиссея, которого окружающие и он сам в основном называют «Скитальцем». 
Потеряв из-за чумной эпидемии Пенелопу и Телемаха, владыка Итаки отправился в Египет, где встретил Елену Троянскую и 
стал объектом вожделения царицы Мериамун, жены фараона Мернептаха. Романтический сюжет посвящён поискам идеальной 
любви, правящей миром, которая и есть истина. В романном повествовании светловолосая и голубоглазая Елена 
символизирует небесную, первую чистую любовь, а сумрачная черноволосая и черноглазая Мериамун — земную, плотскую.

Роман публиковался с продолжением в 1890 году в журнале The New Rewiew (апрель — декабрь), отдельное издание 
последовало в том же 1890 году в издательстве «Longman» десятитысячным тиражом. После 1894 года роман неизменно 
публиковался с иллюстрациями Мориса Грейффенхагена[en]. По данным Internet Speculative Fiction Database, 
роман регулярно переиздавался на протяжении всего XX века, был переведён на нидерландский (1930), немецкий (1985), 
итальянский (1998) и испанский (2009) языки. На русском языке впервые опубликован в 1903 году под названием «Мечта 
мира», переиздания и новые переводы последовали после 1990 года, чаще всего под названием «Скиталец». Несмотря на 
то, что роман был негативно оценён критиками, он пользовался популярностью у читателей, в том числе профессиональных египтологов."""

print(top_10_words(text))