class WordsFinder:
    def __init__(self, *args):
        self.file_names = []
        for file in args:
            self.file_names.append(file)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for file in self.file_names:
            with open(file, encoding="utf-8") as current_file:
                values = []
                for line in current_file:
                    line = line.lower()
                    for p in punctuation:
                        line = line.replace(p, ' ')
                    list_of_words = line.split()
                    values.extend(list_of_words)
                all_words[file] = values
        return all_words

    def find(self, word):
        find_word = {}
        for name, words in self.get_all_words().items():
            for w in words:
                if word.lower() == w:
                    find_word[name] = words.index(w) + 1
                    break
        return find_word

    def count(self, word):
        count_word = {}

        for name, words in self.get_all_words().items():
            count = 0
            for w in words:
                if word.lower() == w:
                    count += 1
            count_word[name] = count
        return count_word



finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
