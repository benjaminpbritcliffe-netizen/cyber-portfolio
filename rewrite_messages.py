# rewrite_messages.py
import re

TYPES = ["feat","fix","docs","style","refactor","perf","test","build","ci","chore","revert"]

# Heuristics you can tweak
RULES = [
    (r"\bfix|bug|hotfix|patch\b", "fix"),
    (r"\badd(ed)?|implement|feature|create|introduce\b", "feat"),
    (r"\brefactor\b", "refactor"),
    (r"\bdoc(s|umentation)?\b|\breadme\b", "docs"),
    (r"\btest(s|ing)?\b|\bunit\b", "test"),
    (r"\bperf(ormance)?\b|\boptimi[sz]e\b", "perf"),
    (r"\bci\b|\bworkflow\b|\baction(s)?\b", "ci"),
    (r"\bbuild\b|\bdeps?\b|\bdependency\b|\bpackage\.json\b|\brequirements\.txt\b", "build"),
    (r"\brevert\b", "revert"),
]

def already_conventional(subject: str) -> bool:
    return re.match(r"^(?:%s)(?:\([^)]*\))?:\s" % "|".join(TYPES), subject) is not None

def guess_type(subject: str) -> str:
    low = subject.lower()
    for patt, t in RULES:
        if re.search(patt, low):
            return t
    return "chore"

def callback(message: bytes) -> bytes:
    text = message.decode("utf-8", errors="replace")
    lines = text.splitlines()
    if not lines:
        return message
    subject = lines[0]

    if not already_conventional(subject):
        t = guess_type(subject)
        lines[0] = f"{t}: {subject}"

    new_text = "\n".join(lines)
    if not new_text.endswith("\n"):
        new_text += "\n"
    return new_text.encode("utf-8")
