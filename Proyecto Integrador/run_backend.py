"""Entry point to run the backend (cross-platform).

Usage:
    python run_backend.py

This starts uvicorn pointing to the existing `api:app` module.
"""
import uvicorn


def main() -> None:
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)


if __name__ == "__main__":
    main()
