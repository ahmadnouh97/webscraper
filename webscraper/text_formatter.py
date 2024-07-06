import re


class TextFormatter:
    @staticmethod
    def format_and_extract_tags(text):
        match = re.search(
            r"([\s\S]+?)(\n\n(?:\w+(?:\s\w+){0,2})(?:\n\n\w+(?:\s\w+){0,2})*\n*)$", text
        )
        if match:
            main_text = match.group(1).strip()
            tags = match.group(2).strip().split("\n\n")
            formatted_tags = ", ".join(tags)
            return f"{main_text}\n\n{formatted_tags}", tags
        return text, []
