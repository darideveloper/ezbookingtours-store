# Capability: install-django-unfold-utils

Utility callbacks for `django-unfold`.

## ADDED Requirements

### Requirement: Create environment callbacks
Functions SHALL be implemented to provide environment status to the admin header.
#### Scenario: Implement `environment_callback` in `utils/callbacks.py`
Given the need for environment-specific styling
When I create `utils/callbacks.py` and implement `environment_callback`
Then the admin header should display the environment status.
