# Tasks: Simplify Seema Rohan Payload Parsing

Ordered tasks to simplify the `Sale.from_payload` method.

## 1. Implementation
- [x] 1.1 Update `seema_rohan/models.py` with the new dictionary-based parsing loop.
    - #### Validation
    - Test the `Sale.from_payload()` method in the Django shell with several sample payloads (One Way, Round Trip, Other Hotel).
    - Ensure all fields are correctly populated as before.
- [x] 1.2 Verify that nothing else in the view or admin is broken.
    - #### Validation
    - Verify that a test sale still creates a correct `Sale` object and triggers the email correctly.
