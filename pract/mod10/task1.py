import re


def is_valid_password(password):
    """
    Проверяет, является ли переданный пароль корректным.
    Ограничения на пароли:
        - пароль должен содержать только латинские символы, цифры и специальные символы ^$%@#&*
        - пароль должен состоять из не менее чем восьми символов
        - пароль должен содержать по крайней мере два латинских символа в нижнем регистре
        - пароль должен содержать по крайней мере одну цифру
        - пароль должен содержать по крайней мере три различных специальных символа
        - пароль не должен содержать символы ,.!?

    >>> is_valid_password("rtG&3FG#Tr^e")
    True
    >>> is_valid_password("a^A1@*@1Aa")
    True
    >>> is_valid_password("oF^a1D@y5%e6")
    True
    >>> is_valid_password("enroi#$*rkdeR#$*092uwedchf34tguv394h")
    True
    >>> is_valid_password("пароль")
    False
    >>> is_valid_password("password")
    False
    >>> is_valid_password("qwerty")
    False
    >>> is_valid_password("lOngPa$$W0Rd")
    False
    """
    regex = (
        r'^(?=.*[a-z].*[a-z])'
        r'(?=.*\d)'
        r'(?=.*[\^$%@#&*].*[\^$%@#&*].*[\^$%@#&*])'
        r'(?!.*[,.!?])'
        r'[A-Za-z0-9^$%@#&*]{8,}$'
    )

    return bool(re.match(regex, password))


if __name__ == "main":
    import doctest
    doctest.testmod(verbose=True)