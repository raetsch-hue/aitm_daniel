> **Offline-Kopie** aus dem Hugging-Face-MCP-Kurs, Kapitel „3.1. Use Case: Build a Pull Request Agent on the Hub“.
> Original online: <https://huggingface.co/learn/mcp-course/unit3_1/quiz2> · Quelltext: `AI_Course/mcp-course/units/unit3_1/quiz2.mdx`
> Aufbereitet von `coursetools/mcp-course-aufbereiten.py` — MDX-Bausteine
> wurden zu Markdown umgebaut, der Text ist unverändert.

# Quiz 2: Pull Request Agent Integration

Test your knowledge of the complete Pull Request Agent system including MCP client integration and webhook handling.

### Q1: What is the primary purpose of the webhook listener in the Pull Request Agent architecture?

- **A.** To provide a user interface for managing pull requests
- **B.** To receive and process Hugging Face Hub discussion comment events in real-time
- **C.** To store pull request data permanently in a database
- **D.** To authenticate users with the Hugging Face Hub

<details><summary>Auflösung</summary><p>· A — The webhook listener handles GitHub events, not user interfaces.</p><p>✅ <b>B (richtig)</b> — Correct! The webhook listener responds to Hub discussion events to trigger agent actions.</p><p>· C — While it may process PR data, its primary role is event handling, not storage.</p><p>· D — Webhook listeners handle events, not user authentication.</p></details>


### Q2: In the Agent-based MCP client implementation, how does the client connect to the MCP server?

- **A.** Through direct function calls in the same process
- **B.** Using stdio connection type to communicate with the MCP server as a subprocess
- **C.** By writing files to a shared directory
- **D.** Through HTTP REST API calls

<details><summary>Auflösung</summary><p>· A — The Agent uses subprocess communication, not direct function calls.</p><p>✅ <b>B (richtig)</b> — Correct! The Agent starts the MCP server with 'python mcp_server.py' and communicates via stdin/stdout.</p><p>· C — MCP uses real-time communication, not file-based communication.</p><p>· D — The stdio connection type doesn't use HTTP - it uses standard input/output streams.</p></details>


### Q3: Why does the webhook handler use FastAPI's `background_tasks.add_task()` instead of processing requests synchronously?

- **A.** To reduce server memory usage
- **B.** To comply with Hugging Face Hub requirements
- **C.** To return responses quickly (within 10 seconds) while allowing complex tag processing in the background
- **D.** To enable multiple webhook requests to be processed in parallel

<details><summary>Auflösung</summary><p>· A — Background tasks don't necessarily reduce memory usage.</p><p>· B — While Hub expects timely responses, this isn't a specific Hub requirement.</p><p>✅ <b>C (richtig)</b> — Correct! Webhook endpoints must respond quickly or be considered failed by the sending platform.</p><p>· D — While this enables parallelism, the primary reason is response time requirements.</p></details>


### Q4: What is the purpose of validating the `X-Webhook-Secret` header in the webhook handler?

- **A.** To identify which repository sent the webhook
- **B.** To prevent unauthorized requests and ensure the webhook is legitimate from Hugging Face
- **C.** To decode the webhook payload data
- **D.** To determine which MCP tools to use

<details><summary>Auflösung</summary><p>· A — Repository information comes from the webhook payload, not the secret header.</p><p>✅ <b>B (richtig)</b> — Correct! The shared secret acts as authentication between Hugging Face and your application.</p><p>· C — The secret is for authentication, not for decoding payload data.</p><p>· D — Tool selection is based on the webhook content, not the secret header.</p></details>


### Q5: In the Agent implementation, what happens when `await agent_instance.load_tools()` is called?

- **A.** It downloads tools from the Hugging Face Hub
- **B.** It discovers and makes available the MCP tools from the connected server (get_current_tags and add_new_tag)
- **C.** It starts the FastAPI webhook server
- **D.** It authenticates with the Hugging Face API

<details><summary>Auflösung</summary><p>· A — The tools are local MCP server tools, not downloaded from the Hub.</p><p>✅ <b>B (richtig)</b> — Correct! This discovers what tools the MCP server provides and makes them available to the agent's reasoning engine.</p><p>· C — load_tools() is specific to MCP tool discovery, not starting web servers.</p><p>· D — Authentication happens during agent creation, not during tool loading.</p></details>


### Q6: How does the Agent intelligently use MCP tools when processing a natural language instruction?

- **A.** It randomly calls available tools until one works
- **B.** It always calls get_current_tags first, then add_new_tag second
- **C.** It reasons about the instruction and determines which tools to call and in what sequence
- **D.** It requires explicit function calls to be specified in the instruction

<details><summary>Auflösung</summary><p>· A — The Agent uses reasoning to determine which tools to call and in what order.</p><p>· B — While this might be a common pattern, the Agent reasons about which tools to use based on the instruction.</p><p>✅ <b>C (richtig)</b> — Correct! The Agent can understand complex instructions and create tool execution plans automatically.</p><p>· D — The Agent can work with natural language instructions without explicit function specifications.</p></details>


### Q7: What filtering logic determines whether a webhook event should trigger tag processing?

- **A.** All webhook events are processed regardless of type
- **B.** Only events where action='create' and scope='discussion.comment'
- **C.** Only events from verified repository owners
- **D.** Only events that contain the word 'tag' in the comment

<details><summary>Auflösung</summary><p>· A — The handler filters events to only process relevant ones.</p><p>✅ <b>B (richtig)</b> — Correct! This ensures we only process new discussion comments, ignoring other Hub events.</p><p>· C — The filtering is based on event type, not user verification status.</p><p>· D — Event filtering happens before content analysis - we filter by event type first.</p></details>


Congrats on finishing this Quiz 🥳! If you need to review any elements, take the time to revisit the chapter to reinforce your knowledge.
