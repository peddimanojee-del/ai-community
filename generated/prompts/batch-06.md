# Image Prompts — Batch 6

## Page 51 — SPRING BOOT + AUTO-CONFIGURATION

```text
Create ONE finished handwritten educational notes page, page 51 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “51 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): SPRING BOOT + AUTO-CONFIGURATION
EASY DEFINITION (place directly below the title): Spring Boot makes Spring applications faster to start by providing useful defaults, dependency starters, and automatic configuration.
LAYOUT BLUEPRINT: @SpringBootApplication branches and conditional decision flow.

EXACT PAGE CONTENT
  PANEL 1 — WHAT BOOT PROVIDES
  - Starter dependencies collect common libraries, such as spring-boot-starter-web.
  - Auto-configuration suggests beans based on libraries, properties, and existing beans.
  - An embedded server lets a web app run as one executable JAR.
  - Actuator adds optional production health and metric endpoints.
  Visual instruction: Spring Boot box: starters, auto-config, server, actuator.
  PANEL 2 — @SpringBootApplication
  - It includes configuration support.
  - It starts component scanning from its package downward.
  - It enables Boot's auto-configuration selection.
  - Place the main class near the top package so features are scanned.
  PANEL 3 — CONDITIONAL SETUP
  - Is a required class present?
  - Is a property enabled?
  - Did the application already define its own bean?
  - When a user bean exists, auto-configuration often backs off.
  - The condition report helps explain why a configuration matched.
  Visual instruction: Decision diamonds ending Create default bean / Back off.

CODE BOXES (copy exactly, preserve punctuation)
  @SpringBootApplication
  public class ShopApplication {
    public static void main(String[] args) {
      SpringApplication.run(ShopApplication.class, args);
    }
  }

FLOWCHART / DIAGRAM
Classpath + properties + user beans → conditions → auto-configured beans → running application.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Auto-configuration is conditional setup, not magic.
• Do not exclude an auto-configuration before understanding what condition matched.

CHECK YOUR UNDERSTANDING (small bordered box)
? What three ideas are combined by @SpringBootApplication?

SUMMARY (lower-right cloud outline)
✓ Boot supplies sensible conditional defaults.
✓ The application can replace defaults when needed.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “51 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 52 — CONFIGURATION + PROFILES

```text
Create ONE finished handwritten educational notes page, page 52 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “52 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): CONFIGURATION + PROFILES
EASY DEFINITION (place directly below the title): Configuration means values that may change between environments without changing the Java code.
LAYOUT BLUEPRINT: One JAR to three environments and typed properties card.

EXACT PAGE CONTENT
  PANEL 1 — EXTERNAL CONFIG
  - application.properties or application.yml provides defaults.
  - Environment variables and command-line values can override configuration.
  - Use the same built artifact in development, test, and production.
  - Inject each environment's URLs, limits, and feature values during deployment.
  Visual instruction: One JAR flows to dev/stage/prod; each supplies config.
  PANEL 2 — PROFILES
  - A profile activates environment- or purpose-specific configuration/beans.
  - Example: application-dev.yml.
  - Profiles may be combined, so test the real combination.
  - Do not use profiles for every small business feature choice.
  PANEL 3 — TYPED PROPERTIES
  - @ConfigurationProperties maps a group of values to a typed class/record.
  - Validation can stop startup when a required value is missing.
  - This is clearer than many scattered @Value fields.
  - Secrets belong in a secret manager/platform secret, never Git.

CODE BOXES (copy exactly, preserve punctuation)
  @ConfigurationProperties(prefix = "payment")
  public record PaymentProperties(
      String baseUrl,
      Duration timeout) {}

  payment:
    base-url: https://api.example.com
    timeout: 2s

FLOWCHART / DIAGRAM
Config sources → precedence/override → typed binding → validation → bean uses safe values.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Never log all environment values because they may contain secrets.
• Configuration changes environment behavior; the artifact stays unchanged.

CHECK YOUR UNDERSTANDING (small bordered box)
? Why should production secrets not be stored in application.yml in Git?

SUMMARY (lower-right cloud outline)
✓ External configuration keeps code and environment values separate.
✓ Typed properties make configuration clear and testable.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “52 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 53 — SPRING MVC REQUEST LIFECYCLE

