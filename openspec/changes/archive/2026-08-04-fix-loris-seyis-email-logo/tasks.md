## 1. Update loris email template

- [x] 1.1 Change the `<img src>` in `loris/templates/loris/mail.html` from `https://cancunconciergedmc.com/loris/imgs/logo.png` to `https://cancunconciergedmc.com/imgs/logo.png`
- [x] 1.2 Verify no remaining reference to the broken URL `https://cancunconciergedmc.com/loris/imgs/logo.png` in `loris/templates/loris/mail.html`

## 2. Update seyis email template

- [x] 2.1 Add an `<img>` element in `seyis/templates/seyis/mail.html` above the "Name" `<h2>` block, with `src="https://cancunconciergedmc.com/imgs/logo.png"` and `width="200"` matching the loris style
- [x] 2.2 Verify the `<img>` element is present in `seyis/templates/seyis/mail.html` with the correct URL

## 3. Verification

- [x] 3.1 Render both templates (e.g. via Django test shell) and confirm the logo URL appears in the output
- [x] 3.2 Confirm `https://cancunconciergedmc.com/imgs/logo.png` returns HTTP 200
- [x] 3.3 Run the loris and seyis test suites to ensure no regressions
