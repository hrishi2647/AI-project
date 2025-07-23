import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def check_guidelines(text: str):
    matches = tool.check(text)
    return [{
        "message": match.message,
        "sentence": match.context,
        "offset": match.offset
    } for match in matches]

def correct_text(text: str):
    return tool.correct(text)
