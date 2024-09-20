from twttr import shorten


def test_uppercase():
    assert shorten("POKEMON") == "PKMN"
    assert shorten("ADNAN") == "DNN"
    assert shorten("KFC") == "KFC"


def test_lowercase():
    assert shorten("pokemon") == "pkmn"
    assert shorten("adnan") == "dnn"
    assert shorten("kfc") == "kfc"

def test_numbers():
    assert shorten("i HAVE 7 tOeS") == " HV 7 tS"


def test_mixedcase():
    assert shorten("PokEmoN") == "PkmN"
    assert shorten("AdNan") == "dNn"
    assert shorten("KfC") == "KfC"
    assert shorten("aeIOu") == ""


def test_aA():
    assert shorten("Apples and ants danced at a bashful catamaran party") == "ppls nd nts dncd t  bshfl ctmrn prty"
    assert shorten("aA") == ""

def test_eE():
    assert shorten("Every eel sleeps") == "vry l slps"
    assert shorten("Ee") == ""


def test_iI():
    assert shorten("I think dirt is itchy") == " thnk drt s tchy"
    assert shorten("iI") == ""


def test_oO():
    assert shorten("Olly obvs shoots bombs") == "lly bvs shts bmbs"
    assert shorten("oO") == ""

def test_uU():
    assert shorten("why my buggy rusty bruh") == "why my bggy rsty brh"
    assert shorten("uU") == ""


def test_blank():
    assert shorten("") == ""

def test_symbols1():
    assert shorten("hello_my_name_is_adnan") == "hll_my_nm_s_dnn"


def test_symbols2():
    assert shorten("poKeMon.i$,da/best") == "pKMn.$,d/bst"



