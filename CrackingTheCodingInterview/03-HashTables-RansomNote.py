import collections


def ransom_note(magazine, ransom):
    magazine_dict = collections.Counter(magazine)
    ransom_dict = collections.Counter(ransom)
    return all([c <= magazine_dict[k] for k, c in ransom_dict.items()])


m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if answer:
    print("Yes")
else:
    print("No")
