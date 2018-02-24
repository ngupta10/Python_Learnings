def changes(text):
    text = str(text.lower())
    print(text)
    text = str(text.replace(",", "."))
    print(text)
    text = str("".join(text.split(".")))
    print(text)
    text = str("".join(text.split(" ")))
    print(text)
    return text




def reverse(text):
    return text[::-1]


def is_palindrome(text):
    texta = changes(text)
    print(texta)
    return texta == reverse(texta)


something = raw_input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")