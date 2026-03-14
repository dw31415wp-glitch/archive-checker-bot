# Interstitial Page Task List

## 1. Define scope and success criteria

- [ ] Confirm the target GitHub Pages URL structure for the interstitial page.
- [ ] Document the accepted incoming query parameter format: `?url=<archive.today-url>`.
- [ ] Define which archive domains are allowed, such as `archive.today` and any supported aliases.
- [ ] Define failure behavior for missing, malformed, or unsupported `url` values.
- [ ] Write acceptance criteria for the three user actions: proceed, go back, and use safer alternative.

## 2. Build the page shell

- [ ] Create the interstitial page entry file for GitHub Pages hosting.
- [ ] Add the page layout for the warning title, explanatory copy, and action buttons.
- [ ] Add semantic markup and page metadata, including a descriptive page title.
- [ ] Ensure the page works as a static site without server-side dependencies.

## 3. Implement warning content and UX

- [ ] Write clear warning text explaining why archive.today links may be risky.
- [ ] Add a prominent **Proceed** action that is visually distinct but clearly secondary to the warning.
- [ ] Add a **Go Back** action that returns the user to the previous page when possible.
- [ ] Add a **Use Safer Alternative** action that links to the selected replacement tool or guidance.
- [ ] Add fallback copy for cases where browser history is unavailable.

## 4. Implement link parsing and navigation logic

- [ ] Read the `url` query parameter from the page URL.
- [ ] Validate and normalize the destination URL before rendering or navigation.
- [ ] Block navigation when the destination is not an allowed archive.today URL.
- [ ] Wire the **Proceed** action to navigate to the validated destination.
- [ ] Wire the **Go Back** action to browser history with a safe fallback.
- [ ] Wire the **Use Safer Alternative** action to the configured safer destination.

## 5. Style the page

- [ ] Add CSS for a simple, readable warning layout.
- [ ] Make the warning and actions clear on desktop and mobile screen sizes.
- [ ] Use visual hierarchy that emphasizes caution without making the page hard to use.
- [ ] Add visible focus states and hover states for interactive controls.

## 6. Accessibility and content quality

- [ ] Ensure the page is keyboard navigable end to end.
- [ ] Verify sufficient color contrast for text, warnings, and buttons.
- [ ] Use accessible button and link labels that clearly describe the outcome.
- [ ] Check that screen readers announce the warning and actions in a sensible order.

## 7. Test behavior

- [ ] Test a valid `archive.today` URL passed through the query string.
- [ ] Test missing `url` parameters.
- [ ] Test malformed URLs and unsupported domains.
- [ ] Test the **Go Back** flow with and without browser history available.
- [ ] Test the safer alternative link behavior.
- [ ] Test the page in a local static preview and in GitHub Pages deployment.

## 8. Deployment and documentation

- [ ] Verify the page is published correctly through GitHub Pages.
- [ ] Confirm the final public URL format to share in docs or integrations.
- [ ] Document how to generate interstitial links for archive.today URLs.
- [ ] Document any configured safer alternative target and how to update it later.
