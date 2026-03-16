from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"


# MY EDIT targeted: "when NOT ok, don't append guess to history" (app.py line 92-97)
# Before the fix, invalid guesses were still appended to history and counted as attempts.
# This test simulates the conditional logic: only append to history when parse_guess returns ok=True.
def test_invalid_guess_not_added_to_history():
    history = []

    # Simulate submitting an invalid (non-numeric) guess
    ok, guess_int, _ = parse_guess("abc")
    if ok:
        history.append(guess_int)

    # Invalid input should not pollute history
    assert len(history) == 0


def test_valid_guess_added_to_history():
    history = []

    # Simulate submitting a valid guess
    ok, guess_int, _ = parse_guess("42")
    if ok:
        history.append(guess_int)

    # Valid input should be recorded in history
    assert len(history) == 1
    assert history[0] == 42
