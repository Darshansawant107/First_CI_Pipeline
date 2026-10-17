import importlib

module = importlib.import_module("22_anagram_strings")
is_anagram = module.is_anagram


def test_simple_anagram():
    assert is_anagram("listen", "silent") is True


def test_case_is_ignored():
    assert is_anagram("Listen", "Silent") is True


def test_spaces_are_ignored():
    assert is_anagram("conversation", "voices rant on") is True


def test_different_strings():
    assert is_anagram("hello", "world") is False


def test_same_string():
    assert is_anagram("python", "python") is True