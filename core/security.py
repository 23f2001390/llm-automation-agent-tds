from pathlib import Path
from fastapi import HTTPException

def validate_path_security(path: Path) -> bool:
    """Ensure path is within /data directory."""
    try:
        data_dir = Path("/data").resolve()
        target_path = path.resolve()
        return data_dir in target_path.parents
    except Exception:
        return False

def secure_path(path: str) -> Path:
    """Validate and return secure path."""
    path_obj = Path(path)
    if not validate_path_security(path_obj):
        raise HTTPException(
            status_code=403, 
            detail="Access denied: Can only access files within /data directory"
        )
    return path_obj 