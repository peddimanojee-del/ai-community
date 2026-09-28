# Image Prompts — Batch 7

## Page 61 — TESTING: JUNIT, MOCKITO + SPRING

```text
Create ONE finished handwritten educational notes page, page 61 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “61 / 65” at bottom center.
- Avoid: typeset font, calligraphy, illegible pseudo-text, misspelled code, 3D effects, decorative illustrations unrelated to learning, undefined expert jargon, long academic paragraphs.

KNOWN IMAGE-MODEL FAILURE GUARDRAILS — CHECK EVERY RULE BEFORE RENDERING
- PORTRAIT IS NON-NEGOTIABLE: output one vertical A4 sheet at 210:297; width must be smaller than height. Never rotate or use a landscape composition, even when a table or code is wide.
- STYLE DIRECTIONS ARE NOT PAGE CONTENT: never print prompt labels or directions such as Visual instruction, Layout blueprint, Footer, Bottom, orange warning, exact text, or page geometry.
- EXACTLY ONCE: render every supplied heading, bullet, question, and summary point once. Never duplicate, omit, truncate, merge, or invent a bullet. Reject fragments such as cont.
- JAVA CODE IS CASE-SENSITIVE: copy code character-for-character in sentence/mixed case. Never convert code, identifiers, keywords, class names, or method names to all caps.
- PRESERVE CODE STRUCTURE: retain line breaks, indentation, braces, parentheses, semicolons, quotes, comments, and statement order. Check that every statement remains inside its intended class/method/constructor before rendering.
- BODY TEXT USES SENTENCE CASE: uppercase is reserved for the main title and occasional tiny table labels; definitions, bullets, code, and explanations must not become all caps.
- VERSION FACTS STAY INDEPENDENT: place each Java-version fact on its own complete line so wrapping cannot connect the wrong feature to a version.
- NO TECHNICAL-WORD HYPHENATION: do not split identifiers or important terms across lines, for example abstraction, RuntimeException, hashCode, ArrayList, and @Transactional.
- FIT WITHOUT DISTORTION: if content is dense, reduce handwriting size or spacing slightly. Never solve fit by changing to landscape, cropping, deleting text, or overlapping panels.
- EXACT FOOTER: the first footer line is only the zero-padded page number, slash, and total. The second line is only Java Backend • Easy Notes. Add no label, punctuation, semicolon, period, or extra word.

MODULE: Module 6 — Complete Spring Backend
TITLE (large uppercase, centered, double-underlined): TESTING: JUNIT, MOCKITO + SPRING
EASY DEFINITION (place directly below the title): A test runs code with a known setup and checks that the result matches expected behavior.
LAYOUT BLUEPRINT: Testing pyramid, AAA example, and test-type table.

EXACT PAGE CONTENT
  PANEL 1 — TESTING LEVELS
  - Unit test: one small class/rule without Spring or real infrastructure.
  - Slice test: one Spring area such as MVC or JPA.
  - Integration test: several real parts working together, often with a real database container.
  - End-to-end test: a complete important user journey.
  - Many fast small tests plus fewer broad tests give useful confidence.
  Visual instruction: Pyramid unit → slice/integration → end-to-end.
  PANEL 2 — ARRANGE, ACT, ASSERT
  - Arrange creates input and starting state.
  - Act performs one behavior.
  - Assert checks the visible result.
  - A good test name describes the rule.
  - Tests should be deterministic and not depend on order or sleep timing.
  PANEL 3 — TOOLS
  - JUnit 5 supplies @Test, setup, parameterized tests, and assertions.
  - Mockito creates mocks for collaborator interfaces at a unit boundary.
  - @WebMvcTest checks routing, JSON, validation, security, and controller behavior.
  - @DataJpaTest checks repositories/JPA.
  - @SpringBootTest loads the complete application context.
  - Testcontainers can start real PostgreSQL, Kafka, or Redis for tests.

CODE BOXES (copy exactly, preserve punctuation)
  @Test
  void rejectsNegativeQuantity() {
    var order = new Order();

    var error = assertThrows(IllegalArgumentException.class,
        () -> order.add(product, -1));

    assertEquals("Quantity must be positive", error.getMessage());
  }

FLOWCHART / DIAGRAM
Rule/risk → choose smallest trustworthy test boundary → arrange → act → assert.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Do not use @SpringBootTest for a simple pure Java unit test.
• Mocks are useful at boundaries; mocking every object makes tests fragile.

CHECK YOUR UNDERSTANDING (small bordered box)
? When would you use @WebMvcTest instead of @SpringBootTest?

SUMMARY (lower-right cloud outline)
✓ Small tests give fast feedback.
✓ Broader tests prove framework and infrastructure wiring.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “61 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 62 — LOGGING, METRICS + TRACING

```text
Create ONE finished handwritten educational notes page, page 62 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “62 / 65” at bottom center.
- Avoid: typeset font, calligraphy, illegible pseudo-text, misspelled code, 3D effects, decorative illustrations unrelated to learning, undefined expert jargon, long academic paragraphs.

