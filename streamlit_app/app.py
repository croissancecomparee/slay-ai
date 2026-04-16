import streamlit as st
import requests

st.title("Slay The Spire Deck Analyzer")

# input for the deck
deck_input = st.text_area("Enter your deck (one card name per line)" \
"separated by commas" \
"Strike, Defend, Bash, etc.")

if st.button("Analyze Deck"):
    # split the input into a list of card names
    deck = [card.strip() for card in deck_input.split(",")]

    # send the deck to the API for analysis
    response = requests.post("http://localhost:8000/deck/analyze", json=deck)

    if response.status_code == 200:
        stats = response.json()
        st.write("Deck Statistics:")
        st.write(f"Size: {stats['size']}")
        st.write(f"Attack Cards: {stats['attack_count']}")
        st.write(f"Skill Cards: {stats['skill_count']}")
        st.write(f"Power Cards: {stats['power_count']}")
        st.write(f"Average Cost: {stats['avg_cost']}")
        st.write(f"Total Damage: {stats['total_damage']}")
        st.write(f"Total Block: {stats['total_block']}")
        st.write(f"Cards to Draw: {stats['draw_count']}")
        st.write("Tags:")
        for tag, count in stats["tags"].items():
            st.write(f"{tag}: {count}")
    else:
        st.error("Error analyzing deck. Please try again.")