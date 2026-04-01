import fastapi

import src.router


app = fastapi.FastAPI(
    title='Table Recognition API',
    version='1.0',
)

app.include_router(src.router.router)
