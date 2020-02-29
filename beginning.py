from ui import ask

camp = ask(
            [
                ["resistance", "revolte", "rebellion", "résistant"],
                ["reine", "lydia", "von hardenberg", "royaume"],
            ], 
            'Veuillez choisir un camp !'
        )

if camp == "reine":
    import story.queen_side
else:
    import story.resistance_side
