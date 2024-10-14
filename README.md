# LangGraph-Chainlit-Ollama Project

This fully local LLM chat project integrates LangGraph, LangChain, Chainlit, Ollama, and SearxNG to create a web-based interface for interacting with language models and search results. 
The system is containerized using Docker and is meant to be started using docker compose.

## Project Structure

- **Ollama**: Provides the main language model (e.g., `llama3.2`) that processes user inputs.
- **Chainlit**: A web interface that connects the user to the language model and search tools.
- **SearxNG**: A metasearch engine used for retrieving additional information during interactions.

## Prerequisites

- Docker and Docker Compose installed on your system.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd langgraph-chainlit-ollama
   ```

2. **Configure environment variables**:

   You can customize the following environment variables in a .env file:

    - OLLAMA_DOCKER_TAG: The Docker tag for the Ollama image (default: latest).
    - OLLAMA_MODEL: The model name to be pulled by Ollama (default: llama3.2).
    - SEARXNG_DOCKER_TAG: The Docker tag for the SearxNG image (default: latest).
    - SEARXNG_NAME: Instance name for the SearxNG service (default: searxng).
    - Modify SearxNG settings: Ensure that the SearxNG configuration file is placed in the ./searxng directory.

3. **Build and run the services**:

   To start all services using Docker Compose, run the following command:

   ```bash
    docker-compose up --build
   ```
## Components

### Ollama
  - Purpose: Hosts the Ollama model (e.g., llama3.2) and serves it via an API.
  - Endpoint: Exposed on port 11434 inside the Docker network.
  - Docker Setup:
     - Uses a volume to store Ollama data (ollama:/root/.ollama).
     - Configured to support NVIDIA GPU.

### Chainlit
  - Purpose: Provides a web-based chat interface to interact with the language model and SearxNG.
  - Endpoint: Exposed on port 8000.
  - Environment Variables:
     - OLLAMA_API_URL: URL for accessing Ollama's API.
     - OLLAMA_MODEL: The model name used by Ollama (default: llama3.2).
     - SEARNGX_URL: URL for the SearxNG instance.

### SearxNG
  - Purpose: A privacy-respecting metasearch engine that aggregates results from various search engines.
  - Endpoint: Exposed on port 8080.
  - Configuration: Located in the ./searxng directory, the settings.yml file defines the search engine setup and other parameters. Only change was to enable search formats: json 

## Usage
  Access the Chainlit Interface: Open your browser and navigate to http://localhost:8000. This will open the Chainlit interface where you can chat with the Ollama language model that can use SearxNG for search queries.
