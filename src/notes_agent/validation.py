from __future__ import annotations

from collections import Counter

from .models import PageScript


REQUIRED_TERMS = {
    "java": ["JVM", "collection", "exception", "stream", "concurrency"],
    "data": ["SQL", "JPA", "transaction", "index"],
    "spring": ["IoC", "Spring Boot", "REST", "Security", "testing"],
    "production": ["observability", "cache", "Kafka", "Docker", "resilience"],
}


def validate_pages(pages: list[PageScript]) -> list[str]:
    errors: list[str] = []
    numbers = [page.page for page in pages]
    if len(pages) != 65:
        errors.append(f"Expected exactly 65 pages; found {len(pages)}")
    expected = list(range(1, 66))
    if numbers != expected:
        errors.append(f"Page numbering must be continuous 1..65; got {numbers}")
    duplicates = [title for title, count in Counter(p.title for p in pages).items() if count > 1]
    if duplicates:
        errors.append(f"Duplicate titles: {', '.join(duplicates)}")

    corpus = " ".join(
        text
        for page in pages
        for text in [
            page.title,
            page.objective,
            *(panel.heading for panel in page.panels),
            *(line for panel in page.panels for line in panel.copy),
            *page.important,
            *page.summary,
        ]
    )
    lowered = corpus.lower()
    for group, terms in REQUIRED_TERMS.items():
        missing = [term for term in terms if term.lower() not in lowered]
        if missing:
            errors.append(f"Missing {group} coverage: {', '.join(missing)}")

    for page in pages:
        if len(page.objective.split()) > 35:
            errors.append(f"Page {page.page}: easy definition is too long")
        if len(page.panels) < 2:
            errors.append(f"Page {page.page}: needs at least two content panels")
        if len(page.summary) < 2:
            errors.append(f"Page {page.page}: needs at least two summary points")
        if not page.interview_checks:
            errors.append(f"Page {page.page}: needs an interview check")
        if not (page.flowchart or any(panel.visual for panel in page.panels)):
            errors.append(f"Page {page.page}: needs a diagram or visual instruction")
    return errors
