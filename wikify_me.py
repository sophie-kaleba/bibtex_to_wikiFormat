import fileinput
import sys

"""
friendly reminder that we are trying to parse this kind of bibtex reference (the number of lines can vary)

"@inproceedings{Eisl:2016:TRA:2972206.2972211,
 author = {Eisl, Josef and Grimmer, Matthias and Simon, Doug and W\"{u}rthinger, Thomas and M\"{o}ssenb\"{o}ck, Hanspeter},
 title = {Trace-based Register Allocation in a JIT Compiler},
 booktitle = {Proceedings of the 13th International Conference on Principles and Practices of Programming on the Java Platform: Virtual Machines, Languages, and Tools},
 series = {PPPJ '16},
 year = {2016},
 isbn = {978-1-4503-4135-6},
 location = {Lugano, Switzerland},
 pages = {14:1--14:11},
 articleno = {14},
 numpages = {11},
 url = {http://doi.acm.org/10.1145/2972206.2972211},
 doi = {10.1145/2972206.2972211},
 acmid = {2972211},
 publisher = {ACM},
 address = {New York, NY, USA},
 keywords = {Just-in-Time Compilation, Linear Scan, Register Allocation, Trace Compilation, Trace Register Allocation, Virtual Machines},
}"

to get this kind of wikipedia reference

{{cite journal
| last       =
| first      =
| last2      =
| first2     =
| date       =
| title      =
| url        =
| journal    =
| volume     =
| issue      =
| pages      =
| doi        =
| access-date =
}}

"""
def parseAllThatShit(result):
    i = 0
    year=""
    for line in fileinput.input():
        if "@" in line:
            result = parseTypeOfRef(line, result)
        if "author" in line:
            (result, lastname) = parseListOfAuthors(line, result)
        else:
            (result,year) = parseRegularLine(line, result, year)
    result += " | id = "+lastname+year
    return result

def parseTypeOfRef(line, result):
    if ("inproceedings" in line) or ("INPROCEEDINGS" in line) or ("inProceedings" in line):
        result += "conference"
    elif "article" in line:
        result += "journal"
    return result


def parseRegularLine(line, result, year):
    try:
        splitline = line.split(" = ")
        if len(splitline) == 2:
            result += " | "+splitline[0].strip()+" = "
            if ("year" in splitline[0]):
                year = splitline[1][1:-3]
            new = splitline[1].strip()[1:-2]
            result += new
    except IndexError:
        pass
    return (result, year)

def getFirstLastName(authorsList):
    return str(authorsList[0].split(",")[0])

def parseListOfAuthors(authorsList, result):
    arrOfAuth = authorsList.split(" = ")
    arrOfAuth = arrOfAuth[1][1:-1].split(" and ")
    i = 1 #index of author
    author_id = getFirstLastName(arrOfAuth)
    for e in arrOfAuth :
        name_first = e.split(",")
        result += " | last"+str(i)+" = "
        result += name_first[0].strip()
        result += " | first"+str(i)+" = "
        result += name_first[1].strip()
        i+=1
    return (result, author_id)

if __name__ == '__main__':
    result = "{{ cite "
    result = parseAllThatShit(result)+" }}"
    print(result)
