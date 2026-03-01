import subprocess
import os
import sys

def run_cli_command(command):
    return subprocess.run(command, capture_output=True, text=True)

def test_add_task():
    result = run_cli_command(
        [sys.executable, "-m", "lib.cli_tool", "add-task", "Alice", "Submit report"]
    )
    assert "Task 'Submit report' added to Alice." in result.stdout

def test_complete_task_with_script(tmp_path):
    script_path = tmp_path / "script.py"
    project_root = os.getcwd()

    script_content = f"""
import sys
sys.path.insert(0, r"{project_root}")

from lib.models import Task, User

user = User("Bob")
task = Task("Finish lab")
user.add_task(task)
task.complete()
"""

    script_path.write_text(script_content)

    result = subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True
    )

    assert "Task 'Finish lab' completed." in result.stdout