
def count_words(text):
    return text.split()


def count_chars(text):
    d = {}
    for char in text.lower():
        if not d.get(char, None):
            d[char] = 1
        else: d[char] += 1
    return d

def sort_count_chars(dic):
    return dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))