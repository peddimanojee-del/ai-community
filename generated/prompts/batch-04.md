# Image Prompts — Batch 4

## Page 31 — LAMBDAS + FUNCTIONAL INTERFACES

```text
Create ONE finished handwritten educational notes page, page 31 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “31 / 65” at bottom center.
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

MODULE: Module 3 — Useful Modern Java
TITLE (large uppercase, centered, double-underlined): LAMBDAS + FUNCTIONAL INTERFACES
EASY DEFINITION (place directly below the title): A lambda is a short way to provide a piece of behavior. A functional interface is an interface with one abstract method.
LAYOUT BLUEPRINT: Anonymous class to lambda transformation; four-interface table below.

EXACT PAGE CONTENT
  PANEL 1 — FROM LONG TO SHORT
  - Before lambdas, a small behavior often needed an anonymous class.
  - A lambda writes parameters, an arrow ->, and the action.
  - The lambda receives its meaning from a functional interface type.
  - Use @FunctionalInterface to clearly mark the intended contract.
  Visual instruction: Long anonymous class shrinks into (x) -> action.
  PANEL 2 — COMMON INTERFACES
  - Predicate<T>: takes T and returns true/false.
  - Function<T,R>: changes T into R.
  - Consumer<T>: accepts T and returns nothing.
  - Supplier<T>: takes nothing and returns T.
  Visual instruction: Table Interface | Shape | Method | Easy example.
  PANEL 3 — METHOD REFERENCE
  - A method reference is a shorter lambda that calls an existing method.
  - name -> print(name) can become System.out::println.
  - Keep lambdas short; move larger logic to a named method.

CODE BOXES (copy exactly, preserve punctuation)
  Predicate<Integer> adultAge = age -> age >= 18;
  Function<String, Integer> length = String::length;
  Consumer<String> print = System.out::println;
  Supplier<UUID> newId = UUID::randomUUID;

FLOWCHART / DIAGRAM
Input → lambda behavior → output; target interface explains input/output types.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• A lambda may use a local variable only when it is final or effectively final.
• Do not hide large business logic inside one long lambda.

CHECK YOUR UNDERSTANDING (small bordered box)
? What are Predicate and Function used for?

SUMMARY (lower-right cloud outline)
✓ Lambda passes behavior as a value.
✓ Functional interfaces give lambdas a clear type.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “31 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 32 — STREAM API — FILTER, MAP + COLLECT

```text
Create ONE finished handwritten educational notes page, page 32 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “32 / 65” at bottom center.
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

MODULE: Module 3 — Useful Modern Java
TITLE (large uppercase, centered, double-underlined): STREAM API — FILTER, MAP + COLLECT
EASY DEFINITION (place directly below the title): A stream is a pipeline that reads data from a source, transforms it, and produces a result.
LAYOUT BLUEPRINT: Large conveyor-belt pipeline with intermediate/terminal table.

EXACT PAGE CONTENT
  PANEL 1 — STREAM PIPELINE
  - Source: a collection, array, or other data source.
  - filter keeps items that match a condition.
  - map changes each item into another value.
  - sorted orders items; distinct removes duplicates.
  - A terminal operation such as toList, count, or collect produces the result.
  Visual instruction: Orders → filter paid → map IDs → sorted → list.
  PANEL 2 — LAZY WORK
  - Intermediate operations are lazy: they wait until a terminal operation starts.
  - A stream is normally used once.
  - A stream does not store the items; the source stores them.
  - Avoid changing shared outside data inside a stream operation.
  PANEL 3 — USEFUL OPERATIONS
  - anyMatch asks whether any item matches.
  - findFirst returns an Optional result.
  - flatMap opens and combines nested groups.
  - groupingBy groups items using a selected value.

CODE BOXES (copy exactly, preserve punctuation)
  List<String> names = users.stream()
      .filter(User::isActive)
      .map(User::getName)
      .sorted()
      .toList();

FLOWCHART / DIAGRAM
Collection → filter → map → sort → terminal result.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Use a normal loop when it is clearer than a stream.
• Parallel streams are not automatically faster and are poor for ordinary blocking database/API calls.

CHECK YOUR UNDERSTANDING (small bordered box)
? What is the difference between filter and map?

