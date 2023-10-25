import logging
import sys

from dotenv import load_dotenv

from api.controller import run_task
from lessons.helloapi.exercise import resolve, task_name

load_dotenv()

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

run_task(task_name, resolve)
