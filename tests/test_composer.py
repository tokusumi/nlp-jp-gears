from nlp_jp_gears import Composer
from nlp_jp_gears import ZenToHanConverter, TextBtwBracketsRemover


def test_composer():
    text = "Ｐｙｔｈｏｎ（パイソン）で自然言語処理？"
    txt_btw_brackets_remover = TextBtwBracketsRemover()
    zenhan_converter = ZenToHanConverter()

    composer = Composer(txt_btw_brackets_remover, zenhan_converter)
    out = composer(text)
    assert out == "Pythonで自然言語処理?"
