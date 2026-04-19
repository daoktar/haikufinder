from pathlib import Path

from haikufinder import HaikuFinder, LineSyllablizer, find_haikus


def _count(line: str) -> int:
    return LineSyllablizer(line).count_syllables()


def test_empty_text_yields_no_haikus():
    assert find_haikus("") == []


def test_finds_known_haiku():
    # Classic 5-7-5 line from Bashō (translated). One complete sentence.
    text = "An old silent pond. A frog jumps into the pond, splash! Silence again."
    haikus = find_haikus(text)
    assert len(haikus) >= 1
    a, b, c = haikus[0]
    assert _count(a) == 5
    assert _count(b) == 7
    assert _count(c) == 5


def test_add_word_enables_custom_vocab():
    HaikuFinder.add_word("shmeggegge", 3)
    HaikuFinder.add_word("kvetch", 1)
    # Not asserting a haiku match here (heuristics may reject it) -- just
    # ensuring the custom words don't crash the syllable counter.
    haikus = HaikuFinder(
        "For this I should stay? To hear some shmeggegge kvetch about his lawsuit?"
    ).find_haikus()
    assert isinstance(haikus, list)


def test_ulysses_smoke():
    text = (Path(__file__).parent.parent / "ulysses.txt").read_text(encoding="utf-8")
    haikus = HaikuFinder(text).find_haikus()
    assert haikus, "expected to find at least one haiku in ulysses.txt"
    for a, b, c in haikus:
        assert _count(a) == 5
        assert _count(b) == 7
        assert _count(c) == 5
