from fastapi import FastAPI

from routes.logs import router as logs_router
from routes.analytics import router as analytics_router
from routes.context import router as context_router
from routes.priority import router as priority_router

app = FastAPI(
    title="AeroFix AI Backend"
)

app.include_router(logs_router)
app.include_router(analytics_router)
app.include_router(context_router)
app.include_router(priority_router)


@app.get("/")
def home():

    return {
        "message": "AeroFix Backend Running"
    }