KNOWN IMAGE-MODEL FAILURE GUARDRAILS — CHECK EVERY RULE BEFORE RENDERING
- PORTRAIT IS NON-NEGOTIABLE: output one vertical A4 sheet at 210:297; width must be smaller than height. Never rotate or use a landscape composition, even when a table or code is wide.
- STYLE DIRECTIONS ARE NOT PAGE CONTENT: never print prompt labels or directions such as Visual instruction, Layout blueprint, Footer, Bottom, orange warning, exact text, or page geometry.
- EXACTLY ONCE: render every supplied heading, bullet, question, and summary point once. Never duplicate, omit, truncate, merge, or invent a bullet. Reject fragments such as cont.
- JAVA CODE IS CASE-SENSITIVE: copy code character-for-character in sentence/mixed case. Never convert code, identifiers, keywords, class names, or method names to all caps.
- PRESERVE CODE STRUCTURE: retain line breaks, indentation, braces, parentheses, semicolons, quotes, comments, and statement order. Check that every statement remains inside its intended class/method/constructor before rendering.
- BODY TEXT USES SENTENCE CASE: uppercase is reserved for the main title and occasional tiny table labels; definitions, bullets, code, and explanations must not become all caps.
- VERSION FACTS STAY INDEPENDENT: place each Java-version fact on its own complete line so wrapping cannot connect the wrong feature to a version.
- NO TECHNICAL-WORD HYPHENATION: do not split identifiers or important terms across lines, for example abstraction, RuntimeException, hashCode, ArrayList, and @Transactional.
- FIT WITHOUT DISTORTION: if content is dense, reduce handwriting size or spacing slightly. Never solve fit by changing to landscape, cropping, deleting text, or overlapping panels.
- EXACT FOOTER: the first footer line is only the zero-padded page number, slash, and total. The second line is only Java Backend • Easy Notes. Add no label, punctuation, semicolon, period, or extra word.

MODULE: Module 6 — Complete Spring Backend
TITLE (large uppercase, centered, double-underlined): LOGGING, METRICS + TRACING
EASY DEFINITION (place directly below the title): Observability means understanding a running system through logs, metrics, and traces.
LAYOUT BLUEPRINT: Three-column signal comparison and one request correlation flow.

EXACT PAGE CONTENT
  PANEL 1 — THREE SIGNALS
  - Logs record individual events with useful context.
  - Metrics are numbers measured over time, such as request count and latency.
  - Traces show one request's path through services and database calls.
  - Use metrics to detect, traces to locate, and logs to explain.
  Visual instruction: Columns Signal | Answers | Example.
  PANEL 2 — GOOD LOGGING
  - Use structured fields such as traceId, orderId, operation, and outcome.
  - ERROR is a real failure, WARN is unexpected/degraded, INFO is a useful milestone, DEBUG is detailed diagnosis.
  - Log a failure at the boundary that handles it instead of at every layer.
  - Never log passwords, tokens, or full sensitive request bodies.
  PANEL 3 — METRICS + HEALTH
  - RED metrics: request Rate, Error rate, and Duration.
  - Use percentiles such as p95/p99; an average can hide slow requests.
  - Do not use userId/orderId as metric labels because they create too many time series.
  - Actuator can expose health and metrics.
  - Readiness means able to receive traffic; liveness means restart may help.
  PANEL 4 — TRACING
  - A trace ID connects work for one request.
  - Spans measure controller, database, HTTP, or message steps.
  - Propagate trace information across service and message boundaries.

