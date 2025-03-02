def get_num_words(content:str):
    words=content.split()
    return len(words)

def freq_of_char(content:str)->dict:
    char_freq = {}
    for char in content.lower():
        if char.isalpha():
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1
    # Return the dictionary directly instead of converting to a list
    return char_freq

def sorted_word_list(dict):
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)
