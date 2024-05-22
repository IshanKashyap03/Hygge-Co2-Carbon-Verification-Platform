from fastapi import APIRouter, FastAPI, HTTPException
from controller import verify_certificate


app = FastAPI()
api_router = APIRouter()


@api_router.post("/api/v1/verify")
def verify(certificate_number: int, total_emissions: float):
    if total_emissions < 0:
        raise HTTPException(400, "Total emissions is negative")
    return verify_certificate(certificate_number, total_emissions)


app.include_router(api_router)
