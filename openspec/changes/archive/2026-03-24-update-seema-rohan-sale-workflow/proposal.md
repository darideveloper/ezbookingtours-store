---
change-id: update-seema-rohan-sale-workflow
title: Update Seema Rohan Sale Workflow (Unpaid Initial State, Dynamic Price, and Hotel Name Fix)
description: This change updates the seema_rohan app to mark new sales as "unpaid" (is_paid=False) initially, removes the redundant "price" field from the Sale model, and fixes the bug where "hotel_name" was incorrectly populated for standard hotels.
author: Gemini CLI
date: 2026-03-23
---

# Proposal: Update Seema Rohan Sale Workflow

This proposal combines three related updates to the `seema_rohan` app to align with current requirements, improve data integrity, and fix reported bugs.

## 1. Mark Sales as Unpaid on Creation
Currently, the specification requires sales to be marked as `is_paid=True` immediately. We will update this to mark sales as `is_paid=False` initially when they are created via the `buy` endpoint. The `is_paid` field will only be set to `True` when the user reaches the `success` view.

## 2. Remove Redundant "price" Field
The `Sale` model currently stores a `price` field that is also provided in the payload. However, this price can be derived from the `Transport` model (via `transport_type`) and the `Hotel` model (via `hotel.extra_price`). To ensure data integrity and remove redundancy, we will:
- Remove the `price` field from the `Sale` model's database schema.
- Add a `total_price` property to the `Sale` model that calculates the sum of `transport_type.price` and `hotel.extra_price`.
- Update views and admin to use this dynamic property.

## 3. Fix Redundant Hotel Name in Sales
Currently, when a standard hotel is selected, both the `hotel` (ForeignKey) and `hotel_name` (CharField) are populated. We will update the logic to:
- Clear `hotel_name` if a corresponding `Hotel` object is found in the database.
- Only populate `hotel_name` for custom hotels.

## Proposed Changes

### `seema_rohan/models.py`
- Remove the `price` field from `Sale`.
- Add a `total_price` property to `Sale`.
- Update `from_payload` to stop using the `price` from the payload for the `Sale` instance.
- Update `from_payload` to set `hotel_name` only if no matching `Hotel` record is found.

### `seema_rohan/views.py`
- Ensure `BuyView.post` creates sales with `is_paid=False`.
- Update `BuyView.post` to use `sale.total_price` in the confirmation email.

### `seema_rohan/admin.py`
- Update `SaleAdmin` to display `total_price` instead of the database `price` field.

### `openspec/specs/seema-rohan-refactor/spec.md`
- Update requirements to reflect all changes.

### `seema_rohan/tests.py`
- Update tests to reflect new behavior.

## Impact
- A database migration will be required.
- Cleaner data for hotel names.
- More robust price calculation.
