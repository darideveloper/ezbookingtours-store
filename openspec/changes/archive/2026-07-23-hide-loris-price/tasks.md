## 1. Email Template

- [x] 1.1 Remove the price `<h2>` block from `loris/templates/loris/mail.html`

## 2. View Validation

- [x] 2.1 In `loris/views.py`, remove `price is not None` from the required fields check in `SalesView.post()`
- [x] 2.2 Use `json_body.get("price", 0)` instead of `json_body.get("price")` so price defaults to 0 when omitted

## 3. Tests

- [x] 3.1 Add test case: POST without price field returns success and saves with `price = 0`
- [x] 3.2 Verify existing `test_post_missing_data` still passes (still requires name, last-name, details, email)
- [x] 3.3 Add test case: rendered email template does not contain "Price" or price value
- [x] 3.4 Run all loris tests to confirm nothing is broken
