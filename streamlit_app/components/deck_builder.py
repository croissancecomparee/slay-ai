import streamlit as st
from api import get_card_score

def render_deck_builder(cards):
    st.subheader("🃏 Available Cards")

    search = st.text_input("Search card")

    filtered_cards = [
        c for c in cards
        if search.lower() in c["name"].lower()
    ]

    for card in filtered_cards:
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

        col1.write(f"{card['name']} (cost: {card['cost']}) [{card['type_card']}]")
        # col1.write(f"Score: {get_card_score(card['name'])}")

        if col2.button("+", key=f"add_{card['name']}"):
            st.session_state.deck[card["name"]] = \
                st.session_state.deck.get(card["name"], 0) + 1

        if col3.button("-", key=f"remove_{card['name']}"):
            if card["name"] in st.session_state.deck:
                st.session_state.deck[card["name"]] -= 1
                if st.session_state.deck[card["name"]] <= 0:
                    del st.session_state.deck[card["name"]]

        if col4.button("ℹ️", key=f"info_{card['name']}"):
            st.session_state.selected_card = card["name"]