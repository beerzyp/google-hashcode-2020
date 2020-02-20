import copy
import itertools
import sys

hashGlobal = dict()

def score_lib(lib, scores):
    score = 0
    for book in lib['listBooks']:
        score += scores[book]
    return score

def greedy_max_score(all_libraries):
    lo,hi = sys.maxint,-sys.maxint-1
    for x in (item['the_key'] for item in dict_list):
        lo,hi = min(x,lo),max(x,hi)

def main():
    infile = open("a_example.txt", "r")
    #infile = open("b_read_on.txt", "r")
    #infile = open("c_incunabula.txt", "r")
    #infile = open("d_tough_choices.txt", "r")
    #infile = open("e_so_many_books.txt", "r")
    #infile = open("f_libraries_of_the_world.txt", "r")

    firstLine = infile.readline().split()
    numBooks = int(firstLine[0])
    numLibs = int(firstLine[1])
    numDays = int(firstLine[2])
    scores = infile.readline().split()
    allLibraries = []
    for i in range(int(numLibs)):
        library = dict()
        firstLine = infile.readline().split()
        library['numBooks'] = int(firstLine[0])
        library['signDays'] = int(firstLine[1])
        library['booksPerDay'] = int(firstLine[2])
        secondLine = infile.readline().split()
        library['listBooks'] = secondLine
        score = score_lib(library, scores)
        library['score'] = score
        allLibraries.append(library)
    print(allLibraries)

# def auxCombination(): # Calculates sum for each combo

if __name__ == '__main__':
    main()
