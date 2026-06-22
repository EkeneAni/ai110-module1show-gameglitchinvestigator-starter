def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
    return 1, 100


def parse_guess(raw: str):
    """
    Turn the raw user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret, low=None, high=None):
    """
    Compare guess to secret and return (outcome, message).

    If low and high are provided, a guess outside the inclusive [low, high]
    range is rejected with an "Out of Range" outcome before any comparison.

    outcome examples: "Win", "Too High", "Too Low", "Out of Range"
    """
    if low is not None and high is not None and not (low <= guess <= high):
        return "Out of Range", f"🚫 Enter a number between {low} and {high}."

    if guess == secret:
        return "Win", "🎉 Correct!"

    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Update score based on outcome and attempt number.

    A win rewards fewer attempts (100 on the first guess, dropping by 10
    each attempt, floored at 10). A wrong guess always costs 5 points,
    regardless of direction. The score never drops below 0.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        if points < 10:
            points = 10
        new_score = current_score + points
    elif outcome in ("Too High", "Too Low"):
        new_score = current_score - 5
    else:
        new_score = current_score

    return max(0, new_score)
