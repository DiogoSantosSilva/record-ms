from fastapi import FastAPI
from app.controllers import record_controller
from app.config import settings
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(record_controller.router)

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=settings.HOST, port=settings.PORT)
