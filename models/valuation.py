from pydantic import BaseModel, Field


class ValuationFinding(BaseModel):
    method: str
    estimated_value: str
    assumptions: list[str] = Field(default_factory=list)
    interpretation: str
    confidence: str
    evidence_ids: list[str] = Field(default_factory=list)