import genanki

# Create the Anki model (flashcard template)
model = genanki.Model(
    1607392319,
    "Major System Memory",
    fields=[
        {"name": "Number"},
        {"name": "Word"},
        {"name": "Phonetic Breakdown"},
    ],
    templates=[
        {
            "name": "Major System Card",
            "qfmt": "<h2>{{Number}}</h2>",
            "afmt": """
            <h2>{{Number}}</h2>
            <b>Word:</b> {{Word}} <br>
            <b>Phonetic Breakdown:</b> {{Phonetic Breakdown}} <br>
            """,
        }
    ],
)

# Major System word list (1-100)
major_system_words = {
    1: ("Tea", "T"),
    2: ("Noah", "N"),
    3: ("Ma", "M"),
    4: ("Ray", "R"),
    5: ("Law", "L"),
    6: ("Shoe", "Sh"),
    7: ("Cow", "K"),
    8: ("Ivy", "V"),
    9: ("Bee", "B"),
    10: ("Dice", "D-S"),
    11: ("Dot", "D-T"),
    12: ("Dan", "D-N"),
    13: ("Dam", "D-M"),
    14: ("Deer", "D-R"),
    15: ("Doll", "D-L"),
    16: ("Dish", "D-Sh"),
    17: ("Duck", "D-K"),
    18: ("Dove", "D-V"),
    19: ("Tape", "T-P"),
    20: ("Nose", "N-S"),
    21: ("Net", "N-T"),
    22: ("Nun", "N-N"),
    23: ("Name", "N-M"),
    24: ("Nero", "N-R"),
    25: ("Nail", "N-L"),
    26: ("Notch", "N-Ch"),
    27: ("Neck", "N-K"),
    28: ("Knife", "N-F"),
    29: ("Nap", "N-P"),
    30: ("Mouse", "M-S"),
    31: ("Mat", "M-T"),
    32: ("Moon", "M-N"),
    33: ("Mummy", "M-M"),
    34: ("Mare", "M-R"),
    35: ("Mail", "M-L"),
    36: ("Match", "M-Ch"),
    37: ("Mug", "M-K"),
    38: ("Muff", "M-F"),
    39: ("Map", "M-P"),
    40: ("Rose", "R-S"),
    41: ("Rat", "R-T"),
    42: ("Rain", "R-N"),
    43: ("Ram", "R-M"),
    44: ("Roar", "R-R"),
    45: ("Roll", "R-L"),
    46: ("Roach", "R-Ch"),
    47: ("Rock", "R-K"),
    48: ("Roof", "R-F"),
    49: ("Rope", "R-P"),
    50: ("Lasso", "L-S"),
    51: ("Lid", "L-D"),
    52: ("Lion", "L-N"),
    53: ("Lime", "L-M"),
    54: ("Lure", "L-R"),
    55: ("Lily", "L-L"),
    56: ("Leech", "L-Ch"),
    57: ("Log", "L-K"),
    58: ("Lava", "L-V"),
    59: ("Lip", "L-P"),
    60: ("Chess", "Ch-S"),
    61: ("Sheet", "Sh-T"),
    62: ("Chain", "Ch-N"),
    63: ("Jam", "J-M"),
    64: ("Chair", "Ch-R"),
    65: ("Jail", "J-L"),
    66: ("Judge", "J-J"),
    67: ("Chalk", "Ch-K"),
    68: ("Chef", "Sh-F"),
    69: ("Jeep", "J-P"),
    70: ("Case", "K-S"),
    71: ("Cat", "K-T"),
    72: ("Can", "K-N"),
    73: ("Comb", "K-M"),
    74: ("Car", "K-R"),
    75: ("Coal", "K-L"),
    76: ("Cage", "K-J"),
    77: ("Coke", "K-K"),
    78: ("Cave", "K-V"),
    79: ("Cap", "K-P"),
    80: ("Face", "F-S"),
    81: ("Fat", "F-T"),
    82: ("Fan", "F-N"),
    83: ("Foam", "F-M"),
    84: ("Fur", "F-R"),
    85: ("File", "F-L"),
    86: ("Fish", "F-Sh"),
    87: ("Fig", "F-K"),
    88: ("Fife", "F-F"),
    89: ("Fib", "F-B"),
    90: ("Bus", "B-S"),
    91: ("Bat", "B-T"),
    92: ("Bone", "B-N"),
    93: ("Bomb", "B-M"),
    94: ("Bear", "B-R"),
    95: ("Bell", "B-L"),
    96: ("Bush", "B-Sh"),
    97: ("Book", "B-K"),
    98: ("Beef", "B-F"),
    99: ("Pipe", "P-P"),
    100: ("Daisy", "D-S"),
}

# Create the Anki deck
deck = genanki.Deck(2059400110, "Major System (1-100)")

# Add flashcards
for num, (word, phonetic) in major_system_words.items():
    note = genanki.Note(
        model=model,
        fields=[str(num), word, phonetic]
    )
    deck.add_note(note)

# Save the deck to a file
genanki.Package(deck).write_to_file("Major_System_1-100.apkg")

print("Anki deck created: Major_System_1-100.apkg")


