import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger():
    """初始化 Friday 引擎的全局日志系统"""
    logger = logging.getLogger("FridayEngine")
    logger.setLevel(logging.DEBUG) # 抓取所有级别

    # 避免重复添加处理器
    if logger.handlers: return logger

    # 格式化器：时间 - 级别 - 消息
    formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] >>> %(message)s', datefmt='%H:%M:%S')

    # 1. 控制台处理器（给本地看，带点颜色）
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # 2. 文件处理器（给云端留存，自动按 5MB 切割，最多留 3 个备份）
    log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    
    file_handler = RotatingFileHandler(
        os.path.join(log_dir, 'friday.log'), 
        maxBytes=5*1024*1024, 
        backupCount=3, 
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger

# 导出全局唯一实例
logger = setup_logger()