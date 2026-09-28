# Image Prompts — Batch 5

## Page 41 — HTTP, URL + JSON BASICS

```text
Create ONE finished handwritten educational notes page, page 41 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “41 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): HTTP, URL + JSON BASICS
EASY DEFINITION (place directly below the title): HTTP is the request-response language used by web clients and servers. JSON is a common text format for request and response data.
LAYOUT BLUEPRINT: Large HTTP request/response cards and method table.

EXACT PAGE CONTENT
  PANEL 1 — HTTP REQUEST
  - Method says the action: GET, POST, PUT, PATCH, DELETE.
  - URL identifies the address/resource.
  - Headers carry extra information such as content type or authorization.
  - Body carries data when needed, often JSON.
  Visual instruction: Request card with method, path, headers, body labels.
  PANEL 2 — HTTP RESPONSE
  - Status code explains the result.
  - Headers describe the response.
  - Body carries returned data or an error.
  - Common codes: 200 OK, 201 Created, 204 No Content, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 500 Server Error.
  PANEL 3 — JSON
  - JSON objects use { } and name-value pairs.
  - JSON arrays use [ ].
  - Strings use double quotes.
  - JSON has no comments and does not know Java class types by itself.

CODE BOXES (copy exactly, preserve punctuation)
  POST /orders HTTP/1.1
  Content-Type: application/json

  {
    "productId": 10,
    "quantity": 2
  }

FLOWCHART / DIAGRAM
Client builds HTTP request → server processes → server sends status + headers + optional JSON.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• HTTPS is HTTP protected by TLS encryption in transit.
• A 401 means authentication is needed/failed; 403 means the known user is not allowed.

CHECK YOUR UNDERSTANDING (small bordered box)
? What are the four main parts of an HTTP request?

SUMMARY (lower-right cloud outline)
✓ HTTP carries requests and responses.
✓ JSON carries structured text data.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “41 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 42 — DATABASE + SQL CRUD

```text
Create ONE finished handwritten educational notes page, page 42 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “42 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): DATABASE + SQL CRUD
EASY DEFINITION (place directly below the title): A relational database stores information in tables. SQL is the language used to create, read, update, and delete that information.
LAYOUT BLUEPRINT: Table anatomy on top; CRUD four-row examples below.

EXACT PAGE CONTENT
  PANEL 1 — TABLE BASICS
  - A table represents one kind of information, such as customers.
  - A row represents one record.
  - A column represents one property and has a data type.
  - A primary key uniquely identifies a row.
  - A foreign key links a row to another table.
  Visual instruction: Customer table with row, column, primary key labels.
  PANEL 2 — CRUD
  - CREATE data: INSERT.
  - READ data: SELECT.
  - UPDATE data: UPDATE.
  - DELETE data: DELETE.
  - WHERE chooses which rows are affected.
  PANEL 3 — SAFE VALUES
  - Use SQL parameters instead of joining user input into SQL text.
  - Database constraints such as NOT NULL, UNIQUE, CHECK, and FOREIGN KEY protect valid data.
  - Application validation gives friendly errors; database constraints protect every writer.

CODE BOXES (copy exactly, preserve punctuation)
  INSERT INTO customer(name, email) VALUES (?, ?);

  SELECT id, name FROM customer WHERE email = ?;

  UPDATE customer SET name = ? WHERE id = ?;

  DELETE FROM customer WHERE id = ?;

FLOWCHART / DIAGRAM
Application sends parameterized SQL → database checks constraints → rows change/result returns.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• UPDATE or DELETE without the intended WHERE can affect every row.
• NULL means missing/unknown; check it with IS NULL, not = NULL.

CHECK YOUR UNDERSTANDING (small bordered box)
? What is the purpose of a primary key and foreign key?

SUMMARY (lower-right cloud outline)
✓ Tables contain rows and columns.
✓ CRUD means create, read, update, and delete.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “42 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 43 — SQL FILTERING, GROUPING + JOINS

