"""Word Finder: finds random words from a dictionary."""

from mimetypes import init

class WordFinder:

    """Machine for finding random words from dictionary.
    
    >>> wf = WordFinder("words.txt")
    5 words read

    >>> wf.random() in ["cat", "dog", "mouse", "flower", "tree"]
    True

    >>> wf.random() in ["cat", "dog", "mouse", "flower", "tree"]
    True

    >>> wf.random() in ["cat", "dog", "mouse", "flower", "tree"]
    True
    """

    word_list = []

    def __init__(self, words):
        """Open file, split onto separate lines, print '{Number} of words read'"""
        file = open("/mnt/c/Users/there/OneDrive/Desktop/Python/python-oo-practice/words.txt", "r")
        words = file.read().split("\n")  
        self.words = words
        self.word_list.append(words)
        print(f"{len(self.words)} words read")

    def random(self):
        """Return random word"""
        import random
        return random.choice(self.words)

  
class SpecialWordFinder(WordFinder):

    """Machine for finding random words from dictionary with spaces and comments.
    
    >>> wf = WordFinder("words2.txt")
    5 words read

    >>> wf.random() in ["cat", " ", "mouse", "#flower", "tree"]
    True

    >>> wf.random() in ["cat", " ", "mouse", "#flower", "tree"]
    True

    >>> wf.random() in ["cat", " ", "mouse", "#flower", "tree"]
    True
    """

    def __init__(self, words):
        """Open words2.txt file and split onto separate lines."""

        super(SpecialWordFinder, self).__init__(words)
        file = open("words2.txt", "r")
        words = file.read().split("\n")  
        self.words = words
        self.word_list.append(words)

    def remove(self):
        """Remove comments and blank spaces from list"""

        for line in self.words:
            for str in line:
                if line[str] == " " or line[str] == "#":
                    del line[str]

    def random(self):
        """Return random word"""
        import random
        return random.choice(self.words)

# class SpecialWordFinder(WordFinder):
#     """Machine for finding random words from dictionary.
    
#     >>> wf = WordFinder("words.txt")
#     5 words read

#     >>> wf.random() in ["cat", " ", "mouse", "#flower", "tree"]
#     True

#     >>> wf.random() in ["cat", " ", "mouse", "#flower", "tree"]
#     True

#     >>> wf.random() in ["cat", " ", "mouse", "#flower", "tree"]
#     True
#     """

#     def parse(self, dict_file):
#         """Parse dict_file -> list of words, skipping blanks/comments."""

#         return [w.strip() for w in dict_file
#                 if w.strip() and not w.startswith("#")]