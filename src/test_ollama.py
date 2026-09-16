from ollama import chat


def get_today_news():
    return "OpenAI released a new model today."


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_today_news",
            "description": "Get today's latest news.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    }
]


messages = [
    {
        "role": "user",
        "content": input("Enter your prompt: "),
    }
]


# First call: ask the model what it wants to do
response = chat(
    model="qwen3.5:0.8b",
    messages=messages,
    tools=tools,
    think=False,
)

print("TOOL CALLS:", response.message.tool_calls)
print("MODEL CONTENT:", response.message.content)


# Check whether the model requested a tool
if response.message.tool_calls:

    # Add the model's response to the conversation
    messages.append(response.message)

    for tool_call in response.message.tool_calls:

        if tool_call.function.name == "get_today_news":

            # Execute the actual Python function
            result = get_today_news()

            # Send the tool result back to the model
            messages.append(
                {
                    "role": "tool",
                    "tool_name": "get_today_news",
                    "content": result,
                }
            )


    # Second call: let the model use the tool result
    response = chat(
        model="qwen3.5:0.8b",
        messages=messages,
        think=False,
        stream=True,
    )

    # Stream the final answer
    for chunk in response:
        print(chunk.message.content, end="", flush=True)

    print()

else:
    # The model didn't need a tool
    print(response.message.content)