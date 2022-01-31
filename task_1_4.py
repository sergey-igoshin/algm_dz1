"""
Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""
import bcrypt


# O(n**2)
def hash_password(a):
    users_hash = {}     # O(1)
    for key, val in a.items():  # O(n)
        hash_salt = bcrypt.hashpw(val.encode('utf-8'), bcrypt.gensalt(8)) # O(1+n)
        users_hash[key] = {
            'hash': hash_salt,  # O(1)
            'action': 0     # O(1)
        }   # O(1)
    return users_hash   # O(1)
# T(n) = 1+n*(1+n+1+1)+1 = n**2+3n+2


# O(n)
def valid(login, password, hash):
    h = hash[login]['hash']     # O(1)
    action = hash[login]['action']  # O(1)
    if bcrypt.checkpw(password.encode('utf-8'), h):     # O(n)
        if action == 1:     # O(n)
            return 1    # O(1)
        else:   # O(1)
            return actions(login, password, hash)   # O(1)
    else:   # O(1)
        return 0    # O(1)
# T(n) = 1+1+n+n+1 = 2n+3


# O(n)
def actions(login, password, hash):
    action = input('Необходима активировация y/n: ')    # O(1)
    if action == 'y':   # O(n)
        hash[login]['action'] = 1   # O(1)
        return valid(login, password, hash)     # O(1)
    else:   # O(1)
        return 2    # O(1)
# T(n) = 1+n+1+1 = n+3

users = {
    'sergey@mail.ru': 'pass',   # O(1)
    'oleg@mail.ru': 'pass2'     # O(1)
}
hash = hash_password(users)     # O(1)

while True:
    login = input('Логин: ')    # O(1)
    password = input('Пароль: ')    # O(1)
    v = valid(login, password, hash)    # O(1)
    if v == 1:  # O(n)
        print('Доступ открыт')  # O(1)
        break   # O(1)
    elif v == 0:    # O(n)
        print('Пара логин пароль не правильные, проверьте раскладку')   # O(1)
    else:   # O(1)
        print('Вы вышли из системы')    # O(1)
        break   # O(1)
