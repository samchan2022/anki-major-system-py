import csv
import genanki

def read_csv_and_add_to_deck(csv_filename, deck, model):
    with open(csv_filename, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Use DictReader to skip the header automatically
        
        for row in reader:
            number = row['Number']
            word = row['Word']
            phonetic = row['Phonetic Breakdown']

            try:
                # Convert number to integer for proper ordering in Anki deck
                number_int = int(number)
            except ValueError:
                print(f"Skipping invalid number: {number}")
                continue

            # Create a note with the fields
            note = genanki.Note(
                model=model,
                fields=[str(number_int), word, phonetic]
            )

            # Add the note to the deck
            deck.add_note(note)

# Anki model setup (your existing setup)
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

# Create the Anki deck
deck = genanki.Deck(2059400110, "Major System (1-100)")

# Call the function with the CSV filename
read_csv_and_add_to_deck("major_system_nouns_phonetic.csv", deck, model)

# Save the deck to a file
genanki.Package(deck).write_to_file("Major_System_1-100.apkg")

print("Anki deck created: Major_System_1-100.apkg")
