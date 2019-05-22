import os
from kalamine import KeyboardLayout


def load_layout(filename):
    path = os.path.join('.', 'layouts', filename + '.yaml')
    return KeyboardLayout(path)


def test_layouts():
    layout = load_layout('ansi')
    assert layout.layers[0]['ad01'] == 'q'
    assert layout.layers[1]['ad01'] == 'Q'
    assert layout.layers[0]['tlde'] == '`'
    assert layout.layers[1]['tlde'] == '~'
    assert not layout.has_altgr
    assert not layout.has_1dk
    assert '**' not in layout.dead_keys

    layout = load_layout('prog')
    assert layout.layers[0]['ad01'] == 'q'
    assert layout.layers[1]['ad01'] == 'Q'
    assert layout.layers[0]['tlde'] == '`'
    assert layout.layers[1]['tlde'] == '~'
    assert layout.layers[4]['tlde'] == '*`'
    assert layout.layers[5]['tlde'] == '*~'
    assert layout.has_altgr
    assert not layout.has_1dk
    assert '**' not in layout.dead_keys

    layout = load_layout('intl')
    assert layout.layers[0]['ad01'] == 'q'
    assert layout.layers[1]['ad01'] == 'Q'
    assert layout.layers[0]['tlde'] == '*`'
    assert layout.layers[1]['tlde'] == '*~'
    assert not layout.has_altgr
    assert layout.has_1dk
    assert '**' in layout.dead_keys
    assert layout.dead_keys['**']['base'] == 'euioac.EUIOAC'
    assert layout.dead_keys['**']['alt'] == 'éúíóáç…ÉÚÍÓÁÇ'
    assert layout.dead_keys['**']['alt_self'] == '´'
