#!/usr/bin/env python3
"""
Tavily Search CLI
Usage: python tavily_search.py "<query>" [--max-results 5]
"""

import argparse
import json
import os
import sys
import io

# Fix Windows GBK encoding for stdout
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

try:
    from tavily import TavilyClient
except ImportError:
    print("Error: 'tavily' package not installed. Run: pip install tavily-python")
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(description="Search the web using Tavily AI")
    parser.add_argument("query", help="Search query")
    parser.add_argument("--max-results", type=int, default=5, help="Maximum number of results (default: 5)")
    args = parser.parse_args()

    api_key = os.environ.get("TVILY_API_KEY")
    if not api_key:
        print("Error: TVILY_API_KEY environment variable not set.")
        print("Get your API key at https://tavily.com")
        sys.exit(1)

    client = TavilyClient(api_key=api_key)
    results = client.search(args.query, max_results=args.max_results)

    print(json.dumps(results, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
