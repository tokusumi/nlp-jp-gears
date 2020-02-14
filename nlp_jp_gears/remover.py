import re
from typing import Optional, List


def text_remover_btw_brackets(
    targets: Optional[List[str]] = None, excludes: Optional[List[str]] = None,
):
    """
    remove brackets and the contents.
    support:
        <>{}\[\]()「」『』（）［］〈〉《》〔〕｛｝«»‹›
    args:
        targets: declaire target brackets. if None (default), all support brackets is removed.
        excludes: declaire brackets to keep.
    """
    _patdel = _get_delete_pattern(targets, excludes)
    _patdel = re.compile(_patdel)

    def remove(text: str) -> str:
        out = _patdel.sub("", text)
        return out

    return remove


def _get_delete_pattern(
    targets: Optional[List[str]] = None, excludes: Optional[List[str]] = None,
):
    """
    create regular expression to remove brackets and the contents.
    """
    pat_f = "<{[(「『（［〈《〔｛«‹"
    pat_b = ">}])」』）］〉》〕｝»›"
    if targets:
        pat = [
            f"(\\{f}.*?\\{g})"
            for f, g in zip(pat_f, pat_b)
            if f in targets or g in targets
        ]
    elif excludes:
        pat = [
            f"(\\{f}.*?\\{g})"
            for f, g in zip(pat_f, pat_b)
            if f not in excludes and g not in excludes
        ]
    else:
        pat = [f"(\\{f}.*?\\{g})" for f, g in zip(pat_f, pat_b)]

    return r"|".join(pat)
