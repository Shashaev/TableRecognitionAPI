import abc
import pathlib

import paddleocr


def format_html(html_table: str) -> str:
    """Formats the html code of the table"""
    html_code = """<html>
    <head>
    <meta charset="UTF-8">
    <style>
    table, th, td {
      border: 1px solid black;
      font-size: 10px;
    }
    </style>
    </head>
    <body>
    <table frame="hsides" rules="groups" width="100%%">
    %s
    </table>
    </body>
    </html>""" % html_table
    return html_code


class TableRecognizer(abc.ABC):
    @abc.abstractmethod
    def pred(self, path_to_img: pathlib.Path) -> str:
        pass


pipeline = paddleocr.PaddleOCRVL(
    device='cpu',
    precision='fp32',
)


class RotationPaddleRecognizer(TableRecognizer):
    def pred(self, path_to_img: pathlib.Path) -> str:
        """Recognition using PaddleOCRVL"""
        output = pipeline.predict(str(path_to_img))
        try:
            res = next(iter(output))
            html = res['parsing_res_list'][0].content
        except Exception:
            html = ''

        return format_html(html)


model = RotationPaddleRecognizer()
