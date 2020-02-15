from nlp_jp_gears import zen_to_han, han_to_zen


def test_zen_to_han():
    zen_symbol = "！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～"
    zen_number = "０１２３４５６７８９"
    zen_alphabet = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    tot_zen = zen_symbol + zen_number + zen_alphabet
    han_symbol = '!"#$%&' + r"'()*+,-./:;<=>?@[\]^_`{|}~"
    han_number = "0123456789"
    han_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    tot_han = han_symbol + han_number + han_alphabet

    assert zen_to_han()(tot_zen) == tot_han
    assert (
        zen_to_han(targets="０")(tot_zen)
        == zen_symbol + "0" + zen_number[1:] + zen_alphabet
    )
    assert (
        zen_to_han(excludes="！")(tot_zen)
        == '！"#$%&' + r"'()*+,-./:;<=>?@[\]^_`{|}~" + han_number + han_alphabet
    )
    assert zen_to_han(number=False)(tot_zen) == han_symbol + zen_number + han_alphabet
    assert zen_to_han(alphabet=False)(tot_zen) == han_symbol + han_number + zen_alphabet


def test_han_to_zen():
    zen_symbol = "！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～"
    zen_number = "０１２３４５６７８９"
    zen_alphabet = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    tot_zen = zen_symbol + zen_number + zen_alphabet
    han_symbol = '!"#$%&' + r"'()*+,-./:;<=>?@[\]^_`{|}~"
    han_number = "0123456789"
    han_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    tot_han = han_symbol + han_number + han_alphabet

    assert han_to_zen()(tot_han)
    assert (
        han_to_zen(targets="0")(tot_han)
        == han_symbol + "０" + han_number[1:] + han_alphabet
    )
    assert han_to_zen(excludes="!")(tot_han)
    assert han_to_zen(number=False)(tot_han)
    assert han_to_zen(alphabet=False)(tot_han)

    assert han_to_zen()(tot_han) == tot_zen
    assert (
        han_to_zen(excludes="!")(tot_han)
        == "!＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～" + zen_number + zen_alphabet
    )
    assert han_to_zen(number=False)(tot_han) == zen_symbol + han_number + zen_alphabet
    assert han_to_zen(alphabet=False)(tot_han) == zen_symbol + zen_number + han_alphabet
