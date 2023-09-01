def filter_text(text):
    return ''.join([char if char.isalnum() else ' ' for char in text]).lower()

def find_substring(text1, text2, start_index, length=1024):
    step = length // 2
    best_fragment = None
    best_position = -1

    while step >= 1:
        fragment = text1[start_index:start_index+length]
        pos = text2.find(fragment)

        if pos != -1:
            best_fragment = fragment
            best_position = pos
            length += step
        else:
            length -= step

        step //= 2

    return best_fragment, best_position

def main():
    with open("1.txt", "r", encoding="utf-8") as file1, open("2.txt", "r", encoding="utf-8") as file2:
        original_text1 = file1.read()
        text2 = file2.read()

    filtered_text1 = filter_text(original_text1)
    filtered_text2 = filter_text(text2)

    start_index = 0
    replacements = []

    while start_index < len(filtered_text1) - 3:
        fragment, position = find_substring(filtered_text1, filtered_text2, start_index)
        if position != -1:
            replacements.append((start_index, fragment, position))
            start_index += len(fragment)
        else:
            start_index += 1

    for start, fragment, position in reversed(replacements):
        original_text1 = original_text1[:start] + f"{{{original_text1[start:start+len(fragment)]} {position}}}" + original_text1[start + len(fragment):]

    print("Текст 1:", original_text1)

main()