def first_unique(text):
    counts = {}

    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1

    for ch in text:
        if counts.get(ch) == 1:
            return ch

    return None
