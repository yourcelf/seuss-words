import json
import textwrap
from collections import defaultdict

import phones

def load_phonemes():
    phonemes = defaultdict(dict)
    with open("cmudict.0.7a") as fh:
        for line in fh:
            if line.startswith(";;;"):
                continue
            parts = line.split()
            phonemes[len(parts) - 1][tuple(parts[1:])] = parts[0]
    return phonemes

def find_matches(phonemes):
    matches = defaultdict(list)
    for size in phonemes:
        for phoneme in phonemes[size]:
            for i in range(len(phoneme)):
                if phones.get_type(phoneme[i]) != "vowel":
                    continue
                minusone = list(phoneme)
                minusone[i] = "?"
                matches[tuple(minusone)].append(phoneme)
    return matches

def report_matches(matches, phonemes):
    by_length = defaultdict(list)
    # Organize by phoneme length
    for phoneme, matchlist in matches.iteritems():
        by_length[len(phoneme)].append((phoneme, matchlist))

    top = []
    # Sort within phoneme length groups by number of matches
    for length, matchlist in by_length.iteritems():
        top += matchlist
    
    top.sort(key=lambda a: len(a[1]), reverse=True)
    for match in top[:100]:
        text = textwrap.wrap(
            " ".join(phonemes[len(m)][tuple(m)].lower() for m in match[1]),
            initial_indent="   ",
            subsequent_indent="   "
        )
        print phones.to_ipa(match[0]), len(match[1])
        for line in text:
            print line
        

def main():
    phonemes = load_phonemes()
    matches = find_matches(phonemes)
    report_matches(matches, phonemes)

if __name__ == "__main__":
    main()
