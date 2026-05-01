import streamlit as st

from api import get_all_cards, analyze_deck
from state import init_state

from components.deck_builder import render_deck_builder
from components.deck_display import render_deck
from components.stats_display import render_stats
from components.card_details import render_card_details

st.title("Slay The Spire Deck Analyzer")

init_state()

cards = get_all_cards()

col_left, col_right = st.columns([2, 1])

with col_left:
    render_deck_builder(cards)

with col_right:
    render_deck()

with st.sidebar:
    render_card_details()

# build deck list
deck_list = []
for card_name, item in st.session_state.deck.items():
    card = item["card"]
    count = item["count"]
    deck_list.extend([card] * count)

if st.button("Analyze Deck"):
    stats = analyze_deck(deck_list)

    if stats:
        render_stats(stats)
    else:
        st.error("Error analyzing deck. Please try again.")
