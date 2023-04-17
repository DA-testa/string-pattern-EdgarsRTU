def read_input():
    fileorno = input()
    if "I" in fileorno or "i" in fileorno:
        pattern = input().rstrip()
        text = input().rstrip()
    elif "F" in fileorno or "f" in fileorno:
        file = "06"
        if "a" not in file:
            with open("tests/" + file, 'r')as f:
                pattern = f.readline().rstrip()
                text = f.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    prime = 1
    i_len, j_len = len(pattern), len(text)
    pattern_hash = sum(ord(pattern[i]) * pow(prime, i) for i in range(i_len))
    text_hash = sum(ord(text[i]) * pow(prime, i) for i in range(i_len))
    occurrences = []
    for i in range(j_len - i_len + 1):
        if pattern_hash == text_hash:
            if pattern == text[i:i+i_len]:
                occurrences.append(i)
        if i < j_len - i_len:
            text_hash = (text_hash - ord(text[i])) / prime + ord(text[i+i_len]) * pow(prime, i_len-1)
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
#Edgars Miklaševičs 211RKB044
