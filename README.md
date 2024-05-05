
# Application Setup and Usage Guide

This guide provides detailed steps on setting up and running the Python application within a virtual environment. Follow these instructions to ensure the application operates correctly.

## Setting Up the Virtual Environment

Before running the application, you must activate the Python virtual environment. This environment has all the necessary dependencies installed. To activate the virtual environment, navigate to the project directory and run the following command:

\`\`\`bash
source ../env/bin/activate
\`\`\`

This command assumes that you are currently in the application directory and that the virtual environment is located in the parent directory under \`env/bin/\`.

## Starting the Application

Once the virtual environment is activated, you can start the application server by using the \`manage.py\` script included in the project. Replace \`<PORT>\` with the actual port number where you want the application to listen for requests. For example, to start the server on port 8080, run:

\`\`\`bash
python manage.py runserver 8080
\`\`\`

## API Endpoint

The application features an API listening on the \`/prompt\` endpoint. You can access the API through the following URL, substituting \`8080\` with your chosen port number if different:

\`\`\`
http://127.0.0.1:8080/prompt
\`\`\`

### API Request Format

The API expects a POST request with a JSON body containing the following structure:

\`\`\`json
{
    "username": "<USERNAME>",
    "prompt": "<PROMPT>"
}
\`\`\`

Replace \`<USERNAME>\` and \`<PROMPT>\` with the actual username and the prompt text, respectively. Both fields are required and should be of type string.

### Example API Request

Here is an example of how to use \`curl\` to send a POST request to the API:

\`\`\`bash
curl -X POST http://127.0.0.1:8080/prompt -H "Content-Type: application/json" -d '{"username": "user123", "prompt": "Tell me about OpenAI."}'
\`\`\`

This command sends a request to the API with the username \`user123\` and a prompt asking about OpenAI.

---

Ensure to follow these instructions accurately to avoid issues with application setup and API interaction. If you encounter any problems, verify that the virtual environment is activated and that the server is running on the correct port.
