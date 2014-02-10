# the shittiest plugin ever
# -- I mean crappiest!

replace_things = [
    ('motherfuck', 'fuck'),   # just remove 'mother' entirely from it
    ('mother fuck', 'fuck'),  # because it's easier that way
    ('MOTHERFUCK', 'FUCK'),
    ('MOTHER FUCK', 'FUCK'),
    ('fucking', 'bloody'),
    ('FUCKING', 'BLOODY'),
    ("fuckin'", 'bloody'),
    ("FUCKIN'", 'BLOODY'),
    ('fuckin', 'bloody'),
    ('FUCKIN', 'BLOODY'),
    ('fooking', 'bloody'),
    ("FOOKIN'", 'BLOODY'),
    ("fookin'", 'bloody'),
    ("FOOKIN", 'BLOODY'),
    ('fookin', 'bloody'),
    ('fuck', 'bugger'),
    ('Fuck', 'Bugger'),
    ('FUCK', 'BUGGER'),
    ('shitty', 'crappy'),
    ('SHITTY', 'CRAPPY'),
    ('shitti', 'crappi'),
    ('shiti', 'crapi'),
    ('shit', 'crap'),
    ('SHIT', 'CRAP'),
    ('Shit', 'Crap'),
    ('penis', 'wewe'),
    ('vagina', 'hoo-hah'),
    ('vulva', 'hoo-hah'),
    ('cunt', 'hoo-hah'),
    ('CUNT', 'HOO-HAH'),
    ('ass', 'arse'),
    ('dammit', 'darn it'),
    ('damnit', 'darn it'),
    ('damn', 'darn'),
    ('DAMMIT', 'DARN IT'),
    ('DAMN', 'DARN'),
    ('ASS', 'ARSE'),
    ('bitch', 'witch'),
    ('BITCH', 'WITCH'),
    ('Bitch', 'Witch'),
]

import weechat

def maybe_censor_message(data, modifier, modifier_data, string):
    buf = str(string)  # deep copy
    for bad, replace in replace_things:
        buf = buf.replace(bad, replace)
    return buf

weechat.register("bawlderdise", "Andrew Wilcox", "0.1", "MIT", "[censored!]", "", "")

weechat.hook_modifier("irc_in_privmsg", "maybe_censor_message", "")
