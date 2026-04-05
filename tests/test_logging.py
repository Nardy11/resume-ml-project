import os
from app.logger import log_inference_time

LOG_FILE = "logs/app.log"


def test_log_file_created():
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    log_inference_time(0.5)

    assert os.path.exists(LOG_FILE)


def test_log_content_written():
    log_inference_time(1.23)

    with open(LOG_FILE, "r") as f:
        content = f.read()

    assert "Inference time" in content


def test_multiple_logs_append():
    log_inference_time(0.1)
    log_inference_time(0.2)

    with open(LOG_FILE, "r") as f:
        lines = f.readlines()
    assert len(lines) >= 2