# Калькулятор "силы" пароля

Скрипт запрашивает у пользователя пароль и выдаёт ему 
оценку от 1 до 10. 1 – очень слабый пароль, 10 – очень крутой.

Скрипт выполняет проверку по:
 * наличию строчных и прописных букв
 * наличию цифр
 * наличию специальных символов (@#!$...)
 * вхождению в blacklist.
 
Для проверки на совпадение с паролем из блэклиста 
пользователь может:
* указать его в командной строке после имени исполнеямого
файла с ключом -b;
* поместить его в папку со скриптом, предварительно переименовав
его в blacklist.txt.

Если пользователь не воспользовался ни одним из вышеприведенных 
методов и не определил расположение блэклиста, то проверка по 
вхождению не производится. В этом случае максимальная оценка
пароля не может превышать 6.  

# Использование и пример вывода.

Для использования необходим установленный Python 3.5.
```bush
$ python3 password_strength.py -b <path-to-blacklist-file>

Enter a password: 
Your password strength: 10

```

# Цели проекта

Данный код написан в образовательных целях. Обучающий курс для веб-разработчиков - [DEVMAN.org](https://devman.org)
