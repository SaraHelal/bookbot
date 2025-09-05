def get_num_words(text):
    return len(text.split())

def get_chars_from_word(text):
    count_chars_dic = {}
    for char in text.lower():
        if char in count_chars_dic:
            count_chars_dic[char] += 1
        else:
            count_chars_dic[char] = 1
    refactor_dict(count_chars_dic)
    return count_chars_dic

def refactor_dict(chars_dict):
    res_arr = []
    for key, value in chars_dict.items():
        new_dict = {}
        new_dict["char"] = key
        new_dict["num"] = value
        res_arr.append(new_dict)
    sorted_arr = sort_dict(res_arr)
    print_output(sorted_arr)
    return sorted_arr

    return
def sort_on(items):
    return items["num"]

def sort_dict(chars_dict):
    chars_dict.sort(reverse=True, key=sort_on)
    return chars_dict

def print_output(sorted_arr):
    for obj in sorted_arr:
        if obj['char'].isalpha():
            print(f"{obj['char']}: {obj['num']}")