# Interstitial Page

## GitHub Page Demo

This uses GitHub Pages to demonstrate an interstitial page for potentially unsafe outbound links, with archive.today as the primary example.

## Purpose

Archive.today is a web archiving service that allows users to save snapshots of web pages. However it has been blacklisted by some browsers and security software due to its association with malicious content. This interstitial page serves as a warning to users that they are about to visit a potentially unsafe site, while still allowing them to proceed if they choose to do so. Although the original use case is archive.today, the page should accept any incoming destination URL supplied through the query string.

## Implementation

The interstitial page is implemented using HTML, CSS, and JavaScript. It displays a warning message to the user, along with options to either proceed to the destination link, go back, or link to a tool to replace the destination with a safer alternative. The page is designed to be simple and user-friendly, while effectively communicating the potential risks associated with the destination. Its visual presentation should feel similar to Wikipedia, using a centered reading column, restrained colors, serif-forward body text, and subtle framed content areas.

### Incoming Link Specification

The interstitial page can be accessed by appending the destination URL as a query parameter to the interstitial page URL. It should accept any incoming domain, while still rejecting missing, malformed, or unsafe-protocol URLs. For example:
`https://your-interstitial-page-url.com/?url=https://archive.today/some-archived-page`

### Warning Message

The warning message should clearly inform users about the potential risks of visiting the destination link, including the possibility of encountering malicious content. For archive.today links, the copy should explain why the service may trigger browser or security warnings. It should also provide options for users to proceed, go back, or use a safer alternative.

### User Options

- **Proceed**: This option allows users to continue to the destination link despite the warning.
- **Go Back**: This option takes users back to the previous page they were on before encountering the interstitial page.
- **Use Safer Alternative**: This option can link to a tool or service that provides a safer alternative when one is available, such as a different web archiving service or a browser extension that can safely handle archived content.
