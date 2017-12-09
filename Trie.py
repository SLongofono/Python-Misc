
"""

This demonstrates a simple Trie or prefix-tree data structure for storing a
dictionary or other ordered data type.  Linear lookup is fast if the average
sequence length is small.  Adding is similar time complexity.  Space
complexity is a little more nebulous, as it will depend on the specific
dictionary in use.

This is an interesting way to solve a boggle board.  Using a breadth-first
traversal of the board, all valid sequences can be checking in short order.

"""
VERBOSE = False

class Node():
    def __init__(self):
        self.endpoint = False
        self.dict = {}

class Trie():

    def __init__(self, dictFile):
        self.root = Node()

        with open(dictFile, 'r') as infile:
            word = infile.readline()
            while len(word) > 0:
                if VERBOSE:
                    print("Adding {}".format(self.clean(word)))
                self.add(word)
                word = infile.readline()

    def clean(self, word):
        ret = word.strip('\n')
        ret = ret.lower()
        return ret

    def find(self, word):
        s = self.clean(word)
        curr = self.root
        last = len(s) - 1
        for i, letter in enumerate(s):
            if letter in curr.dict:
                curr = curr.dict[letter]
                if i == last:
                    return curr.endpoint
            else:
                if VERBOSE:
                    print("Broken at {}".format(s[:i+1]))
                break

        return False

    def add(self, word):
        word = self.clean(word)
        curr = self.root
        last = len(word) -1
        for i, letter in enumerate(word):
            if letter in curr.dict:
                curr = curr.dict[letter]
                if i == last:
                    # This is a valid stopping point, so set a flag
                    curr.endpoint = True
            else:
                newNode = Node()
                curr.dict[letter] = newNode
                curr = curr.dict[letter]
                if i == last:
                    # This is a valid stopping point, so set a flag
                    curr.endpoint = True

if __name__ == "__main__":
    myTrie = Trie("words")

    testWords = ["Code", "it", "navigation", "fqwexo", "baz", "aeiou",
                 "apple", "biplane", "moose", "goose", "pond", "scum",
                 "garbage", "windows", "portal", "video", "compression",
                 "injury", "insult", "negative", "positive", "circuit",
                 "dobby", "theelf", "harrypotter"
                ]

    for word in testWords:
        print("{:<20} is in dictionary: {}".format(word, myTrie.find(word)))

