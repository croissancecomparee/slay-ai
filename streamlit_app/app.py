import streamlit as st
import requests
import pandas as pd

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