SUMMARY (lower-right cloud outline)
✓ Streams describe a data-processing pipeline.
✓ Intermediate steps are lazy; a terminal step starts the work.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “32 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 33 — Optional + DATE/TIME API

```text
Create ONE finished handwritten educational notes page, page 33 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “33 / 65” at bottom center.
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

MODULE: Module 3 — Useful Modern Java
TITLE (large uppercase, centered, double-underlined): Optional + DATE/TIME API
EASY DEFINITION (place directly below the title): Optional represents a result that may be present or absent. java.time classes represent dates and time clearly.
LAYOUT BLUEPRINT: Left Optional railway; right time-type choice table.

EXACT PAGE CONTENT
  PANEL 1 — OPTIONAL
  - Optional.of(value) holds a non-null value.
  - Optional.empty() represents no value.
  - Use map, orElseGet, and orElseThrow instead of immediately calling get().
  - It is most useful as a method return type when absence is normal.
  Visual instruction: Present track → map; empty track → fallback/throw.
  PANEL 2 — TIME TYPES
  - LocalDate: a date such as 2026-09-27.
  - LocalTime: time of day without a date.
  - LocalDateTime: date and time but no zone/offset.
  - Instant: one exact moment on the global timeline.
  - ZonedDateTime: date/time with time-zone rules.
  - Duration measures time; Period measures calendar dates.
  Visual instruction: Type | Contains | Easy use table.
  PANEL 3 — TESTABLE TIME
  - Use Clock as a dependency when code needs the current time.
  - Store global event times as Instant/UTC in many backend systems.
  - Convert to a user's zone when displaying time.

CODE BOXES (copy exactly, preserve punctuation)
  User user = repository.findById(id)
      .orElseThrow(() -> new UserNotFound(id));

  Instant now = clock.instant();
  LocalDate today = LocalDate.now(clock);

FLOWCHART / DIAGRAM
Could result be absent? → Optional return. Need exact event moment? → Instant. Human calendar date? → LocalDate.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• orElse creates its fallback immediately; orElseGet creates it only when needed.
• LocalDateTime alone does not identify one global moment.

CHECK YOUR UNDERSTANDING (small bordered box)
? What is the difference between Instant and LocalDateTime?

SUMMARY (lower-right cloud outline)
✓ Optional clearly shows possible absence.
✓ Choose a time type that contains the information you need.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “33 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 34 — FILES + INPUT/OUTPUT STREAMS

```text
Create ONE finished handwritten educational notes page, page 34 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “34 / 65” at bottom center.
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

MODULE: Module 3 — Useful Modern Java
TITLE (large uppercase, centered, double-underlined): FILES + INPUT/OUTPUT STREAMS
EASY DEFINITION (place directly below the title): Input means reading data; output means writing data. Java streams move bytes or characters between a program and another place.
LAYOUT BLUEPRINT: Byte/character comparison and file read/write lifecycle.

EXACT PAGE CONTENT
  PANEL 1 — BYTE vs CHARACTER
  - InputStream and OutputStream work with raw bytes, useful for images and binary files.
  - Reader and Writer work with characters, useful for text.
  - Buffered versions reduce expensive small read/write operations.
  - Files utility methods provide simple operations for paths and small files.
  Visual instruction: Binary file → byte stream; text file → reader/writer.
  PANEL 2 — PATH + FILES
  - Path represents a file-system path.
  - Files.exists checks existence.
  - Files.readString/writeString are convenient for small text files.
  - Large files should be streamed instead of fully loaded into memory.
  PANEL 3 — SAFE USE
  - Use try-with-resources so open files close.
  - Choose the correct character encoding, commonly UTF-8.
  - Validate file names/paths when they come from users to prevent path traversal.

CODE BOXES (copy exactly, preserve punctuation)
  Path path = Path.of("notes.txt");
  Files.writeString(path, "Hello", UTF_8);
  String text = Files.readString(path, UTF_8);

  try (var lines = Files.lines(path)) {
    lines.forEach(System.out::println);
  }

FLOWCHART / DIAGRAM
Path → open → read/write in chunks → close automatically.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• A file is outside Java heap memory, but loaded file contents use heap memory.
• Never trust a user-provided file path without validation.

CHECK YOUR UNDERSTANDING (small bordered box)
? When would you use Reader instead of InputStream?

