> **Offline-Kopie** aus dem Hugging-Face-MCP-Kurs, Kapitel „1. Introduction to Model Context Protocol“.
> Original online: <https://huggingface.co/learn/mcp-course/unit1/quiz2> · Quelltext: `AI_Course/mcp-course/units/unit1/quiz2.mdx`
> Aufbereitet von `coursetools/mcp-course-aufbereiten.py` — MDX-Bausteine
> wurden zu Markdown umgebaut, der Text ist unverändert.

# Quiz 2: MCP SDK

Test your knowledge of the MCP SDKs and their functionalities.

### Q1: What is the main purpose of the MCP SDKs?

- **A.** To define the MCP protocol specification
- **B.** To make it easier to implement MCP clients and servers
- **C.** To provide a visual interface for MCP interactions
- **D.** To replace the need for programming languages

<details><summary>Auflösung</summary><p>· A — The SDKs implement the protocol, they don't define it. The specification is separate.</p><p>✅ <b>B (richtig)</b> — Correct! SDKs abstract away low-level protocol details.</p><p>· C — While some tools might offer this (like MCP Inspector), it's not the primary purpose of the SDKs themselves.</p><p>· D — SDKs are libraries used within programming languages.</p></details>


### Q2: Which of the following functionalities do the MCP SDKs typically handle?

- **A.** Optimizing MCP Servers
- **B.** Defining new AI algorithms
- **C.** Message serialization/deserialization
- **D.** Hosting Large Language Models

<details><summary>Auflösung</summary><p>· A — This is outside the scope of MCP SDKs, which focus on protocol implementation.</p><p>· B — This is outside the scope of MCP SDKs, which focus on protocol implementation.</p><p>✅ <b>C (richtig)</b> — Correct! This is a core function for handling JSON-RPC messages.</p><p>· D — MCP enables connection to LLMs, but the SDKs themselves don't host them.</p></details>


### Q3: According to the provided text, which company maintains the official Python SDK for MCP?

- **A.** Google
- **B.** Anthropic
- **C.** Microsoft
- **D.** JetBrains

<details><summary>Auflösung</summary><p>· A — The text lists Anthropic as the maintainer.</p><p>✅ <b>B (richtig)</b> — Correct! The course material indicates Anthropic maintains the Python SDK.</p><p>· C — Microsoft maintains the C# SDK according to the text.</p><p>· D — JetBrains maintains the Kotlin SDK according to the text.</p></details>


### Q4: What command is used to start a development MCP server using a Python file named `server.py`?

- **A.** python server.py run
- **B.** mcp start server.py
- **C.** mcp dev server.py
- **D.** serve mcp server.py

<details><summary>Auflösung</summary><p>· A — While you run Python scripts with `python`, MCP has a specific CLI command.</p><p>· B — The command is `mcp dev`, not `mcp start`.</p><p>✅ <b>C (richtig)</b> — Correct! This command initializes the development server.</p><p>· D — This is not the standard MCP CLI command shown in the course material.</p></details>


### Q5: What is the role of JSON-RPC 2.0 in MCP?

- **A.** As a primary transport mechanism for remote communication
- **B.** As the message format for all communication between Clients and Servers
- **C.** As a tool for debugging AI models
- **D.** As a method for defining AI capabilities like Tools and Resources

<details><summary>Auflösung</summary><p>· A — HTTP+SSE or Streamable HTTP are transport mechanisms; JSON-RPC is the message format.</p><p>✅ <b>B (richtig)</b> — Correct! MCP uses JSON-RPC 2.0 for structuring messages.</p><p>· C — While its human-readable nature helps in debugging communications, it's not a debugging tool for AI models themselves.</p><p>· D — Capabilities are defined by their own schemas; JSON-RPC is used to invoke them and exchange data.</p></details>


Congrats on finishing this Quiz 🥳! If you need to review any elements, take the time to revisit the chapter to reinforce your knowledge.
