from typing import Optional, List, Dict, Any
from pydantic import BaseModel

class NamespaceURL(BaseModel):
    title: str
    link: str

class NamespaceAPIResponse(BaseModel):
    status: str
    status_code: int
    error: Optional[Dict[str, Any]] = None
    result: Optional[Dict[str, Any]] = None
    # result example: {"namespaces": ["ns1", "ns2"], "urls": [{"title": "PR", "link": "https://pr.url"}, {"title": "Jira", "link": "https://jira.url"}]}
