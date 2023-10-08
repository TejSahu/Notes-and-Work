def print_utf8_characters():
    for char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
        utf8_encoded = char.encode('utf-8')
        utf_value = ord(char)
        print(f"Character: {char}, UTF Value: {utf_value}")


# Call the function to print characters in UTF-8 encoding
if __name__ == '__main__':
    print_utf8_characters()
