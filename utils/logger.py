"""日志服务"""
import os
import sys

from nb_log import get_logger

PROJECT_BASE_PATH = sys.path[1]

LOGGER_DIR = os.path.join(PROJECT_BASE_PATH, "logs")


def get_log_obj(filename: str, son_file_name: str = None):
    """创建一个日志对象，可以将日志内容存储在不同的文件、文件夹中

    : param filename: 日志存储的文件名
    : return : 创建的日志对象
    """
    if son_file_name is not None:
        folder_path = f"{LOGGER_DIR}/{son_file_name}"
    else:
        folder_path = LOGGER_DIR
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    new_logger = get_logger(
        name=filename,
        log_filename=f"{filename}.log",
        log_level_int=20,
        log_path=folder_path,
        do_not_use_color_handler=True,
        is_add_stream_handler=False,
        log_file_handler_type=6
    )
    return new_logger


if __name__ == '__main__':
    log_obj = get_log_obj("test")
    log_obj.info("test")