SUMMARY (lower-right cloud outline)
✓ Byte streams handle binary; character streams handle text.
✓ Close resources and choose encoding explicitly.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “34 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 35 — THREADS + CONCURRENCY BASICS

```text
Create ONE finished handwritten educational notes page, page 35 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “35 / 65” at bottom center.
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

MODULE: Module 3 — Useful Modern Java
TITLE (large uppercase, centered, double-underlined): THREADS + CONCURRENCY BASICS
EASY DEFINITION (place directly below the title): A thread is one path of work inside a program. Concurrency means several tasks can make progress during the same time period.
LAYOUT BLUEPRINT: Thread lifecycle on top; race-condition timeline below.

EXACT PAGE CONTENT
  PANEL 1 — WHY THREADS?
  - A server handles many user requests, often using many threads.
  - Concurrency can improve responsiveness and throughput.
  - More threads do not always mean more speed; CPU and other resources are limited.
  - Call start() to begin a new thread; directly calling run() is a normal method call.
  Visual instruction: Thread states: NEW → RUNNABLE → WAITING/BLOCKED → TERMINATED.
  PANEL 2 — RACE CONDITION
  - A race happens when threads read/write shared data without safe coordination.
  - count++ is read, add, and write—not one guaranteed atomic step.
  - Two threads may both read 10 and both write 11, losing one update.
  - Prefer immutable/local data before adding locks.
  Visual instruction: Two-thread timeline showing lost update.
  PANEL 3 — SAFE TOOLS
  - synchronized allows one thread at a time in a protected section and makes changes visible.
  - volatile helps visibility for one variable but does not make count++ atomic.
  - AtomicInteger provides atomic operations for a single integer value.

CODE BOXES (copy exactly, preserve punctuation)
  private final AtomicInteger count = new AtomicInteger();

  void increment() {
    count.incrementAndGet();
  }

FLOWCHART / DIAGRAM
Shared mutable data? → avoid sharing if possible → otherwise choose atomic value or protected critical section.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• sleep pauses a thread but does not release a lock it holds.
• Interruption is a cooperative request for a thread to stop/wake, not a forced kill.

CHECK YOUR UNDERSTANDING (small bordered box)
? Why is volatile not enough for count++?

SUMMARY (lower-right cloud outline)
✓ Threads allow concurrent work.
✓ Shared changing data needs a safety plan.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “35 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 36 — EXECUTORS + CompletableFuture

```text
Create ONE finished handwritten educational notes page, page 36 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “36 / 65” at bottom center.
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

MODULE: Module 3 — Useful Modern Java
TITLE (large uppercase, centered, double-underlined): EXECUTORS + CompletableFuture
EASY DEFINITION (place directly below the title): An Executor manages worker threads for us. CompletableFuture represents work that may finish later.
LAYOUT BLUEPRINT: Executor queue diagram and future composition railway.

EXACT PAGE CONTENT
  PANEL 1 — EXECUTOR
  - Submit a Runnable when no result is needed.
  - Submit a Callable<T> when a result is needed.
  - A thread pool reuses a limited number of worker threads.
  - A bounded queue prevents unlimited waiting tasks from filling memory.
  - Shut down an executor when its owner stops.
  Visual instruction: Tasks → bounded queue → worker threads → results.
  PANEL 2 — CompletableFuture
  - supplyAsync starts work that returns a value.
  - thenApply changes a completed value.
  - thenCompose starts a next async step and avoids a nested future.
  - thenCombine joins independent results.
  - exceptionally can provide a fallback for a failure.
  PANEL 3 — LIMITS
  - Always use timeouts for remote work.
  - Choose an intentional executor for blocking work.
  - Async code does not make a slow database faster.
  - Modern virtual threads make many blocking tasks cheaper, but downstream limits still matter.

CODE BOXES (copy exactly, preserve punctuation)
  CompletableFuture<User> user =
      CompletableFuture.supplyAsync(() -> loadUser(id), pool);

  return user.thenApply(UserResponse::from)
             .orTimeout(1, SECONDS);

FLOWCHART / DIAGRAM
Submit task → queue → worker executes → future completes → next step or error path.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• A very large pool can overload the database or another service.
• thenApply maps a value; thenCompose connects another future.

CHECK YOUR UNDERSTANDING (small bordered box)
? What is the difference between thenApply and thenCompose?

