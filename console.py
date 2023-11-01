import importlib

import click
import os

from api.controller import get_task, check_task, run_task


def get_lessons(path):
    return [
        name for name in os.listdir(path)
        if os.path.isdir(os.path.join(path, name))
    ]


def import_resolve_function(task_name):
    try:
        module_path = f'lessons.{task_name}.exercise'
        module = importlib.import_module(module_path)
        resolve_function = getattr(module, 'resolve')
        return resolve_function
    except ModuleNotFoundError:
        print(f"Module for task '{task_name}' not found.")
        return None
    except AttributeError:
        print(f"Function 'resolve' not found in module for task '{task_name}'.")
        return None


@click.command()
def main():
    lessons_path = 'lessons'
    lessons = get_lessons(lessons_path)

    for i, lesson in enumerate(lessons, 1):
        click.echo(f"{i}. {lesson}")

    lesson_number = click.prompt(
        "Please enter a lesson number",
        type=click.IntRange(1, len(lessons))
    )
    selected_lesson = lessons[lesson_number - 1]
    click.echo(f"You selected: {selected_lesson}")

    actions = [
        {'name': 'get task', 'function': get_task},
        {'name': 'check task', 'function': check_task},
        {'name': 'run task', 'function': run_task},
    ]
    for i, action in enumerate(actions, 1):
        click.echo(f"{i}. {action['name']}")

    action_number = click.prompt(
        "Please choose an action",
        type=click.IntRange(1, len(actions))
    )
    selected_action = actions[action_number - 1]
    click.echo(f"You selected: {selected_action['name']}")

    click.echo(f"Performing '{selected_action['name']}' on lesson '{selected_lesson}'.")

    resolve = import_resolve_function(selected_lesson)
    selected_action['function'](selected_lesson, resolve)