```text
Create ONE finished handwritten educational notes page, page 53 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “53 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): SPRING MVC REQUEST LIFECYCLE
EASY DEFINITION (place directly below the title): Spring MVC receives an HTTP request, finds the correct controller method, converts data, and creates an HTTP response.
LAYOUT BLUEPRINT: Full-page numbered request sequence with component notes.

EXACT PAGE CONTENT
  PANEL 1 — BEFORE CONTROLLER
  - 1. The embedded server accepts the request.
  - 2. Servlet Filters run for concerns such as security and request IDs.
  - 3. DispatcherServlet acts as Spring MVC's front controller.
  - 4. HandlerMapping finds a matching controller method.
  - 5. Argument resolvers and message converters create method parameters.
  Visual instruction: Client → Server/Filters → DispatcherServlet → Controller.
  PANEL 2 — CONTROLLER + SERVICE
  - 6. JSON may be converted into a request DTO.
  - 7. Validation runs when requested.
  - 8. The controller calls an application service.
  - 9. The service applies rules and uses repositories.
  - 10. The controller returns a result or ResponseEntity.
  PANEL 3 — RESPONSE
  - 11. A message converter changes the response object into JSON.
  - 12. Exception handlers translate known failures into safe error responses.
  - 13. The response passes back through filters to the client.

CODE BOXES (copy exactly, preserve punctuation)
  @RestController
  @RequestMapping("/products")
  class ProductController {
    @GetMapping("/{id}")
    ProductResponse get(@PathVariable long id) {
      return service.get(id);
    }
  }

FLOWCHART / DIAGRAM
Client → filters → DispatcherServlet → mapping/binding → controller → service → repository → JSON response.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Controllers are singleton beans, so do not store one user's request data in controller fields.
• Spring MVC normally uses the servlet blocking model; WebFlux is a separate reactive stack.

CHECK YOUR UNDERSTANDING (small bordered box)
? What happens between incoming JSON and a controller parameter?

SUMMARY (lower-right cloud outline)
✓ DispatcherServlet coordinates the MVC request.
✓ Controllers adapt HTTP to application calls.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “53 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 54 — REST CONTROLLERS + API DESIGN

```text
Create ONE finished handwritten educational notes page, page 54 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “54 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): REST CONTROLLERS + API DESIGN
EASY DEFINITION (place directly below the title): A REST API exposes resources through HTTP methods, URLs, status codes, headers, and representations such as JSON.
LAYOUT BLUEPRINT: Resource URL examples, HTTP method table, status-code guide.

EXACT PAGE CONTENT
  PANEL 1 — RESOURCE URLS
  - Use nouns: /orders and /orders/42.
  - Avoid action names such as /getOrder when GET already describes the action.
  - A nested path such as /orders/42/items can show clear ownership.
  - Query parameters filter, sort, search, or paginate a collection.
  Visual instruction: Cross out /getOrders; green /orders/{id}.
  PANEL 2 — METHOD MEANING
  - GET reads without changing the intended resource state.
  - POST creates or starts an operation.
  - PUT replaces a resource at a known URL.
  - PATCH changes part of a resource.
  - DELETE removes a resource.
  PANEL 3 — GOOD RESPONSES
  - 200 for normal success with a body.
  - 201 + Location when a resource is created.
  - 204 for success without a body.
  - 400 for invalid request, 404 for missing resource, 409 for state conflict.
  - 500 for an unexpected server problem—not for client mistakes.
  PANEL 4 — IDEMPOTENCY
  - Repeating an idempotent request has the same intended server effect.
  - GET, PUT, and DELETE are defined as idempotent in meaning.
  - A critical POST can use an idempotency key stored with its result so a retry does not create the action twice.

CODE BOXES (copy exactly, preserve punctuation)
  @PostMapping
  ResponseEntity<OrderResponse> create(
      @Valid @RequestBody CreateOrderRequest request) {
    OrderResponse result = service.create(request);
    return ResponseEntity.created(uri(result.id())).body(result);
  }

FLOWCHART / DIAGRAM
HTTP method + resource URL → validate → perform use case → choose status + headers + JSON.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• REST design uses HTTP meaning, not only JSON fields.
• A client timeout does not prove the server operation failed; retry safety matters.

CHECK YOUR UNDERSTANDING (small bordered box)
? What should POST /orders return after creating an order?

SUMMARY (lower-right cloud outline)
✓ URLs name resources; methods name actions.
✓ Status codes clearly tell the result.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “54 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 55 — DTOs + VALIDATION

