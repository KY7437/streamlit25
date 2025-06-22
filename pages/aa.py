import streamlit as st
import random

st.title("Memorization of the Text")
st.write("Fill in the blanks directly in the passage below. If you don't know the word, leave it empty.")

# Text passage
text = """In the small town of Willowby, there stood an old library that was rumored to be enchanted. Every night at midnight, the books inside would whisper stories to each other, bringing their characters to life. One evening, Sarah, a curious 15-year-old book lover, decided to sneak into the library to see if the rumors were true.

As the clock struck twelve, the books began to rustle. To Sarah's amazement, characters stepped out of their pages. She met Alice from Wonderland, the White Rabbit, and even pirates from Treasure Island. They invited her to join their midnight council, where they discussed the tales of their adventures and the wisdom they contained.

Sarah spent the whole night listening and learning from the characters, promising to keep their secret. As dawn approached, they returned to their pages. Sarah left the library, inspired and filled with stories to tell, forever changed by the magic of the Midnight Library.
"""

# Difficulty selection
difficulty = st.selectbox("Select Difficulty", ["Easy", "Normal", "Hard"])

# Set blank ratio based on difficulty
blank_ratio = {"Easy": 0.15, "Normal": 0.30, "Hard": 0.50}[difficulty]

# Split text into words and create blanks
words = text.split()
num_blanks = int(len(words) * blank_ratio)
blank_indices = sorted(random.sample(range(len(words)), num_blanks))

# Process words to create blanks and collect user inputs
answer_words = []
processed_words = []
user_inputs = {}

for i, word in enumerate(words):
    if i in blank_indices:
        stripped = word.strip(".,!?;:")
        suffix = word[len(stripped):]
        answer_words.append(stripped)
        # Create a text input for each blank
        user_input = st.text_input(f"Blank {len(answer_words)}", key=f"blank_{i}")
        user_inputs[i] = user_input.strip()
        processed_words.append(f"({len(answer_words)}){suffix}")
    else:
        processed_words.append(word)

# Display the text with placeholders
st.markdown(" ".join(processed_words))

# Check answers when user submits
if st.button("Submit"):
    st.subheader("Check Your Answers")
    for idx, (i, correct) in enumerate(zip(blank_indices, answer_words)):
        user = user_inputs.get(i, "")
        if correct.lower() == user.lower():
            st.markdown(f"✅ **Blank {idx+1} ({user})** (Correct)")
        else:
            st.markdown(f"❌ **Blank {idx+1} ({user})** → Correct answer: **{correct}**")

    # Calculate and display the score
    score = sum([correct.lower() == user_inputs[i].lower() for i, correct in zip(blank_indices, answer_words)])
    st.success(f"Correct Answers: {score} / {len(answer_words)}")

