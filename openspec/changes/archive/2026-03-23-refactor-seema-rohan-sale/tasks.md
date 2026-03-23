# Tasks: Refactor Seema Rohan Sale Model

Ordered tasks to implement the model refactor in `seema_rohan`.

## 1. Implementation
- [x] 1.1 Update `seema_rohan/models.py` with new fields and relationships
    - #### Validation
    - Run `python manage.py makemigrations seema_rohan`
    - Run `python manage.py migrate seema_rohan`
    - Verify table schema in database or Django shell
- [x] 1.2 Update `seema_rohan/views.py` to parse payload and populate new fields
    - #### Validation
    - Submit a test POST request to `/buy/` with full booking details
    - Verify that the created `Sale` object has all fields correctly populated (not just in `stripe_data`)
- [x] 1.3 Update `seema_rohan/admin.py` to display and filter by new fields
    - #### Validation
    - Log in to Django Admin
    - Verify `Sale` list view shows new columns (Hotel, Transport Type, Date)
    - Verify filters work as expected
- [x] 1.4 Verify confirmation email functionality
    - #### Validation
    - Check that `tools.send_sucess_mail` still receives the correct `details_objs`
    - Verify email content for a test sale contains all booking details
