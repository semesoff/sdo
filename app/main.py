# sdo project
from uvicorn import run
from fastapi import FastAPI
from app.config.config import init_config

from app.routers import router as app_router

app = FastAPI()


def main():
    app.include_router(app_router)  # include all routers
    cfg = init_config()  # load config

    run(app, host=cfg['app']['host'], port=cfg['app']['port'])  # run app


if __name__ == '__main__':
    main()
