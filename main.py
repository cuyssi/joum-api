from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import translation, dictionary, suggestion, admin
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/ping")
def ping():
    return JSONResponse(content={"message": "pong"})

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(translation.router)
app.include_router(dictionary.router)
app.include_router(suggestion.router, prefix="/sugerencias")
app.include_router(admin.router, prefix="/admin")
