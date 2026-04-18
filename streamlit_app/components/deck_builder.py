import streamlit as st
from api import get_cards_scores
from utils.score_utils import get_score_color
from utils.rarity_color import get_rarity_color

def render_deck_builder(cards):
    st.subheader("🃏 Available Cards")

    search = st.text_input("Search card")

    filtered_cards = [
        c for c in cards
        if search.lower() in c["name"].lower()
    ]
    card_names = [c["name"] for c in filtered_cards]
    scores = get_cards_scores(card_names)

    sort_by_score = st.checkbox("Sort by score")

    if sort_by_score:
        filtered_cards.sort(
            key=lambda c: scores.get(c["name"], 0),
            reverse=True
        )

    rarity_filter = st.selectbox(
        "Filter by rarity",
        ["all", "starter", "common", "uncommon", "rare"]
    )

    filtered_cards = [
        c for c in cards
        if rarity_filter == "all" or c["rarity"] == rarity_filter
    ]

    for card in filtered_cards:
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

        score = scores.get(card["name"], "N/A")
        color = get_score_color(score)
        rarity_color = get_rarity_color(card["rarity"])

        # Affichage du nom de la carte, de son coût, de son type et de son score avec une couleur correspondante
        col1.markdown(
            f"""
            <div style="border-left: 4px solid {rarity_color}; padding-left: 8px; display:flex; align-items:center; gap:8px;">
                <span style="font-weight:bold;">{card['name']} (cost: {card['cost']}) [{card['type_card']}]</span>
                <span style="
                    background-color:{rarity_color};
                    color:black;
                    padding:2px 6px;
                    border-radius:6px;
                    font-size:10px;
                ">
                    {card['rarity']}
                </span>
            </div>
            
            <span style='color:{color}; font-weight:bold'>Score: {score}</span>
            """,
            unsafe_allow_html=True
        )

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