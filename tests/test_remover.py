from nlp_jp_gears import TextBtwBracketsRemover
from nlp_jp_gears.remover import AbstractRemover


def test_abstract():
    remover = AbstractRemover()
    try:
        remover("")
        assert False
    except NotImplementedError:
        pass


def test_remove_txt_btw_brackets():
    text = r"<あ>{い}P[う](え)y「お」『か』t（き）h［く］〈け〉o《こ》〔さ〕｛し｝«す»n‹せ›"
    remover = TextBtwBracketsRemover()
    assert remover.removes == "<{[(「『（［〈《〔｛«‹"
    _text = remover(text)
    assert _text == "Python"


def test_remove_txt_btw_brackets_targets():

    text = r"<あ>{い}P[う](え)y「お」『か』t（き）h［く］〈け〉o《こ》〔さ〕｛し｝«す»n‹せ›"
    remover = TextBtwBracketsRemover(targets=["(", "（", "「"])
    assert remover.removes == "(「（"
    _text = remover(text)
    assert _text == r"<あ>{い}P[う]y『か』th［く］〈け〉o《こ》〔さ〕｛し｝«す»n‹せ›"


def test_remove_txt_btw_brackets_excludes():

    text = r"<あ>{い}P[う](え)y「お」『か』t（き）h［く］〈け〉o《こ》〔さ〕｛し｝«す»n‹せ›"
    remover = TextBtwBracketsRemover(excludes=["<", "‹"])
    assert remover.removes == "{[(「『（［〈《〔｛«"
    _text = remover(text)
    assert _text == "<あ>Python‹せ›"
