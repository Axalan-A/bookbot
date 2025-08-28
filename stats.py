def count_words(text):
    split_text = text.split()
    word_count = len(split_text)
    print(f"Found {word_count} total words")

def count_characters(text):
    lowercase_text = text.lower()
    character_count = {}
    characters_seen = set()
    for character in lowercase_text:
        if character not in characters_seen:
            characters_seen.add(character)
            character_count[character] = 1
        else:
            character_count[character] += 1
    return(character_count)

def sorter(items):
    return items["num"]

def sort_counts(count_dictionary):
    count_list = []
    for character in count_dictionary:
        if character.isalpha():
            count_entry = {"char": character, "num": count_dictionary[character]}
            count_list.append(count_entry)

    count_list.sort(reverse=True, key=sorter)
    for entry in count_list:
        print(f"{entry["char"]}: {entry["num"]}")
