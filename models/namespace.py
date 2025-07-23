import re
from typing import Optional, List, Dict
from pydantic import BaseModel, Field, field_validator

APP_ID_REGEX = re.compile(r"^[a-zA-Z0-9]{5}$")
NAMESPACE_REGEX = re.compile(r"^[a-z0-9]([-a-z0-9]*[a-z0-9])?$")
CLUSTER_ENVS = {"lab", "nonprod", "prod"}

class NamespaceValidationBase(BaseModel):
    name: str = Field(..., max_length=63, pattern=NAMESPACE_REGEX.pattern, examples=["my-namespace"], description="Kubernetes namespace name (RFC 1123 label)")
    app_id: str = Field(..., min_length=5, max_length=5, pattern=APP_ID_REGEX.pattern, examples=["a1b2C"], description="5 character alphanumeric app ID")
    cluster_env: str = Field(..., examples=["lab"], description="Cluster environment: lab, nonprod, or prod")
    cluster: str = Field(..., examples=["my-cluster"], description="Cluster name")

    @field_validator("cluster_env")
    @classmethod
    def valid_cluster_env(cls, v):
        if v not in CLUSTER_ENVS:
            raise ValueError("cluster_env must be one of: lab, nonprod, prod")
        return v

class NamespaceBase(NamespaceValidationBase):
    labels: Optional[List[Dict[str, str]]] = None

from .quota import Quota

class NamespaceCreate(NamespaceBase):
    quota: Quota

class NamespaceUpdate(NamespaceBase):
    pass

class NamespaceQuotaUpdate(NamespaceValidationBase):
    quota: Quota

class NamespaceDelete(NamespaceValidationBase):
    pass
