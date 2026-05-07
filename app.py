import streamlit as st

st.title("Anime Recommendation System")

anime = st.selectbox(
    "Choose Anime",
    ["Naruto", "One Piece", "Death Note"]
)

if st.button("Recommend"):
    st.write("Recommended Anime:")
    st.write("Attack on Titan")
    st.write("Demon Slayer")