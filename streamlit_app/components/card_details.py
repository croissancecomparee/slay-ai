import streamlit as st
from api import get_card, get_card_score
from utils.string import slugify_card_name

def render_card_details():
    if st.session_state.selected_card:
        st.subheader(f"📖 {st.session_state.selected_card}")

        card = get_card(st.session_state.selected_card)
        card_score = get_card_score(st.session_state.selected_card)

        st.write(f"**Cost:** {card['cost']}")
        st.write(f"**Type:** {card['type_card']}")
        st.write(f"**Description:** {card['description']}")
        st.write(f"**Score:** {card_score['score']}")
        st.write("**Stats:**")
        st.write(f"Damage: {card['damage']}")
        st.write(f"Block: {card['block']}")
        st.write(f"Draw: {card['draw']}")

        st.write("**Tags:**", ", ".join(card["tags"]))

        url_name = slugify_card_name(card["name"])

        st.markdown(
                f"[View on wiki SS1](https://slay-the-spire.fandom.com/wiki/{url_name})"
            )
        st.markdown(
                f"[View on wiki SS2](https://slaythespire.wiki.gg/wiki/Slay_the_Spire_2:{url_name})"
            )


        if "upgraded" in card:
            st.write("🔼 **Upgraded version:**")
            st.write(card["upgraded"])