```text
Create ONE finished handwritten educational notes page, page 43 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “43 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): SQL FILTERING, GROUPING + JOINS
EASY DEFINITION (place directly below the title): Filtering chooses rows, grouping summarizes rows, and joins combine related rows from tables.
LAYOUT BLUEPRINT: Top logical query order. Middle joins drawing. Bottom aggregate example.

EXACT PAGE CONTENT
  PANEL 1 — FILTER + GROUP
  - WHERE filters individual rows.
  - GROUP BY places matching values into groups.
  - COUNT, SUM, AVG, MIN, and MAX summarize data.
  - HAVING filters completed groups.
  - ORDER BY sorts the final result.
  Visual instruction: Rows → WHERE → groups → HAVING → ordered result.
  PANEL 2 — JOINS
  - INNER JOIN returns rows with a match on both sides.
  - LEFT JOIN keeps every left row and uses NULL where no right match exists.
  - The ON condition explains how rows are related.
  - Joining one-to-many data can produce several result rows for one parent.
  Visual instruction: Customers and Orders key rows connected; show inner/left results.
  PANEL 3 — LOGICAL ORDER
  - FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT.
  - Knowing this order explains why a selected alias may not be usable in WHERE.

CODE BOXES (copy exactly, preserve punctuation)
  SELECT c.id, c.name, COUNT(o.id) AS order_count
  FROM customer c
  LEFT JOIN orders o ON o.customer_id = c.id
  WHERE c.active = TRUE
  GROUP BY c.id, c.name
  HAVING COUNT(o.id) >= 2
  ORDER BY order_count DESC;

FLOWCHART / DIAGRAM
Choose tables → join → filter rows → group → filter groups → select → sort.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• A condition on the right table in WHERE can accidentally remove unmatched LEFT JOIN rows.
• Select only the columns the application needs.

CHECK YOUR UNDERSTANDING (small bordered box)
? What is the difference between INNER JOIN and LEFT JOIN?

SUMMARY (lower-right cloud outline)
✓ WHERE filters rows; HAVING filters groups.
✓ Joins combine related table data.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “43 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 44 — INDEXES + ACID TRANSACTIONS

```text
Create ONE finished handwritten educational notes page, page 44 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “44 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): INDEXES + ACID TRANSACTIONS
EASY DEFINITION (place directly below the title): An index helps a database find rows faster. A transaction groups database work into one reliable unit.
LAYOUT BLUEPRINT: B-tree picture on left; ACID four-box diagram and transfer flow on right.

EXACT PAGE CONTENT
  PANEL 1 — DATABASE INDEX
  - An index is an extra ordered structure built from selected columns.
  - It can speed up filtering, joining, and sorting.
  - It uses storage and makes inserts/updates/deletes do extra work.
  - A composite index contains more than one column; column order matters.
  - Use the database query plan to check whether an index helps.
  Visual instruction: Book index analogy and small B-tree.
  PANEL 2 — ACID
  - Atomicity: all transaction steps succeed or all are undone.
  - Consistency: constraints/rules remain valid.
  - Isolation: concurrent transactions do not see unsafe partial work.
  - Durability: committed data survives expected failures.
  Visual instruction: Four boxes around money transfer.
  PANEL 3 — ISOLATION IDEA
  - Concurrent users may read/change the same rows.
  - Isolation levels choose which changes can be seen and what conflicts may happen.
  - Keep transactions short so locks and database connections are not held too long.

CODE BOXES (copy exactly, preserve punctuation)
  BEGIN;
  UPDATE account SET balance = balance - 100 WHERE id = 1;
  UPDATE account SET balance = balance + 100 WHERE id = 2;
  COMMIT;

FLOWCHART / DIAGRAM
Begin → perform related SQL → success? commit : rollback.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• More indexes are not always better; they cost space and write time.
• A transaction does not automatically include a remote API or message broker.

CHECK YOUR UNDERSTANDING (small bordered box)
? What does Atomicity mean in a bank transfer?

SUMMARY (lower-right cloud outline)
✓ Indexes trade write/storage cost for faster reads.
✓ Transactions protect a group of database changes.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “44 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 45 — JDBC + CONNECTION POOL

