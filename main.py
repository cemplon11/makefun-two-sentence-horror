"""Two-Sentence Horror — a make.fun entry.

The program writes one horror story, exactly two sentences long, to
/output/entry.txt. The story is fixed text: nothing is random, nothing
is read from the network or the environment, so every run produces the
same file byte for byte.

The scare lives in the count. The first sentence sets up a nightly
routine that is already unsettling on its own; the second sentence
re-reads it as something worse, because the number of chairs pulled
out is one more than the number of chairs the house owns. Somebody —
or something — has been sitting down to eat with them.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

MAX_CHARS = 400

FIRST_SENTENCE = (
    "Since we moved in, my wife has sleepwalked to the kitchen every "
    "night, and each morning I find one more chair pulled out from "
    "the table."
)

SECOND_SENTENCE = (
    "This morning there were six chairs pulled out, and we only own five."
)

STORY = FIRST_SENTENCE + " " + SECOND_SENTENCE


def validate(text: str) -> None:
    """Check the story against the competition gate before writing it.

    The gate needs UTF-8 text of 1 to 400 characters, not only
    whitespace, told in exactly two sentences. A period marks the end
    of each sentence here, so two periods means two sentences.
    """
    if not text.strip():
        raise ValueError("story must not be empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"story is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if text.count(".") != 2:
        raise ValueError(
            f"story must be exactly two sentences, found "
            f"{text.count('.')} sentence-ending periods"
        )
    text.encode("utf-8")


def write_entry() -> Path:
    """Validate the story and write it to the output path."""
    validate(STORY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(STORY, encoding="utf-8")
    return OUTPUT_PATH


def main() -> None:
    path = write_entry()
    print(f"wrote {len(STORY)} characters, 2 sentences, to {path}")


if __name__ == "__main__":
    main()