CODE BOXES (copy exactly, preserve punctuation)
  log.info("Order created orderId={} total={}",
      order.id(), order.total());

FLOWCHART / DIAGRAM
Request with trace ID → controller span → DB/client spans → metrics + structured logs → dashboard/debug.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Health endpoints must be protected and reveal little detail publicly.
• High-cardinality metric labels can cause high cost and poor performance.

CHECK YOUR UNDERSTANDING (small bordered box)
? Why is orderId good in a log but bad as a metric label?

SUMMARY (lower-right cloud outline)
✓ Metrics tell when, traces tell where, logs explain details.
✓ All signals should share request correlation.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “62 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 63 — CACHING + REDIS

```text
Create ONE finished handwritten educational notes page, page 63 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “63 / 65” at bottom center.
- Avoid: typeset font, calligraphy, illegible pseudo-text, misspelled code, 3D effects, decorative illustrations unrelated to learning, undefined expert jargon, long academic paragraphs.

KNOWN IMAGE-MODEL FAILURE GUARDRAILS — CHECK EVERY RULE BEFORE RENDERING
- PORTRAIT IS NON-NEGOTIABLE: output one vertical A4 sheet at 210:297; width must be smaller than height. Never rotate or use a landscape composition, even when a table or code is wide.
- STYLE DIRECTIONS ARE NOT PAGE CONTENT: never print prompt labels or directions such as Visual instruction, Layout blueprint, Footer, Bottom, orange warning, exact text, or page geometry.
- EXACTLY ONCE: render every supplied heading, bullet, question, and summary point once. Never duplicate, omit, truncate, merge, or invent a bullet. Reject fragments such as cont.
- JAVA CODE IS CASE-SENSITIVE: copy code character-for-character in sentence/mixed case. Never convert code, identifiers, keywords, class names, or method names to all caps.
- PRESERVE CODE STRUCTURE: retain line breaks, indentation, braces, parentheses, semicolons, quotes, comments, and statement order. Check that every statement remains inside its intended class/method/constructor before rendering.
- BODY TEXT USES SENTENCE CASE: uppercase is reserved for the main title and occasional tiny table labels; definitions, bullets, code, and explanations must not become all caps.
- VERSION FACTS STAY INDEPENDENT: place each Java-version fact on its own complete line so wrapping cannot connect the wrong feature to a version.
- NO TECHNICAL-WORD HYPHENATION: do not split identifiers or important terms across lines, for example abstraction, RuntimeException, hashCode, ArrayList, and @Transactional.
- FIT WITHOUT DISTORTION: if content is dense, reduce handwriting size or spacing slightly. Never solve fit by changing to landscape, cropping, deleting text, or overlapping panels.
- EXACT FOOTER: the first footer line is only the zero-padded page number, slash, and total. The second line is only Java Backend • Easy Notes. Add no label, punctuation, semicolon, period, or extra word.

MODULE: Module 7 — Production + Distributed Systems
TITLE (large uppercase, centered, double-underlined): CACHING + REDIS
EASY DEFINITION (place directly below the title): A cache stores a temporary copy of data so later reads can return faster. Redis is a common remote in-memory data store.
LAYOUT BLUEPRINT: Cache-aside numbered flow and problem/solution cards.

EXACT PAGE CONTENT
  PANEL 1 — CACHE-ASIDE
  - 1. Application asks the cache for a key.
  - 2. On a hit, return the cached value.
  - 3. On a miss, read the database.
  - 4. Store the result in cache with an expiry time (TTL).
  - 5. Return the result.
  - After a database update, invalidate or safely update the cached copy.
  Visual instruction: App → Redis hit; miss → DB → Redis → app.
  PANEL 2 — KEY + TTL
  - A key includes every input that changes the result, such as tenant and product ID.
  - TTL limits how long stale data and unused keys stay.
  - Add small random TTL variation so many keys do not expire together.
  - Cache null/missing results briefly only when it safely reduces repeated load.
  PANEL 3 — COMMON PROBLEMS
  - Stale data: cache and database differ.
  - Stampede: many requests miss one hot key and all hit the database.
  - Penetration: repeated missing/random keys reach the database.
  - Redis outage: fallback may overload the database, so use timeouts and capacity limits.
  PANEL 4 — SPRING CACHE
  - @Cacheable reads/stores results; @CacheEvict removes; @CachePut updates.
  - These annotations use proxies, so self-invocation can bypass them.
  - A cache action and database transaction are not automatically one atomic operation.

CODE BOXES (copy exactly, preserve punctuation)
  @Cacheable(cacheNames = "products", key = "#id")
  public ProductResponse getProduct(long id) {
    return repository.findById(id).map(mapper::toResponse)
        .orElseThrow(ProductNotFound::new);
  }

FLOWCHART / DIAGRAM
Request → cache hit return | miss → single loader → database → cache with TTL → return.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Cache is normally a temporary copy; the database remains the source of truth.
• A cache makes reads faster but adds freshness and failure decisions.

CHECK YOUR UNDERSTANDING (small bordered box)
? What is a cache stampede and one way to reduce it?

SUMMARY (lower-right cloud outline)
✓ Cache trades freshness/complexity for speed and lower database load.
✓ Keys, TTL, invalidation, and fallback belong to one design.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “63 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 64 — MESSAGING, KAFKA + OUTBOX

```text
Create ONE finished handwritten educational notes page, page 64 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “64 / 65” at bottom center.
- Avoid: typeset font, calligraphy, illegible pseudo-text, misspelled code, 3D effects, decorative illustrations unrelated to learning, undefined expert jargon, long academic paragraphs.

