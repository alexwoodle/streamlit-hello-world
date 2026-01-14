import streamlit as st

# st.markdown(
#     """
#     <style>
#     [data-testid="stToolbar"] {
#         visibility: hidden;
#         height: 0;
#         position: fixed;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )


def home():
    st.title("Home")


pg = st.navigation([home, "pages/page_1.py", "pages/page_2.py"])
pg.run()
