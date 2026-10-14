from fastapi import FastAPI, Header, HTTPException
from jwt_validator import verify_token

app = FastAPI()

@app.get("/admin/records")
def get_admin_records(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    # CodeRabbit must inspect auth-core-lib to discover that this validation has verify_signature=False
    payload = verify_token(token)

    if payload.get("role") != "admin":
        raise HTTPException(status_code=403, detail="Unauthorized")

    return {"data": "Sensitive organization records"}
