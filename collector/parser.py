# Implementing the extract_text_from_html function with the suggested changes
from bs4 import BeautifulSoup
from loguru import logger
import warnings
from bs4 import BeautifulSoup, SoupStrainer


def extract_text_from_html(
    html_content="E:/00.Coding/megai/webscraper/html_content.html",
):
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore", category=UserWarning, module="bs4")
        try:
            with open("html_content.html", "r", encoding="utf-8") as file:
                html_content = file.read()

            # logger.debug(html_content[10:])

            # Initialize BeautifulSoup object
            soup = BeautifulSoup(html_content, "html.parser")

            # Find paragraphs with class 'title'
            paragraphs = soup.get_text("h", True), SoupStrainer("p")
            logger.debug(paragraphs)
            if not paragraphs:
                raise ValueError("No paragraphs found.")

            # Initialize an empty string to collect the text content
            text_content = ""

            # Add paragraphs to the text content
            for paragraph in paragraphs:
                text_content += f"\n\n{paragraph}\n"

            # Log the extractions
            with open("src/paragraphs.txt", "w", encoding="utf-8") as file:
                file.write(text_content)

            # For demonstration purposes, returning the first 500 characters of the text content
            return text_content[:500]

        except Exception as e:
            logger.error(f"An error occurred: {e}")
            return None


if __name__ == "__main__":
    extract_text_from_html("src/html_content.html")
