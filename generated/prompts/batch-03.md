# Image Prompts — Batch 3

## Page 21 — STRING, STRINGBUILDER + STRING POOL

```text
Create ONE finished handwritten educational notes page, page 21 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “21 / 65” at bottom center.
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

MODULE: Module 2 — Object-Oriented Java
TITLE (large uppercase, centered, double-underlined): STRING, STRINGBUILDER + STRING POOL
EASY DEFINITION (place directly below the title): String represents text. String objects are immutable, meaning their text cannot be changed after creation.
LAYOUT BLUEPRINT: Top string pool drawing. Middle method examples. Bottom comparison table.

EXACT PAGE CONTENT
  PANEL 1 — STRING IMMUTABILITY
  - A String operation returns a new String instead of changing the old one.
  - Immutability makes String safe to share and suitable as a map key.
  - String literals with the same text can share one object in the string pool.
  - new String(...) normally creates a separate object.
  Visual instruction: Two literal references point to one pooled 'Java'; new String points outside.
  PANEL 2 — USEFUL METHODS
  - length gives character count.
  - equals compares text; equalsIgnoreCase ignores letter case.
  - substring takes part of the text.
  - trim/strip removes surrounding whitespace.
  - split separates text into parts.
  PANEL 3 — BUILDING TEXT
  - Repeated + inside a loop can create many temporary String objects.
  - StringBuilder is mutable and efficient for building text on one thread.
  - StringBuffer is synchronized and is less commonly needed.

CODE BOXES (copy exactly, preserve punctuation)
  String name = "Java";
  String upper = name.toUpperCase();

  StringBuilder text = new StringBuilder();
  text.append("Order: ").append(42);
  String result = text.toString();

FLOWCHART / DIAGRAM
Original String → operation → new String; StringBuilder → many appends → final String.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Use equals, not ==, for String content.
• A String can be empty ("") or null; they are different.

CHECK YOUR UNDERSTANDING (small bordered box)
? Why does name.toUpperCase() not change the original String?

SUMMARY (lower-right cloud outline)
✓ String is immutable text.
✓ StringBuilder is useful for repeated text building.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “21 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 22 — WRAPPER CLASSES, ENUMS + RECORDS

```text
Create ONE finished handwritten educational notes page, page 22 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “22 / 65” at bottom center.
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

MODULE: Module 2 — Object-Oriented Java
TITLE (large uppercase, centered, double-underlined): WRAPPER CLASSES, ENUMS + RECORDS
EASY DEFINITION (place directly below the title): Wrapper classes turn primitive values into objects; enums define fixed choices; records define small data carriers.
LAYOUT BLUEPRINT: Three reference-style rows with definition, example, and use.

EXACT PAGE CONTENT
  PANEL 1 — WRAPPER CLASSES
  - Integer wraps int, Long wraps long, Double wraps double, and Boolean wraps boolean.
  - Generics and collections use objects, so List<Integer> is used instead of List<int>.
  - Autoboxing converts primitive to wrapper; unboxing converts back.
  - A wrapper may be null, which can cause a problem during unboxing.
  Visual instruction: int 5 ↔ Integer object.
  PANEL 2 — ENUM
  - An enum lists a fixed set of named values.
  - It is safer than passing random text for a known choice.
  - Enums may contain fields, constructors, and methods.
  - Example states: NEW, PAID, SHIPPED.
  PANEL 3 — RECORD
  - A record is a short way to create a data-focused class.
  - It creates a constructor, accessors, equals, hashCode, and toString.
  - Its fields cannot be reassigned, but an object stored inside can still be mutable.

CODE BOXES (copy exactly, preserve punctuation)
  enum OrderStatus { NEW, PAID, SHIPPED }

  record UserResponse(long id, String name) {}

  List<Integer> scores = List.of(10, 20);

FLOWCHART / DIAGRAM
Simple number → wrapper when object is needed; fixed choices → enum; small data result → record.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Compare enum values with ==.
• Do not use a wrapper as a field when a primitive clearly cannot be absent.

CHECK YOUR UNDERSTANDING (small bordered box)
? Why does List<int> not work, but List<Integer> does?

