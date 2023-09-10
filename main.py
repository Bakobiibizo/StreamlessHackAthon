import uvicorn
import json

# from collector import scraper, parser, translate
from fastapi import FastAPI, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


# __all__ = ["scraper", "parser", "translate"]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)


@app.get("/")
def root():
    return {"message": "Translation endpoint.\n See /docs for more information."}


class translation_options(BaseModel):
    url: str
    source_language: str
    target_language: str


@app.post("/translate")
def translate_text():  # translation_options: translation_options):
    # url = translation_options.url
    # raw_data = scraper.main(url)
    # translation = translate.process_text(
    #    input_text=raw_data,
    #    source_language=translation_options.source_language,
    #    target_language=translation_options.target_language,
    # )
    response = Response(
        content={"message": "Success"}, status_code=200, media_type="application/json"
    )

    return json.dumps(response) or HTTPException(
        status_code=404, detail="No translation found."
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
