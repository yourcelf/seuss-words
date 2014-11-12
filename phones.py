# -*- coding: utf-8 -*-

arpabet = {
    "AA": {"type": "vowel", "ipa": u"ɑ"},
    "AE": {"type": "vowel", "ipa": u"æ"},
    "AH": {"type": "vowel", "ipa": u"ə"},
    "AO": {"type": "vowel", "ipa": u"ɔ"},
    "AW": {"type": "vowel", "ipa": u"aʊ"},
    "AY": {"type": "vowel", "ipa": u"aɪ"},
    "B": {"type": "stop", "ipa": u"b"},
    "CH": {"type": "affricate", "ipa": u"tʃ"},
    "D": {"type": "stop", "ipa": u"d"},
    "DH": {"type": "fricative", "ipa": u"ð"},
    "EH": {"type": "vowel", "ipa": u"ɛ"},
    "ER": {"type": "vowel", "ipa": u"ɝ"},
    "EY": {"type": "vowel", "ipa": u"eɪ"},
    "F": {"type": "fricative", "ipa": u"f"},
    "G": {"type": "stop", "ipa": u"g"},
    "HH": {"type": "aspirate", "ipa": u"h"},
    "IH": {"type": "vowel", "ipa": u"ɪ"},
    "IY": {"type": "vowel", "ipa": u"i"},
    "JH": {"type": "affricate", "ipa": u"dʒ"},
    "K": {"type": "stop", "ipa": u"k"},
    "L": {"type": "liquid", "ipa": u"ɫ"},
    "M": {"type": "nasal", "ipa": u"m"},
    "N": {"type": "nasal", "ipa": u"n"},
    "NG": {"type": "nasal", "ipa": u"ŋ"},
    "OW": {"type": "vowel", "ipa": u"oʊ"},
    "OY": {"type": "vowel", "ipa": u"ɔɪ"},
    "P": {"type": "stop", "ipa": u"p"},
    "R": {"type": "liquid", "ipa": u"r"},
    "S": {"type": "fricative", "ipa": u"s"},
    "SH": {"type": "fricative", "ipa": u"ʃ"},
    "T": {"type": "stop", "ipa": u"t"},
    "TH": {"type": "fricative", "ipa": u"θ"},
    "UH": {"type": "vowel", "ipa": u"ʊ"},
    "UW": {"type": "vowel", "ipa": u"u"},
    "V": {"type": "fricative", "ipa": u"v"},
    "W": {"type": "semivowel", "ipa": u"w"},
    "Y": {"type": "semivowel", "ipa": u"j"},
    "Z": {"type": "fricative", "ipa": u"z"},
    "ZH": {"type": "fricative", "ipa": u"ʒ"},
    "?": {"type": "meta", "ipa": u"?"},
}

def _lookup(arpabet_phoneme):
    a = arpabet_phoneme
    while a and a not in arpabet:
        a = a[:-1]
    if not a:
        raise Exception("Unknown phoneme: {}".format(arpabet_phoneme))
    return arpabet.get(a)

def get_type(arpabet_phoneme):
    return _lookup(arpabet_phoneme)["type"]

def to_ipa(arpabet_list):
    return "".join(_lookup(a)["ipa"] for a in arpabet_list)
