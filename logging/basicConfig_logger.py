import logging

# 基本設定：https://python.civic-apps.com/basic-logging/
# basicConfigでフォーマットとレベル指定
#logging.basicConfig(level=logging.DEBUG, format="%(asctime)s %(levelname)s %(message)s")

# basicConfigでファイルへ出力
logging.basicConfig(level=logging.DEBUG,
    filename="./log/test.log",
    format="%(asctime)s %(levelname)-7s %(message)s")

# ロガーを必ず生成して使用(ロガー名は完全修飾名を使用)
log = logging.getLogger(__name__)

log.debug("debug message")
log.info("info message")
log.warning("warning")
log.error("error")