KNOWN IMAGE-MODEL FAILURE GUARDRAILS — CHECK EVERY RULE BEFORE RENDERING
- PORTRAIT IS NON-NEGOTIABLE: output one vertical A4 sheet at 210:297; width must be smaller than height. Never rotate or use a landscape composition, even when a table or code is wide.
- STYLE DIRECTIONS ARE NOT PAGE CONTENT: never print prompt labels or directions such as Visual instruction, Layout blueprint, Footer, Bottom, orange warning, exact text, or page geometry.
- EXACTLY ONCE: render every supplied heading, bullet, question, and summary point once. Never duplicate, omit, truncate, merge, or invent a bullet. Reject fragments such as cont.
- JAVA CODE IS CASE-SENSITIVE: copy code character-for-character in sentence/mixed case. Never convert code, identifiers, keywords, class names, or method names to all caps.
- PRESERVE CODE STRUCTURE: retain line breaks, indentation, braces, parentheses, semicolons, quotes, comments, and statement order. Check that every statement remains inside its intended class/method/constructor before rendering.
- BODY TEXT USES SENTENCE CASE: uppercase is reserved for the main title and occasional tiny table labels; definitions, bullets, code, and explanations must not become all caps.
- VERSION FACTS STAY INDEPENDENT: place each Java-version fact on its own complete line so wrapping cannot connect the wrong feature to a version.
- NO TECHNICAL-WORD HYPHENATION: do not split identifiers or important terms across lines, for example abstraction, RuntimeException, hashCode, ArrayList, and @Transactional.
- FIT WITHOUT DISTORTION: if content is dense, reduce handwriting size or spacing slightly. Never solve fit by changing to landscape, cropping, deleting text, or overlapping panels.
- EXACT FOOTER: the first footer line is only the zero-padded page number, slash, and total. The second line is only Java Backend • Easy Notes. Add no label, punctuation, semicolon, period, or extra word.

MODULE: Module 7 — Production + Distributed Systems
TITLE (large uppercase, centered, double-underlined): MESSAGING, KAFKA + OUTBOX
EASY DEFINITION (place directly below the title): Messaging lets one part of a system send work or events without waiting for the receiver to finish immediately.
LAYOUT BLUEPRINT: Broker flow, Kafka/RabbitMQ table, and outbox reliability diagram.

