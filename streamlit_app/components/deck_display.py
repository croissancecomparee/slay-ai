import streamlit as st

def render_deck():
    st.subheader("📦 Your Deck")

    total_cards = sum(st.session_state.deck.values())
    st.metric("Total cards", total_cards)

    for card, count in st.session_state.deck.items():
        st.write(f"{card} x{count}")