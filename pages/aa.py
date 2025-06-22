import streamlit as st
import random

st.title("Memorization of the Text")
st.write("Fill in the blanks directly in the passage. If you don't know the word, please leave it empty.")

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

# Process words to create blanks
answer_words = []
processed_words = []
for i, word in enumerate(words):
    if i in blank_indices:
        stripped = word.strip(".,!?;:")
        suffix = word[len(stripped):]
        answer_words.append(stripped)
        blank = f"<input id='blank_{i}' style='width: 100px;' type='text'/>"
        processed_words.append(f"{blank}{suffix}")
    else:
        processed_words.append(word)

# Display text with blanks using HTML
st.markdown(" ".join(processed_words), unsafe_allow_html=True)

# Collect user input for each blank
user_answers = []
for i in blank_indices:
    user_input = st.text_input(f"Word for position {i + 1}", key=f"blank_input_{i}")
    user_answers.append(user_input.strip())

# Check answers when user submits
if st.button("Submit"):
    st.subheader("Check Your Answers")
    for idx, (correct, user) in enumerate(zip(answer_words, user_answers)):
        if correct.lower() == user.lower():
            st.markdown(f"✅ **{idx+1}. {user}** (Correct)")
        else:
            st.markdown(f"❌ **{idx+1}. {user}** → Correct answer: **{correct}**")

    # Calculate and display the score
    score = sum([correct.lower() == user.lower() for correct, user in zip(answer_words, user_answers)])
    st.success(f"Correct Answers: {score} / {len(answer_words)}")
