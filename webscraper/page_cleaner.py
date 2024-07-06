import re


class PageCleaner:
    def __init__(self, formatter):
        self.formatter = formatter

    def clean(self, page):
        title_match = re.search(r"# .+", page)
        title = title_match.group(0) if title_match else ""

        paragraphs_match = re.search(r"Share\n\n(.+?)(?=\n\n\S)", page, re.DOTALL)
        paragraphs = paragraphs_match.group(1).strip() if paragraphs_match else ""

        tags_match = re.search(
            rf"{re.escape(paragraphs)}\n\n(.+?)(?=\n\nFollow)", page, re.DOTALL
        )
        tags_text = tags_match.group(1).strip() if tags_match else ""

        tags_text = re.sub(r"\n\n\\--\n\n\\--$", "", tags_text)
        tags_text, tags = self.formatter.format_and_extract_tags(tags_text)

        author_match = re.search(r"## Written by .+", page)
        author = author_match.group(0) if author_match else ""

        cleaned_page = f"{title}\n\n{paragraphs}\n\n{tags_text}\n\n{author}"
        return cleaned_page, tags
