import os

from kalamine import KeyboardLayout


def load_layout(filename):
    return KeyboardLayout(os.path.join(".", "layouts", filename + ".toml"))


def test_ansi():
    layout = load_layout("ansi")
    assert layout.layers[0]["ad01"] == "q"
    assert layout.layers[1]["ad01"] == "Q"
    assert layout.layers[0]["tlde"] == "`"
    assert layout.layers[1]["tlde"] == "~"
    assert not layout.has_altgr
    assert not layout.has_1dk
    assert "**" not in layout.dead_keys


def test_prog():  # AltGr + dead keys
    layout = load_layout("prog")
    assert layout.layers[0]["ad01"] == "q"
    assert layout.layers[1]["ad01"] == "Q"
    assert layout.layers[0]["tlde"] == "`"
    assert layout.layers[1]["tlde"] == "~"
    assert layout.layers[4]["tlde"] == "*`"
    assert layout.layers[5]["tlde"] == "*~"
    assert layout.has_altgr
    assert not layout.has_1dk
    assert "**" not in layout.dead_keys
    assert len(layout.dead_keys["*`"]) == 18
    assert len(layout.dead_keys["*~"]) == 21


def test_intl():  # 1dk + dead keys
    layout = load_layout("intl")
    assert layout.layers[0]["ad01"] == "q"
    assert layout.layers[1]["ad01"] == "Q"
    assert layout.layers[0]["tlde"] == "*`"
    assert layout.layers[1]["tlde"] == "*~"
    assert not layout.has_altgr
    assert layout.has_1dk
    assert "**" in layout.dead_keys

    assert len(layout.dead_keys) == 5
    assert "**" in layout.dead_keys
    assert "*`" in layout.dead_keys
    assert "*^" in layout.dead_keys
    assert "*¨" in layout.dead_keys
    assert "*~" in layout.dead_keys
    assert len(layout.dead_keys["**"]) == 15
    assert len(layout.dead_keys["*`"]) == 18
    assert len(layout.dead_keys["*^"]) == 43
    assert len(layout.dead_keys["*¨"]) == 21
    assert len(layout.dead_keys["*~"]) == 21

    # ensure the 1dk parser does not accumulate values from a previous run
    layout = load_layout("intl")
    assert len(layout.dead_keys["*`"]) == 18
    assert len(layout.dead_keys["*~"]) == 21

    assert len(layout.dead_keys) == 5
    assert "**" in layout.dead_keys
    assert "*`" in layout.dead_keys
    assert "*^" in layout.dead_keys
    assert "*¨" in layout.dead_keys
    assert "*~" in layout.dead_keys
    assert len(layout.dead_keys["**"]) == 15
    assert len(layout.dead_keys["*`"]) == 18
    assert len(layout.dead_keys["*^"]) == 43
    assert len(layout.dead_keys["*¨"]) == 21
    assert len(layout.dead_keys["*~"]) == 21
