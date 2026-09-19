from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_warden_reconstruction_is_runtime_neutral():
    text = (ROOT / "WARDEN.md").read_text(encoding="utf-8")
    assert "future chat/session operating as Noah" not in text
    assert "future runtime/session operating as Noah" in text
    assert "No permanent ChatGPT conversation is part of Noëtarch/Noah identity or recovery" in text
    assert "The same rule applies when Four or Vera is instantiated for the project" in text


def test_current_state_is_repository_entrypoint():
    text = (ROOT / "CURRENT.md").read_text(encoding="utf-8")
    assert "repository entrypoint for currentness" in text
