# admin-implementation Specification

## Purpose
TBD - created by archiving change install-django-unfold. Update Purpose after archive.
## Requirements
### Requirement: Update app admin classes
All app `admin.py` files SHALL be modified to use the new Unfold base class.
#### Scenario: Inherit from `ModelAdminUnfoldBase`
Given existing app admins
When I update them to inherit from `ModelAdminUnfoldBase`
Then they should display the modern Unfold UI.

### Requirement: Update auth models admin
`User` and `Group` SHALL be re-registered using Unfold's custom admin classes.
#### Scenario: Register `User` and `Group` with Unfold's `ModelAdmin`
Given the need for consistent UI across auth models
When I unregister `User` and `Group` and re-register them with Unfold's `ModelAdmin`
Then the authentication models should also use the Unfold interface.

