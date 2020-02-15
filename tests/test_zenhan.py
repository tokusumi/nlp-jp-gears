from nlp_jp_gears import ZenToHanConverter, HanToZenConverter
from nlp_jp_gears.zenhan import AbstractZenHanConverter


def test_abstract():
    converter = AbstractZenHanConverter()
    try:
        converter("")
        assert False
    except NotImplementedError:
        pass


def test_ZenToHanConverter():
    zen_s = "！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～"
    zen_n = "０１２３４５６７８９"
    zen_a = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    tot_zen = zen_s + zen_n + zen_a
    han_s = '!"#$%&' + r"'()*+,-./:;<=>?@[\]^_`{|}~"
    han_n = "0123456789"
    han_a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    tot_han = han_s + han_n + han_a

    default_converter = ZenToHanConverter()
    assert default_converter(tot_zen) == tot_han
    assert default_converter.converts == tot_zen, f"{default_converter.converts}"

    tar_converter = ZenToHanConverter(targets="０")
    assert tar_converter(tot_zen) == zen_s + "0" + zen_n[1:] + zen_a
    assert tar_converter.converts == zen_n[0], f"{tar_converter.converts}"

    exc_converter = ZenToHanConverter(excludes="！")
    assert exc_converter(tot_zen) == "！" + han_s[1:] + han_n + han_a
    assert exc_converter.converts == zen_s[1:] + zen_n + zen_a

    s_converter = ZenToHanConverter(symbol=False)
    assert s_converter(tot_zen) == zen_s + han_n + han_a
    assert s_converter.converts == zen_n + zen_a

    n_converter = ZenToHanConverter(number=False)
    assert n_converter(tot_zen) == han_s + zen_n + han_a
    assert n_converter.converts == zen_s + zen_a

    a_converter = ZenToHanConverter(alphabet=False)
    assert a_converter(tot_zen) == han_s + han_n + zen_a
    assert a_converter.converts == zen_s + zen_n


def test_HanToZenConverter():
    zen_s = "！＂＃＄％＆＇（）＊＋，－．／：；＜＝＞？＠［＼］＾＿｀｛｜｝～"
    zen_n = "０１２３４５６７８９"
    zen_a = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
    tot_zen = zen_s + zen_n + zen_a
    han_s = '!"#$%&' + r"'()*+,-./:;<=>?@[\]^_`{|}~"
    han_n = "0123456789"
    han_a = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    tot_han = han_s + han_n + han_a

    default_converter = HanToZenConverter()
    assert default_converter(tot_han) == tot_zen
    assert default_converter.converts == tot_han, f"{default_converter.converts}"

    tar_converter = HanToZenConverter(targets="0")
    assert tar_converter(tot_han) == han_s + "０" + han_n[1:] + han_a
    assert tar_converter.converts == han_n[0], f"{tar_converter.converts}"

    exc_converter = HanToZenConverter(excludes="!")
    assert exc_converter(tot_han) == "!" + zen_s[1:] + zen_n + zen_a
    assert exc_converter.converts == han_s[1:] + han_n + han_a

    s_converter = HanToZenConverter(symbol=False)
    assert s_converter(tot_han) == han_s + zen_n + zen_a
    assert s_converter.converts == han_n + han_a

    n_converter = HanToZenConverter(number=False)
    assert n_converter(tot_han) == zen_s + han_n + zen_a
    assert n_converter.converts == han_s + han_a

    a_converter = HanToZenConverter(alphabet=False)
    assert a_converter(tot_han) == zen_s + zen_n + han_a
    assert a_converter.converts == han_s + han_n