SUMMARY (lower-right cloud outline)
✓ Executors control thread resources.
✓ CompletableFuture connects work that finishes later.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “36 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 37 — JVM MEMORY + GARBAGE COLLECTION

```text
Create ONE finished handwritten educational notes page, page 37 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “37 / 65” at bottom center.
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

MODULE: Module 3 — Useful Modern Java
TITLE (large uppercase, centered, double-underlined): JVM MEMORY + GARBAGE COLLECTION
EASY DEFINITION (place directly below the title): The JVM uses several memory areas. Garbage collection automatically frees heap objects that are no longer reachable.
LAYOUT BLUEPRINT: Large labeled memory map and reachable-object drawing.

EXACT PAGE CONTENT
  PANEL 1 — MEMORY AREAS
  - Heap: most objects and arrays; shared by threads.
  - Stack: each thread's method calls and local working values.
  - Metaspace: class information in native memory.
  - Code cache: machine code created by the JIT compiler.
  - Direct/native memory: buffers, thread stacks, and native libraries outside the heap.
  Visual instruction: One process split into heap, per-thread stacks, metaspace, code cache, native.
  PANEL 2 — GARBAGE COLLECTION
  - GC starts from roots such as active thread stacks and static references.
  - Objects reachable from roots stay alive.
  - Unreachable objects may be collected.
  - GC manages memory, but it does not close files or database connections for us.
  Visual instruction: Green reachable graph and faded unreachable island.
  PANEL 3 — COMMON PROBLEMS
  - StackOverflowError often comes from endless/deep recursion.
  - OutOfMemoryError means a memory area could not provide more space.
  - An unbounded cache or list can keep unwanted objects reachable.
  - Use measurements, GC logs, thread dumps, heap dumps, and Java Flight Recorder to investigate.

CODE BOXES (copy exactly, preserve punctuation)
  No separate code box.

FLOWCHART / DIAGRAM
Create object → reachable while used → no path from roots → eligible for collection.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• A Java memory leak means unwanted objects are still reachable.
• Do not call System.gc() as a normal fix.

CHECK YOUR UNDERSTANDING (small bordered box)
? Can Java have a memory leak even with garbage collection?

SUMMARY (lower-right cloud outline)
✓ Heap stores objects; stacks hold thread method work.
✓ GC removes unreachable objects.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “37 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 38 — SOLID PRINCIPLES — EASY VERSION

```text
Create ONE finished handwritten educational notes page, page 38 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “38 / 65” at bottom center.
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

MODULE: Module 4 — Design, Build + Web Basics
TITLE (large uppercase, centered, double-underlined): SOLID PRINCIPLES — EASY VERSION
EASY DEFINITION (place directly below the title): SOLID is a set of five design ideas that help code stay understandable and easier to change.
LAYOUT BLUEPRINT: Five reference-style rows with simple definition and example.

EXACT PAGE CONTENT
  PANEL 1 — S — SINGLE RESPONSIBILITY
  - A class should have one main reason to change.
  - OrderService should not also generate PDFs and send every email.
  Visual instruction: Large mixed class splits into focused helpers.
  PANEL 2 — O — OPEN/CLOSED
  - Add a new behavior with a safe extension instead of repeatedly changing stable code.
  - PaymentStrategy can gain a new payment type.
  PANEL 3 — L — LISKOV SUBSTITUTION
  - A child implementation must keep the promise of its parent type.
  - A subtype should not surprise callers by rejecting valid parent operations.
  PANEL 4 — I — INTERFACE SEGREGATION
  - Prefer small useful interfaces over one huge interface.
  - A reader should not be forced to implement write methods.
  PANEL 5 — D — DEPENDENCY INVERSION
  - Business code depends on a useful contract, not directly on vendor/database details.
  - CheckoutService depends on PaymentGateway.

CODE BOXES (copy exactly, preserve punctuation)
  class CheckoutService {
    private final PaymentGateway gateway;

    CheckoutService(PaymentGateway gateway) {
      this.gateway = gateway;
    }
  }

FLOWCHART / DIAGRAM
Find responsibility → find change point → create smallest clear boundary → test the behavior.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• SOLID is guidance, not a rule to create the maximum number of classes.
• Create an abstraction only when it makes the design clearer.

CHECK YOUR UNDERSTANDING (small bordered box)
? Explain one SOLID principle with a simple example.

