# bibtex_to_wikiFormat
Quick and dirty script to wikify a bibtex entry (so it can be cited in a wikipedia article)

2 possible inputs:
  - from a file (containing one and only one bibtex entry)
    `cat <yourfile> | python3 ./wikifyMe.py
  - from stdin
    `python3 ./wikifyMe.py << printf <yourbibtexentry>

The excpected bibtex entry should look like that:

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




