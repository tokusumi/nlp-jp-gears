from nlp_jp_gears import text_remover_btw_brackets


def test_remove_txt_btw_brackets():
    text = r"<あ>{い}P[う](え)y「お」『か』t（き）h［く］〈け〉o《こ》〔さ〕｛し｝«す»n‹せ›"
    remover = text_remover_btw_brackets()
    _text = remover(text)
    assert _text == "Python"


def test_remove_txt_btw_brackets_targets():

    text = r"<あ>{い}P[う](え)y「お」『か』t（き）h［く］〈け〉o《こ》〔さ〕｛し｝«す»n‹せ›"
    remover = text_remover_btw_brackets(targets=["(", "（", "「"])
    _text = remover(text)
    assert _text == r"<あ>{い}P[う]y『か』th［く］〈け〉o《こ》〔さ〕｛し｝«す»n‹せ›"


def test_remove_txt_btw_brackets_excludes():

    text = r"<あ>{い}P[う](え)y「お」『か』t（き）h［く］〈け〉o《こ》〔さ〕｛し｝«す»n‹せ›"
    remover = text_remover_btw_brackets(excludes=["<", "‹"])
    _text = remover(text)
    assert _text == "<あ>Python‹せ›"
