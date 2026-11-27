
import json
import os
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]

def _unique_pairs(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result

def _read_object(path):
    if path.is_symlink() or not path.is_file():
        raise ValueError("expected regular configuration")
    data = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique_pairs)
    if type(data) is not dict:
        raise ValueError("expected JSON object")
    return data

def check_workspace(root):
    for name in ("ini", "inq"):
        if os.path.lexists(root / ".vscode" / name):
            raise ValueError("held workspace path present")
    settings = _read_object(root / ".vscode/settings.json")
    if settings.get("task.allowAutomaticTasks") != "off":
        raise ValueError("automatic tasks must be explicitly off")
    tasks = _read_object(root / ".vscode/tasks.json")
    if tasks != {"version": "2.0.0", "tasks": []}:
        raise ValueError("workspace tasks must be empty")
    ignored = (root / ".gitignore").read_text(encoding="utf-8").splitlines()
    if any(line.strip() in {"config.bat", "/config.bat", "**/config.bat"} for line in ignored):
        raise ValueError("config.bat must not have the known ignore rule")

class WorkspaceContainmentTests(unittest.TestCase):
    def test_repository(self):
        check_workspace(ROOT)

    def test_inert_negative_controls(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / ".vscode").mkdir()
            settings = root / ".vscode/settings.json"
            tasks = root / ".vscode/tasks.json"
            ignore = root / ".gitignore"
            def reset():
                settings.write_text('{"task.allowAutomaticTasks":"off"}', encoding="utf-8")
                tasks.write_text('{"version":"2.0.0","tasks":[]}', encoding="utf-8")
                ignore.write_text("node_modules\n", encoding="utf-8")
            reset()
            check_workspace(root)
            for name in ("ini", "inq"):
                marker = root / ".vscode" / name
                marker.write_bytes(b"inert fixture")
                with self.subTest(name=name), self.assertRaises(ValueError):
                    check_workspace(root)
                marker.unlink()
            for data in ('{}', '{"task.allowAutomaticTasks":"on"}',
                         '{"task.allowAutomaticTasks":"on","task.allowAutomaticTasks":"off"}'):
                reset()
                settings.write_text(data, encoding="utf-8")
                with self.subTest(settings=data), self.assertRaises(ValueError):
                    check_workspace(root)
            for data in ('{}', '{"version":"2.0.0","tasks":[{}]}',
                         '{"version":"2.0.0","tasks":[],"tasks":[]}'):
                reset()
                tasks.write_text(data, encoding="utf-8")
                with self.subTest(tasks=data), self.assertRaises(ValueError):
                    check_workspace(root)
            reset()
            ignore.write_text("config.bat\n", encoding="utf-8")
            with self.assertRaises(ValueError):
                check_workspace(root)
            reset()
            check_workspace(root)

if __name__ == "__main__":
    unittest.main()
