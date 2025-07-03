def get_word_count(content):
    words = content.split()
    return len(words)

def get_key(items):
    return items["num"]

def final_op(content):
    dictionary = get_word_freq(content)
    list = create_list(dictionary=dictionary)
    sort_dict(list)
    return list

def create_list(dictionary):
    list = []
    for key in dictionary:
        if key.isalpha():
            list.append({"char": key, "num": dictionary[key]})
    return list

def get_word_freq(content):
    content = content.lower()
    word_freq = {}
    for word in content:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

def sort_dict(list):
    list.sort(reverse=True, key=get_key)