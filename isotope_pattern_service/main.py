from fastapi import FastAPI

from isotope_pattern_service.routers.compute import router

app = FastAPI(title="Isotope Pattern Service")
app.include_router(router)
