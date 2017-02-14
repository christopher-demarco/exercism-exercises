def _normalize(word):
    word = word.lower()
    word = [x for x in word]
    word.sort()
    word = ''.join(word)
    return word

def detect_anagrams(word, candidates):
    anagrams = []
    if type(candidates) is not list:
        candidates = [c for c in candidates.split()]
    for candidate in candidates:
        if word.lower() == candidate.lower():
            continue
        if _normalize(word) == _normalize(candidate):
            anagrams.append(candidate)

    return anagrams



