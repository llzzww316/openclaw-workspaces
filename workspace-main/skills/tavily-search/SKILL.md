---
name: tavily-search
description: Web search using the Tavily AI search API. Use when you need to search the web for current information, research topics, find answers, or look up facts. Triggers on queries like "search for X", "look up X", "find information about X", "what is X", "how to do X". Requires a Tavily API key (TVILY_API_KEY).
---

# Tavily Search

## Overview

Provides web search capabilities via the Tavily AI search API. Returns relevant results with snippets, URLs, and scores.

## Quick Start

1. Ensure `TVILY_API_KEY` is set in your environment or gateway config
2. Use the search script: `python scripts/tavily_search.py "<query>" [--max-results 5]`

## Usage

### Basic Search

```bash
python scripts/tavily_search.py "OpenClaw documentation"
```

### With Custom Result Count

```bash
python scripts/tavily_search.py "Python best practices" --max-results 10
```

## Output Format

Returns JSON with:
- `query`: The search query
- `results`: Array of {`url`, `title`, `content`, `score`}
- `answer`: AI-generated summary (if available)

## API Key Setup

Set your Tavily API key:
- **Gateway config**: `openclaw configure --section tavily`
- **Environment variable**: `TVILY_API_KEY=<your-key>`

Get an API key at: https://tavily.com
