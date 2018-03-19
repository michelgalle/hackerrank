import pprint
pp = pprint.PrettyPrinter(indent=4)


class Trie:
    def __init__(self):
        self.contact_indices = {}

    # all letters, a, ab, abc, ..
    def edge_ngram(self, contact):
        return [contact[0:idx] for idx in range(1, len(contact) + 1)]

    def add(self, contact):
        for token in self.edge_ngram(contact):
            self.contact_indices[token] = self.contact_indices.get(token, 0) + 1

    def find(self, name):
        return self.contact_indices.get(name, 0)


trie = Trie()
n = int(input().strip())
for a0 in range(n):
    op, contact = input().strip().split(' ')
    if op == 'add':
        trie.add(contact)
    elif op == 'find':
        print(trie.find(contact))

