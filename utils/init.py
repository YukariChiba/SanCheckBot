from pathlib import Path
import os

def chk_dir(dir):
    Path(dir).mkdir(parents=True, exist_ok=True)

def init():
    chk_dir(os.getenv("DATA_DIR"))
    chk_dir(os.getenv("CACHE_DIR"))
