"""Application entry point.

Run with ``python -m senscritique_mcp`` or the installed ``senscritique_mcp`` script.
"""

from __future__ import annotations

from .logger import build_logger


def main() -> int:
    logger = build_logger(__package__ or "senscritique_mcp")
    logger.info("senscritique_mcp started")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