SUMMARY (lower-right cloud outline)
✓ Wrappers provide object forms of primitives.
✓ Enums name fixed choices; records carry data concisely.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “22 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 23 — EXCEPTIONS + try-catch-finally

```text
Create ONE finished handwritten educational notes page, page 23 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “23 / 65” at bottom center.
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

MODULE: Module 2 — Object-Oriented Java
TITLE (large uppercase, centered, double-underlined): EXCEPTIONS + try-catch-finally
EASY DEFINITION (place directly below the title): An exception is an object that tells us something unexpected stopped the normal flow of a program.
LAYOUT BLUEPRINT: Throwable tree on top; try/catch flow and good practices below.

EXACT PAGE CONTENT
  PANEL 1 — EXCEPTION FAMILY
  - Throwable is the top type.
  - Error usually represents a serious JVM/system problem an application does not normally handle.
  - Exception represents problems application code may report or handle.
  - RuntimeException is unchecked; other common Exception types are checked by the compiler.
  Visual instruction: Tree Throwable → Error and Exception → RuntimeException.
  PANEL 2 — TRY, CATCH, FINALLY
  - try contains code that may fail.
  - catch handles a matching exception.
  - finally runs after try/catch for cleanup in normal cases.
  - Do not use a wide catch(Exception) unless that boundary can handle it properly.
  PANEL 3 — GOOD ERROR HANDLING
  - Catch an exception only when you can recover, add useful context, or translate it.
  - Keep the original cause when creating another exception.
  - Never ignore an exception with an empty catch block.
  - Do not show stack traces or database details to API users.

CODE BOXES (copy exactly, preserve punctuation)
  try {
    int value = Integer.parseInt(input);
    System.out.println(value);
  } catch (NumberFormatException ex) {
    System.out.println("Please enter a number");
  } finally {
    System.out.println("Finished");
  }

FLOWCHART / DIAGRAM
Normal work → problem thrown → matching catch → continue or return safe error.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Checked exceptions must be caught or declared; unchecked exceptions do not have that compiler rule.
• Exceptions should not be used as normal loop or decision logic.

CHECK YOUR UNDERSTANDING (small bordered box)
? What is the job of try, catch, and finally?

SUMMARY (lower-right cloud outline)
✓ Exceptions describe failed program flow.
✓ Handle them at a place that can make a useful decision.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “23 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 24 — CUSTOM EXCEPTIONS + RESOURCE SAFETY

```text
Create ONE finished handwritten educational notes page, page 24 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “24 / 65” at bottom center.
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

MODULE: Module 2 — Object-Oriented Java
TITLE (large uppercase, centered, double-underlined): CUSTOM EXCEPTIONS + RESOURCE SAFETY
EASY DEFINITION (place directly below the title): A custom exception gives a failure a clear application meaning. Try-with-resources closes resources automatically.
LAYOUT BLUEPRINT: Left exception translation ladder; right resource lifecycle.

EXACT PAGE CONTENT
  PANEL 1 — CUSTOM EXCEPTION
  - Create one when the failure has a useful domain meaning such as OrderNotFound.
  - Give it a clear name and useful safe information.
  - Pass the original exception as the cause when translating a lower-level failure.
  - Do not create a different exception class for every tiny message.
  Visual instruction: Database error → OrderLoadException → safe API response.
  PANEL 2 — TRY-WITH-RESOURCES
  - Files, streams, and database resources must be closed.
  - A resource implementing AutoCloseable can be declared inside try(...).
  - Java closes resources automatically, even when work throws an exception.
  - Resources close in reverse order of creation.

CODE BOXES (copy exactly, preserve punctuation)
  class OrderNotFoundException extends RuntimeException {
    OrderNotFoundException(long id) {
      super("Order not found: " + id);
    }
  }

  try (var reader = Files.newBufferedReader(path)) {
    return reader.readLine();
  }

FLOWCHART / DIAGRAM
Open resource → use resource → success or exception → automatic close.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Garbage collection does not replace closing files and database connections.
• Public error messages must not expose secrets or internal system details.

CHECK YOUR UNDERSTANDING (small bordered box)
? Why is try-with-resources safer than manually closing a file?

