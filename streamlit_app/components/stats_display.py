import streamlit as st
import pandas as pd

def render_stats(stats):
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

    df = pd.DataFrame({
        "Type": ["Attack", "Skill", "Power"],
        "Count": [
            stats["attack_count"],
            stats["skill_count"],
            stats["power_count"],
        ]
    })

    st.bar_chart(df.set_index("Type"))

    st.subheader("🧪 Tags")

    for tag, count in stats["tags"].items():
        st.write(f"{tag}: {count}")