from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import translation, dictionary, suggestion, admin

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(translation.router)
app.include_router(dictionary.router)
app.include_router(
    suggestion.router, prefix="/sugerencias"
)  # ✅ ya tiene el prefix correcto
app.include_router(admin.router, prefix="/admin")