SUMMARY (lower-right cloud outline)
✓ Custom exceptions give failures clear meaning.
✓ Try-with-resources makes cleanup reliable.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “24 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 25 — GENERICS — TYPE-SAFE REUSABLE CODE

```text
Create ONE finished handwritten educational notes page, page 25 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “25 / 65” at bottom center.
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

MODULE: Module 2 — Object-Oriented Java
TITLE (large uppercase, centered, double-underlined): GENERICS — TYPE-SAFE REUSABLE CODE
EASY DEFINITION (place directly below the title): Generics let one class or method work with different types while the compiler still checks type safety.
LAYOUT BLUEPRINT: Before/after boxes and type parameter anatomy.

EXACT PAGE CONTENT
  PANEL 1 — WHY GENERICS?
  - Without generics, an Object container needs casts and may fail at runtime.
  - With Box<String>, the compiler knows only String values belong there.
  - A type parameter such as T is a placeholder for a real type.
  - Generics make collections and reusable APIs safer.
  Visual instruction: Object box with unsafe cast versus Box<String> with compiler check.
  PANEL 2 — COMMON FORMS
  - Class: Box<T>.
  - Two types: Map<K,V> for key and value.
  - Method: <T> T first(List<T> items).
  - Bound: <T extends Number> accepts Number subtypes.
  PANEL 3 — IMPORTANT LIMIT
  - List<Integer> is not a child of List<Number>.
  - Most generic type details are removed at runtime; this is called type erasure.
  - Primitive types cannot be type arguments; use wrappers such as Integer.

CODE BOXES (copy exactly, preserve punctuation)
  class Box<T> {
    private T value;
    void set(T value) { this.value = value; }
    T get() { return value; }
  }

  Box<String> box = new Box<>();

FLOWCHART / DIAGRAM
Write generic T once → use as String, Integer, Order, and other reference types.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Avoid raw List or Box because it removes useful compiler checks.
• Use clear type names such as T, K, V, or descriptive names in complex code.

CHECK YOUR UNDERSTANDING (small bordered box)
? What problem does Box<T> solve compared with storing Object?

SUMMARY (lower-right cloud outline)
✓ Generics provide reusable code with type safety.
✓ The compiler catches many wrong-type mistakes early.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “25 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 26 — WILDCARDS + PECS

```text
Create ONE finished handwritten educational notes page, page 26 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “26 / 65” at bottom center.
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

MODULE: Module 2 — Object-Oriented Java
TITLE (large uppercase, centered, double-underlined): WILDCARDS + PECS
EASY DEFINITION (place directly below the title): A wildcard ? means an unknown type. It helps a method accept a safe family of generic types.
LAYOUT BLUEPRINT: Producer/consumer two-column table with arrows and small examples.

EXACT PAGE CONTENT
  PANEL 1 — ? extends — PRODUCER
  - List<? extends Number> means a list of some Number subtype.
  - We can safely read its items as Number.
  - We cannot safely add an Integer because the real list might be List<Double>.
  - Remember: a producer gives values to us.
  Visual instruction: List<Integer>/List<Double> arrows into read Number.
  PANEL 2 — ? super — CONSUMER
  - List<? super Integer> means a list that can receive Integer values.
  - We may add an Integer safely.
  - When reading, only Object is guaranteed.
  - Remember: a consumer accepts values from us.
  PANEL 3 — PECS RULE
  - Producer Extends, Consumer Super.
  - Use exact List<T> when the method both reads and writes T.
  - Use a named T when parameter and return types must be connected.

CODE BOXES (copy exactly, preserve punctuation)
  double sum(List<? extends Number> values) {
    return values.stream()
        .mapToDouble(Number::doubleValue).sum();
  }

  void addId(List<? super Long> out) {
    out.add(10L);
  }

FLOWCHART / DIAGRAM
Only read T? → extends. Only add T? → super. Read and add T? → exact type.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Wildcards are mainly useful in method/API boundaries.
• Do not return complicated wildcard types unless callers truly need them.

CHECK YOUR UNDERSTANDING (small bordered box)
? Explain PECS in one sentence.

