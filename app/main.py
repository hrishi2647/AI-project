from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI English Compliance Checker")
app.include_router(router)