```text
Create ONE finished handwritten educational notes page, page 45 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “45 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): JDBC + CONNECTION POOL
EASY DEFINITION (place directly below the title): JDBC is Java's basic API for talking to relational databases. A connection pool reuses a limited set of database connections.
LAYOUT BLUEPRINT: JDBC sequence on top; pool checkout/return below.

EXACT PAGE CONTENT
  PANEL 1 — JDBC PARTS
  - DataSource provides database connections.
  - Connection represents one database session.
  - PreparedStatement holds parameterized SQL.
  - ResultSet lets code read returned rows.
  - SQLException describes a database-access failure.
  Visual instruction: Java → DataSource → Connection → PreparedStatement → DB → ResultSet.
  PANEL 2 — PREPARED STATEMENT
  - SQL structure and input values are kept separate.
  - This is the normal defense against SQL injection for values.
  - Each ? placeholder receives a typed value.
  - Close Connection, Statement, and ResultSet with try-with-resources.
  PANEL 3 — CONNECTION POOL
  - Opening a physical connection is expensive, so a pool reuses connections.
  - A request borrows a connection and closing it returns it to the pool.
  - Pool size is limited because the database has limited capacity.
  - Slow queries/long transactions can exhaust the pool.

CODE BOXES (copy exactly, preserve punctuation)
  try (Connection c = dataSource.getConnection();
       PreparedStatement ps = c.prepareStatement(
           "SELECT name FROM customer WHERE id = ?")) {
    ps.setLong(1, id);
    try (ResultSet rs = ps.executeQuery()) {
      if (rs.next()) return rs.getString("name");
    }
  }

FLOWCHART / DIAGRAM
Borrow connection → prepare/bind → execute → read result → close returns connection.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Never build SQL by directly joining untrusted input into the query.
• A larger connection pool can overload the database instead of fixing slow SQL.

CHECK YOUR UNDERSTANDING (small bordered box)
? Why should JDBC code use PreparedStatement?

SUMMARY (lower-right cloud outline)
✓ JDBC sends safe SQL and reads results.
✓ A pool treats connections as limited reusable resources.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “45 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 46 — JPA + HIBERNATE BASICS

```text
Create ONE finished handwritten educational notes page, page 46 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “46 / 65” at bottom center.
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

MODULE: Module 5 — JPA, Spring + Spring Boot
TITLE (large uppercase, centered, double-underlined): JPA + HIBERNATE BASICS
EASY DEFINITION (place directly below the title): JPA is a Java standard for mapping objects to relational data. Hibernate is a common tool that implements JPA.
LAYOUT BLUEPRINT: Object/table mapping picture and entity lifecycle below.

EXACT PAGE CONTENT
  PANEL 1 — ORM IDEA
  - ORM means Object-Relational Mapping.
  - A Java entity class maps to a database table.
  - An entity object maps to a row; fields map to columns.
  - JPA defines annotations/APIs; Hibernate performs the work.
  - JPA saves boilerplate but does not remove the need to understand SQL.
  Visual instruction: Order object fields align with orders table columns.
  PANEL 2 — ENTITY BASICS
  - @Entity marks a persistent class.
  - @Id marks its identity/primary key.
  - @GeneratedValue asks a configured strategy to create an ID.
  - Entities need an accessible no-argument constructor for JPA.
  - Use a transaction when changing stored data.
  PANEL 3 — ENTITY STATES
  - Transient: new object not managed/saved.
  - Managed: tracked by the persistence context.
  - Detached: no longer tracked.
  - Removed: marked for deletion.
  - Dirty checking writes changes made to managed entities.
  Visual instruction: State circles with persist, detach, remove arrows.

CODE BOXES (copy exactly, preserve punctuation)
  @Entity
  @Table(name = "product")
  class Product {
    @Id
    private Long id;

    private String name;
    private BigDecimal price;
  }

FLOWCHART / DIAGRAM
Entity object → EntityManager/Hibernate → generated SQL → database row.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Do not expose JPA entities directly as API response objects.
• flush sends pending SQL but transaction commit makes it durable.

CHECK YOUR UNDERSTANDING (small bordered box)
? What is the difference between JPA and Hibernate?

SUMMARY (lower-right cloud outline)
✓ JPA maps objects and tables.
✓ Hibernate tracks managed entities and executes SQL.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “46 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 47 — JPA RELATIONSHIPS, FETCHING + N+1

