from pydantic import BaseModel, Field


class RiskFinding(BaseModel):
    risk_area: str
    risk_level: str
    summary: str
    impact: str
    mitigation: str
    evidence_ids: list[str] = Field(default_factory=list)