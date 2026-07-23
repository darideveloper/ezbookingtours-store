## ADDED Requirements

### Requirement: Detail values with colons are preserved
When parsing booking detail lines that contain colons in the value portion (e.g., times like "15:13"), the system SHALL preserve the full value including all colons after the first.

#### Scenario: Time value with colons is parsed correctly
- **WHEN** a detail line contains `Arriving time: 15:13`
- **AND** the line is split by comma then by colon with `split(":", 1)`
- **THEN** the name SHALL be `"Arriving time"`
- **THEN** the value SHALL be `"15:13"` (not truncated to `"15"`)
- **THEN** the rendered email SHALL show the full time value

### Requirement: Whitespace is cleaned from parsed parts
When parsing booking detail lines, leading and trailing whitespace SHALL be removed from both the name and value parts.

#### Scenario: Whitespace is stripped from name and value
- **WHEN** a comma-split detail line contains leading whitespace such as `" Arriving time: 15:13"`
- **AND** the line is split by colon
- **THEN** the name SHALL be `"Arriving time"` (no leading space)
- **THEN** the value SHALL be `"15:13"` (no leading space)
