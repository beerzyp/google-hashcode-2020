import operator
import collections
import copy
import itertools
import sys

hashGlobal = dict()
booksUsed = set()
libsUsed = set()

def score_lib(lib, scores):
    score = 0
    for book in lib['listBooks']:
        if book in booksUsed:
            continue
        score += scores[book]
    return score

def remove_extra_books(lib):
    new_list = []
    for b in lib['listBooks']:
        if b not in booksUsed:
            new_list.append(b)
    return new_list

def greedy_max_score(all_libraries, max_days, scores):

    sorted_libraries = sorted(all_libraries, key=operator.itemgetter('score','signDays'), reverse = True)
    i = 0
    days = 0
    next_lib = True
    final_lib = []
    while next_lib:
        sorted_libraries[0]["listBooks"] = remove_extra_books(sorted_libraries[0])
        final_lib.append(sorted_libraries[0])

        #adicionar ao used books e used lists
        for book in sorted_libraries[0]["listBooks"]:
            booksUsed.add(book)
        libsUsed.add(sorted_libraries[0]["id"])

        days += sorted_libraries[0]['signDays']
        if days > max_days or (i+1) >= len(sorted_libraries):
            next_lib = False   
        i += 1

        #recalcular o score
        for lib in all_libraries:
            lib["score"] = score_lib(lib,scores)

        sorted_libraries = sorted(all_libraries, key=operator.itemgetter('score','signDays'), reverse = True)

    #print(final_lib)
    return final_lib

def createOutputFile(allLibraries):
    #infile = open("a_example.txt", "r")
    #infile = open("b_read_on.txt", "r")
    #infile = open("c_incunabula.txt", "r")
    #infile = open("d_tough_choices.txt", "r")
    #infile = open("e_so_many_books.txt", "r")
    #infile = open("f_libraries_of_the_world.txt", "r")

    #file = open("a_example_out.txt", "w")
    file = open("b_read_on_out.txt", "w")
    #file = open("c_incunabula_out.txt", "w")
    #file = open("d_tough_choices_out.txt", "w")
    #file = open("e_so_many_books_out.txt", "w")
    #file = open("f_libraries_of_the_world_out.txt", "w")

    file.write(str(len(allLibraries)) + "\n")
    for lib in allLibraries:
        file.write(str(lib['id']) + " " + str(len(lib['listBooks'])) + "\n")
        for book in lib['listBooks']:
            file.write(str(book))
            file.write(" ")
        file.write("\n")

def main():
    infile = open("a_example.txt", "r")
    #infile = open("b_read_on.txt", "r")
    #infile = open("c_incunabula.txt", "r")
    #infile = open("d_tough_choices.txt", "r")
    #infile = open("e_so_many_books.txt", "r")
    #infile = open("f_libraries_of_the_world.txt", "r")

    firstLine = infile.readline().split()
    numBooks = int(firstLine[0])
    print(numBooks)
    numLibs = int(firstLine[1])
    print(numLibs)
    numDays = int(firstLine[2])
    print(numDays)
    scores = infile.readline().split()
    scores = [int(i) for i in scores]
    allLibraries = []
    for i in range(int(numLibs)):
        library = dict()
        firstLine = infile.readline().split()
        library['id'] = i
        library['numBooks'] = int(firstLine[0])
        library['signDays'] = int(firstLine[1])
        library['booksPerDay'] = int(firstLine[2])
        secondLine = infile.readline().split()
        secondLine = [int(i) for i in secondLine]
        finalSortedBooks = sortBooksByScore(secondLine, scores)
        library['listBooks'] = finalSortedBooks
        score = score_lib(library, scores)
        library['score'] = score
        allLibraries.append(library)
    sortedLibraries = orderingSignUp(allLibraries) # sorts by signUpDays and BooksPerDay
    for i in sortedLibraries:
        print(i)

def sortBooksByScore(listOfBooks,scores):
    books = {k: scores[v] for v, k in enumerate(listOfBooks)}
    final = [key for key in sorted(books.keys(), reverse=True)]
    return final

def orderingSignUp(allLibraries):
    #sorting by longest signup period
    sortedLibraries = sorted(allLibraries, key=operator.itemgetter('signDays','booksPerDay'), reverse=True)
    return sortedLibraries

if __name__ == '__main__':
    main()