```text
Create ONE finished handwritten educational notes page, page 55 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “55 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): DTOs + VALIDATION
EASY DEFINITION (place directly below the title): A DTO is an object used to carry input or output across a boundary. Validation checks whether received data follows required rules.
LAYOUT BLUEPRINT: Entity/DTO boundary diagram and three validation layers.

EXACT PAGE CONTENT
  PANEL 1 — WHY DTOs?
  - A request DTO contains only fields the client is allowed to send.
  - A response DTO contains only fields the API should show.
  - JPA entities contain persistence details and may load extra data during JSON conversion.
  - Separate DTOs let the database model and API change at different speeds.
  Visual instruction: JSON ↔ DTO | safe boundary | service/entity ↔ database.
  PANEL 2 — JAKARTA VALIDATION
  - @NotNull: value must exist.
  - @NotBlank: text must contain non-space characters.
  - @Size: text/collection length range.
  - @Positive, @Min, @Max: number rules.
  - @Email and @Pattern: format checks.
  - @Valid checks nested request objects.
  Visual instruction: Annotation | Easy meaning | Example table.
  PANEL 3 — THREE LAYERS
  - DTO validation checks shape and simple input rules.
  - Service/domain checks current business rules, such as enough stock.
  - Database constraints protect final stored truth and concurrent writers.
  - The same rule should have a clear owner, even when defenses exist at several layers.

CODE BOXES (copy exactly, preserve punctuation)
  public record CreateUserRequest(
      @NotBlank String name,
      @Email @NotBlank String email,
      @Min(18) int age) {}

FLOWCHART / DIAGRAM
JSON → bind DTO → validate fields → service business rules → database constraints.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Never trust a client-supplied owner ID or role when it should come from authenticated identity.
• Do not return JPA entities directly from controllers.

CHECK YOUR UNDERSTANDING (small bordered box)
? Why should an API use DTOs instead of returning entities?

SUMMARY (lower-right cloud outline)
✓ DTOs protect API boundaries.
✓ Validation happens from input shape to business rule to database truth.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “55 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 56 — GLOBAL ERROR HANDLING

```text
Create ONE finished handwritten educational notes page, page 56 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “56 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): GLOBAL ERROR HANDLING
EASY DEFINITION (place directly below the title): Global error handling changes application exceptions into one clear, safe, and consistent API error format.
LAYOUT BLUEPRINT: Exception-to-response ladder and ProblemDetail card.

EXACT PAGE CONTENT
  PANEL 1 — WHY CENTRAL HANDLING?
  - Without it, every controller repeats try/catch code.
  - @RestControllerAdvice holds handlers used by many controllers.
  - @ExceptionHandler chooses a response for a known exception type.
  - Unknown failures return a general 500 message while detailed information stays in protected logs.
  Visual instruction: Controller exceptions funnel into one advice component.
  PANEL 2 — ERROR RESPONSE
  - status: HTTP status number.
  - code/type: stable machine-readable error name.
  - title/detail: safe human explanation.
  - fieldErrors: invalid input fields when useful.
  - traceId: value that helps support find the matching logs.
  - instance/path: the failed request location.
  Visual instruction: ProblemDetail-shaped JSON card.
  PANEL 3 — COMMON MAPPING
  - Bad JSON/DTO validation → 400.
  - Missing resource → 404.
  - Wrong current state or duplicate unique value → 409.
  - Unauthenticated → 401; not allowed → 403.
  - Unexpected bug → safe 500.

CODE BOXES (copy exactly, preserve punctuation)
  @RestControllerAdvice
  class ApiErrors {
    @ExceptionHandler(OrderNotFound.class)
    ProblemDetail notFound(OrderNotFound ex) {
      var error = ProblemDetail.forStatus(404);
      error.setTitle("Order not found");
      error.setProperty("code", "ORDER_NOT_FOUND");
      return error;
    }
  }

FLOWCHART / DIAGRAM
Exception → matching handler → status + safe body + trace ID → client; detailed cause → protected log.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Never return stack traces, SQL statements, passwords, or internal class names to a client.
• Keep error codes stable even when the human message changes.

CHECK YOUR UNDERSTANDING (small bordered box)
? What information should and should not appear in an API error?

SUMMARY (lower-right cloud outline)
✓ One handler keeps API errors consistent.
✓ Public errors are safe; internal logs keep useful details.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “56 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 57 — SPRING DATA JPA REPOSITORIES