```text
Create ONE finished handwritten educational notes page, page 47 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “47 / 65” at bottom center.
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

MODULE: Module 5 — JPA, Spring + Spring Boot
TITLE (large uppercase, centered, double-underlined): JPA RELATIONSHIPS, FETCHING + N+1
EASY DEFINITION (place directly below the title): JPA relationships map links between entities. Fetching decides when related data is loaded.
LAYOUT BLUEPRINT: Relationship symbols on top; N+1 query timeline and fixes below.

EXACT PAGE CONTENT
  PANEL 1 — RELATIONSHIPS
  - @OneToOne: one row relates to one row.
  - @OneToMany: one parent relates to many children.
  - @ManyToOne: many children point to one parent.
  - @ManyToMany: many on both sides, usually through a join table.
  - The owning side controls the foreign key/join mapping.
  Visual instruction: Customer 1 → many Orders; Order 1 → many LineItems.
  PANEL 2 — LAZY vs EAGER
  - Lazy means related data loads when it is accessed.
  - Eager means it is requested with the entity, but exact SQL still matters.
  - Neither choice is correct for every use case.
  - Choose a fetch plan for the data one screen/API needs.
  PANEL 3 — N+1 PROBLEM
  - One query loads N parent rows.
  - Reading each lazy child list causes up to N more queries.
  - Fix choices include fetch join, EntityGraph, DTO projection, or batch fetching.
  - Loading everything eagerly can create another performance problem.
  Visual instruction: One parent query followed by N red child queries.
  PANEL 4 — CASCADE
  - Cascade passes operations such as persist/remove from parent to related entities.
  - orphanRemoval deletes a child removed from an owned collection.
  - Use both only when object lifecycle ownership is clear.

CODE BOXES (copy exactly, preserve punctuation)
  @OneToMany(mappedBy = "order", cascade = PERSIST)
  private List<LineItem> items = new ArrayList<>();

FLOWCHART / DIAGRAM
API data need → choose projection/fetch plan → run query → count queries and rows.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• A collection fetch join and pagination can produce wrong/expensive results; often page parent IDs first.
• Keep both sides of a bidirectional relationship consistent.

CHECK YOUR UNDERSTANDING (small bordered box)
? What is the N+1 problem and one way to fix it?

SUMMARY (lower-right cloud outline)
✓ Mappings describe relationships and ownership.
✓ N+1 means one starting query plus many repeated queries.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “47 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 48 — SPRING, IoC + DEPENDENCY INJECTION

```text
Create ONE finished handwritten educational notes page, page 48 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “48 / 65” at bottom center.
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

MODULE: Module 5 — JPA, Spring + Spring Boot
TITLE (large uppercase, centered, double-underlined): SPRING, IoC + DEPENDENCY INJECTION
EASY DEFINITION (place directly below the title): Spring is a Java framework that creates and connects application objects. IoC means Spring controls this object setup.
LAYOUT BLUEPRINT: Without/with Spring comparison and constructor injection example.

EXACT PAGE CONTENT
  PANEL 1 — WITHOUT SPRING
  - A class directly creates its dependencies using new.
  - Object setup becomes spread across the application.
  - Replacing a real dependency with a test version becomes harder.
  Visual instruction: OrderService → new OrderRepository/new EmailClient.
  PANEL 2 — WITH SPRING IoC
  - We describe which classes are Spring beans.
  - ApplicationContext creates the bean objects.
  - It finds their dependencies and connects them.
  - It also manages lifecycle and may add proxy behavior.
  Visual instruction: Container creates Repository and injects it into Service.
  PANEL 3 — CONSTRUCTOR INJECTION
  - Required dependencies appear in the constructor.
  - They can be final and are available when the object is created.
  - A plain unit test can call the constructor directly.
  - Too many constructor parameters may mean a class has too many jobs.

CODE BOXES (copy exactly, preserve punctuation)
  @Service
  class OrderService {
    private final OrderRepository orders;

    OrderService(OrderRepository orders) {
      this.orders = orders;
    }
  }

FLOWCHART / DIAGRAM
Spring reads configuration/components → creates beans → finds constructor needs → injects dependencies.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• An object created manually with new is not automatically managed by Spring.
• Constructor injection is usually clearer than hidden field injection.

CHECK YOUR UNDERSTANDING (small bordered box)
? Why is constructor injection useful?

SUMMARY (lower-right cloud outline)
✓ IoC gives object setup to the container.
✓ Dependency injection supplies the objects a class needs.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “48 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 49 — SPRING BEANS + COMMON ANNOTATIONS

