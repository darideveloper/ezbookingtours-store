# email-reply-to Specification

## Purpose
Ensure replies to outgoing emails are routed to the monitored admin inbox (`EMAIL_CLIENT`) through a `Reply-To` header, applied explicitly at every send site and enforced by a custom SMTP backend so future send sites are covered by default.

## Requirements

### Requirement: Reply-To header on all outgoing emails
The system SHALL include a `Reply-To` header equal to the `EMAIL_CLIENT` setting on every outgoing email, including both the buyer-facing and admin-copy messages sent by the shared email util.

#### Scenario: Buyer replies to a confirmation email
- **WHEN** the system sends a confirmation email to the buyer from `EMAIL_HOST_USER`.
- **THEN** the message carries `Reply-To: <EMAIL_CLIENT>` so the reply is delivered to the admin inbox.

#### Scenario: Admin copy email
- **WHEN** the shared util sends the second (admin) copy of a confirmation email.
- **THEN** that message also carries `Reply-To: <EMAIL_CLIENT>`.

### Requirement: Explicit reply_to at direct send sites
The system SHALL pass `reply_to=[settings.EMAIL_CLIENT]` explicitly at every current send call site that constructs email messages directly (`digitalrealty.views`, `rohan_karisma.views`, `ashley_jonathan.views`, `store.tools`, and the `EmailMessage` send in the `store.views` test endpoint).

#### Scenario: Digital Realty confirmation email
- **WHEN** a sale completes in the Digital Realty app and the confirmation email is constructed.
- **THEN** the `EmailMultiAlternatives` message includes `reply_to=[EMAIL_CLIENT]`.

#### Scenario: Ashley Jonathan confirmation email
- **WHEN** a sale completes in the Ashley Jonathan app and the confirmation email is constructed.
- **THEN** the `EmailMultiAlternatives` message includes `reply_to=[EMAIL_CLIENT]`.

#### Scenario: Test endpoint email
- **WHEN** the `test-email/` endpoint sends an email via `EmailMessage`.
- **THEN** the message includes `reply_to=[EMAIL_CLIENT]`.

### Requirement: Backend safety net for reply-to injection
The system SHALL use a custom SMTP backend that injects `Reply-To = EMAIL_CLIENT` into any outgoing message that does not already define a `reply_to`, so future send sites are covered by default.

#### Scenario: Future app forgets to set reply_to
- **WHEN** a new app sends an email without `reply_to` through the configured backend.
- **THEN** the backend injects `reply_to = [EMAIL_CLIENT]` before sending.

#### Scenario: Message already defines reply_to
- **WHEN** a message already has a `reply_to` value.
- **THEN** the backend SHALL NOT overwrite it.

### Requirement: Graceful handling of unset admin inbox
The system SHALL NOT fail sending when `EMAIL_CLIENT` is unset or empty; send sites and the backend SHALL skip all `Reply-To` injection in that case.

#### Scenario: Local development without email client configured
- **WHEN** `EMAIL_CLIENT` is empty and an email is sent.
- **THEN** the message is sent without a `Reply-To` header and no exception is raised.
