# Llama 2 Security Insights API
An experimental self-hosted instance of Llama 2 for providing cyber security insights and context.

## Architecture

### LlamaIndex

**Why LlamaIndex?**
LLMs offer a natural language interface between humans and data. Widely available models come pre-trained on huge amounts of publicly available data like Wikipedia, mailing lists, textbooks, source code and more.

However, while LLMs are trained on a great deal of data, they are not trained on your data, which may be private or specific to the problem you’re trying to solve. It’s behind APIs, in SQL databases, or trapped in PDFs and slide decks.

LlamaIndex solves this problem by connecting to these data sources and adding your data to the data LLMs already have. This is often called Retrieval-Augmented Generation (RAG). RAG enables you to use LLMs to query your data, transform it, and generate new insights. You can ask questions about your data, create chatbots, build semi-autonomous agents, and more. To learn more, check out our Use Cases on the left.

Read about the high level concepts of LlamaIndex [here](https://docs.llamaindex.ai/en/stable/getting_started/concepts.html)

**How can LlamaIndex help?**
LlamaIndex provides the following tools:

- Data connectors ingest your existing data from their native source and format. These could be APIs, PDFs, SQL, and (much) more.

- Data indexes structure your data in intermediate representations that are easy and performant for LLMs to consume.

- Engines provide natural language access to your data. For example: - Query engines are powerful retrieval interfaces for knowledge-augmented output. - Chat engines are conversational interfaces for multi-message, “back and forth” interactions with your data.

- Data agents are LLM-powered knowledge workers augmented by tools, from simple helper functions to API integrations and more.

- Application integrations tie LlamaIndex back into the rest of your ecosystem. This could be LangChain, Flask, Docker, ChatGPT, or… anything else!

### FastAPI

**Why FastAPI?**

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.

The key features are:

- Fast: Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
- Fast to code: Increase the speed to develop features by about 200% to 300%. *
- Fewer bugs: Reduce about 40% of human (developer) induced errors. *
- Intuitive: Great editor support. Completion everywhere. Less time debugging.
- Easy: Designed to be easy to use and learn. Less time reading docs.
- Short: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- Robust: Get production-ready code. With automatic interactive documentation.
- Standards-based: Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

## Getting Started with the API

### Step 1: Install Pre-reqs

- Install the latest version of Python from [python.org](https://www.python.org/) or your favourite package manager

- Create a [virtual environment](https://docs.python.org/3/library/venv.html): ```python -m venv .venv```

- Activate the virtual environment: ```.venv/Scripts/activate```

**Installation will fail if a C++ compiler cannot be located.** To get one:

- Windows: Install Visual Studio Community with the “Desktop development with C++” workload. It is free for individuals an open-source developers. See the C++ installation guide for more information.

```python
# Install required libraries
pip install -r requirements.txt
```

### Step 2: Dump data into data folder

- Dump the data that you need indexing in the storage folder.
- There is a publically available OpenSSH structured CSV log saved to the .\storage folder.
- Use this as an example to interact with the API and ask questions.

### Step 3: Load API

```python
cd .\app
python .\main.py
```

- Navigate to `http://localhost:8000/docs` to see the Swagger OpenAPI docs.

### Step 4: Call the API

- There is a sample Python script to call the API and return a JSON payload with the answer.

```Python
# Use POST as there is no limit to characters like GET

import requests
import json

url = "http://localhost:8000/ask"

payload = json.dumps({
  "question": "Q: How many failed password attempts were there?"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
```

The response

# CPU vs GPU Comparisons
With a decent CPU but without any GPU assistance, expect output on the order of 1 token per second, and excruciatingly slow prompt ingestion. Any decent Nvidia GPU will dramatically speed up ingestion, but for fast generation, you need 48GB VRAM to fit the entire model. That means 2x RTX 3090 or better.

| Azure Virtual Machine Size      | CPU | GPU | Time to Response in ms |
| ----------- | ----------- | ----------- | ----------- |
| Standard_D4s_v4 | Intel(R) Xeon(R) Platinum 8272CL CPU @ 2.60GHz | None | xxxx ms |
| NC4as_T4_v3   | Intel(R) Xeon(R) Platinum 8272CL CPU @ 2.60GHz | 16GB Nvidia Tesla T4 GPU | xxxx ms |

# Notes

* [ ] The CSV file is loaded and indexed at startup. Can I load new data in dynamically without having to reload the app?
* [ ] Performance loading the model of a single 350kb CSV is slow (10+ minutes) on 4vCPU and 16GB.

# Associated projects:

- 🏡 LlamaHub: https://llamahub.ai | A large (and growing!) collection of custom data connectors
- 🧪 LlamaLab: https://github.com/run-llama/llama-lab | Ambitious projects built on top of LlamaIndex