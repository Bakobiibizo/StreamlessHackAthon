import streamlit as st 
from streamlit.config import get_config_options
from translate import process_text
from scraper import extract_text_from_html
from typing import Literal
MAX_LENGTH = 1024


def translate_headlines(headlines: str, language: str, target_lang: str="eng"):
    translated_headlines = {}
    translation = ""
    for headline in headlines:
        if len(headline) > MAX_LENGTH:
            headline = headline[:MAX_LENGTH]
            translation = process_text(input_text=headlines, source_language=language, target_language=target_lang)
            for headline in translation.split("\n")[0:1]:
                translated_headlines[headline] = headline
        translated_headlines[headline] = translation
    return translated_headlines


config = get_config_options(force_reparse=True, options_from_flags={
    "page_title": "Multi Language Site Scraper",
    "page_icon": "🌎",
    "layout": "centered",
    "initial_sidebar_state": "expanded"
})


def set_page_config(config):
    st.set_page_config(config)
    
#  Unsupported, may break if the app changes. adjust the style of side bar to keep the page options at the top
st.markdown("""
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
""", unsafe_allow_html=True)


#Start of Streamlit app
st.title("Xinhua News Translation to Google Sheets")  
st.write("Translate important Xinhua News headlines into your language and update a Google Sheet.") 

#Dropdown for selecting target language
language = st.selectbox("Target Language", ["English", "Spanish", "French", "German", "Cantonese"])  

language_map = {
    "English": "eng",
    "Spanish": "spa",
    "French": "fra",
    "German": "deu",
    "Cantonese": "yue"
}


with st.sidebar:
    url = st.text_area("Input url", "", height=100)
    if not url.startswith("http"):
        url = f"http://{url}"
    if not url:
        raise ValueError("No URL provided.")

#Button to initiate translation and update Google Sheet via webhook
if st.button("Translate & Update"):  
    # Fetch news headlines from Xinhua
    headlines = extract_text_from_html(html_content=url)
    
    if not headlines:
        raise ValueError("No headlines found.")
    
    # Translate headlines
    translated_headlines = translate_headlines(headlines, language=language, target_lang=language_map[language])
    
st.column_config(width=3)
    with st.column(3):
        st.write("")
    
    
    # Display translated headlines on the app for review
    st.write(f"Translated Headlines in {language}:")  environment
    st.write(translated_headlines)  

    response = process_text(input_text=headlines, source_language=language, target_language=language_map[language])    

    if response == "Success":  
        st.write("Translated headlines updated in Google Sheet.")  
    else:      
        st.write("Failed to update Google Sheet. Please try again.")  

