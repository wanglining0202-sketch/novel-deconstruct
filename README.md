# novel-deconstruct

**Deconstruct Chinese web novels with AI — extract what makes a hit novel work.**

A command-line tool that feeds a novel to an OpenAI-compatible LLM and extracts
reusable writing patterns: the "golden first 3 chapters", a 9-dimension opening
score, the core premise, reusable "payoff formulas", and chapter-level outlines.

Built for web novel authors who need to reverse-engineer a breakout hit before
writing their own.

## What problem it solves

Chinese web novel authors (on platforms like Fanqie, Qidian, Qimao) face a hard
question: **why did this book blow up?** The answer lives in its opening hook,
its golden-finger setup, its payoff rhythm, and its core premise — but manually
tearing a 3-million-character novel apart takes days.

`novel-deconstruct` automates that: drop in a `.txt`, pick a mode, and get a
structured breakdown you can actually learn from — powered by the OpenAI API.

## Who it's for

- Web novel authors who deconstruct competitor novels before writing their own
- New authors learning pacing / payoff / premise design
- Editors and content teams triaging submissions

## Features

Five deconstruction modes, each backed by a battle-tested prompt distilled from
real web-novel deconstruction workflows:

| Mode | What it extracts |
|------|------------------|
| `golden3` | Golden first 3 chapters: hook, golden-finger reveal, first payoff |
| `score9` | 9-dimension opening score + "angry editor" fix suggestions |
| `core` | Core premise in 6 layers (setup / protagonist desire / golden finger / audience / model / segmented premise) |
| `formula` | Reusable "payoff formulas" (name / equation / slots / beats / variables / emotion curve) |
| `outline` | Chapter-level outline + main-line structure + upgrade system |

## Quick start

```bash
pip install -r requirements.txt
export OPENAI_API_KEY="sk-..."
python deconstruct.py novel.txt --mode score9
python deconstruct.py novel.txt --mode golden3
python deconstruct.py novel.txt --mode formula
```

All OpenAI-compatible endpoints work (set `OPENAI_BASE_URL` and `OPENAI_MODEL`
to use any compatible provider).

## Why OpenAI

Every mode is a single, carefully-designed prompt executed through the OpenAI
Chat Completions API. The prompts are the product — they encode years of web
novel deconstruction know-how into reusable instructions.

## License

MIT
