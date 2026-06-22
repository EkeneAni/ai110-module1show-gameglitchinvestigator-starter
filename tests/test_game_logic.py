from logic_utils import check_guess, update_score

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

def test_too_high_guess_directs_lower():
    """A guess above the secret must tell the player to go LOWER.

    Targets the fixed bug where a "Too High" guess was incorrectly
    telling the player to "Go HIGHER".
    """
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message
    assert "HIGHER" not in message


def test_too_low_guess_directs_higher():
    """A guess below the secret must tell the player to go HIGHER.

    The mirror case of the same direction bug.
    """
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message
    assert "LOWER" not in message


def test_guess_above_range_is_rejected():
    """A guess above the high bound is flagged Out of Range, not compared."""
    outcome, _ = check_guess(99, 25, low=1, high=50)
    assert outcome == "Out of Range"


def test_guess_below_range_is_rejected():
    """A guess below the low bound is flagged Out of Range, not compared."""
    outcome, _ = check_guess(0, 25, low=1, high=50)
    assert outcome == "Out of Range"


def test_range_bounds_are_inclusive():
    """The low and high bounds themselves are valid, playable guesses."""
    assert check_guess(1, 25, low=1, high=50)[0] == "Too Low"
    assert check_guess(50, 25, low=1, high=50)[0] == "Too High"


def test_no_range_args_skips_range_check():
    """Omitting low/high preserves the original two-argument behavior."""
    assert check_guess(999, 50)[0] == "Too High"


def test_win_on_first_attempt_scores_full():
    """Winning on the first guess awards the full 100 points."""
    assert update_score(0, "Win", 1) == 100


def test_win_reward_decreases_with_attempts():
    """Each extra attempt reduces the win reward by 10, floored at 10."""
    assert update_score(0, "Win", 2) == 90
    assert update_score(0, "Win", 11) == 10   # would be negative; floored at 10
    assert update_score(0, "Win", 50) == 10


def test_wrong_guess_always_penalizes():
    """Both Too High and Too Low cost 5, regardless of attempt parity."""
    assert update_score(20, "Too High", 2) == 15
    assert update_score(20, "Too High", 3) == 15
    assert update_score(20, "Too Low", 4) == 15


def test_score_never_goes_negative():
    """A penalty that would drop the score below 0 is clamped to 0."""
    assert update_score(0, "Too High", 1) == 0
    assert update_score(3, "Too Low", 1) == 0
