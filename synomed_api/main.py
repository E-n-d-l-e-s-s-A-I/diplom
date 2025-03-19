from fastapi import FastAPI
import uvicorn
from api import API
from settings import settings
from schemas import Term

app = FastAPI(
    title="Synomed API",
    description="API для получения синонимов термина",
    version="1.0.0",
)
api = API(settings.UMLS_API_KEY)


@app.post("/synonyms")
async def synonyms(term: Term) -> list[Term]:
    """Получает синонимы термина."""

    eng_term = api.translate_ru_to_eng(term.term)
    synonyms = api.get_synonyms(eng_term)
    promt = "\n".join(synonyms)
    translated = api.translate_eng_to_ru(promt).split("\n")
    
    return [Term(term=synonym.lower()) for synonym in translated]


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)
