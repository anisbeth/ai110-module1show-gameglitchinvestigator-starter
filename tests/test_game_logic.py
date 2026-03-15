from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)


def test_get_range_for_easy():
    assert get_range_for_difficulty("Easy") == (1, 20)


def test_get_range_for_normal():
    assert get_range_for_difficulty("Normal") == (1, 50)


def test_get_range_for_hard():
    assert get_range_for_difficulty("Hard") == (1, 100)


def test_parse_guess_valid_integer():
    ok, value, err = parse_guess("42")
    assert ok is True
    assert value == 42
    assert err is None


def test_parse_guess_empty():
    ok, value, err = parse_guess("")
    assert ok is False
    assert value is None
    assert err == "Enter a guess."


def test_parse_guess_invalid_text():
    ok, value, err = parse_guess("abc")
    assert ok is False
    assert value is None
    assert err == "That is not a whole number."


def test_check_guess_win():
    outcome, message = check_guess(25, 25)
    assert outcome == "Win"
    assert "Correct" in message


def test_check_guess_too_high_returns_lower_hint():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_check_guess_too_low_returns_higher_hint():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_update_score_win():
    assert update_score(0, "Win", 1) == 100


def test_update_score_wrong_guess():
    assert update_score(20, "Too High", 2) == 15
    assert update_score(20, "Too Low", 2) == 15