```text
Create ONE finished handwritten educational notes page, page 49 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “49 / 65” at bottom center.
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

MODULE: Module 5 — JPA, Spring + Spring Boot
TITLE (large uppercase, centered, double-underlined): SPRING BEANS + COMMON ANNOTATIONS
EASY DEFINITION (place directly below the title): A Spring bean is an object created and managed by the Spring container.
LAYOUT BLUEPRINT: Annotation family tree and bean creation flow.

EXACT PAGE CONTENT
  PANEL 1 — STEREOTYPE ANNOTATIONS
  - @Component: general Spring-managed component.
  - @Service: application/business service.
  - @Repository: data-access component; also supports exception translation.
  - @Controller: MVC controller that may return views.
  - @RestController: controller whose methods normally return response bodies such as JSON.
  Visual instruction: @Component branches to specialized stereotypes.
  PANEL 2 — EXPLICIT BEANS
  - @Configuration marks a class containing bean configuration.
  - @Bean marks a method whose returned object becomes a bean.
  - This is useful for third-party classes we cannot annotate.
  - A single constructor normally does not need @Autowired.
  PANEL 3 — MULTIPLE BEANS
  - When two beans match one type, Spring needs help choosing.
  - @Primary marks the normal choice.
  - @Qualifier names the intended role.
  - Injecting a Map<String, Strategy> can support many strategies.

CODE BOXES (copy exactly, preserve punctuation)
  @Configuration
  class AppConfig {
    @Bean
    Clock clock() {
      return Clock.systemUTC();
    }
  }

FLOWCHART / DIAGRAM
Component scan or @Bean → bean definition → object created → dependencies injected → ready.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• The annotation name communicates purpose but does not automatically make business design correct.
• Circular constructor dependencies usually show responsibilities that should be redesigned.

CHECK YOUR UNDERSTANDING (small bordered box)
? When would you use @Bean instead of @Component?

SUMMARY (lower-right cloud outline)
✓ A bean is a container-managed object.
✓ Scanning and @Bean methods register beans.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “49 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 50 — BEAN LIFECYCLE, SCOPES + PROXIES

```text
Create ONE finished handwritten educational notes page, page 50 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “50 / 65” at bottom center.
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

MODULE: Module 5 — JPA, Spring + Spring Boot
TITLE (large uppercase, centered, double-underlined): BEAN LIFECYCLE, SCOPES + PROXIES
EASY DEFINITION (place directly below the title): Bean lifecycle describes how Spring creates, prepares, uses, and destroys a bean. Scope describes how many bean objects exist.
LAYOUT BLUEPRINT: Lifecycle conveyor, scope table, and proxy wrapper picture.

EXACT PAGE CONTENT
  PANEL 1 — LIFECYCLE
  - Spring reads a bean definition.
  - It creates the object and injects dependencies.
  - Bean post-processors can inspect or wrap it.
  - @PostConstruct runs after setup.
  - The bean is used.
  - @PreDestroy runs during a normal container shutdown.
  Visual instruction: Definition → create → inject → initialize → use → destroy.
  PANEL 2 — SCOPES
  - singleton: one bean per ApplicationContext; the normal scope.
  - prototype: a new bean when requested from the container.
  - request: one bean per web request.
  - session: one bean per web session.
  - Singleton beans serve many threads, so avoid request-specific mutable fields.
  Visual instruction: Scope | Lifetime | Simple use table.
  PANEL 3 — PROXY
  - Spring can return a wrapper called a proxy around a bean.
  - The proxy adds transactions, security, caching, or async behavior.
  - A call from a method to another method on this may skip the proxy.
  - That is why self-invoked @Transactional may not work as expected.
  Visual instruction: Caller → Proxy → target bean; internal arrow bypasses proxy.

CODE BOXES (copy exactly, preserve punctuation)
  No separate code box.

FLOWCHART / DIAGRAM
Caller → proxy extra behavior → real method → proxy finishes behavior → result.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Singleton means one per container, not one in the whole cluster.
• Do not start slow work or unmanaged threads inside a bean constructor.

CHECK YOUR UNDERSTANDING (small bordered box)
? Why can self-invocation bypass @Transactional?

SUMMARY (lower-right cloud outline)
✓ Spring controls bean creation and cleanup.
✓ Proxies add framework behavior around method calls.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “50 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```
