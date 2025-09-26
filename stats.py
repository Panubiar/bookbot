def get_num_words(whole_text):
    word_amount = len(whole_text.split())
    return word_amount

def get_num_characters(whole_text):
    counts = {}
    low_text = whole_text.lower()
    for character in low_text:
        if character in counts:
            counts[character] += 1
        else:
            counts[character] = 1
    
    return counts

def get_sorted(counts):
    char_counts = []
    for character in counts:
        count = counts[character]
        char_counts.append({"char": character, "num": count})
    char_counts.sort(reverse=True, key=helper_sort)
    return char_counts       

def helper_sort(item):
    return item["num"]
