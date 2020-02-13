from typing import Optional, List


def zen_to_han(targets: Optional[List[str]] = None,
               excludes: Optional[List[str]] = None,
               symbol: bool = True,
               number: bool = True,
               alphabet: bool = True
               ):
    """
    convert Japanese "zenkaku" text into "hankaku" text
    Supports:
        ！＂＃＄％＆＇（）＊＋，－．／
        ：；＜＝＞？＠［＼］＾＿｀｛｜｝～
        ０１２３４５６７８９
        ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ
        ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ
    args:
        targets: declaire target characters. if None (default), all support characters is converted.
        excludes: declaire characters to keep format.
        symbol: if True (default), symbol is converted.
        number: if True (default), number is converted.
        alphabet: if True (default), alphabet is converted.
    """
    targets = tuple(targets) if targets else {}
    excludes = tuple(excludes) if excludes else {}
    dic = {chr(0xFF01 + i): chr(0x21 + i) for i in _range(symbol, number, alphabet)}
    if targets:
        dic = {key: val for key, val in dic.items() if key in targets}
    if excludes:
        dic = {key: val for key, val in dic.items() if key not in excludes}

    def _zen_to_han(text):
        return text.translate(str.maketrans(dic))
    return _zen_to_han


def han_to_zen(targets: Optional[List[str]] = None,
               excludes: Optional[List[str]] = None,
               symbol: bool = True,
               number: bool = True,
               alphabet: bool = True):
    """
    convert Japanese "hankaku" symbols into "zenkaku" symbols
    Supports:
        !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        0123456789
        ABCDEFGHIJKLMNOPQRSTUVWXYZ
        abcdefghijklmnopqrstuvwxyz
    args:
        targets: declaire target characters. if None (default), all support characters is converted.
        excludes: declaire characters to keep format.
        symbol: if True (default), symbol is converted.
        number: if True (default), number is converted.
        alphabet: if True (default), alphabet is converted.
    """
    targets = tuple(targets) if targets else {}
    excludes = tuple(excludes) if excludes else {}
    dic = {chr(0x21 + i): chr(0xFF01 + i) for i in _range(symbol, number, alphabet)}
    if targets:
        dic = {key: val for key, val in dic.items() if key in targets}
    if excludes:
        dic = {key: val for key, val in dic.items() if key not in excludes}

    def _han_to_zen(text):
        return text.translate(str.maketrans(dic))
    return _han_to_zen


def _range(symbol: bool, number: bool, alphabet: bool):
    if symbol:
        for i in range(15):
            yield i
        for i in range(25, 32):
            yield i
        for i in range(58, 64):
            yield i
        for i in range(90, 94):
            yield i
    if number:
        for i in range(15, 25):
            yield i
    if alphabet:
        for i in range(32, 58):
            yield i
        for i in range(64, 90):
            yield i
