## Admin sidebar order

`UNFOLD["SIDEBAR"]["navigation"]` in `ezbookingtours_store/settings.py`: two pinned sections on top, everything else alphabetical.

- **Pinned on top, never sorted:** `Autenticación` first, then `Tienda`. Keep this order.
- **Everything after them sorted A–Z** by `title`; each section's `items` sorted A–Z by `title`.
- Case-insensitive; accents sort as their base letter (`Á` = `A`).
- Sort the Spanish source string inside `_()`, not a translation.
- Adding a section or item = insert at its alphabetical position. Never append to the end.
- `Sección de Traslados` is intentionally an empty, sorted header. Leave it in the S block.
