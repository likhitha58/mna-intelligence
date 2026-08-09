from uuid import uuid4


def generate_evidence_id() -> str:
    return f"EV-{uuid4().hex[:8].upper()}"