```text
Create ONE finished handwritten educational notes page, page 57 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “57 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): SPRING DATA JPA REPOSITORIES
EASY DEFINITION (place directly below the title): Spring Data JPA creates repository implementations from interfaces, reducing repeated data-access code.
LAYOUT BLUEPRINT: Repository interface to proxy to EntityManager flow and query choice ladder.

EXACT PAGE CONTENT
  PANEL 1 — REPOSITORY BASICS
  - JpaRepository<Entity,IdType> provides save, findById, delete, paging, and more.
  - Spring creates a proxy object that implements the interface.
  - findById returns Optional because the row may not exist.
  - Collection queries normally return an empty collection, not null.
  Visual instruction: Interface → Spring Data proxy → EntityManager → database.
  PANEL 2 — QUERY METHODS
  - A simple method name can become a query: findByEmail.
  - Combine fields carefully: findByStatusAndCreatedAtBefore.
  - @Query writes JPQL using entity and field names.
  - Native SQL uses table/column names and database features.
  - Complex reports may be clearer in a custom read repository.
  Visual instruction: Simple derived → @Query → Specification/custom ladder.
  PANEL 3 — PAGING + PROJECTION
  - Pageable asks for page number, size, and sorting.
  - Page includes content and a count; Slice only knows whether a next part exists.
  - A projection returns only fields needed by the screen/API.
  - Always use deterministic sorting, including a unique tie-breaker.

CODE BOXES (copy exactly, preserve punctuation)
  interface OrderRepository extends JpaRepository<Order, UUID> {
    List<Order> findByStatus(OrderStatus status);

    @Query("select o from Order o where o.customer.id = :id")
    Page<Order> findForCustomer(UUID id, Pageable page);
  }

FLOWCHART / DIAGRAM
Call repository method → derive/read query → proxy executes through JPA → result/projection returns.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Generated repository methods still run real SQL; inspect SQL and query plans.
• Changing a managed entity in a transaction is saved by dirty checking without calling save again.

CHECK YOUR UNDERSTANDING (small bordered box)
? What implementation class do you write for a normal Spring Data repository interface?

SUMMARY (lower-right cloud outline)
✓ Spring Data creates common repository code.
✓ Method names and @Query define reads.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “57 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 58 — @Transactional + LOCKING

```text
Create ONE finished handwritten educational notes page, page 58 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “58 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): @Transactional + LOCKING
EASY DEFINITION (place directly below the title): A transaction makes related database changes succeed or fail as one unit. @Transactional asks Spring to manage that boundary.
LAYOUT BLUEPRINT: Proxy transaction flow, rollback rules, and two-user version drawing.

EXACT PAGE CONTENT
  PANEL 1 — HOW @Transactional WORKS
  - A Spring proxy starts or joins a transaction before the method.
  - Repository operations use that transaction.
  - Normal completion commits it.
  - A matching failure rolls it back.
  - The normal default rolls back for RuntimeException/Error, not every checked exception.
  Visual instruction: Caller → transaction proxy → begin → method → commit/rollback.
  PANEL 2 — GOOD BOUNDARY
  - Put the transaction around one application use case.
  - Keep it short.
  - Avoid slow network calls while holding database locks/connections when the design allows.
  - Private/self-invoked methods may skip proxy behavior.
  PANEL 3 — CONCURRENT UPDATE
  - Optimistic locking uses an @Version field.
  - Two users read version 3; the first update creates version 4.
  - The second update using version 3 fails instead of silently overwriting.
  - Pessimistic locking asks the database to block conflicting access and must be used carefully.
  Visual instruction: Two users read v3; first wins v4; second gets conflict.
  PANEL 4 — PROPAGATION IDEA
  - REQUIRED joins an existing transaction or starts one; it is the normal default.
  - REQUIRES_NEW pauses the outer transaction and starts an independent one.
  - Independent commits can change the all-or-nothing behavior, so choose deliberately.

CODE BOXES (copy exactly, preserve punctuation)
  @Transactional
  public void pay(UUID orderId) {
    Order order = orders.findById(orderId)
        .orElseThrow(OrderNotFound::new);
    order.markPaid();
  }

FLOWCHART / DIAGRAM
Proxy call → begin/join transaction → work → success commit | exception rule rollback.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Catching an exception and returning normally may allow commit.
• A retry after an optimistic conflict must read the newest state and safely repeat the use case.

CHECK YOUR UNDERSTANDING (small bordered box)
? Why may @Transactional not work on a method called through this?

SUMMARY (lower-right cloud outline)
✓ @Transactional manages a local database unit of work.
✓ Version checks prevent silent lost updates.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “58 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 59 — SPRING SECURITY BASICS

