from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from isotope_pattern_service.routers.compute import router

app = FastAPI(title="Isotope Pattern Service")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["POST"],
    allow_headers=["Content-Type"],
)
app.include_router(router)
