# Design: Simplify Seema Rohan Payload Parsing

Use a more concise mapping approach within the `Sale.from_payload` class method.

## Decisions

### 1. Simple Mapping Dictionary
Define a dictionary `SIMPLE_MAPPING` that maps raw description labels to the corresponding `booking_details` key and its parsing function.

### 2. Sequence Handling
Duplicate labels (like "Airline" and "Flight") occur twice in "Round Trip" payloads. A `SEQUENCE_MAPPING` and a simple counter will determine whether a value is assigned to the "arriving" or "departing" field.

### 3. Hotel Logic
Keep the special handling for "Hotel" (ignoring "other") and "Hotel name" to ensure custom names are correctly captured.

## Implementation Example
The core loop will become:
```python
for line in details_lines:
    # ... split key and value ...
    if key in SIMPLE_MAPPING:
        field, parser = SIMPLE_MAPPING[key]
        try: booking_details[field] = parser(value)
        except: pass
    elif key in SEQUENCE_MAPPING:
        # ... use counter to pick target field ...
    # ... etc ...
```
