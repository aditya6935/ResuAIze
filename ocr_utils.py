import pytesseract
import language_tool_python
import spacy

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")

def extract_text_from_image(image):
    text = pytesseract.image_to_string(image)
    return text

def grammar_and_spelling_check(text):
    tool = language_tool_python.LanguageTool('en-US')
    doc = nlp(text)

    # Extract named entities to ignore them in grammar/spelling checks
    named_entities = set(ent.text for ent in doc.ents)

    matches = tool.check(text)
    corrections = []
    for match in matches:
        context = text[match.offset:match.offset + match.errorLength]
        if context not in named_entities:
            corrections.append({
                "issue": match.message,
                "suggestion": match.replacements,
                "context": match.context
            })
    return corrections
