import streamlit as st
import pandas as pd
from gtts import gTTS
from io import BytesIO
import random

st.write("🌱 Vocabulary learning")

# Define tabs
tab1, tab2, tab3 = st.tabs(["❄️ Word List", "❄️ 2. Wordle", "❄️ 3. Role Playing"])

with tab1:
    st.write("Content for Word List tab goes here.")
    # Add functionality for the Word List tab here

with tab2:
    # Define dictionary of words and their definitions
    words = {
        "magic": "a power that makes strange or wonderful things happen",
        "sneak": "to move quietly so no one can see or hear you",
        "rumor": "a story that people talk about, but it may not be true"
    }

    def compare_words(guess, answer):
        result = []
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                result.append("🟩")  # Correct letter and position
            elif guess[i] in answer:
                result.append("🟨")  # Correct letter wrong position
            else:
                result.append("⬛")  # Letter not in word
        return "".join(result)

    # Initialize session state variables
    if 'answer' not in st.session_state:
        st.session_state.answer = random.choice(list(words.keys()))
        st.session_state.definition = words[st.session_state.answer]
        st.session_state.attempt = 0
        st.session_state.used_letters = set()
        st.session_state.correct = False

    st.title("🎯 Welcome to Wordle!")
    st.write("Guess the 5-letter word. You have 6 attempts.")

    # Input field for user's guess
    guess = st.text_input(f"Attempt {st.session_state.attempt + 1}: Enter your guess:").lower()

    # Process the guess when the user clicks the submit button
    if st.button("Submit") and not st.session_state.correct:
        if len(guess) != 5:
            st.warning("⚠️ Please enter a 5-letter word.")
        elif guess not in words:
            st.warning("⚠️ Please guess one of these words: magic, sneak, rumor")
        else:
            st.session_state.attempt += 1
            feedback = compare_words(guess, st.session_state.answer)
            st.write("Result: ", feedback)

            if guess == st.session_state.answer:
                st.session_state.correct = True
                st.success(f"✅ Correct! The word is '{st.session_state.answer.upper()}'.")
                st.info(f"📘 Meaning: {st.session_state.definition}")
            else:
                for i in range(5):
                    if guess[i] in st.session_state.answer and guess[i] != st.session_state.answer[i]:
                        st.session_state.used_letters.add(guess[i])

                if st.session_state.used_letters:
                    hint_letters = ", ".join(sorted(letter.upper() for letter in st.session_state.used_letters))
                    st.write(f"🔤 Hint letters: {hint_letters}")

    if st.session_state.attempt >= 6 and not st.session_state.correct:
        st.error(f"❌ Sorry, you used all attempts. The word was '{st.session_state.answer.upper()}'.")
        st.info(f"📘 Meaning: {st.session_state.definition}")

with tab3:
    # Grammar example sentence dictionary
    EXPRESSION_DB = {
        "that": {
            "examples": [
                "A: Did you watch the movie that I recommended yesterday?",
                "B: Yes, I did! I loved the part that shows the main character’s childhood.",
                "A: Me too! The scene that made me cry was at the end.",
                "B: Same here. I think it’s a movie that everyone should watch."
            ]
        },
        "be p.p": {
            "examples": [
                "A: Did you hear? Our classroom was cleaned yesterday.",
                "B: Really? It looks so much better now.",
                "A: Yeah, and new computers were installed this morning.",
                "B: That’s great! I heard the old ones were broken last week.",
                "A: Right. The whole room was redesigned by the school’s tech team."
            ]
        }
    }

    # Input expression
    expression = st.text_input("📝 Enter expressions (ex. that, be p.p): ").strip().lower()

    # Output results
    if expression in EXPRESSION_DB:
        data = EXPRESSION_DB[expression]
        st.write("🗣️ Sample sentences:")
        for ex in data["examples"]:
            st.write(f"- {ex}")
    else:
        st.write("⚠️ Please use expressions we used in class!!")
