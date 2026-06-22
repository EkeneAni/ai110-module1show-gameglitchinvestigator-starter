from logic_utils import check_guess


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
