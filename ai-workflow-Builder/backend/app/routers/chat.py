from fastapi import APIRouter, HTTPException
router = APIRouter()
from app.routers.workflows import STORE

# Very small runner: expects graph with presence of nodes; returns canned answer
@router.post('/{workflow_id}')
def chat(workflow_id: int, payload: dict):
    wf = STORE.get(workflow_id)
    if not wf:
        raise HTTPException(404, 'Workflow not found')
    query = payload.get('query', '')
    # In starter, we return an echo + note to implement LLM
    answer = f"[starter] Echo: {query}\n\nReplace with real LLM + KB pipeline."
    return {'answer': answer, 'context_used': False}
