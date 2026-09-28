# Beginner Java Backend Handwritten Notes Agent

A human-in-the-loop pipeline for producing **65 easy A4 handwritten study sheets** covering Java, Spring Boot, databases, security, testing, and backend production basics.

No work experience is assumed. The writing follows the supplied reference: define the topic in normal words, show a small example/table/flowchart, list important points, and finish with a summary cloud. Facts target **Java 17/21 and Spring Boot 3.x**, so outdated claims from the visual reference are corrected.

## Main deliverables

- [`content/master-script.md`](content/master-script.md) — reviewable script for all 65 pages
- [`content/pages.json`](content/pages.json) — machine-readable page and layout specifications
- [`content/style-profile.json`](content/style-profile.json) — visual and easy-writing contract
- [`content/reference-analysis.md`](content/reference-analysis.md) — what is preserved and corrected
- `generated/prompts/batch-XX.md` — generated only after script approval
- `state/workflow.json` — human decisions and workflow history

## Human-in-the-loop workflow

```text
Beginner Curriculum Planner (65 pages)
              ↓
Easy Page Script Writer → Coverage + Plain-Language Review
              ↓
        HUMAN SCRIPT REVIEW
              ↓ approved
Prompt Compiler + Image Generator (up to 10 pages)
              ↓
Technical/Visual QA + HUMAN PAGE REVIEW
              ↓ only when every prior page is approved
Next batch → ... → final batch (pages 61–65)
              ↓
A4 image set + PDF assembler
```

The next batch remains locked until every page in the previous batch is approved. This stops style drift and prevents spending generation calls on an incorrect direction.

## 65-page curriculum

| Pages | Module | Topics |
|---|---|---|
| 01–14 | Starting Java | backend meaning, first program, JDK/JRE/JVM, program structure, variables, operators, input, conditions, loops, arrays, methods, classes, constructors, access |
| 15–30 | Object-oriented Java | OOP, encapsulation, inheritance, polymorphism, abstract class/interface, equality, String, wrappers/enums/records, exceptions, generics, collections and ordering |
| 31–37 | Useful modern Java | lambdas, streams, Optional, date/time, files, concurrency, executors, JVM memory and GC |
| 38–45 | Design, build and web/data basics | SOLID, patterns, Maven/Git, HTTP/JSON, SQL, joins, indexes, transactions, JDBC and pools |
| 46–55 | JPA, Spring and Spring Boot | ORM, mappings/N+1, IoC/DI, beans, lifecycle/proxies, Boot, config, MVC, REST, DTOs and validation |
| 56–62 | Complete Spring backend | error handling, Spring Data, transactions/locking, security, JWT/CORS/CSRF, testing and observability |
| 63–65 | Production and distributed systems | Redis caching, Kafka/RabbitMQ/outbox, microservices, resilience, Docker, CI/CD, Kubernetes and an end-to-end order flow |

## Commands

No third-party Python package is required.

```bash
# Validate page count, numbering, topic coverage and easy-definition limits
PYTHONPATH=src python3 -m notes_agent.cli validate

# Reset workflow to full-script review
PYTHONPATH=src python3 -m notes_agent.cli init

# Record human approval of the complete script
PYTHONPATH=src python3 -m notes_agent.cli script-decision \
  --decision approved --note "Beginner script approved"

# Compile pages 1–10 after approval
PYTHONPATH=src python3 -m notes_agent.cli prompts --batch 1

# Record image decisions
PYTHONPATH=src python3 -m notes_agent.cli decide --pages 1-10 --decision generated
PYTHONPATH=src python3 -m notes_agent.cli decide --pages 1-9 --decision approved
PYTHONPATH=src python3 -m notes_agent.cli decide --pages 10 \
  --decision revision_requested --note "Make definition larger"
```

There are seven batches; the final batch contains pages 61–65.

## Image review checklist

1. **Easy reading:** definition is visible first; no unexplained expert words.
2. **Accuracy:** technical terms and code are correct.
3. **Reference match:** warm paper, purple title, navy writing, green arrows, ruled tables, important points, summary cloud.
4. **A4 portrait:** full sheet visible with safe margins and correct page number out of 65.
5. **Learning value:** a reader can understand the page without another book.

Rejected pages are regenerated individually before the next batch is unlocked.

## Prompt guardrails learned from generated batches

The prompt compiler now explicitly blocks recurring image-model mistakes:

- landscape output for wide tables/code;
- printing prompt instructions such as “Footer,” “Bottom,” or color directions;
- duplicated, truncated, omitted, or invented bullets;
- changing case-sensitive Java identifiers to uppercase;
- moving statements outside their constructor/method braces;
- visually attaching a Java version to the wrong feature;
- splitting technical identifiers across lines; and
- adding punctuation or labels to the exact two-line footer.

Every image prompt ends with a six-step pre-render audit covering geometry, content completeness, code structure, instruction leakage, version facts, and footer accuracy.
