# Llama 2 Security Insights API
An experimental self-hosted instance of Llama 2 for providing cyber security insights and context.


<!-- TOC -->

- [Llama 2 Security Insights API](#llama-2-security-insights-api)
    - [Architecture](#architecture)
        - [Llama 2](#llama-2)
            - [Why Llama 2?](#why-llama-2)
        - [LlamaIndex](#llamaindex)
            - [How can LlamaIndex help?](#how-can-llamaindex-help)
            - [Retrieval Augmented Generation RAG](#retrieval-augmented-generation-rag)
        - [FastAPI](#fastapi)
    - [Getting Started with the API](#getting-started-with-the-api)
        - [Step 1: Install Pre-reqs on Windows](#step-1-install-pre-reqs-on-windows)
        - [Step 2: Dump data into data folder](#step-2-dump-data-into-data-folder)
        - [Step 3: Load API](#step-3-load-api)
        - [Step 4: Call the API](#step-4-call-the-api)
- [CPU vs GPU Comparisons](#cpu-vs-gpu-comparisons)
    - [Time to Load Model](#time-to-load-model)
    - [Response Times to Question](#response-times-to-question)
- [Associated Projects](#associated-projects)

<!-- /TOC -->

## Architecture

- **Llama 2** - Large language model for next generation open source natural language generation tasks.
- **LlamaIndex** - LLMs offer a natural language interface between humans and data. Widely available models come pre-trained on huge amounts of publicly available data like Wikipedia, mailing lists, textbooks, source code and more.
- **Retrieval Augmented Generation (RAG)** - LLMs are trained on enormous bodies of data but they aren’t trained on your data. Retrieval-Augmented Generation (RAG) solves this problem by adding your data to the data LLMs already have access to. You will see references to RAG frequently in this documentation.
- **Fast API** - FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.

### Llama 2

#### Why Llama 2?

Llama 2 is Meta's open source large language model (LLM). It's basically the Facebook parent company's response to OpenAI's GPT models and Google's AI models like PaLM 2—but with one key difference: it's freely available for almost anyone to use for research and commercial purposes.

Meta have a great [Getting Started](https://ai.meta.com/llama/get-started/) page as well as a [Getting to Know LLama](https://github.com/facebookresearch/llama-recipes/blob/main/examples/Getting_to_know_Llama.ipynb) Juypter book.

### LlamaIndex

LLMs offer a natural language interface between humans and data. Widely available models come pre-trained on huge amounts of publicly available data like Wikipedia, mailing lists, textbooks, source code and more.

However, while LLMs are trained on a great deal of data, they are not trained on your data, which may be private or specific to the problem you’re trying to solve. It’s behind APIs, in SQL databases, or trapped in PDFs and slide decks.

LlamaIndex solves this problem by connecting to these data sources and adding your data to the data LLMs already have. This is often called Retrieval-Augmented Generation (RAG). RAG enables you to use LLMs to query your data, transform it, and generate new insights. You can ask questions about your data, create chatbots, build semi-autonomous agents, and more. To learn more, check out our Use Cases on the left.

Read about the high level concepts of LlamaIndex [here](https://docs.llamaindex.ai/en/stable/getting_started/concepts.html)

#### How can LlamaIndex help?
LlamaIndex provides the following tools:

- Data connectors ingest your existing data from their native source and format. These could be APIs, PDFs, SQL, and (much) more.

- Data indexes structure your data in intermediate representations that are easy and performant for LLMs to consume.

- Engines provide natural language access to your data. For example: - Query engines are powerful retrieval interfaces for knowledge-augmented output. - Chat engines are conversational interfaces for multi-message, “back and forth” interactions with your data.

- Data agents are LLM-powered knowledge workers augmented by tools, from simple helper functions to API integrations and more.

- Application integrations tie LlamaIndex back into the rest of your ecosystem. This could be LangChain, Flask, Docker, ChatGPT, or… anything else!

#### Retrieval Augmented Generation (RAG)

LLMs are trained on enormous bodies of data but they aren’t trained on your data. Retrieval-Augmented Generation (RAG) solves this problem by adding your data to the data LLMs already have access to. You will see references to RAG frequently in this documentation.

In RAG, your data is loaded and prepared for queries or “indexed”. User queries act on the index, which filters your data down to the most relevant context. This context and your query then go to the LLM along with a prompt, and the LLM provides a response.

Even if what you’re building is a chatbot or an agent, you’ll want to know RAG techniques for getting data into your application.

![alt text](https://docs.llamaindex.ai/en/stable/_images/basic_rag.png "RAG")

**Stages within RAG**

There are five key stages within RAG, which in turn will be a part of any larger application you build. These are:

- **Loading:** this refers to getting your data from where it lives – whether it’s text files, PDFs, another website, a database, or an API – into your pipeline. LlamaHub provides hundreds of connectors to choose from.
- **Indexing:** this means creating a data structure that allows for querying the data. For LLMs this nearly always means creating vector embeddings, numerical representations of the meaning of your data, as well as numerous other metadata strategies to make it easy to accurately find contextually relevant data
- **Storing:** once your data is indexed you will almost always want to store your index, as well as other metadata, to avoid having to re-index it.
- **Querying:** for any given indexing strategy there are many ways you can utilize LLMs and LlamaIndex data structures to query, including sub-queries, multi-step queries and hybrid strategies.
- **Evaluation:** a critical step in any pipeline is checking how effective it is relative to other strategies, or when you make changes. Evaluation provides objective measures of how accurate, faithful and fast your responses to queries are.

Read more [here](https://docs.llamaindex.ai/en/stable/getting_started/concepts.html).

### FastAPI

**Why FastAPI?**

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.8+ based on standard Python type hints.

The key features are:

- **Fast:** Very high performance, on par with NodeJS and Go (thanks to Starlette and Pydantic). One of the fastest Python frameworks available.
- **Fast to code:** Increase the speed to develop features by about 200% to 300%. *
- **Fewer bugs:** Reduce about 40% of human (developer) induced errors. *
- **Intuitive:** Great editor support. Completion everywhere. Less time debugging.
- **Easy:** Designed to be easy to use and learn. Less time reading docs.
- **Short:** Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
- **Robust:** Get production-ready code. With automatic interactive documentation.
- **Standards-based:** Based on (and fully compatible with) the open standards for APIs: OpenAPI (previously known as Swagger) and JSON Schema.

## Getting Started with the API

### Step 1: Install Pre-reqs on Windows

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

The response was:

```text
There were 10 failed password attempts in the log file.
```

Snippet of JSON response:
```json
{"answer":{"response":" There were 10 failed password attempts in the log file.","source_nodes":[{"node":{"id_":"b5223a47-5b13-462c-8755-3b9430d3d984","embedding":null,"metadata":{"file_path":"..\\storage\\OpenSSH_2k.log_structured.csv","file_name":"OpenSSH_2k.log_structured.csv","file_type":"text/csv","file_size":357677,"creation_date":"2023-11-24","last_modified_date":"2023-11-22","last_accessed_date":"2023-11-24"},"excluded_embed_metadata_keys":["file_name","file_type","file_size","creation_date","last_modified_date","last_accessed_date"],"excluded_llm_metadata_keys":["file_name","file_type","file_size","creation_date","last_modified_date","last_accessed_date"],"relationships":{"1":{"node_id":"8b2e22fe-2544-4d5d-99a8-eecdc86e31a4","node_type":"4","metadata":{"file_path":"..\\storage\\OpenSSH_2k.log_structured.csv","file_name":"OpenSSH_2k.log_structured.csv","file_type":"text/csv","file_size":357677,"creation_date":"2023-11-24","last_modified_date":"2023-11-22","last_accessed_date":"2023-11-24"},"hash":"a6256618596266c0bff3b825e045300cfbca908b591d5bbb65a484f3eb98284f"},"2":{"node_id":"77838434-3f21-460f-99ae-5971b79cf67f","node_type":"1","metadata":{"file_path":"..\\storage\\OpenSSH_2k.log_structured.csv","file_name":"OpenSSH_2k.log_structured.csv","file_type":"text/csv",
```

Response times:

```text
llama_print_timings:        load time =   10008.56 ms
llama_print_timings:      sample time =       7.26 ms /    14 runs   (    0.52 ms per token,  1927.84 tokens per second)
llama_print_timings: prompt eval time =  874970.77 ms /  1546 tokens (  565.96 ms per token,     1.77 tokens per second)
llama_print_timings:        eval time =   11232.27 ms /    13 runs   (  864.02 ms per token,     1.16 tokens per second)
llama_print_timings:       total time =  887042.66 ms
```

# CPU vs GPU Comparisons
With a decent CPU but without any GPU assistance, expect output on the order of 1 token per second, and excruciatingly slow prompt ingestion. Any decent Nvidia GPU will dramatically speed up ingestion, but for fast generation, you need 48GB VRAM to fit the entire model. That means 2x RTX 3090 or better.

## Time to Load Model

| Azure Virtual Machine Size      | CPU | GPU | Time to Response in ms |
| ----------- | ----------- | ----------- | ----------- |
| Standard_D4s_v4 | Intel(R) Xeon(R) Platinum 8272CL CPU @ 2.60GHz | None | 600000 ms |
| NC4as_T4_v3   | Intel(R) Xeon(R) Platinum 8272CL CPU @ 2.60GHz | 16GB Nvidia Tesla T4 GPU | xxxx ms |

## Response Times to Question

| Azure Virtual Machine Size      | CPU | GPU | Time to Response in ms |
| ----------- | ----------- | ----------- | ----------- |
| Standard_D4s_v4 | Intel(R) Xeon(R) Platinum 8272CL CPU @ 2.60GHz | None | 887042 ms |
| NC4as_T4_v3   | Intel(R) Xeon(R) Platinum 8272CL CPU @ 2.60GHz | 16GB Nvidia Tesla T4 GPU | xxxx ms |

# Associated Projects

- 🏡 LlamaHub: https://llamahub.ai | A large (and growing!) collection of custom data connectors
- 🧪 LlamaLab: https://github.com/run-llama/llama-lab | Ambitious projects built on top of LlamaIndex