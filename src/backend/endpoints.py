from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

import time
from pydantic import BaseModel
from controller import verify_certificate
import uvicorn
from logger import logger
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(_: FastAPI):
    logger.info("Application starting up")
    # Add startup code after this line but before the yield

    yield
    # Add shutdown code after this line

    logger.info("Application shutting down")
    await logger.complete()
    logger.remove()  # Clear existing sinks before shutdown to prevent semaphore leak


app = FastAPI(lifespan=lifespan)


class CertificateData(BaseModel):
    certificateNumber: str
    carbonEmission: float


@app.post("/api/v1/verify")
async def verify(data: CertificateData):
    logger.info(data)
    if data.carbonEmission < 0:
        logger.warning("Total emissions is negative")
        raise HTTPException(status_code=400, detail="Total emissions is negative")
    return verify_certificate(data.certificateNumber, data.carbonEmission)


# Middleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
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
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
