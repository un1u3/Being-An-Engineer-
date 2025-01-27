# Function to create a Mad Lib
def madlib_generator():
    print("Welcome to the Mad Libs Generator!")

    # Template for the Mad Lib
    story = """
    Once upon a time, there was a [adjective] [noun] who loved to [verb]. 
    One day, the [noun] found a [adjective] treasure chest full of [plural_noun]. 
    Excited, the [noun] decided to [verb] all day long. 
    It was truly a [adjective] adventure!
    """


    # Words the user will provide
    placeholders = ["adjective", "noun", "verb", "plural_noun"]

    # Dictionary to store user inputs
    user_inputs = {}

    # Ask user for inputs
    for placeholder in placeholders:
        user_inputs[placeholder] = input(f"Enter a {placeholder}: ")

    # Replace placeholders with user inputs
    for key, value in user_inputs.items():
        story = story.replace(f"[{key}]", value)

    # Print the final story
    print("\nHere's your Mad Lib story:")
    print(story)


# Run the Mad Lib generator
madlib_generator()
