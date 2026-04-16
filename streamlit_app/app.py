import streamlit as st
import requests
import pandas as pd

st.title("Slay The Spire Deck Analyzer")

col_left, col_right = st.columns([2, 1])

if "deck" not in st.session_state:
    st.session_state.deck = {}

# oour le moment on ne fait rien avec le personnage, mais on pourrait l'utiliser pour filtrer les cartes disponibles ou pour donner des conseils spécifiques à ce personnage.
selected_character = st.selectbox(
    "Choose character",
    ["ironclad", "silent"]
)


# get all the cards
response = requests.get("http://localhost:8000/cards")
cards = response.json()

# Liste des cartes:
with col_left:
    st.subheader("🃏 Available Cards")

    search = st.text_input("Search card")

    filtered_cards = [
        c for c in cards
        if search.lower() in c["name"].lower()
    ]

    for card in filtered_cards:
        col1, col2, col3 = st.columns([3, 1, 1])

        col1.write(f"{card['name']} (cost: {card['cost']}) [{card['type_card']}]")

        if col2.button("+", key=f"add_{card['name']}"):
            st.session_state.deck[card["name"]] = \
                st.session_state.deck.get(card["name"], 0) + 1

        if col3.button("-", key=f"remove_{card['name']}"):
            if card["name"] in st.session_state.deck:
                st.session_state.deck[card["name"]] -= 1
                if st.session_state.deck[card["name"]] <= 0:
                    del st.session_state.deck[card["name"]]


# Deck actuel du joueur:
with col_right:
    st.subheader("📦 Your Deck")

    total_cards = sum(st.session_state.deck.values())
    st.metric("Total cards", total_cards)

    for card, count in st.session_state.deck.items():
        st.write(f"{card} x{count}")

deck_list = []

for card, count in st.session_state.deck.items():
    deck_list.extend([card] * count)

# card_names = [c["name"] for c in cards]

# # on choisi le nombre de cartes:
# deck_dict = {}

# st.subheader("Build your deck")

# for card in card_names:
#     count = st.number_input(
#         f"{card}",
#         min_value=0,
#         max_value=10,
#         step=1,
#         key=card
#     )
#     if count > 0:
#         deck_dict[card] = count

# deck = []
# for card, count in deck_dict.items():
#     deck.extend([card] * count)
# deck = st.multiselect("Select cards for your deck", card_names)
# deck_input = st.text_area("Enter your deck (one card name per line)\n" \
# "separated by commas\n" \
# "Strike, Defend, Bash, etc.")

if st.button("Analyze Deck"):

    # split the input into a list of card names
    # deck = [card.strip() for card in deck_input.split(",")]

    # send the deck to the API for analysis
    response = requests.post("http://localhost:8000/deck/analyze", json=deck_list)

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