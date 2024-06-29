def one_index(text: str, symbol: str) -> int or None:
    first_index = text.find(symbol)
    if first_index == -1:
        return None
    if len(symbol) == 1:
        one_index = text.find(symbol, first_index + 1)
    else:
        one_index = text.find(symbol, first_index + len(symbol))
    if one_index == -1:
        return None

    return one_index
print(one_index("sims", "s"))
print(one_index("fd the river", "e"))
print(one_index("hi", " "))
print(one_index("Hello, hello", "lo"))