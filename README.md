





# LLM Automation Agent

A FastAPI-based automation agent that handles various AI tasks including audio transcription, image processing, and file manipulation using LLMs.

## Features

- Audio transcription using Whisper
- Image processing and compression
- Markdown formatting
- File operations
- API integrations
- Git operations
- SQL queries
- Web scraping

## Setup

### 1. Create Virtual Environment
```bash
# Install uv (if not already installed)
pip install uv

# Create and activate virtual environment
uv venv
source .venv/bin/activate  # On Unix/macOS
# OR
.venv\Scripts\activate  # On Windows
```

### 2. Install Dependencies
```bash
uv pip install -r requirements.txt
```

### 3. Set Environment Variables
Instead of using a .env file, set the required environment variables directly:

```bash
# Unix/macOS
export AIPROXY_TOKEN=your_aiproxy_token
export GOOGLE_API_KEY=your_google_api_key
export OPENROUTER_API_KEY=your_openrouter_api_key
export OPENAI_API_KEY=your_openai_api_key

# Windows (CMD)
set AIPROXY_TOKEN=your_aiproxy_token
set GOOGLE_API_KEY=your_google_api_key
set OPENROUTER_API_KEY=your_openrouter_api_key
set OPENAI_API_KEY=your_openai_api_key

# Windows (PowerShell)
$env:AIPROXY_TOKEN="your_aiproxy_token"
$env:GOOGLE_API_KEY="your_google_api_key"
$env:OPENROUTER_API_KEY="your_openrouter_api_key"
$env:OPENAI_API_KEY="your_openai_api_key"
```

### 4. Run the Application
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

## Docker Usage

Build and run using Docker:
```bash
# Build the image
docker build -t your-username/llm-automation-agent-tds .

# Run with environment variables
docker run -p 8000:8000 \
  -e AIPROXY_TOKEN=$AIPROXY_TOKEN \
  -e GOOGLE_API_KEY=$GOOGLE_API_KEY \
  -e OPENROUTER_API_KEY=$OPENROUTER_API_KEY \
  -e OPENAI_API_KEY=$OPENAI_API_KEY \
  your-username/llm-automation-agent-tds
```

Or using docker-compose:
```bash
docker-compose up
```

## API Endpoints

### POST /run
Execute various tasks through a single endpoint.

Example tasks:
```bash
# Audio transcription
curl -X POST "http://localhost:8000/run?task=transcribe%20data/audio.mp3%20to%20transcript.txt"

# Image compression
curl -X POST "http://localhost:8000/run?task=compress%20data/image.jpg%20to%20quality%2080%20save%20to%20compressed.jpg"

# Markdown formatting
curl -X POST "http://localhost:8000/run?task=Format%20/data/format.md%20with%20prettier%203.4.2"
```

### GET /read
Read file contents:
```bash
curl "http://localhost:8000/read?path=/data/output.txt"
```

## Response Format
```json
{
    "status": "success",
    "message": "Task completed successfully",
    "output_file": "/data/output.txt",
    "additional_info": {}
}
```

## Error Handling
- 400: Bad Request (invalid input)
- 404: File Not Found
- 500: Internal Server Error

## Security Notes
- Environment variables are used for all sensitive tokens
- File operations are restricted to the /data directory
- Input validation and sanitization implemented
- Proper error handling and logging in place

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README:
1. Uses uv for virtual environment and package management
2. Emphasizes environment variables over .env files
3. Provides clear Docker instructions
4. Shows example API calls
5. Includes security notes
6. Matches your project's actual functionality