SUMMARY (lower-right cloud outline)
✓ SOLID helps separate responsibilities and changes.
✓ Simple code is more important than blindly following a pattern.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “38 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 39 — COMMON DESIGN PATTERNS

```text
Create ONE finished handwritten educational notes page, page 39 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “39 / 65” at bottom center.
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

MODULE: Module 4 — Design, Build + Web Basics
TITLE (large uppercase, centered, double-underlined): COMMON DESIGN PATTERNS
EASY DEFINITION (place directly below the title): A design pattern is a common way to solve a problem that appears again and again in software.
LAYOUT BLUEPRINT: Four pattern cards with problem, shape, and backend example.

EXACT PAGE CONTENT
  PANEL 1 — FACTORY
  - Problem: the program must choose which object to create.
  - Factory keeps creation/selection in one place.
  - Example: NotificationFactory returns EmailSender or SmsSender.
  Visual instruction: Input type → Factory → chosen object.
  PANEL 2 — BUILDER
  - Problem: an object has many optional construction values.
  - Builder names each value and creates the final object.
  - Example: building an HTTP request or test data.
  PANEL 3 — STRATEGY
  - Problem: one task has several interchangeable ways.
  - Each strategy follows one contract.
  - Example: CardPayment and UpiPayment implement PaymentStrategy.
  PANEL 4 — ADAPTER + DECORATOR
  - Adapter changes an external API into the interface our app expects.
  - Decorator wraps an object to add logging, caching, metrics, or retry.
  - Spring often uses proxies with decorator-like behavior.

CODE BOXES (copy exactly, preserve punctuation)
  PaymentStrategy strategy = strategies.get(type);
  PaymentResult result = strategy.pay(command);

FLOWCHART / DIAGRAM
Repeated design problem → understand trade-offs → choose smallest useful pattern → keep code readable.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Patterns are names for solutions, not goals by themselves.
• Singleton means one instance in a particular container/context, not one object in the whole distributed system.

CHECK YOUR UNDERSTANDING (small bordered box)
? What problem does the Strategy pattern solve?

SUMMARY (lower-right cloud outline)
✓ Patterns give developers a shared design language.
✓ Use one only when it makes the problem simpler.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “39 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 40 — MAVEN, PROJECT STRUCTURE + GIT

```text
Create ONE finished handwritten educational notes page, page 40 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “40 / 65” at bottom center.
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

MODULE: Module 4 — Design, Build + Web Basics
TITLE (large uppercase, centered, double-underlined): MAVEN, PROJECT STRUCTURE + GIT
EASY DEFINITION (place directly below the title): Maven builds Java projects and manages libraries. Git records code changes and helps a team work together.
LAYOUT BLUEPRINT: Maven lifecycle at top, project tree and Git flow below.

EXACT PAGE CONTENT
  PANEL 1 — MAVEN
  - pom.xml describes the project, dependencies, plugins, and settings.
  - A dependency is a library the code uses.
  - A plugin performs build work.
  - Common flow: validate → compile → test → package → verify → install.
  - Maven Wrapper (mvnw) helps a team use the intended Maven version.
  Visual instruction: Long lifecycle arrow.
  PANEL 2 — PROJECT STRUCTURE
  - src/main/java contains application Java code.
  - src/main/resources contains configuration/templates/static resources.
  - src/test/java contains tests.
  - target contains generated build output and should not be committed.
  - Grouping code by business feature often keeps related work together.
  PANEL 3 — GIT FLOW
  - Create a small branch/change, make focused commits, and open a pull request.
  - Automated checks and review run before merging.
  - Never commit passwords, secret keys, target output, or personal IDE files.

CODE BOXES (copy exactly, preserve punctuation)
  ./mvnw clean verify
  ./mvnw spring-boot:run
  git status
  git add .
  git commit -m "Add order validation"

FLOWCHART / DIAGRAM
Source + pom.xml → compile → test → package JAR → deploy; Git commit → review → main.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Use dependency:tree to understand library version conflicts.
• A secret remains in old Git history even after deleting it from the latest file.

CHECK YOUR UNDERSTANDING (small bordered box)
? What is the difference between a Maven dependency and plugin?

SUMMARY (lower-right cloud outline)
✓ Maven makes builds repeatable.
✓ Git records and reviews code changes.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “40 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```
