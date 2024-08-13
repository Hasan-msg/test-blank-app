import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)


from shiny.express import ui

ui.page_opts(title = "Title")

with ui.sidebar():
    "Sidebar (input)"

"Main content (output)"