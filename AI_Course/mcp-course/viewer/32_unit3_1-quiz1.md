> **Offline-Kopie** aus dem Hugging-Face-MCP-Kurs, Kapitel „3.1. Use Case: Build a Pull Request Agent on the Hub“.
> Original online: <https://huggingface.co/learn/mcp-course/unit3_1/quiz1> · Quelltext: `AI_Course/mcp-course/units/unit3_1/quiz1.mdx`
> Aufbereitet von `coursetools/mcp-course-aufbereiten.py` — MDX-Bausteine
> wurden zu Markdown umgebaut, der Text ist unverändert.

# Quiz 1: MCP Server Implementation

Test your knowledge of MCP server concepts and implementation for the Pull Request Agent.

### Q1: What is the primary role of an MCP Server in the Pull Request Agent architecture?

- **A.** To host the user interface for the application
- **B.** To expose tools and resources that the AI agent can use to interact with GitHub
- **C.** To expose tools for reading and updating model repository tags on the Hugging Face Hub
- **D.** To train the AI model on pull request data

<details><summary>Auflösung</summary><p>· A — The MCP Server provides backend capabilities, not the user interface.</p><p>· B — Close, but this project focuses on the Hugging Face Hub, not GitHub.</p><p>✅ <b>C (richtig)</b> — Correct! The MCP Server provides get_current_tags and add_new_tag tools for Hub interactions.</p><p>· D — MCP Servers provide runtime capabilities, not model training functionality.</p></details>


### Q2: In the FastMCP implementation, why must all MCP tool functions return strings instead of Python objects?

- **A.** To improve performance by reducing memory usage
- **B.** To ensure reliable data exchange between the MCP server and client
- **C.** To make the code easier to debug
- **D.** To comply with Hugging Face Hub API requirements

<details><summary>Auflösung</summary><p>· A — While strings might be more memory efficient, this is not the primary reason.</p><p>✅ <b>B (richtig)</b> — Correct! MCP protocol requires string responses, so we use json.dumps() to serialize data.</p><p>· C — While JSON strings are readable, this is not the primary technical requirement.</p><p>· D — This is an MCP protocol requirement, not specific to the Hub API.</p></details>


### Q3: When implementing the `add_new_tag` tool, what is the purpose of checking if a tag already exists before creating a pull request?

- **A.** To reduce API calls and improve performance
- **B.** To prevent creating duplicate pull requests and provide better user feedback
- **C.** To comply with Hugging Face Hub rate limits
- **D.** To ensure the tag format is valid

<details><summary>Auflösung</summary><p>· A — While this helps performance, it's not the primary reason for the check.</p><p>✅ <b>B (richtig)</b> — Correct! This validation prevents unnecessary PRs and returns meaningful status messages.</p><p>· C — While avoiding unnecessary calls helps with rate limits, this is not the primary purpose.</p><p>· D — Tag validation is separate from checking if it already exists.</p></details>


### Q4: In the MCP server implementation, what happens when a model repository doesn't have an existing README.md file?

- **A.** The add_new_tag tool will fail with an error
- **B.** The tool creates a new ModelCard with ModelCardData and proceeds with the tag addition
- **C.** The tool skips adding the tag and returns a warning
- **D.** The tool automatically creates a default README with placeholder content

<details><summary>Auflösung</summary><p>· A — The implementation handles this case gracefully.</p><p>✅ <b>B (richtig)</b> — Correct! The code handles HfHubHTTPError and creates a new model card when none exists.</p><p>· C — The tool doesn't skip the operation - it creates what's needed.</p><p>· D — It creates a minimal model card structure, not placeholder content.</p></details>


### Q5: What is the significance of using `create_pr=True` in the `hf_api.create_commit()` function call?

- **A.** It makes the commit directly to the main branch
- **B.** It automatically creates a pull request instead of committing directly to the main branch
- **C.** It creates a private branch that only the repository owner can see
- **D.** It validates the commit before creating it

<details><summary>Auflösung</summary><p>· A — Setting create_pr=True creates a pull request, not a direct commit to main.</p><p>✅ <b>B (richtig)</b> — Correct! This enables the review workflow and follows repository governance practices.</p><p>· C — Pull requests are visible to repository collaborators and can be public.</p><p>· D — Validation happens regardless of the create_pr parameter.</p></details>


### Q6: Why does the MCP server implementation use extensive logging with emojis throughout the code?

- **A.** To make the code more fun and engaging for developers
- **B.** To help with debugging and monitoring when the server runs autonomously in response to Hub events
- **C.** To comply with FastMCP logging requirements
- **D.** To reduce the amount of text in log files

<details><summary>Auflösung</summary><p>· A — While emojis are visually appealing, there's a more practical reason.</p><p>✅ <b>B (richtig)</b> — Correct! Since the agent responds to webhooks automatically, detailed logs are crucial for troubleshooting.</p><p>· C — FastMCP doesn't require specific logging formats or emojis.</p><p>· D — Emojis don't significantly reduce log file size and this isn't the primary goal.</p></details>


Congrats on finishing this Quiz 🥳! If you need to review any elements, take the time to revisit the chapter to reinforce your knowledge.
