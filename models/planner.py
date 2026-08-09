from pydantic import BaseModel, Field


class ResearchTask(BaseModel):
    agent: str = Field(
        description="The specialized agent responsible for this task."
    )

    objective: str = Field(
        description="The specific research objective."
    )


class ResearchPlan(BaseModel):
    tasks: list[ResearchTask] = Field(
        description="List of research tasks required for the acquisition analysis."
    )