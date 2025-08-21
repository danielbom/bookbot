def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()


def words_count(content):
    return len(content.split())


def chars_count(content):
    counter = {}
    for ch in content.lower():
        if ch not in counter:
            counter[ch] = 0
        counter[ch] += 1
    return counter


def sort_counter(counter):
    result = list(counter.items())
    result.sort(key=lambda pair: pair[1], reverse=True)
    return result

