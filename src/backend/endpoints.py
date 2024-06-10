from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.middleware.cors import CORSMiddleware

import time
from pydantic import BaseModel
from controller import verify_certificate, lifespan
import uvicorn
from logger import logger
from auth import get_current_user


app = FastAPI(lifespan=lifespan)


class CertificateData(BaseModel):
    certificateNumber: str
    carbonEmission: float


@app.post("/hcevp-api/v1/verify")
async def verify(data: CertificateData, _: dict = Depends(get_current_user)):
    logger.info(data)
    if data.carbonEmission < 0:
        logger.warning("Total emissions is negative")
        raise HTTPException(status_code=400, detail="Total emissions is negative")
    return verify_certificate(data.certificateNumber, data.carbonEmission)


# Middleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://localhost:8080",
        "https://hygge-test.ddns.net:8080",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def log_middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logger.info(
        "Request processed in {process_time:.3f} seconds for {path}",
        process_time=process_time,
        path=request.url.path,
    )
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=7090, reload=True)
