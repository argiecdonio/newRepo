def exchange_first_last(string):

    if len(string) < 2:
        return string
    else:
        first_char = string[0]
        last_char = string[-1]

        middle_chars = string[1:-1]

        new_string = last_char + middle_chars + first_char
        return new_string

given_string = "AEIOU"
new_string = exchange_first_last(given_string)
print("Given String: ", given_string)
print("New String: ", new_string)
