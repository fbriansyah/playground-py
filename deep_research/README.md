## Deep Research

This is a deep research agent that can answer questions about any topic. It uses a multi-agent system to plan, search, and write comprehensive reports.

### Project Structure

```
deep_research/
├── app.py                      # Main entry point (Gradio UI)
├── managers/
│   └── research_manager.py     # Orchestrates the research process
├── models/
│   ├── planner.py              # Data models for planning
│   └── report.py               # Data models for reports
└── research_agents/
    ├── planner_agent.py        # Agent responsible for planning the research
    ├── search_agent.py         # Agent responsible for executing search queries
    └── writer_agent.py         # Agent responsible for compiling findings into a report
```

### Modules

- **Core Application**: `app.py` provides a Gradio interface for users to input topics and receive generated reports.
- **Managers**: `managers/research_manager.py` handles the coordination between different agents and the flow of data.
- **Agents**:
    - `planner_agent.py`: Breaks down the user query into research steps.
    - `search_agent.py`: Performs web searches to gather information.
    - `writer_agent.py`: Synthesizes the gathered information into a final report.
- **Models**: Contains Pydantic models to define the structure of data exchanged between components.

### Usage

Run the application using the following command:

```bash
uv run app.py
```
