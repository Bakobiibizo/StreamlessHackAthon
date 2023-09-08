from src.seamless_communication.models.inference import translator
from collector import scraper, parser, translate, app
from demo import app as demo
import subprocess
__all__ = ["translator", "scraper", "parser", "translate", "app", "demo"]


if __name__ =="__main__":
    subprocess.run(["streamlit", "run", "collector/app.py"])