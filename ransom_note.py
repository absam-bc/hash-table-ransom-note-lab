def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Check whether ransomNote can be built using letters from magazine.
    Each letter from magazine can only be used once.
    """

    # Store how many times each character appears in magazine.
    letter_counts = {}

    for letter in magazine:
        if letter in letter_counts:
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    # Check whether each letter in ransomNote is available.
    for letter in ransomNote:
        if letter not in letter_counts or letter_counts[letter] == 0:
            return False

        # Use one occurrence of this letter.
        letter_counts[letter] -= 1

    return True
