import logging
import os
import sys

import openai
from dotenv import load_dotenv

# from lessons.helloapi.exercise import resolve, task_name
# from lessons.moderation.exercise import resolve, task_name
# from lessons.blogger.exercise import resolve, task_name
# from lessons.liar.exercise import resolve, task_name
# from lessons.inprompt.exercise import resolve, task_name
from lessons.embedding.exercise import resolve, task_name

load_dotenv()

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

openai.api_key = os.getenv('OPENAI_API_KEY')

# from api.controller import get_task
# get_task(task_name)

# from api.controller import check_task
# check_task(task_name, resolve)

from api.controller import run_task
run_task(task_name, resolve)
