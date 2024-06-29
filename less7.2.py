def value(text):
    if not text:
        return text
    value = text[0].upper() + text[1:]
    if not text.endswith('.'):
        value += '.'

    return value
print(value("hello world"))
print(value("how are you"))
print(value("this is a sentence."))
print(value("another example"))