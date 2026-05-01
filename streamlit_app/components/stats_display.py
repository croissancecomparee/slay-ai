import streamlit as st
import pandas as pd

from utils.score_utils import get_score_color

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

    # Score display


    color = get_score_color(stats["avg_score"])

    st.markdown(
        f"""
        <h3>⭐ Deck Score</h3>
        <p style="font-size:20px;">
            Average score:
            <span style="color:{color}; font-weight:bold;">
                {stats["avg_score"]}
            </span>
        </p>
        """,
        unsafe_allow_html=True
    )

    best = stats["best_card"]
    worst = stats["worst_card"]

    best_color = get_score_color(best["score"])
    worst_color = get_score_color(worst["score"])

    st.markdown(
        f"""
        <p>
            🏆 Best card:
            <span style="color:{best_color}; font-weight:bold;">
                {best["name"]} ({best["score"]})
            </span>
        </p>

        <p>
            💀 Worst card:
            <span style="color:{worst_color}; font-weight:bold;">
                {worst["name"]} ({worst["score"]})
            </span>
        </p>
        """,
        unsafe_allow_html=True
    )

    df_scores = pd.DataFrame(stats["card_scores"])
    df_scores = df_scores.sort_values(by="score", ascending=False)
    st.bar_chart(df_scores.set_index("name"))