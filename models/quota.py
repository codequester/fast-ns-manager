import re
from pydantic import BaseModel, Field, field_validator

CPU_REGEX = re.compile(r"^(\d{1,4})(m)?$")
MEMORY_REGEX = re.compile(r"^(\d{1,4})(Mi|Gi)$")

class Quota(BaseModel):
    requests_cpu: str = Field(
        ..., 
        pattern=CPU_REGEX.pattern,
        examples= ["1", "1000m"],
        description="CPU requests, up to 4 digits, optional 'm' suffix (e.g., 1000m, 1), max 9999"
    )
    limits_cpu: str = Field(
        ..., 
        pattern=CPU_REGEX.pattern,
        examples=["2", "2000m"],
        description="CPU limits, up to 4 digits, optional 'm' suffix (e.g., 2000m, 2), max 9999"
    )
    max_pods: int = Field(
        ..., 
        ge=1,
        le=999,
        examples=[10],
        description="Maximum number of pods, 1-999"
    )
    requests_memory: str = Field(
        ..., 
        pattern=MEMORY_REGEX.pattern,
        examples=["1Gi", "1024Mi"],
        description="Memory requests, up to 4 digits with 'Mi' or 'Gi' suffix (e.g., 1024Mi, 1Gi), max 9999"
    )
    limits_memory: str = Field(
        ..., 
        pattern=MEMORY_REGEX.pattern,
        examples=["2Gi", "2048Mi"],
        description="Memory limits, up to 4 digits with 'Mi' or 'Gi' suffix (e.g., 208Mi, 2Gi), max 9999"
    )

    @field_validator("requests_cpu", "limits_cpu")
    @classmethod
    def cpu_max_value(cls, v):
        # Already pattern-checked, just check numeric portion
        num = int(v.rstrip('m'))
        if num > 9999:
            raise ValueError("CPU value cannot exceed 9999")
        return v

    @field_validator("requests_memory", "limits_memory")
    @classmethod
    def memory_max_value(cls, v):
        m = MEMORY_REGEX.match(v)
        if m and int(m.group(1)) > 9999:
            raise ValueError("Memory value cannot exceed 9999")
        return v
