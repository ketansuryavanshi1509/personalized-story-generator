from transformers import pipeline  # type: ignore

def remove_repeated_sentences(text):
    seen = set()
    result = []
    for sentence in text.split('. '):
        clean_sentence = sentence.strip()
        if clean_sentence not in seen:
            seen.add(clean_sentence)
            result.append(clean_sentence)
    return '. '.join(result) + '.'


def generate_story(name, age, animal, theme, length):
    # Create a structured, repetition-resistant prompt
    prompt = (
        f"Write a {length} {theme.lower()} story for a {age}-year-old child named {name}. "
        f"The story should include a {animal} as a friend. "
        f"Make sure the story has 3 parts:\n"
        f"1. Beginning – introduce {name} and where they live.\n"
        f"2. Middle – describe their adventure with the {animal}.\n"
        f"3. Ending – how the adventure ends happily.\n"
        f"Use simple, age-appropriate words. Avoid repeating the same sentence."
    )

    # Load the FLAN-T5 model
    generator = pipeline(
        "text2text-generation",
        model="google/flan-t5-large"
    )

    # Generate the story
    raw_output = generator(
        prompt,
        max_new_tokens=512
    )[0]['generated_text']

    # Clean repeated lines
    cleaned_story = remove_repeated_sentences(raw_output)

    return cleaned_story
