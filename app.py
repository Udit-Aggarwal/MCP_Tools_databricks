from fastmcp import FastMCP

mcp = FastMCP("mcp-tools-server")

@mcp.tool()
def calculator(expression: str) -> str:
    """Evaluate a math expression"""
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {str(e)}"

@mcp.tool()
def reverse_text(text: str) -> str:
    """Reverse the given text"""
    return text[::-1]

if __name__ == "__main__":
    mcp.run(transport="sse", host="0.0.0.0", port=8000)
