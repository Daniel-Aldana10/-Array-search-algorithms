
## Coverage

Make sure you have "coverage" in your requirements.txt file and run pip install. Then run `python -m coverage run -m unittest discover` and after that run `python -m coverage report` to get the following table:
```
Name                          Stmts   Miss  Cover
-------------------------------------------------
array_search\algorithms.py       36      2    94%
data\constants.py                 2      0   100%
data\data_generator.py            6      1    83%
test\test_algorithms.py          20      1    95%
test\test_data_generator.py      29      1    97%
-------------------------------------------------
TOTAL                            93      5    95%
```
---
If you want to see the lines that are not being used you can run 'python -m cover html' and then 'start htmlcov\index.html'