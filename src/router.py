import pathlib
import typing

import fastapi

import src.ml


router = fastapi.APIRouter()

PATH_TO_FILES = pathlib.Path(__file__).parent / 'data'
PATH_TO_FILES.mkdir(exist_ok=True)


@router.get('/ping')
def ping() -> dict[
    typing.Literal['status'],
    typing.Literal['ok'],
]:
    """Healthcheck"""
    return {'status': 'ok'}


@router.post('/recognize')
def recognize(upl_file: fastapi.UploadFile) -> str:
    """Recognizes the html code of the table from the image"""
    if upl_file.filename is not None:
        name_file = f'{id(upl_file.file)}_{upl_file.filename}'
    else:
        name_file = f'{id(upl_file.file)}.png'

    path_to_file = PATH_TO_FILES / name_file

    with open(path_to_file, 'wb') as file:
        file.write(upl_file.file.read())

    result = src.ml.model.pred(path_to_file)
    path_to_file.unlink(missing_ok=True)
    return result