SUMMARY (lower-right cloud outline)
✓ extends is good for reading.
✓ super is good for adding.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “26 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 27 — COLLECTIONS FRAMEWORK OVERVIEW

```text
Create ONE finished handwritten educational notes page, page 27 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “27 / 65” at bottom center.
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

MODULE: Module 2 — Object-Oriented Java
TITLE (large uppercase, centered, double-underlined): COLLECTIONS FRAMEWORK OVERVIEW
EASY DEFINITION (place directly below the title): A collection stores and organizes a group of objects. Different collection types provide different rules.
LAYOUT BLUEPRINT: Large hierarchy tree and four-question choice guide.

EXACT PAGE CONTENT
  PANEL 1 — MAIN INTERFACES
  - List keeps item positions and allows duplicates.
  - Set keeps unique items.
  - Queue keeps items waiting to be processed.
  - Deque works at both ends and can act as queue or stack.
  - Map stores key-value pairs and is not a child of Collection.
  Visual instruction: Iterable → Collection → List/Set/Queue → Deque; separate Map branch.
  PANEL 2 — CHOOSE BY NEED
  - Need position/order and duplicates? List.
  - Need uniqueness? Set.
  - Need lookup by key? Map.
  - Need first/next work item? Queue.
  - Need sorted data? Choose a sorted implementation such as TreeSet/TreeMap.
  PANEL 3 — INTERFACE + IMPLEMENTATION
  - Declare the general interface when possible: List<String>.
  - Choose an implementation for behavior: new ArrayList<>().
  - Most normal collections are not safe for changing from many threads at once.

CODE BOXES (copy exactly, preserve punctuation)
  List<String> names = new ArrayList<>();
  Set<String> uniqueNames = new HashSet<>();
  Map<Long, String> nameById = new HashMap<>();

FLOWCHART / DIAGRAM
What rule do the items need? → List / Set / Queue / Map → choose implementation.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Collections store objects, so primitives use wrappers.
• Ordering, uniqueness, and thread safety are part of correctness.

CHECK YOUR UNDERSTANDING (small bordered box)
? When would you choose Set instead of List?

SUMMARY (lower-right cloud outline)
✓ Collection type describes the rule for stored items.
✓ Choose by behavior, not habit.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “27 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 28 — LIST, SET, QUEUE + DEQUE

```text
Create ONE finished handwritten educational notes page, page 28 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “28 / 65” at bottom center.
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

MODULE: Module 2 — Object-Oriented Java
TITLE (large uppercase, centered, double-underlined): LIST, SET, QUEUE + DEQUE
EASY DEFINITION (place directly below the title): List, Set, Queue, and Deque are collection interfaces made for different ways of storing and reading items.
LAYOUT BLUEPRINT: Four reference-style rows: meaning, implementations, example, caution.

EXACT PAGE CONTENT
  PANEL 1 — LIST
  - ArrayList uses a resizable array and is the common general choice.
  - It gives fast index access; middle insert/remove may shift items.
  - LinkedList uses linked nodes and has slow index access.
  Visual instruction: Array boxes with index numbers.
  PANEL 2 — SET
  - HashSet gives expected fast membership checks and no sorted order.
  - LinkedHashSet keeps insertion order.
  - TreeSet keeps sorted order.
  - Uniqueness depends on equals and hashCode (or comparison for sorted sets).
  PANEL 3 — QUEUE + DEQUE
  - Queue normally processes the next item first.
  - offer adds, poll removes, and peek reads the head without removing.
  - ArrayDeque is a good normal queue/stack implementation.
  - PriorityQueue returns the highest-priority head, not fully sorted iteration.

CODE BOXES (copy exactly, preserve punctuation)
  List<String> list = new ArrayList<>();
  list.add("A");

  Set<String> set = new HashSet<>();
  set.add("A");

  Deque<String> jobs = new ArrayDeque<>();
  jobs.offerLast("email");

FLOWCHART / DIAGRAM
Items → need position? List; unique? Set; processing order? Queue/Deque.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• ArrayList is often faster than LinkedList in real programs because arrays use memory efficiently.
• Do not depend on HashSet iteration order.