EXACT PAGE CONTENT
  PANEL 1 — BASIC FLOW
  - Producer creates a message.
  - Broker stores/routes it.
  - Consumer receives and processes it.
  - Acknowledgement/offset tells the broker how far processing succeeded.
  - Messages may be delivered more than once, so consumer work should be idempotent.
  Visual instruction: Producer → broker → consumer → database; retry/DLQ side path.
  PANEL 2 — KAFKA vs RABBITMQ
  - Kafka: a retained ordered log split into partitions; consumers can replay using offsets.
  - RabbitMQ: exchanges route messages to queues; consumers acknowledge queue deliveries.
  - Kafka order exists inside one partition.
  - A Kafka consumer group shares partitions among its members.
  - Choose based on replay, ordering, routing, throughput, and team operations—not trend.
  Visual instruction: Comparison table Model | Replay | Ordering | Common use.
  PANEL 3 — SAFE MESSAGE
  - Include eventId, type, version, time, correlation ID, and payload.
  - An event describes a fact that happened: OrderCreated.
  - A command asks an owner to do something: ReserveStock.
  - Use compatible schema changes and do not publish secrets/entire ORM entities.
  PANEL 4 — OUTBOX PATTERN
  - Problem: database save succeeds but broker publish fails, or the reverse.
  - In one database transaction, save business data and an outbox row.
  - A relay later publishes the outbox event and retries safely.
  - Duplicates are still possible, so consumers store processed event IDs or use an idempotent update.
  Visual instruction: Transaction bracket around Order + Outbox → relay → broker.

CODE BOXES (copy exactly, preserve punctuation)
  BEGIN;
  INSERT INTO orders(id, status) VALUES (?, 'CREATED');
  INSERT INTO outbox(event_id, type, payload) VALUES (?, 'OrderCreated', ?);
  COMMIT;

FLOWCHART / DIAGRAM
Local transaction [business row + outbox] → relay → broker → idempotent consumer → acknowledge.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• A dead-letter queue holds failed messages but still needs alerts, investigation, and safe replay.
• Exactly-once claims are limited to particular boundaries; prove the final business effect.

CHECK YOUR UNDERSTANDING (small bordered box)
? What problem does the transactional outbox solve?

SUMMARY (lower-right cloud outline)
✓ Messaging separates work in time.
✓ Outbox avoids an unsafe database-and-broker dual write.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “64 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 65 — MICROSERVICES TO DEPLOYMENT — COMPLETE MAP

