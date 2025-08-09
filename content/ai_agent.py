"""Multi-provider AI agent utilities.

This module loads API keys for multiple providers and
exposes helpers to list available models and validate selections.
"""
from __future__ import annotations

import os
from typing import Dict, List

import google.generativeai as genai
import openai
import anthropic
import groq


PROVIDERS = {
    "openai": "OPENAI_API_KEY",
    "google": "GOOGLE_API_KEY",
    "anthropic": "ANTHROPIC_API_KEY",
    "groq": "GROQ_API_KEY",
}


def load_keys() -> Dict[str, str]:
    """Return available API keys keyed by provider name."""
    return {name: os.getenv(env) for name, env in PROVIDERS.items()}


def _require_key(provider: str, key: str) -> str:
    if not key:
        raise RuntimeError(f"Missing API key for {provider} provider")
    return key


def list_models(provider: str) -> List[str]:
    """Fetch available model IDs for the given provider."""
    keys = load_keys()
    provider = provider.lower()
    if provider == "openai":
        openai.api_key = _require_key(provider, keys.get("openai"))
        return [m.id for m in openai.models.list().data]
    if provider == "google":
        key = _require_key(provider, keys.get("google"))
        genai.configure(api_key=key)
        return [m.name for m in genai.list_models() if "generateContent" in m.supported_generation_methods]
    if provider == "anthropic":
        client = anthropic.Client(_require_key(provider, keys.get("anthropic")))
        resp = client.models.list()
        return [m["id"] for m in resp["data"]]
    if provider == "groq":
        client = groq.Groq(api_key=_require_key(provider, keys.get("groq")))
        resp = client.models.list()
        return [m.id for m in resp.data]
    raise ValueError(f"Unknown provider: {provider}")


def select_model(provider: str, model: str) -> str:
    """Validate and return a chosen model for provider."""
    models = list_models(provider)
    if model not in models:
        raise ValueError(f"Model {model!r} not available for {provider}")
    return model
