from haikufinder import count_syllables


def test_common_words():
    assert count_syllables("haiku") == 2
    assert count_syllables("beautiful") == 3
    assert count_syllables("syllable") == 3
    assert count_syllables("python") == 2


def test_multi_word():
    # "the quick brown fox" -> 1 + 1 + 1 + 1
    assert count_syllables("the quick brown fox") == 4


def test_numbers_and_times():
    # "5:30pm" -> number_syllables[5] + number_syllables[30] + 2 (pm)
    # 5 -> 1, 30 -> 2, pm -> 2 => 5
    assert count_syllables("5:30pm") == 5
    # "3rd" treated as the ordinal for 3 -> 1 syllable
    assert count_syllables("3rd") == 1


def test_dollars():
    # "$12" -> 2 (dollars) + number_syllables[12] (1) => 3
    assert count_syllables("$12") == 3


def test_unknown_word_returns_negative():
    assert count_syllables("zqxjq") == -1


def test_add_word_extends_dictionary():
    from haikufinder import HaikuFinder, count_syllables

    HaikuFinder.add_word("shmeggegge", 3)
    assert count_syllables("shmeggegge") == 3
