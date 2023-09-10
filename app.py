import streamlit as st
from fastapi import requests
from typing import Union

MAX_LENGTH = 1024


def set_page_config():
    st.set_page_config(
        page_title="NewsLingo - Multi Language Site Scraper",
        page_icon="🌎",
        layout="centered",
    )


st.header = "NewsLingo - Multi Language Site Scraper"


#  Unsupported, may break if the app changes. adjust the style of side bar to keep the page options at the top
st.markdown(
    """
<style>
.css-1oe5cao {
    max-height: 10vh;
    list-style: none;
    overflow: overlay;
    margin: 0px;
    padding: 0px;
    padding-top: 0rem;
    padding-bottom: 0rem;
}
</style>
""",
    unsafe_allow_html=True,
)


st.title("Xinhua News Translation to Google Sheets")
st.write(
    "Translate important Xinhua News headlines into your language and update a Google Sheet."
)

language = (
    st.selectbox(
        "Target Language",
        ["English", "Spanish", "French", "German", "Cantonese"],
        index=4,
        placeholder="To",
    )
    or "English"
)

source_language = (
    st.selectbox(
        "Source Language",
        ["English", "Spanish", "French", "German", "Cantonese"],
        index=4,
        placeholder="From",
    )
    or "Cantonese"
)

language_map = {
    "English": "eng",
    "Spanish": "spa",
    "French": "fra",
    "German": "deu",
    "Cantonese": "yue",
}


def display_articles(articles: str) -> None:
    ticker = 0
    sort = {}
    for article in articles:
        head, article = article.split("/n/n")
        ticker += 1
        if ticker >= 4:
            ticker = 3
        sort[ticker] = {article: head}
    for tick in sort:
        col1, col2, col3 = st.columns(3)
        st.header(tick[1]["head"])
        col1.write(tick[1]["article"])
        st.header(tick[2]["head"])
        col2.write(tick[2]["article"])
        st.header(tick[3]["head"])
        col3.write(tick[3]["article"])


def request_headlines(url, headline_url: str):
    response = requests.get(url, body={"url": headline_url})
    return response.text


with st.sidebar:
    url = st.text_area("Input url", "", height=100)
    if not url.startswith("http"):
        url = f"http://{url}"
    if not url:
        raise ValueError("No URL provided.")

    translated_headlines = ""
    if st.button("Translate & Update"):
        translated_headlines = request_headlines(url, headline_url=url)
        if not translated_headlines:
            raise ValueError("No headlines found.")

    display_articles(articles=translated_headlines)
