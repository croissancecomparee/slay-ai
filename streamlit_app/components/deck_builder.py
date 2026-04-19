import textwrap
import streamlit as st
from domain.models.card import Card
from api import get_cards_scores
from utils.score_utils import get_score_color
from utils.rarity_color import get_rarity_color
from utils.type_icon import get_type_icon

def render_deck_builder(cards):
    st.subheader("🃏 Available Cards")

    search = st.text_input("Search card")

    use_upgraded = st.toggle("Use upgraded cards", value=False)

    if use_upgraded:
        st.info("Showing upgraded cards (+)")

    cards = [Card(**c) for c in cards]
    print("cards", cards)

    filtered_cards = [
        c for c in cards
        if search.lower() in c.name.lower()
    ]

    rarity_filter = st.selectbox(
        "Filter by rarity",
        ["all", "starter", "common", "uncommon", "rare"]
    )

    filtered_cards = [
        c for c in filtered_cards
        if rarity_filter == "all" or c.rarity == rarity_filter
    ]

    filtered_cards = [
        card.resolve(upgraded=use_upgraded)
        for card in filtered_cards
    ]
    # print(filtered_cards)
    print("[card.to_dict() for card in filtered_cards]", [card.to_dict() for card in filtered_cards])
    scores = get_cards_scores([card.to_dict() for card in filtered_cards])
    print("scores", scores)
    
    if not scores:
        st.error("Score API failed")
        return

    sort_by_score = st.checkbox("Sort by score")

    if sort_by_score:
        filtered_cards.sort(
            key=lambda c: scores.get(c.name, 0),
            reverse=True
        )

    for card in filtered_cards:
        col1, col2, col3, col4 = st.columns([3, 1, 1, 1])

        name_display = card.name #+ ("+" if use_upgraded else "")

        print("card.name", card.name)
        print("name_display", name_display)

        # on récupère les attributs de la carte pour les afficher
        score = scores.get(card.name, "N/A")
        color = get_score_color(score)
        rarity_color = get_rarity_color(card.rarity)
        icon = get_type_icon(card.type_card)

        # Affichage du nom de la carte, de son coût, de son type et de son score avec une couleur correspondante
        html = textwrap.dedent(f"""
        <div style="border-left: 4px solid {rarity_color};
            padding-left: 8px;
            display:flex;
            align-items:center;
            justify-content:space-between;
        ">
            <div style="display:flex; align-items:center; gap:8px;">
                <span style="font-size:18px;">{icon}</span>
                <span style="font-weight:bold;">
                    {name_display} (cost: {card.cost})
                </span>
            </div>

        </div>

        <div style="margin-left:8px;">
            <span style="color:{color}; font-weight:bold">
                Score: {score}
            </span>
        </div>
        """)

        col1.markdown(html, unsafe_allow_html=True)

        if col2.button("+", key=f"add_{name_display}"):
            st.session_state.deck[name_display] = \
                st.session_state.deck.get(name_display, 0) + 1

        if col3.button("-", key=f"remove_{name_display}"):
            if name_display in st.session_state.deck:
                st.session_state.deck[name_display] -= 1
                if st.session_state.deck[name_display] <= 0:
                    del st.session_state.deck[name_display]

        if col4.button("ℹ️", key=f"info_{card.name}"):
            st.session_state.selected_card = card.name