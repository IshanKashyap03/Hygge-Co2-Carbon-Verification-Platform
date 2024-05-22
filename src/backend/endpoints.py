from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from controller import verify_certificate
import uvicorn

app = FastAPI()


class CertificateData(BaseModel):
    certificateNumber: str
    carbonEmission: float


@app.post("/api/v1/verify")
async def verify(data: CertificateData):
    print(data)
    if data.carbonEmission < 0:
        raise HTTPException(status_code=400, detail="Total emissions is negative")
    return verify_certificate(data.certificateNumber, data.carbonEmission)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
