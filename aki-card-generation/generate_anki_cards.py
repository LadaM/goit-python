import genanki

flashcards = {
    "What is the syntax for slicing a string in Python?": "string[start:end]",
    "How does string slicing work with negative indices?": "Slicing with negative indices counts from the end of the string. For example, string[-3:-1] slices from the 3rd character from the end to the 1st character from the end.",
    "What does string[:3] do?": "It slices the string from the beginning to the 3rd character (exclusive).",
    "How can you slice a string to get every other character?": "You can use the step parameter like this: string[::2].",
    "What happens if you omit the start and end indices in string slicing?": "If you omit both the start and end indices, it slices the entire string.",
    "How do you slice a list in Python?": "The syntax for slicing a list is list[start:end].",
    "What does list[2:5] do?": "It slices the list from the 3rd element to the 5th element (exclusive).",
    "How does list slicing work with negative indices?": "Slicing with negative indices counts from the end of the list. For example, list[-3:-1] slices from the 3rd element from the end to the 1st element from the end.",
    "How can you slice a list to get every other element?": "You can use the step parameter like this: list[::2].",
    "What happens if you omit the start and end indices in list slicing?": "If you omit both the start and end indices, it slices the entire list."
}

# Define Anki note model
model_id = 1607392319
model = genanki.Model(
    model_id,
    'QandA Model',
    fields=[
        {'name': 'Question'},
        {'name': 'Answer'},
    ],
    templates=[
        {
            'name': 'Card 1',
            'qfmt': '{{Question}}',
            'afmt': '{{Answer}}',
        },
        {
            'name': 'Card 2',
            'qfmt': '{{Answer}}',
            'afmt': '{{Question}}',
        },
    ])

# Generate Anki cards and add them to a deck
deck_id = 2059400110
deck = genanki.Deck(deck_id, 'Python generated')

for question, answer in flashcards.items():
    note = genanki.Note(model=model, fields=[question, answer])
    deck.add_note(note)

# Save the deck to an Anki package (*.apkg) file
genanki.Package(deck).write_to_file('flashcards.apkg')