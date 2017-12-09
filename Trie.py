class Node():
    def __init__(self):
        self.endpoint = False
        self.dict = {}

class Trie():

    def __init__(self, dictFile):
        self.root = Node()

        with open(dictFile, 'r') as infile:
            word = infile.readline()
            while word:
                word = word[:-1].lower()
                print("Adding {}".format(word))
                word = infile.readline()
                self.add(word)

    def find(self, word):
        s = word.lower()
        curr = self.root
        last = len(s) - 1
        for letter, i in enumerate(s):
            if letter in curr.dict:
                curr = curr.dict[letter]
            else:
                return False
        # Need to check if we are in the middle of a known word.
        return curr.endpoint

    def add(self, word):
        curr = self.root
        last = len(word) -1
        for letter, i in enumerate(word):
            if letter in curr.dict:
                curr = curr.dict[letter]
            else:
                newNode = Node()
                curr.dict[letter] = newNode
                curr = curr.dict[letter]
            if i == last:
                # This is a valid stopping point, so set a flag
                curr.endpoint = True

if __name__ == "__main__":
    myTrie = Trie("en_US.txt")
    print("'Computer' is in dictionary: {}".format(myTrie.find("Computer")))
    print("'it' is in dictionary: {}".format(myTrie.find("it")))
    print("'foo' is in dictionary: {}".format(myTrie.find("foo")))
    print("'bar' is in dictionary: {}".format(myTrie.find("bar")))