```text
Create ONE finished handwritten educational notes page, page 59 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “59 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): SPRING SECURITY BASICS
EASY DEFINITION (place directly below the title): Security first proves who the caller is (authentication), then checks what that caller may do (authorization).
LAYOUT BLUEPRINT: Two-gate drawing, security filter chain, and 401/403 comparison.

EXACT PAGE CONTENT
  PANEL 1 — TWO QUESTIONS
  - Authentication: Who are you?
  - Authorization: Are you allowed to do this action on this resource?
  - A logged-in user may still be forbidden from another user's order.
  - Use least privilege: give only needed permissions.
  Visual instruction: Identity gate → permission/ownership gate → controller.
  PANEL 2 — FILTER CHAIN
  - Spring Security runs filters before the controller.
  - A filter reads a session, bearer token, or other credentials.
  - AuthenticationManager/Provider checks the evidence.
  - A successful Authentication is stored in SecurityContext.
  - Authorization rules decide whether the request may continue.
  Visual instruction: Request → security filters → authentication → authorization → MVC.
  PANEL 3 — 401 vs 403
  - 401: no valid authentication; the caller must authenticate.
  - 403: identity is known but does not have permission.
  - 404 may sometimes hide whether a protected resource exists.
  - Test allowed and denied cases.
  PANEL 4 — PASSWORDS
  - Store an adaptive one-way hash such as bcrypt or Argon2, never plain passwords.
  - Rate-limit login attempts.
  - Never log passwords or access tokens.
  - Use HTTPS so credentials are protected in transit.

CODE BOXES (copy exactly, preserve punctuation)
  @Bean
  SecurityFilterChain security(HttpSecurity http) throws Exception {
    return http
        .authorizeHttpRequests(auth -> auth
            .requestMatchers("/public/**").permitAll()
            .anyRequest().authenticated())
        .build();
  }

FLOWCHART / DIAGRAM
Credentials → verify identity → create Authentication → check role/ownership → allow or 401/403.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Do not trust a role or user ID sent in an ordinary client header.
• Authorization must also check resource ownership when needed.

CHECK YOUR UNDERSTANDING (small bordered box)
? What is the difference between 401 and 403?

SUMMARY (lower-right cloud outline)
✓ Authentication proves identity.
✓ Authorization checks permission.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “59 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 60 — JWT, CORS + CSRF

```text
Create ONE finished handwritten educational notes page, page 60 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “60 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): JWT, CORS + CSRF
EASY DEFINITION (place directly below the title): JWT is a signed token format. CORS controls browser cross-origin reading. CSRF protects against unwanted requests using automatically sent credentials.
LAYOUT BLUEPRINT: JWT anatomy on top; CORS/CSRF comparison table below.

EXACT PAGE CONTENT
  PANEL 1 — JWT
  - A JWT has header.payload.signature.
  - Header and payload are encoded, not secret; a holder can read them.
  - The server verifies allowed algorithm, signature, issuer, audience, and expiry.
  - Short-lived access tokens limit damage.
  - Do not put passwords or unnecessary private data in claims.
  Visual instruction: Three colored token sections and validation checklist.
  PANEL 2 — CORS
  - Browsers normally restrict one website from reading another origin's response.
  - The server can allow trusted origins, methods, and headers.
  - CORS is not login, authorization, or a server-to-server firewall.
  - Credentialed CORS cannot use a wildcard allowed origin.
  PANEL 3 — CSRF
  - Browsers automatically send some credentials, especially cookies.
  - A malicious page can cause an unwanted state-changing request using them.
  - CSRF tokens and SameSite cookie rules are common defenses.
  - A bearer-only stateless API has a different CSRF model, but token storage must still be protected from XSS.

CODE BOXES (copy exactly, preserve punctuation)
  Authorization: Bearer <access-token>

  Verify: algorithm → signature → issuer → audience → expiry → authorities

FLOWCHART / DIAGRAM
Client gets token → sends bearer token → server verifies cryptography/claims → authorizes action.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• A valid signature alone is not enough; issuer, audience, and time claims matter.
• JWT signing does not encrypt its payload.

CHECK YOUR UNDERSTANDING (small bordered box)
? Can anyone read a normal JWT payload, and what prevents changing it?

SUMMARY (lower-right cloud outline)
✓ JWT carries signed claims, not secret text.
✓ CORS and CSRF solve different browser security problems.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “60 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```
