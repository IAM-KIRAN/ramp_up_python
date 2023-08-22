import random


def totalchar(a):
    total_num_of_char = len(a)
    totalwordsinastring = totalwords(a)
    print("TOTAL NUMBER OF CHARACTERS: ",total_num_of_char-(totalwordsinastring-1))


def totalduplicatechar(a):
    duplicate = []
    for i in a:
        if a.count(i)>1:
            if i not in duplicate:
                if i != " ":
                    duplicate.append(i)
    print("DUPICATE CHARACTERS: ",duplicate)


def totalwords(a):
    words = user_input.split()

    alphabetic_words = [word for word in words if word.isalpha()]

    total_num_of_words = len(alphabetic_words)
    #print("TOTAL NUMBER OF WORDS: ",total_num_of_words)
    return total_num_of_words


def totalduplicatewords(a):
    words = a.lower().split()
    duplicate_count = 0
    seen_words = []

    for word in words:
        if words.count(word) > 1 and word not in seen_words:
            seen_words.append(word)
            duplicate_count += 1
    print("TOTAL NUMBER OF DUPLICATE WORDS: ",duplicate_count)


def reverse_characters(a):
    reversed_statement = a[::-1]
    print("REVERSED CHARACTER: ",reversed_statement)
    return


def reverse_words(statement):
    words = statement.split()
    reversed_words = words[::-1]
    reversed_statement = " ".join(reversed_words)
    print("REVERSED WORDS: ",reversed_statement)


def newword(statement):
    words = statement.split()
    reversed_words = words[::-1]
    random.shuffle(reversed_words)
    new_statement = " ".join(reversed_words)
    print("NEW STATEMENT FORMED: ",new_statement)


def remove_duplicates(statement):
    unique_chars = []
    new_statement = ""

    for char in statement:
        if char.lower() not in unique_chars and char != " ":
            unique_chars.append(char.lower())
            new_statement += char

    print("REMOVED DUPLICATE STRING: ", new_statement)





user_input = input("Enter a statement: ")


totalchar(user_input)
totalduplicatechar(user_input)
totalwords(user_input)
totalduplicatewords(user_input)
reverse_characters(user_input)
reverse_words(user_input)
newword(user_input)
remove_duplicates(user_input)




# cleaned_input = user_input.replace(" ","")
#
# if cleaned_input.isalpha():
#     print("The statement contains only alphabetic characters.")
#     totalchar(cleaned_input)
#     totalduplicate(user_input)
#     totalwords(user_input)
# else:
#     print("The statement contains non-alphabetic characters.")