```text
Create ONE finished handwritten educational notes page, page 65 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “65 / 65” at bottom center.
- Avoid: typeset font, calligraphy, illegible pseudo-text, misspelled code, 3D effects, decorative illustrations unrelated to learning, undefined expert jargon, long academic paragraphs.

KNOWN IMAGE-MODEL FAILURE GUARDRAILS — CHECK EVERY RULE BEFORE RENDERING
- PORTRAIT IS NON-NEGOTIABLE: output one vertical A4 sheet at 210:297; width must be smaller than height. Never rotate or use a landscape composition, even when a table or code is wide.
- STYLE DIRECTIONS ARE NOT PAGE CONTENT: never print prompt labels or directions such as Visual instruction, Layout blueprint, Footer, Bottom, orange warning, exact text, or page geometry.
- EXACTLY ONCE: render every supplied heading, bullet, question, and summary point once. Never duplicate, omit, truncate, merge, or invent a bullet. Reject fragments such as cont.
- JAVA CODE IS CASE-SENSITIVE: copy code character-for-character in sentence/mixed case. Never convert code, identifiers, keywords, class names, or method names to all caps.
- PRESERVE CODE STRUCTURE: retain line breaks, indentation, braces, parentheses, semicolons, quotes, comments, and statement order. Check that every statement remains inside its intended class/method/constructor before rendering.
- BODY TEXT USES SENTENCE CASE: uppercase is reserved for the main title and occasional tiny table labels; definitions, bullets, code, and explanations must not become all caps.
- VERSION FACTS STAY INDEPENDENT: place each Java-version fact on its own complete line so wrapping cannot connect the wrong feature to a version.
- NO TECHNICAL-WORD HYPHENATION: do not split identifiers or important terms across lines, for example abstraction, RuntimeException, hashCode, ArrayList, and @Transactional.
- FIT WITHOUT DISTORTION: if content is dense, reduce handwriting size or spacing slightly. Never solve fit by changing to landscape, cropping, deleting text, or overlapping panels.
- EXACT FOOTER: the first footer line is only the zero-padded page number, slash, and total. The second line is only Java Backend • Easy Notes. Add no label, punctuation, semicolon, period, or extra word.

MODULE: Module 7 — Production + Distributed Systems
TITLE (large uppercase, centered, double-underlined): MICROSERVICES TO DEPLOYMENT — COMPLETE MAP
EASY DEFINITION (place directly below the title): A microservice is an independently deployable service built around a business capability. Production delivery packages, tests, deploys, and operates it safely.
LAYOUT BLUEPRINT: Full-page simple architecture with numbered order flow and compact production checklist.

EXACT PAGE CONTENT
  PANEL 1 — SERVICE BOUNDARIES
  - Start with clear business modules; distribution adds network failures and operational work.
  - A service owns its business rules and data writes.
  - Synchronous HTTP gives an immediate result but connects availability/latency.
  - Asynchronous events allow later reactions but require duplicate and eventual-consistency handling.
  - Keep a modular monolith when independent deployment does not justify microservice cost.
  Visual instruction: Gateway → Order, Payment, Inventory; each owns data.
  PANEL 2 — RESILIENCE
  - Timeout stops waiting after a budget.
  - Retry repeats only transient, safe/idempotent work with backoff and jitter.
  - Circuit breaker temporarily fails fast while a dependency recovers.
  - Bulkhead limits capacity used by one dependency.
  - Saga coordinates service-local transactions and compensation; compensation is a new business action, not database rollback.
  Visual instruction: CLOSED → OPEN → HALF_OPEN breaker plus short Saga arrow.
  PANEL 3 — DOCKER + CI/CD + KUBERNETES
  - Docker image is an immutable package; a container is a running instance.
  - Run as non-root, inject secrets/config at runtime, set memory limits with JVM headroom, and handle SIGTERM gracefully.
  - CI compiles, tests, scans, and publishes one image.
  - CD promotes the same image digest through environments.
  - Kubernetes Deployment manages Pods; Service gives stable networking.
  - Readiness removes an unready Pod from traffic; liveness restarts a stuck one.
  Visual instruction: Commit → CI → image registry → Kubernetes Pods.
  PANEL 4 — END-TO-END ORDER
  - 1 Client POST /orders with authentication and idempotency key.
  - 2 Controller validates DTO; service applies rules.
  - 3 Transaction saves Order + outbox event.
  - 4 API returns 201 Created.
  - 5 Relay publishes OrderCreated.
  - 6 Inventory/notification consumers handle it idempotently.
  - 7 Logs, metrics, and traces follow every step.
  - 8 Docker/Kubernetes run several healthy copies.
  Visual instruction: Numbered full architecture flow.
  PANEL 5 — FINAL REVISION RULE
  - For every topic ask: What is it? Why is it used? Where is it in the request? What can fail? How is it tested and observed?
  - When debugging: define symptom → check metrics/change → follow trace → read correlated logs → test one theory → fix and add a regression test.

CODE BOXES (copy exactly, preserve punctuation)
  No separate code box.

FLOWCHART / DIAGRAM
Client → Gateway/Security → Controller → Service → PostgreSQL [Order+Outbox] → response; Relay → Kafka → consumers; telemetry receives signals from all.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Do not create microservices only because they are popular.
• Every network arrow needs authentication, timeout, failure behavior, and observability.
• Deploy the same tested artifact; change environment configuration outside it.

CHECK YOUR UNDERSTANDING (small bordered box)
? Using the order flow, explain what happens if the client retries after the database committed but before it received the response.

SUMMARY (lower-right cloud outline)
✓ Simple boundaries first; distribute only for a reason.
✓ Reliable backends combine correct code, safe data, security, tests, delivery, and observation.
✓ Trace one request and one event from start to finish.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “65 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```
