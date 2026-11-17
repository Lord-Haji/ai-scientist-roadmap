#!/usr/bin/env python3
"""Check that URLs in the repo's markdown files respond.

Usage:  python scripts/check_links.py [--timeout 15] [--workers 8]

Prints failures; exit code is 1 if any URL failed. Some sites block bots,
so treat failures as "verify manually".
"""
import argparse
import concurrent.futures as cf
import pathlib
import re
import sys
import urllib.error
import urllib.request

URL_RE = re.compile(r"\]\((https?://[^)\s]+)\)|(?<![\(\"'])(https?://[^\s<>)\]\"']+)")
HEADERS = {"User-Agent": "Mozilla/5.0 (link-check)"}


def collect(root: pathlib.Path):
    urls = {}
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for m in URL_RE.finditer(text):
            url = (m.group(1) or m.group(2)).rstrip(".,;")
            urls.setdefault(url, set()).add(str(path.relative_to(root)))
    return urls


def check(url: str, timeout: int):
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, headers=HEADERS, method=method)
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return url, resp.status, None
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405, 400):
                continue
            return url, e.code, str(e)
        except Exception as e:  # noqa: BLE001
            if method == "HEAD":
                continue
            return url, None, str(e)
    return url, None, "unknown"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--timeout", type=int, default=15)
    ap.add_argument("--workers", type=int, default=8)
    args = ap.parse_args()
    root = pathlib.Path(__file__).resolve().parent.parent
    urls = collect(root)
    print(f"Checking {len(urls)} URLs...")
    bad = []
    with cf.ThreadPoolExecutor(max_workers=args.workers) as ex:
        for url, status, err in ex.map(lambda u: check(u, args.timeout), urls):
            if status is None or status >= 400:
                bad.append((url, status, err))
    for url, status, err in sorted(bad):
        files = ", ".join(sorted(urls[url]))
        print(f"FAIL {status} {url}  ({files})")
    print(f"{len(urls) - len(bad)} ok, {len(bad)} failed")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
