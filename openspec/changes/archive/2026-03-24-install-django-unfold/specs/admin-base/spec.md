# Capability: install-django-unfold-admin-base

Base `ModelAdmin` for `django-unfold`.

## ADDED Requirements

### Requirement: Create `ModelAdminUnfoldBase`
A base class SHALL be created to implement default Unfold features like row actions.
#### Scenario: Implement `ModelAdminUnfoldBase` in `ezbookingtours_store/admin.py`
Given the need for consistent admin behavior
When I create `ezbookingtours_store/admin.py` and implement `ModelAdminUnfoldBase`
Then all models inheriting from it should have row actions and compressed fields.
