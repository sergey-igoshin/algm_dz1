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
    for key, val in a.items():  # O(n+1)
        hash_salt = bcrypt.hashpw(val.encode('utf-8'), bcrypt.gensalt(8))   # O(n+1)
        users_hash[key] = {
            'hash': hash_salt,  # O(1)
            'action': 0     # O(1)
        }
    return users_hash   # O(1)
# T(n) = 1+n*(1+n+1+1)+1 = n**2+3n+2


# O(n)
def valid(login, password):
    if login in users.keys():  # O(n)
        h = users_hash[login]['hash']     # O(1)
        action = users_hash[login]['action']  # O(1)
        if bcrypt.checkpw(password.encode('utf-8'), h):     # O(n)
            if action == 1:     # O(1)
                return 1    # O(1)
            else:   # O(1)
                return actions(login, password)   # O(1)
        else:   # O(1)
            return 0    # O(1)
    else:   # O(1)
        return logout()     # O(1)
# T(n) = n+1+1+n+1+1 = 2n+4


# O(n)
def actions(login, password):
    action = input('Необходима активировация y/n: ')    # O(1)
    if action == 'y':   # O(1)
        users_hash[login]['action'] = 1   # O(1)
        return valid(login, password)     # O(1)
    else:   # O(1)
        return 3    # O(1)
# T(n) = 1+1+1+1 = 4

# O(1)
def logout():
    print('Аккаунт не зарегистрирован')    # O(1)
    action = input('Загеристрироваться? y/n: ')    # O(1)
    if action == 'y':    # O(1)
        i = input_in()    # O(1)
        users[i[0]] = i[1]    # O(1)
        hash_password({i[0]: i[1]})    # O(1)
        return 2    # O(1)
    else:    # O(1)
        return 3    # O(1)
# T(n) = 1+1+1+1+1+1+1 = 7

def input_in():
    login = input('Логин: ')  # O(1)
    password = input('Пароль: ')  # O(1)
    return login, password  # O(1)
# T(n) = 1+1+1 = 3

users = {
    'sergey@mail.ru': 'pass',   # O(1)
    'oleg@mail.ru': 'pass2'     # O(1)
}
users_hash = {}                 # O(1)
hash_password(users)     # O(1)

while True:
    i = input_in()  # O(1)
    v = valid(i[0], i[1])  # O(1)
    if v == 1:  # O(1)
        print('Доступ открыт')  # O(1)
        n = input('Продожить? y/n: ')   # O(1)
        if not 'y':   # O(1)
            break   # O(1)
    elif v == 0:    # O(1)
        print('Пара логин пароль не правильные, проверьте раскладку')   # O(1)
    elif v == 2:     # O(1)
        print('Регистрация прошла успешно, активируйте аккаунт')     # O(1)
        actions(i[0], i[1])     # O(1)
    else:   # O(1)
        print('Вы вышли из системы')    # O(1)
        break   # O(1)
