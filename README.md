# DataDruid Labs

A browser-based learning environment featuring Python and R kernels with optional AI model integration.

## Customizing the Interface
Default theme and kernels are configured in `repl/jupyter-lite.json`. Change the `theme` value or toggle entries in
`kernelOptions` to enable or disable specific kernels.

## AI Agent
Set the following environment variables to enable model discovery:

- `OPENAI_API_KEY`
- `GOOGLE_API_KEY`
- `ANTHROPIC_API_KEY`
- `GROQ_API_KEY`

Example usage:

```python
from ai_agent import list_models, select_model
models = list_models("openai")
model = select_model("openai", models[0])
```

Common issues:
- Missing API keys will raise a `RuntimeError`.
- Network errors are reported during model listing.

## Sample Data and Lessons
Datasets reside under `content/data/` and guided notebooks live in `content/lessons/`.

- `content/lessons/python_basics.ipynb` – load data and compute statistics.
- `content/lessons/r_basics.ipynb` – simple R examples.

## Notebook Demonstration
`content/python.ipynb` provides a widget-based workflow to select a provider and model and dispatch a prompt.

## Requirements
Dependencies are listed in `requirements.txt` and include optional clients for major AI providers.
