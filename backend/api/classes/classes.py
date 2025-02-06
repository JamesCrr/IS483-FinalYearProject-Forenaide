"""
base models of pipeline, templates
"""
from uuid import UUID
from typing import Any, Dict, Optional, List
from enum import StrEnum
from pydantic import BaseModel, Field


class PipelineStatus(StrEnum):
    """
    pipeline status enum
    """
    NOT_STARTED = "not_started"
    PROCESSING = "processing"
    FAILED = "failed"
    INCOMPLETE = "incomplete"
    COMPLETED = "completed"


class CreateTemplate(BaseModel):
    """
    base model create template
    """
    name: str
    description: str
    extraction_schema: Dict[str, Any]


class UpdateTemplate(BaseModel):
    """
    base model for updating template
    """
    name: str
    description: str
    extraction_schema: Dict[str, Any]


class TemplateResponse(CreateTemplate):
    """
    base model of template response
    """
    id: UUID
    created_at: str


# ========
class UpdatePipelineRun(BaseModel):
    """
    base model to update pipeline run
    """
    status: PipelineStatus
    completed_at: Optional[str] = None


class CreatePipelineRun(BaseModel):
    """
    base model to create pipeline run
    """
    name: str
    description: Optional[str] = None
    strategy_id: UUID
    extraction_schema: Dict[str, Any]
    status: PipelineStatus = PipelineStatus.NOT_STARTED
    file_uris: List[str] = Field(..., min_items=1)


class PipelineResponse(BaseModel):
    """
    base model for pipeline response
    """
    id: UUID
    name: str
    description: str
    extraction_schema: Dict[str, Any]
    status: PipelineStatus
    file_uris: List[str]
    strategy_id: UUID
    started_at: str
    completed_at: str
# ========
