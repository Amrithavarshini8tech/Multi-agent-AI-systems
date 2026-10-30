# Multi-agent-AI-systems
Install Python and set the env path: Edit the path and add C:\Users\amrit\AppData\Local\Python\bin
Check the version :python --version

Then give information about agent: https://microsoft.github.io/autogen/stable//user-guide/agentchat-user-guide/tutorial/models.html pip install "autogen-ext[openai]"

Now we need to provide information about tools like MCP:https://microsoft.github.io/autogen/stable//user-guide/extensions-user-guide/index.html pip install -U "autogen-ext[mcp]"


Install the AutoGen packages used by `SingleAgent.py`:

```bash
python -m pip install -U "autogen-agentchat" "autogen-ext[openai]"
```

Set `OPENAI_API_KEY` in your environment before running the script. Do not put
API keys in source files or documentation.
