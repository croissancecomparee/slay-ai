import streamlit as st
import requests
import pandas as pd

st.title("Slay The Spire Deck Analyzer")

# oour le moment on ne fait rien avec le personnage, mais on pourrait l'utiliser pour filtrer les cartes disponibles ou pour donner des conseils spécifiques à ce personnage.
selected_character = st.selectbox(
    "Choose character",
    ["ironclad", "silent"]
)

# input for the deck
response = requests.get("http://localhost:8000/cards")
cards = response.json()

card_names = [c["name"] for c in cards]

# on choisi le nombre de cartes:
deck_dict = {}

st.subheader("Build your deck")

for card in card_names:
    count = st.number_input(
        f"{card}",
        min_value=0,
        max_value=10,
        step=1,
        key=card
    )
    if count > 0:
        deck_dict[card] = count

deck = []
for card, count in deck_dict.items():
    deck.extend([card] * count)
# deck = st.multiselect("Select cards for your deck", card_names)
# deck_input = st.text_area("Enter your deck (one card name per line)\n" \
# "separated by commas\n" \
# "Strike, Defend, Bash, etc.")

if st.button("Analyze Deck"):

    # split the input into a list of card names
    # deck = [card.strip() for card in deck_input.split(",")]

    # send the deck to the API for analysis
    response = requests.post("http://localhost:8000/deck/analyze", json=deck)

    if response.status_code == 200:
        stats = response.json()
        st.subheader("📊 Deck Stats")

        col1, col2 = st.columns(2)

        col1.metric("Size", stats["size"])
        col1.metric("Attack", stats["attack_count"])
        col1.metric("Skill", stats["skill_count"])
        col1.metric("Power", stats["power_count"])

        col2.metric("Avg cost", stats["avg_cost"])
        col2.metric("Damage", stats["total_damage"])
        col2.metric("Block", stats["total_block"])
        col2.metric("Draw", stats["draw_count"])

        st.subheader("🧪 Tags")

        st.write(stats["tags"])
        st.write("Tags:")
        for tag, count in stats["tags"].items():
            st.write(f"{tag}: {count}")

        df = pd.DataFrame({"Type": ["Attack", "Skill", "Power"], "Count": [stats["attack_count"], stats["skill_count"], stats["power_count"],]})

        st.bar_chart(df.set_index("Type"))
        
    else:
        st.error("Error analyzing deck. Please try again.")