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
    schema: Dict[str, Any]


class UpdateTemplate(BaseModel):
    """
    base model for updating template
    """
    name: str
    description: str
    schema: Dict[str, Any]
    last_updated_at: str


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


class PipelineFilePath(BaseModel):
    """
    base model for each file
    """
    uri: Optional[str] = None
    mimetype: str
    bucket_path: str
    filename: str
    size: Optional[int] = None


class CreatePipelineRun(BaseModel):
    """
    base model to create pipeline run
    """
    name: str
    description: Optional[str] = None
    strategy_id: UUID
    schema: Dict[str, Any]
    fields: List[Dict[str, Any]]
    status: PipelineStatus = PipelineStatus.NOT_STARTED
    file_paths: List[PipelineFilePath] = Field(..., min_length=1)


class PipelineRunResponse(BaseModel):
    """
    base model for pipeline response
    """
    id: UUID
    name: str
    description: str
    schema: Dict[str, Any]
    fields: List[Dict[str, Any]]
    status: PipelineStatus
    file_paths: List[PipelineFilePath]
    strategy_id: UUID
    started_at: str
    completed_at: str


class OutputResponse(BaseModel):
    id: UUID
    uri: str
    pipeline_id: UUID
    created_at: str


class OutputWithPipelineResponse(BaseModel):
    """
    Response model for output with associated pipeline information
    """
    pipeline: PipelineRunResponse
    outputs: List[OutputResponse]
# ========


class StrategyResponse(BaseModel):
    """
    base model for strategy
    """
    id: UUID
    strategy: str
    name: str
    description: str


class PipelineSourceAssoc(BaseModel):
    """
    base model for source association
    """
    pipeline_id: UUID
    source_id: UUID
