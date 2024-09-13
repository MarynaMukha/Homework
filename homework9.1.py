# v1
def popular_words (text, words):
    text_lower = text.lower().split()

    result = {}
    for i in range(len(words)):
        count_ = {words[i]: text_lower.count(words[i])}
        result.update(count_)
    return result

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')

# v2
def popular_words (text, words):
    text_lower = text.lower().split()

    result = {words[i]: text_lower.count(words[i]) for i in range(len(words))}
    return result

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
