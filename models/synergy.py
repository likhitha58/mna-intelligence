from pydantic import BaseModel, Field


class SynergyFinding(BaseModel):
    synergy_area: str
    synergy_type: str
    summary: str
    potential_value: str
    integration_difficulty: str
    evidence_ids: list[str] = Field(default_factory=list)