filename = 'filtered_words.txt'
words = []

# load filtered_word.txt
with open(filename, 'r', encoding='utf8') as file:
    wordlist = file.readlines()
    for word in wordlist:
        word = word.strip()  # 去除尾部的换行符
        words.append(word)
    print(words)

# input
iptstr = input('please input something:')
outstr = iptstr

# search
for word in words:
    if iptstr.find(word) != -1:
        outstr = outstr.replace(word, '**')

print(outstr)
