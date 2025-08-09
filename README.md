## Welcome to DataDruid Labs
DataDruid Labs is an innovative online platform designed to provide an enabling environment for users to carry out programming lessons and build their skills in data analysis and science. Our lab is accessible directly in your web browser, making it easy to learn and practice programming concepts anywhere, anytime, even on your mobile phone!

## Supported Environments
We currently support the following programming environments:
1. Python (Pyodide)
2. JavaScript (Web Worker)
3. p5.js

## Coming Soon!
We are currently working on providing support for SQL and R programming languages, which will be available in our environments soon. Stay tuned for updates!

## Important Notes
Please note that our lab environment may lack some extensive libraries, and you may experience a delay when first importing a library. We apologize for any inconvenience this may cause.
Our lab is designed for learning and training purposes, and we provide small data sets for practice and exercises. However, for heavy analysis and large-scale projects, we recommend using your local computer for optimal performance.

## Getting Started
1. Access the lab by visiting our website and clicking on the "Launch Lab" button.
2. Choose a programming environment (Python, JavaScript, or p5.js) and start exploring our interactive notebooks and exercises.
3. Use our tutorials and guides to learn new skills and practice your coding abilities.

## Features
1. Interactive notebooks for hands-on learning
2. Medium sized data sets for practice and exercises
3. Accessible on desktop, laptop, tablet, or mobile phone
4. Compatible with popular programming languages (Python, JavaScript, and p5.js)

## Tips and Best Practices
1. Start with our beginner-friendly tutorials and gradually move on to more advanced topics.
2. Practice regularly to reinforce your learning and build your skills.
3. Join our community forums to connect with other users, ask questions, and share knowledge.
4. Digital Innovations for the Future of Analysis

DataDruid Labs is part of a larger initiative to build programming skills for the future of data analysis and science. Our platform is designed to provide an inclusive and accessible environment for users of all levels to learn, grow, and succeed.

## UI Customization and AI Provider Setup

### UI Customizations
DataDruid Labs runs on JupyterLite, allowing you to tailor the workspace to your needs:

* **Theme & Font Size** – Use the settings (gear) icon in the interface to switch between light and dark themes or adjust the editor font size.
* **Extensions** – Enable or disable JupyterLab extensions by editing the `repl/jupyter-lite.json` file and updating the `disabledExtensions` list.

### Environment Variables
Set the following environment variables before launching the lab to connect to different AI providers:

| Provider | Required Variables |
| --- | --- |
| OpenAI | `OPENAI_API_KEY` |
| Anthropic | `ANTHROPIC_API_KEY` |
| Google Gemini | `GOOGLE_API_KEY` |
| Azure OpenAI | `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT` |
| Hugging Face Hub | `HUGGINGFACEHUB_API_TOKEN` |

### Example: Listing and Selecting Models with `ai_agent`
```python
from ai_agent import ModelRegistry

registry = ModelRegistry()

# List available models for each provider
for provider, models in registry.list_models().items():
    print(provider, models)

# Select a model and generate a response
model = registry.get("openai:gpt-4o-mini")
print(model.chat("Hello DataDruid!"))
```

### Troubleshooting API Key Issues
* Verify that the environment variable is exported without quotes (e.g., `export OPENAI_API_KEY=sk-...`).
* Some providers require multiple variables (such as both a key and endpoint for Azure); confirm all are set.
* 401 or 403 errors often indicate an expired or incorrect key—regenerate it from the provider dashboard.
* Ensure your network or firewall allows requests to the provider's API endpoint.

## Acknowledgments
We would like to thank our team of developers, instructors, and contributors who have worked tirelessly to create and maintain this platform. We are grateful for your support and feedback, which help us improve and expand our services.

## Contact Us
If you have any questions, suggestions, or feedback, please don't hesitate to reach out to us using this [[form](https://docs.google.com/forms/d/e/1FAIpQLSfJFRXtw08fOwFRVmQjmbxnFxl1ZASpFwBw9wNLlpJU0bbTlA/viewform)]. We are always here to help and support your learning journey.
