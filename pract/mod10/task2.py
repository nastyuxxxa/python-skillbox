import re


def is_valid_date(date):
    """
    Проверяет, может ли являться входная строка (целиком) датой в одном из нескольких форматов:
    •	день.месяц.год (14.09.2022, 5.02.1995, 01.4.2012)
    •	день/месяц/год (14/09/2022, 5/02/1995, 01/4/2012)
    •	день-месяц-год (14-09-2022, 5-02-1995, 01-4-2012)
    •	год.месяц.день (2022.09.14, 1995.02.5, 2012.4.01)
    •	год/месяц/день (2022/09/14, 1995/02/5, 2012/4/01)
    •	год-месяц-день (2022-09-14, 1995-02-5, 2012-4-01)
    •	день месяц_rus год (14 сентября 2022, 5 февраля 1995, 01 апреля 2012)
    •	Месяц_eng день, год (September 14, 2022, February 5, 1995, April 01, 2012)
    •	Мес_eng день, год (Sep 14, 2022, Feb 5, 1995, Apr 01, 2012)
    •	год, Месяц_eng день (2022, September 14, 1995, February 5, 2012, April 01)
    •	год, Мес_eng день (2022, Sep 14, 1995, Feb 5, 2012, Apr 01)

    Examples:
    >>> is_valid_date('20 января 1806')
    True
    >>> is_valid_date('1924, July 25')
    True
    >>> is_valid_date('26/09/1635')
    True
    >>> is_valid_date('3.1.1506')
    True
    >>> is_valid_date('25.08-1002')
    False
    >>> is_valid_date('декабря 19, 1838')
    False
    >>> is_valid_date('8.20.1973')
    False
    >>> is_valid_date('Jun 7, -1563')
    False
    """

    #Не разабралась, как проверить, что следующих дат не существует:
    #>>> is_valid_date('31 февраля 2023')
    #False
    #>>> is_valid_date('31 июня 2015')
    #False

    date_formats = {
        "dd.mm.yyyy": r"\b(0?[1-9]|[12][0-9]|3[01])\.(0?[1-9]|1[012])\.(0|[1-9][0-9]{3,})\b",
        "dd/mm/yyyy": r"\b(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/(0|[1-9][0-9]{3,})\b",
        "dd-mm-yyyy": r"\b(0?[1-9]|[12][0-9]|3[01])-(0?[1-9]|1[012])-(0|[1-9][0-9]{3,})\b",
        "yyyy.mm.dd": r"\b(0|[1-9][0-9]{3,})\.(0?[1-9]|1[012])\.(0?[1-9]|[12][0-9]|3[01])\b",
        "yyyy/mm/dd": r"\b(0|[1-9][0-9]{3,})/(0?[1-9]|1[012])/(0?[1-9]|[12][0-9]|3[01])\b",
        "yyyy-mm-dd": r"\b(0|[1-9][0-9]{3,})-(0?[1-9]|1[012])-(0?[1-9]|[12][0-9]|3[01])\b",
        "dd month_rus yyyy": r"\b(0?[1-9]|[12][0-9]|3[01]) (января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря) (0|[1-9][0-9]{3,})\b",
        "month_eng dd, yyyy": r"\b(January|February|March|April|May|June|July|August|September|October|November|December) (0?[1-9]|[12][0-9]|3[01]), (0|[1-9][0-9]{3,})\b",
        "mon_eng dd, yyyy": r"\b(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (0?[1-9]|[12][0-9]|3[01]), (0|[1-9][0-9]{3,})\b",
        "yyyy, month_eng dd": r"\b(0|[1-9][0-9]{3,}), (January|February|March|April|May|June|July|August|September|October|November|December) (0?[1-9]|[12][0-9]|3[01])\b",
        "yyyy, mon_eng dd": r"\b(0|[1-9][0-9]{3,}), (Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec) (0?[1-9]|[12][0-9]|3[01])\b"
    }

    for date_format, regex in date_formats.items():
        if re.match(regex, date):
            return True
    return False


if __name__ == "main":
    import doctest
    doctest.testmod(verbose=True)
