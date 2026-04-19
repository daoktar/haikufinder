# haikufinder

A Python hack to find "haikus" in English text. For the purposes of this
module, a "haiku" is one or more complete sentences that, together, can be
broken into groups of **5, 7, and 5 syllables**. Each candidate haiku line,
and then the entire haiku, has to make it through a few heuristics to filter
out constructions that are likely to scan awkwardly (like verb phrases split
across lines). Since this code doesn't really try to understand the texts,
it might throw away a few legitimate phrases, and it certainly lets through
some bad ones.

## Requirements

- Python **3.11+** (tested on 3.11, 3.12, 3.13)
- [NLTK](https://www.nltk.org/) 3.9 or newer

## Installation

```
pip install .
python -m nltk.downloader punkt_tab cmudict
```

For older NLTK (< 3.9), use `punkt` instead of `punkt_tab`.

## Command-line usage

Once installed, a `findhaikus` script is on your `PATH`:

```
findhaikus ulysses.txt
```

Or pipe text on stdin:

```
cat ulysses.txt | findhaikus
```

## Library usage

```python
from haikufinder import HaikuFinder

with open("ulysses.txt", encoding="utf-8") as f:
    text = f.read()

for haiku in HaikuFinder(text).find_haikus():
    print(haiku[0])
    print("    %s" % haiku[1])
    print(haiku[2])
    print()
```

If `haikufinder` doesn't recognize a word you're using, or is counting its
syllables incorrectly, extend the in-memory dictionary:

```python
from haikufinder import HaikuFinder

HaikuFinder.add_word("shmeggegge", 3)
HaikuFinder.add_word("kvetch", 1)
haikus = HaikuFinder(
    "For this I should stay? To hear some shmeggegge kvetch about his lawsuit?"
).find_haikus()
```

For a permanent change, add the word to `haikufinder/cmudict/custom.dict` in
the form `WORD SYLLABLE_COUNT` (one per line) and submit a pull request.

## Regenerating the syllable dictionary

The CMU Pronouncing Dictionary is shipped as a pickle at
`haikufinder/cmudict/cmudict.pickle`. To rebuild it from the NLTK corpus:

```
python -m nltk.downloader cmudict
python haikufinder/cmudict/PickleCMUDict.py
```

## Development

```
pip install -e '.[dev]'
python -m nltk.downloader punkt_tab cmudict
pytest -q
```

## License

"Modified BSD" (BSD 3-Clause). See [`license.txt`](license.txt).
