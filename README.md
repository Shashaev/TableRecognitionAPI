# TableRecognitionAPI

TableRecognitionAPI предоставляет возможности по распознованию таблиц. На вход 
подаются изображения таблиц, а на выходе их html.

## Выбор модели

Тестировались две модели [Qwen3-VL](https://huggingface.co/Qwen/Qwen3-VL-2B-Instruct) и [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR). Далее была сделана модель для предсказания класса поворота (0°, 90°, 180°, 270°). Модели с префиксом "Rotation" сначала поворачивают изображение с помощью модели поворота, а после это модифицированное изображение идёт в модель распознования таблиц.

Модели тестировались на собственном [бенчмарке](https://drive.google.com/file/d/1wLkkvbfTHKm4dZbX4HzompRLdo7bPanp/view?usp=sharing) по метрикам TEDS, TEDS-struct.

| Name                      | TEDS     | TEDS-struct |
| ------------------------- | -------- | ----------- |
| PaddleRecognizer          | 0.605333 | 0.677823    |
| Qwen3VLRecognizer         | 0.129730 | 0.264343    |
| RotationPaddleRecognizer  | **0.638229** | **0.698287**    |
| RotationQwen3VLRecognizer | 0.208242 | 0.315013    |

По итогу лучшая модель — RotationPaddleRecognizer. В текущей версии API используется модель PaddleRecognizer.

## Запуск проекта

### Ограничение по ресурсам

Для запуска желательными являются следующие требования:
- Свободное место на диске: 15 ГБ
- Оперативная память: 8 ГБ

### Что нужно для запуска?

- [Docker](https://www.docker.com/)

### Запуск через Docker

```bash
sudo docker run -p 9999:9999 shashaevkirill/tablerecognitionapi
```

После запуска API можно протестировать в [сагере](http://localhost:9999/docs).
