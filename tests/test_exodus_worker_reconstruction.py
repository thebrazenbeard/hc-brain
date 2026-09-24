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


def test_exodus_checkpoint_reconstructs_noah_without_chat_dependency():
    path = ROOT / "docs/runtime/NOAH_EXODUS_CHECKPOINT_2026-09-19.md"
    text = path.read_text(encoding="utf-8")
    assert "STARTING_SNAPSHOT" in text
    assert "FRESHNESS REQUIRED BEFORE EFFECT" in text
    assert "BT2 Coordinator" in text
    assert "projects/hc-brain/CURRENTNESS.json" in text
    assert "thebrazenbeard/hc-brain#22" in text
    assert "No conversation URL, title, ID, hidden state, or archived chat is part of recovery." in text
    assert "https://chatgpt.com" not in text
