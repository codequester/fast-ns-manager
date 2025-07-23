from fastapi import FastAPI
from models.requests import (
    CreateNamespacesRequest,
    UpdateNamespacesRequest,
    DeleteNamespacesRequest,
    UpdateNamespaceQuotasRequest
)
from models.response import NamespaceAPIResponse, NamespaceURL

app = FastAPI()

@app.post("/namespaces", response_model=NamespaceAPIResponse)
def create_namespaces(payload: CreateNamespacesRequest):
    created = [ns.name for ns in payload.namespaces]
    urls: list[NamespaceURL] = []  # Example: [NamespaceURL(title="PR", link="https://pr.url")]
    return NamespaceAPIResponse(
        status="success",
        status_code=201,
        result={"namespaces": created, "urls": [url.dict() for url in urls]}
    )

@app.put("/namespaces", response_model=NamespaceAPIResponse)
def update_namespaces(payload: UpdateNamespacesRequest):
    updated = [ns.name for ns in payload.namespaces]
    urls: list[NamespaceURL] = []
    return NamespaceAPIResponse(
        status="success",
        status_code=200,
        result={"namespaces": updated, "urls": [url.dict() for url in urls]}
    )

@app.delete("/namespaces", response_model=NamespaceAPIResponse)
def delete_namespaces(payload: DeleteNamespacesRequest):
    deleted = [ns.name for ns in payload.namespaces]
    urls: list[NamespaceURL] = []
    return NamespaceAPIResponse(
        status="success",
        status_code=200,
        result={"namespaces": deleted, "urls": [url.dict() for url in urls]}
    )

@app.put("/namespaces/quotas", response_model=NamespaceAPIResponse)
def update_namespace_quotas(payload: UpdateNamespaceQuotasRequest):
    quota_updated = [ns.name for ns in payload.namespaces]
    urls: list[NamespaceURL] = []
    return NamespaceAPIResponse(
        status="success",
        status_code=200,
        result={"namespaces": quota_updated, "urls": [url.dict() for url in urls]}
    )

