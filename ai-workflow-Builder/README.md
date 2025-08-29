# AI Workflow Builder — Starter Repo (Minimal)
This starter contains a minimal scaffold (frontend + backend) to jumpstart the Full-Stack Internship assignment.

## Quick contents
- backend/: FastAPI app with basic routes and service stubs
- frontend/: Vite + React minimal app
- docker-compose.yml, .env.example

## Quick start (local)
### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```
### Frontend
```bash
cd frontend
npm install
npm run dev
```

## Notes
This scaffold is intentionally minimal. Replace stubs with real implementations (OpenAI/Gemini clients, Chroma adapter, PDF extraction).
