import re

# regex pattern for all important data
PII_PATTERNS = {
    "full_name": r"\b([A-Z][a-z]+(?:\s[A-Z][a-z]+)+)\b",
    "email": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "phone_number": r"\b\d{10}\b",
    "dob": r"\b\d{2}/\d{2}/\d{4}\b",
    "aadhar_num": r"\b\d{4} \d{4} \d{4}\b",
    "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])\/\d{2}\b"
}

# creat a function which take text as input
def mask_pii(text):
    # create a varriable to store input text in masked variable
    masked = text
    # creating empty list to store information
    entities = []
    # loop go to each PII_PATTERNS and its regex pattern
    for entity, pattern in PII_PATTERNS.items():
        # For every regex pattern, this finds all matching input text.
        for match in re.finditer(pattern, text):
            #Gets the start and end positions of the match
            start, end = match.span()
            # Gets the actual text that was matched
            value = match.group()
            #Saves info in the dictionary
            entities.append({
                "position": [start, end],
                "classification": entity,
                "entity": value
            })
            masked = masked.replace(value, f"[{entity}]")
    return masked, entities
