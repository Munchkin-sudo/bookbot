def get_num_words(file_contents):
    words = file_contents.split()
    num_words = len(words)
    return num_words



def get_num_char(file_contents):
    lowercase = file_contents.lower()
    num_char = {}
    for l in lowercase:
        if l in num_char:
            num_char[l] += 1
        else:
            num_char[l] = 1
    return num_char

def get_char_report_data(num_char):
    sorted_num_char = []
    for letter, count in num_char.items():
        sorted_num_char.append({"char": letter, "num": count})
    def sort_on(num):
        return num["num"]
    sorted_num_char.sort(reverse=True, key=sort_on)
    return sorted_num_char