def all_variants(text):
    for cut in range(1, len(text) + 1):
        for i in range(len(text) - 1):
            yield text[i:cut]
            if cut == len(text):
                break
            cut += 1


a = all_variants("abcf")
for i in a:
    print(i)
