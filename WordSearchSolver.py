from WordSearchBlock import WordSearchBlock
import sys

class WordSearchSolver(object):
    """
    This is the solver.  It is instantiated with a text file containing the specified format.
    Once instantiated, it can solve() the puzzle, finding all of the words listed on the first
    line of the text file.
    """
    linecount = None
    words_to_find = None
    rawblock = None

    def __init__(self, filename):
        """
        Provide full or partial patth to a filename containing a wordsearch puzzle in the appropriate format.
        """
        self.linecount = 0
        self.words_to_find = list()
        self.rawblock = list()
        f = open(filename)
        for line in f.readlines():
            if (',') not in line:
                raise ValueError("Invalid input, this line doesn't contain a comma anywhere.")
            if (self.linecount == 0):
                self.words_to_find = line.strip().split(',')   #list of words
            else:
                self.rawblock.append(line.strip().split(','))   #raw block of letters
            self.linecount += 1

        self.wsb = WordSearchBlock(self.rawblock)
    
    def solution(self):
        """
        Get all slices from the WordSearchBlock as WordSearchLine objects.  These objects are
        easy to query simply using Python's "in" operator.  If a word is discovered,
        the Line object will hold the result internally.  Just get the result out and 
        move on to the next word.
        """
        slices = self.wsb.getAllSlices()
        results = list()
        #for each slice, look for every word in the list
        for slice in slices:    #that is cool
            for word in self.words_to_find:
                if word in slice:
                    results.append(slice.get_result_as_string(0))  #assume only one result found, that's why we look for result zero

        results.sort()
        outputstr = "\n".join(results)
        return outputstr

def main():
    """
    Will allow running of arbitrary word puzzes by providing the filename at the commandline:
    WordSearchSolver.py <filename>
    """
    wss = WordSearchSolver(sys.argv[1])
    print(wss.solution())

if __name__ == "__main__":
    main()
