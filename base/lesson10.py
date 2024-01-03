# Регудярное выражение 

import re 

s = 'AC/AC/AC/DC/DC/AC/DC/AC/DC/CA/CA'
result = re.match('DC',s) # ишет в начале строки 
result = re.search('DC',s) # ишет и возврашает первый
result = re.findall('DC',s) # шет все и возврашает список 
result = re.split('/',s,maxsplit=3)  # разбивает и возврашает список maxsplit=3 ограничение на разюиение 
result = re.sub('A','D',s)  # Заменит символы
result = re.fullmatch('A',s) # Является ли шаблон полным совпадением 
result = re. 
print(result)