# bibtex_to_wikiFormat
Quick and dirty script to wikify a bibtex entry (so it can be cited in a wikipedia article)

2 possible inputs:
  - from a file (containing one and only one bibtex entry)
    ```cat <yourfile> | python3 ./wikifyMe.py```
  - from stdin
    ```python3 ./wikifyMe.py << printf <yourbibtexentry>```

