import streamlit as st

def render_deck():
    st.subheader("📦 Your Deck")

    total_cards = sum(item["count"] for item in st.session_state.deck.values())
    st.metric("Total cards", total_cards)

    for card_name in st.session_state.deck:
        # card = st.session_state.deck[card_name]["card"]
        count = st.session_state.deck[card_name]["count"]
        st.write(f"{card_name} x{count}")