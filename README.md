# Dynamic Task Processor API

This FastAPI application processes various file manipulation tasks using LLM assistance. It can handle tasks like file formatting, data analysis, and file modifications using either Google's Gemini or Ollama as the LLM provider.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
Create a `.env` file with:
```
AIPROXY_TOKEN=your-aiproxy-token-here
```

3. Run the application:
```bash
python main.py
```

The server will start at `http://localhost:8000`

## API Usage

### Execute Task Endpoint

```bash
POST /execute_task
```

Request body:
```json
{
    "task": "Your task description here",
    "llm_provider": "gemini",  // or "ollama"
    "model_name": "gemini-pro" // optional, defaults to "gemini-pro"
}
```

Example tasks:
1. Format markdown files:
```json
{
    "task": "Format the contents of /data/format.md using prettier@3.4.2, updating the file in-place"
}
```

2. Process dates:
```json
{
    "task": "Count the number of Wednesdays in /data/dates.txt and write the result to /data/dates-wednesdays.txt"
}
```

3. Sort JSON data:
```json
{
    "task": "Sort the array of contacts in /data/contacts.json by last_name, then first_name, and write to /data/contacts-sorted.json"
}
```

## Response Format

```json
{
    "status": "success",
    "task": "Original task description",
    "generated_code": "Generated Python code",
    "execution_result": {
        "status": "success",
        "message": "Task executed successfully"
    }
}
```

## Error Handling

The API returns appropriate HTTP status codes and error messages:
- 400: Bad Request (invalid input)
- 500: Internal Server Error (execution error)

## Security Notes

- The application runs generated code in a controlled environment
- File operations are restricted to the /data directory
- Proper error handling and logging are implemented 