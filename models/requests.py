from typing import List
from pydantic import BaseModel, Field
from .namespace import NamespaceCreate, NamespaceUpdate, NamespaceDelete, NamespaceQuotaUpdate

class CreateNamespacesRequest(BaseModel):
    requester_id: str = Field(..., max_length=10, examples=["a712456"], description="Requester ID of the user submitting the request")
    auto_merge_pr: bool
    namespaces: List[NamespaceCreate]

class UpdateNamespacesRequest(BaseModel):
    requester_id: str = Field(..., max_length=10, examples=["a712456"], description="Requester ID of the user submitting the request")
    auto_merge_pr: bool
    namespaces: List[NamespaceUpdate]

class DeleteNamespacesRequest(BaseModel):
    requester_id: str = Field(..., max_length=10, examples=["a712456"], description="Requester ID of the user submitting the request")
    auto_merge_pr: bool
    namespaces: List[NamespaceDelete]

class UpdateNamespaceQuotasRequest(BaseModel):
    requester_id: str = Field(..., max_length=10, examples=["a712456"], description="Requester ID of the user submitting the request")
    auto_merge_pr: bool
    namespaces: List[NamespaceQuotaUpdate]
