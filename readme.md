# Word Search Kata

## About
See: https://github.com/PillarTechnology/kata-word-search

## Requirements
Python 3.x (Python 3.7 was used for development)

## Running
You can import WordSearchSolver in your project, or you can run WordSearchSolver.py from the commandline:
```WordSearchSolver.py <filename>```

The test case "carparts_hard_from_pdf.txt" is copy/pasted from https://www.brainzilla.com/media/wordsearch/pdfs/car-parts-hard.pdf, after which a copule of simple regex replacements in vim were used to put it into the correct format.

### Running Tests
I usually use the built-in unittest framework that Python offers, but for this exercise I decided to try out pytest.  

To run tests you can do:
```setup.py pytest```

...or simply ```pytest``` should also work.

To get coverage, you can do:
```pytest --cov```

...or if you want a nice html report, try: ```pytest --cov --cov-report=html```
