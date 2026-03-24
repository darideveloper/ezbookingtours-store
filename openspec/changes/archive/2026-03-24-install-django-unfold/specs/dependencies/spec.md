# Capability: install-django-unfold-dependencies

Dependencies for `django-unfold`.

## ADDED Requirements

### Requirement: Install `django-unfold`
The `django-unfold` package SHALL be installed to provide the modern admin interface.
#### Scenario: Add to `requirements.txt`
Given the project needs a modern admin interface
When I add `django-unfold==0.77.1` to `requirements.txt`
Then the library should be available for installation.