CHECK YOUR UNDERSTANDING (small bordered box)
? What do offer, poll, and peek do?

SUMMARY (lower-right cloud outline)
✓ List = position; Set = unique; Queue = next item.
✓ Implementation decides ordering and speed.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “28 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 29 — Map + HashMap INTERNALS

```text
Create ONE finished handwritten educational notes page, page 29 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “29 / 65” at bottom center.
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

MODULE: Module 2 — Object-Oriented Java
TITLE (large uppercase, centered, double-underlined): Map + HashMap INTERNALS
EASY DEFINITION (place directly below the title): A Map stores a value under a unique key. HashMap uses a key's hashCode and equals methods to find its entry.
LAYOUT BLUEPRINT: Top map picture. Middle put/get flow. Bottom implementation comparison.

EXACT PAGE CONTENT
  PANEL 1 — MAP BASICS
  - put(key,value) adds or replaces a value.
  - get(key) returns the matching value or null when none is found.
  - containsKey checks whether a key exists.
  - Keys are unique; different keys may point to equal values.
  Visual instruction: ID keys on left point to Customer values on right.
  PANEL 2 — HOW HashMap FINDS A KEY
  - 1. Call key.hashCode().
  - 2. Use the hash to choose a bucket.
  - 3. Check equals among keys in that bucket.
  - 4. Return/replace/add the matching entry.
  - Different keys may have the same hash; this is called a collision.
  Visual instruction: Bucket array with two keys in one bucket.
  PANEL 3 — OTHER MAPS
  - LinkedHashMap keeps insertion or configured access order.
  - TreeMap keeps keys sorted.
  - ConcurrentHashMap supports safe concurrent operations and does not allow null keys/values.

CODE BOXES (copy exactly, preserve punctuation)
  Map<Long, String> users = new HashMap<>();
  users.put(10L, "Asha");
  String name = users.get(10L);

FLOWCHART / DIAGRAM
Key → hashCode → bucket → equals check → value.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Do not change fields used by a key's equals/hashCode while it is in the map.
• HashMap allows one null key, but using null often makes code less clear.

CHECK YOUR UNDERSTANDING (small bordered box)
? What happens when two different keys have the same hash code?

SUMMARY (lower-right cloud outline)
✓ Map connects keys to values.
✓ hashCode narrows the search; equals confirms the key.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “29 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 30 — Comparable vs Comparator

```text
Create ONE finished handwritten educational notes page, page 30 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “30 / 65” at bottom center.
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

MODULE: Module 2 — Object-Oriented Java
TITLE (large uppercase, centered, double-underlined): Comparable vs Comparator
EASY DEFINITION (place directly below the title): Comparable defines a type's natural order. Comparator defines a separate chosen order.
LAYOUT BLUEPRINT: Two-column comparison table and sorting examples.

EXACT PAGE CONTENT
  PANEL 1 — COMPARABLE
  - The class implements Comparable<T>.
  - It defines compareTo(T other).
  - It is used for one main natural order.
  - Example: sort Product naturally by product code.
  Visual instruction: Class owns one natural-order arrow.
  PANEL 2 — COMPARATOR
  - It is a separate object/function.
  - It defines compare(a,b).
  - A type can have many comparators.
  - Example: sort Product by price, name, or newest date.
  PANEL 3 — RETURN VALUE
  - Negative means first value comes before second.
  - Zero means equal in this ordering.
  - Positive means first comes after second.
  - Use Comparator.comparing instead of subtracting numbers, which can overflow.

CODE BOXES (copy exactly, preserve punctuation)
  Comparator<Product> byPrice =
      Comparator.comparing(Product::getPrice);

  products.sort(byPrice.thenComparing(Product::getName));

FLOWCHART / DIAGRAM
Need one natural order? → Comparable. Need a situation-specific order? → Comparator.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• TreeSet and TreeMap use comparison to decide sorted uniqueness.
• Comparator can be reversed and chained with thenComparing.

CHECK YOUR UNDERSTANDING (small bordered box)
? How can the same products be sorted by both name and price?

SUMMARY (lower-right cloud outline)
✓ Comparable lives in the class.
✓ Comparator supplies one outside ordering.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “30 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```
