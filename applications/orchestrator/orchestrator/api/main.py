import uvicorn
from fastapi import FastAPI

from orchestrator.api.routers.batches import router as batches_router
from orchestrator.api.routers.entities import router as entities_router

# from orchestrator.core.settings import init_settings

app = FastAPI()


# @asynccontextmanager
# def lifespan(app: FastAPI):
#     init_settings()
#     yield


@app.get("/")
def read_root():
    return {"Hello": "World"}


app = FastAPI(
    # lifespan=lifespan,
    docs_url="/resolution/v1/docs",
    openapi_url="/resolution/v1/openapi.json",
    title="Orchestrator-API",
)
ROUTERS = [batches_router, entities_router]

for router in ROUTERS:
    app.include_router(router, prefix="/resolution/v1")


if __name__ == "__main__":
    uvicorn.run("orchestrator.api.main:app", host="0.0.0.0", port=80, reload=True)
