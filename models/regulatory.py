from pydantic import BaseModel, Field


class RegulatoryFinding(BaseModel):
    regulation: str
    jurisdiction: str
    risk_level: str
    summary: str
    impact: str
    evidence_ids: list[str] = Field(default_factory=list)