from operator import itemgetter
import copy
import itertools
import sys

hashGlobal = dict()

def score_lib(lib, scores):
    score = 0
    for book in lib['listBooks']:
        score += scores[book]
    return score

def greedy_max_score(all_libraries, max_days):
    sorted_libraries = sorted(all_libraries, key=itemgetter('score'))
    i = 0
    days = 0
    flag = True
    final_lib = []
    while flag:
        final_lib.append(sorted_libraries[i])
        days += sorted_libraries[i]['signDays']
        if days > max_days:
            flag = False   
        i += 1
    print(final_lib)
    return final_lib


def main():
    #infile = open("a_example.txt", "r")
    infile = open("b_read_on.txt", "r")
    #infile = open("c_incunabula.txt", "r")
    #infile = open("d_tough_choices.txt", "r")
    #infile = open("e_so_many_books.txt", "r")
    #infile = open("f_libraries_of_the_world.txt", "r")

    firstLine = infile.readline().split()
    numBooks = int(firstLine[0])
    numLibs = int(firstLine[1])
    numDays = int(firstLine[2])
    scores = infile.readline().split()
    scores = [int(i) for i in scores]
    allLibraries = []
    for i in range(int(numLibs)):
        library = dict()
        firstLine = infile.readline().split()
        library['numBooks'] = int(firstLine[0])
        library['signDays'] = int(firstLine[1])
        library['booksPerDay'] = int(firstLine[2])
        secondLine = infile.readline().split()
        secondLine = [int(i) for i in secondLine]
        library['listBooks'] = secondLine
        score = score_lib(library, scores)
        library['score'] = score
        allLibraries.append(library)
    orderingSignUp(allLibraries)


def orderingSignUp(allLibraries):
    #sorting by longest signup period
    sortedLibraries = sorted(allLibraries, key=itemgetter('signDays'), reverse=True)



if __name__ == '__main__':
    main()
