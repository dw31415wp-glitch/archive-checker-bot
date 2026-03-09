import argparse
import json

import pywikibot
from pywikibot.exceptions import Error as PywikibotError


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="archive-checker-bot",
        description="Basic command-line Pywikibot utilities.",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    site_info = subparsers.add_parser("site-info", help="Show wiki site information.")
    site_info.add_argument("--code", default="en", help="Wiki language code (default: en).")
    site_info.add_argument(
        "--family",
        default="wikipedia",
        help="Wiki family (default: wikipedia).",
    )

    page_info = subparsers.add_parser("page-info", help="Show basic page information.")
    page_info.add_argument("title", help="Page title to inspect.")
    page_info.add_argument("--code", default="en", help="Wiki language code (default: en).")
    page_info.add_argument(
        "--family",
        default="wikipedia",
        help="Wiki family (default: wikipedia).",
    )

    return parser


def _build_site(code: str, family: str) -> pywikibot.Site:
    return pywikibot.Site(code=code, fam=family)


def _site_info(site: pywikibot.Site) -> dict:
    return {
        "code": site.code,
        "family": site.family.name,
        "url": site.base_url(site.path()),
    }


def _page_info(site: pywikibot.Site, title: str) -> dict:
    page = pywikibot.Page(site, title)
    exists = page.exists()

    info = {
        "title": page.title(),
        "exists": exists,
    }
    if exists:
        info["is_redirect"] = page.isRedirectPage()
        info["latest_revision_id"] = page.latest_revision_id
    return info


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    try:
        site = _build_site(args.code, args.family)

        if args.command == "site-info":
            output = _site_info(site)
        elif args.command == "page-info":
            output = _page_info(site, args.title)
        else:
            parser.error(f"Unknown command: {args.command}")
            return 2

        print(json.dumps(output, indent=2, sort_keys=True))
        return 0
    except PywikibotError as error:
        print(f"Pywikibot error: {error}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
