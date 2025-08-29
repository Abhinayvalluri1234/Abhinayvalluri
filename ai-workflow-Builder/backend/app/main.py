from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import health, workflows, documents, chat

app = FastAPI(title='AI Workflow Builder (Starter)')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.include_router(health.router, prefix='/health', tags=['health'])
app.include_router(documents.router, prefix='/documents', tags=['documents'])
app.include_router(workflows.router, prefix='/workflows', tags=['workflows'])
app.include_router(chat.router, prefix='/chat', tags=['chat'])
