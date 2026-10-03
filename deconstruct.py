#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""novel-deconstruct — 用 AI 拆解网文爆款书。

一个命令行工具：喂一本小说（txt），选一种拆解模式，调用 OpenAI 兼容 API
自动输出拆解结果，帮网文作者快速拆解对标爆款书、学习套路。

用法:
    python deconstruct.py novel.txt --mode score9
    python deconstruct.py novel.txt --mode golden3 --max-chars 8000

环境变量:
    OPENAI_API_KEY   必填，OpenAI API key
    OPENAI_BASE_URL  可选，兼容端点（默认 https://api.openai.com/v1）
    OPENAI_MODEL     可选，模型名（默认 gpt-4o-mini）
"""

import argparse
import os
import sys

from openai import OpenAI

from prompts import PROMPTS

# 中文约 0.6 token/字，按模型上下文留足余量；默认只喂前 1.2 万字（覆盖黄金三章/开篇评分足够）
DEFAULT_MAX_CHARS = 12000


def main():
    parser = argparse.ArgumentParser(description="AI 网文拆书引擎")
    parser.add_argument("novel", help="小说 txt 文件路径")
    parser.add_argument(
        "--mode",
        choices=list(PROMPTS.keys()),
        default="score9",
        help="拆解模式: golden3(黄金三章) / score9(开篇9维评分) / core(核心梗) / formula(爽点公式) / outline(章节细纲)",
    )
    parser.add_argument("--max-chars", type=int, default=DEFAULT_MAX_CHARS, help="送入模型的正文长度上限(默认12000)")
    args = parser.parse_args()

    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        sys.exit("错误: 请设置环境变量 OPENAI_API_KEY")

    with open(args.novel, encoding="utf-8", errors="ignore") as f:
        text = f.read()

    if len(text) > args.max_chars:
        print(f"[提示] 正文 {len(text)} 字，截取前 {args.max_chars} 字送入模型", file=sys.stderr)
        text = text[: args.max_chars]

    client = OpenAI(
        api_key=api_key,
        base_url=os.environ.get("OPENAI_BASE_URL", "https://api.openai.com/v1"),
    )
    model = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")

    system = PROMPTS[args.mode]
    print(f"[运行] 模式={args.mode}  模型={model}  输入={len(text)}字", file=sys.stderr)

    resp = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": text},
        ],
        temperature=0.3,
    )

    print(resp.choices[0].message.content)


if __name__ == "__main__":
    main()
