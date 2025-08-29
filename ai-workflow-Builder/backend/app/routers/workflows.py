from fastapi import APIRouter, HTTPException
router = APIRouter()
# Minimal in-memory store for starter
STORE = {}
NEXT_ID = 1

@router.post('')
def create_workflow(payload: dict):
    global NEXT_ID
    wid = NEXT_ID
    NEXT_ID += 1
    STORE[wid] = payload
    return {'id': wid}

@router.get('/{workflow_id}')
def get_workflow(workflow_id: int):
    wf = STORE.get(workflow_id)
    if not wf:
        raise HTTPException(404, 'Workflow not found')
    return {'id': workflow_id, 'graph': wf.get('graph'), 'name': wf.get('name')}
