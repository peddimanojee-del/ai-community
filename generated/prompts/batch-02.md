# Image Prompts — Batch 2 (guardrail revision)

## Page 11 — METHODS + PARAMETERS

```text
Create ONE finished handwritten educational notes page, page 11 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “11 / 65” at bottom center.
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

MODULE: Module 1 — Starting Java
TITLE (large uppercase, centered, double-underlined): METHODS + PARAMETERS
EASY DEFINITION (place directly below the title): A method is a named block of code that performs one task and can be used again.
LAYOUT BLUEPRINT: Large method anatomy with labels; call flow beneath.

EXACT PAGE CONTENT
  PANEL 1 — METHOD PARTS
  - Access modifier controls where it can be called.
  - Return type tells what value comes back; void means no value.
  - Method name should describe the action.
  - Parameters are input names in the method definition.
  - Arguments are actual values given when calling it.
  Visual instruction: Label public, int, add, parameters, body, return.
  PANEL 2 — WHY METHODS HELP
  - They divide a large problem into small steps.
  - One tested method can be reused.
  - A short method is easier to read and change.
  - Method overloading allows the same name with different parameter lists.

CODE BOXES (copy exactly, preserve punctuation)
  public int add(int a, int b) {
    int result = a + b;
    return result;
  }

  int total = add(4, 6);

FLOWCHART / DIAGRAM
Caller gives arguments → method parameters receive copied values → body runs → return value goes to caller.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Java passes every argument by value; an object argument copies the reference value.
• A method should usually do one clearly named job.

CHECK YOUR UNDERSTANDING (small bordered box)
? What is the difference between a parameter and an argument?

SUMMARY (lower-right cloud outline)
✓ Parameters bring values in; return sends a value out.
✓ Methods organize and reuse logic.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “11 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 12 — CLASS vs OBJECT

```text
Create ONE finished handwritten educational notes page, page 12 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “12 / 65” at bottom center.
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

MODULE: Module 1 — Starting Java
TITLE (large uppercase, centered, double-underlined): CLASS vs OBJECT
EASY DEFINITION (place directly below the title): A class is a blueprint. An object is one real instance created from that blueprint.
LAYOUT BLUEPRINT: Reference-style comparison table and two-object memory drawing.

EXACT PAGE CONTENT
  PANEL 1 — EASY COMPARISON
  - Class: describes fields and methods shared by a kind of thing.
  - Object: has its own field values and can use the class methods.
  - One class can create many objects.
  - The new keyword normally creates an object and calls a constructor.
  Visual instruction: Two columns Class | Object with definition, creation, memory, example.
  PANEL 2 — STATE + BEHAVIOR
  - State means the current data, such as account balance.
  - Behavior means actions, such as deposit or withdraw.
  - Each BankAccount object can have a different balance.
  - Methods protect how state is changed.

CODE BOXES (copy exactly, preserve punctuation)
  class Car {
    String color;
    void drive() {
      System.out.println("Moving");
    }
  }

  Car redCar = new Car();
  redCar.color = "Red";

FLOWCHART / DIAGRAM
Class blueprint → new → object 1 and object 2, each with separate field values.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• A variable such as redCar stores a reference to the object.
• Two references can point to the same object.

CHECK YOUR UNDERSTANDING (small bordered box)
? Can one class create many objects? Give an example.

SUMMARY (lower-right cloud outline)
✓ Class describes; object exists.
✓ Objects combine data and actions.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “12 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 13 — CONSTRUCTORS, this + static

```text
Create ONE finished handwritten educational notes page, page 13 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “13 / 65” at bottom center.
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

MODULE: Module 1 — Starting Java
TITLE (large uppercase, centered, double-underlined): CONSTRUCTORS, this + static
EASY DEFINITION (place directly below the title): A constructor prepares a new object. this means the current object. static belongs to the class rather than one object.
LAYOUT BLUEPRINT: Three horizontal parts with object creation flow.

EXACT PAGE CONTENT
  PANEL 1 — CONSTRUCTOR
  - A constructor has the same name as the class and no return type.
  - It runs when new creates an object.
  - It should place the object in a valid starting state.
  - Constructors can be overloaded with different parameter lists.
  Visual instruction: new Product(...) arrow into constructor then ready object.
  PANEL 2 — this
  - this.name means the name field of the current object.
  - It is useful when a parameter and field have the same name.
  - this(...) calls another constructor and must be the first constructor statement.
  PANEL 3 — static
  - A static field is shared by all objects of the class.
  - A static method can be called using the class name.
  - A static method cannot directly use instance fields because no current object is selected.

CODE BOXES (copy exactly, preserve punctuation)
  class Product {
    static int count = 0;
    private String name;

    Product(String name) {
      this.name = name;
      count++;
    }
  }

FLOWCHART / DIAGRAM
new Product("Book") → constructor validates/sets fields → object is ready; shared count increases.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Java supplies a no-argument default constructor only when no constructor is written.
• Do not use static as a replacement for proper objects and dependencies.

CHECK YOUR UNDERSTANDING (small bordered box)
? Why is this.name = name used in a constructor?

SUMMARY (lower-right cloud outline)
✓ Constructor creates a valid starting object.
✓ this is current object; static is class-level.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “13 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 14 — ACCESS MODIFIERS + PACKAGES

```text
Create ONE finished handwritten educational notes page, page 14 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “14 / 65” at bottom center.
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

MODULE: Module 1 — Starting Java
TITLE (large uppercase, centered, double-underlined): ACCESS MODIFIERS + PACKAGES
EASY DEFINITION (place directly below the title): Access modifiers control where a class member can be used. Packages group related classes and avoid name conflicts.
LAYOUT BLUEPRINT: Large four-row visibility table plus package tree.

EXACT PAGE CONTENT
  PANEL 1 — VISIBILITY
  - private: only inside the same class.
  - no modifier (package-private): classes in the same package.
  - protected: same package and qualifying subclasses.
  - public: available from other packages when the class is accessible.
  Visual instruction: Table Modifier | Same class | Same package | Subclass | Other package.
  PANEL 2 — PACKAGES
  - A package name usually follows a reversed internet-domain style: com.example.shop.
  - The folder structure normally follows the package name.
  - import gives a short way to refer to a class from another package.
  - java.lang classes such as String are imported automatically.

CODE BOXES (copy exactly, preserve punctuation)
  package com.example.shop.order;

  public class Order {
    private double total;

    public double getTotal() {
      return total;
    }
  }

FLOWCHART / DIAGRAM
Application → feature package → related classes; public API outside, private details inside.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Choose the smallest visibility that the design needs.
• private data is accessed through meaningful methods, not automatically through a setter for every field.

CHECK YOUR UNDERSTANDING (small bordered box)
? What is the difference between private and public?

SUMMARY (lower-right cloud outline)
✓ Modifiers protect access.
✓ Packages organize related code.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “14 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 15 — OOP CONCEPTS — ONE EASY VIEW

```text
Create ONE finished handwritten educational notes page, page 15 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “15 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): OOP CONCEPTS — ONE EASY VIEW
EASY DEFINITION (place directly below the title): Object-oriented programming organizes software around objects that contain data and actions.
LAYOUT BLUEPRINT: Reference-style five-row grid with definition, small example, and benefit.

EXACT PAGE CONTENT
  PANEL 1 — 1. ENCAPSULATION
  - Keep data and the methods that safely change it together.
  - Example: BankAccount keeps balance private and provides deposit().
  - Benefit: protects valid data.
  Visual instruction: Row arrow → Data protection.
  PANEL 2 — 2. ABSTRACTION
  - Show what an object can do and hide unnecessary internal steps.
  - Example: pay() hides payment-provider details.
  - Benefit: simpler use.
  Visual instruction: Row arrow → Hides complexity.
  PANEL 3 — 3. INHERITANCE
  - A child class receives accessible behavior from a parent class.
  - Example: Dog extends Animal.
  - Benefit: shared behavior when there is a true IS-A relation.
  Visual instruction: Animal → Dog.
  PANEL 4 — 4. POLYMORPHISM
  - The same method call can behave differently for different objects.
  - Example: shape.draw() works for Circle and Rectangle.
  - Benefit: flexible code.
  Visual instruction: Shape branches to Circle/Rectangle.
  PANEL 5 — 5. ASSOCIATION
  - Objects can use or contain other objects.
  - Example: Order has Customer and LineItem objects.
  - Benefit: models relationships.

CODE BOXES (copy exactly, preserve punctuation)
  No separate code box.

FLOWCHART / DIAGRAM
Real thing → class model → data + methods → collaborating objects.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• OOP is not only writing classes; it is placing responsibilities in clear objects.
• Prefer simple object relationships over deep inheritance trees.

CHECK YOUR UNDERSTANDING (small bordered box)
? Explain each OOP concept using one simple example.

SUMMARY (lower-right cloud outline)
✓ OOP groups state and behavior.
✓ Four main ideas are encapsulation, abstraction, inheritance, and polymorphism.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “15 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 16 — ENCAPSULATION + DATA HIDING

```text
Create ONE finished handwritten educational notes page, page 16 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “16 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): ENCAPSULATION + DATA HIDING
EASY DEFINITION (place directly below the title): Encapsulation means keeping an object's data private and allowing it to change only through safe methods.
LAYOUT BLUEPRINT: Top definition. Middle bad/good comparison. Bottom account example.

EXACT PAGE CONTENT
  PANEL 1 — WHY HIDE DATA?
  - Public fields can be changed to any value from anywhere.
  - Private fields stop outside code from changing data directly.
  - Public methods can check a value before changing the field.
  - This keeps the object in a valid state.
  Visual instruction: Open box with unsafe arrows versus protected box with one checked entrance.
  PANEL 2 — GETTERS AND SETTERS
  - A getter returns a value when callers need to read it.
  - A setter changes a value, but it should validate the new value.
  - Not every field needs both a getter and setter.
  - A meaningful method such as withdraw(amount) is clearer than setBalance(value).

CODE BOXES (copy exactly, preserve punctuation)
  class BankAccount {
    private double balance;

    public void deposit(double amount) {
      if (amount <= 0) throw new IllegalArgumentException();
      balance += amount;
    }

    public double getBalance() { return balance; }
  }

FLOWCHART / DIAGRAM
Caller → public method → validation → private field changes safely.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Encapsulation is more than private fields; it protects rules.
• Expose actions the object supports, not all internal details.

CHECK YOUR UNDERSTANDING (small bordered box)
? Why is withdraw(amount) better than a public balance field?

SUMMARY (lower-right cloud outline)
✓ Private data + safe methods = encapsulation.
✓ The object protects its own valid state.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “16 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 17 — INHERITANCE + IS-A RELATIONSHIP

```text
Create ONE finished handwritten educational notes page, page 17 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “17 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): INHERITANCE + IS-A RELATIONSHIP
EASY DEFINITION (place directly below the title): Inheritance lets one class receive behavior from another class when the child is truly a type of the parent.
LAYOUT BLUEPRINT: Parent/child diagram, syntax, and use/do-not-use comparison.

EXACT PAGE CONTENT
  PANEL 1 — PARENT AND CHILD
  - The parent or superclass contains common behavior.
  - The child or subclass uses extends and may add or change behavior.
  - A Dog IS-A Animal, so the relationship can make sense.
  - Constructors are not inherited, but a child constructor can call super(...).
  Visual instruction: Animal top box; Dog and Cat child boxes.
  PANEL 2 — WHEN TO USE
  - Use inheritance when every child can safely be used wherever the parent is expected.
  - Do not use inheritance only to copy some code.
  - A Car is not an Engine; a Car HAS-A Engine, so composition is better.
  - Java classes can extend only one class.

CODE BOXES (copy exactly, preserve punctuation)
  class Animal {
    void eat() { System.out.println("Eating"); }
  }

  class Dog extends Animal {
    void bark() { System.out.println("Woof"); }
  }

FLOWCHART / DIAGRAM
General parent → common behavior → specialized child adds behavior.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• private parent fields are not directly accessible in the child.
• Favor composition when there is no clear IS-A relationship.

CHECK YOUR UNDERSTANDING (small bordered box)
? Is Car extends Engine a good design? Why or why not?

SUMMARY (lower-right cloud outline)
✓ Inheritance shares behavior through an IS-A relation.
✓ A child should respect the parent's promise.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “17 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 18 — POLYMORPHISM: OVERLOADING vs OVERRIDING

```text
Create ONE finished handwritten educational notes page, page 18 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “18 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): POLYMORPHISM: OVERLOADING vs OVERRIDING
EASY DEFINITION (place directly below the title): Polymorphism means 'many forms': one name or contract can work in more than one way.
LAYOUT BLUEPRINT: Reference-style two-column comparison and runtime object diagram.

EXACT PAGE CONTENT
  PANEL 1 — METHOD OVERLOADING
  - Same method name, different parameter list.
  - Usually written in the same class.
  - The compiler selects the method using the argument types.
  - Return type alone cannot create a valid overload.
  Visual instruction: Compile-time label with two add methods.
  PANEL 2 — METHOD OVERRIDING
  - A child class gives a new implementation of an inherited method.
  - Name and parameter list match the parent method.
  - @Override lets the compiler check our intention.
  - The real object type chooses the method while the program runs.
  Visual instruction: Animal reference points to Dog object; sound() prints Woof.
  PANEL 3 — WHY IT HELPS
  - Code can use a general type such as PaymentMethod.
  - Different objects perform pay() in their own way.
  - The caller does not need a large if/else for every concrete type.

CODE BOXES (copy exactly, preserve punctuation)
  int add(int a, int b) { return a + b; }
  double add(double a, double b) { return a + b; }

  Animal animal = new Dog();
  animal.sound(); // Dog version runs

FLOWCHART / DIAGRAM
General reference → actual object → overridden method runs.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Overloading is chosen at compile time; overriding is chosen at runtime.
• Use @Override whenever a method is intended to override.

CHECK YOUR UNDERSTANDING (small bordered box)
? Give one difference between overloading and overriding.

SUMMARY (lower-right cloud outline)
✓ Overloading changes parameters.
✓ Overriding changes inherited behavior.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “18 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 19 — ABSTRACT CLASS vs INTERFACE

```text
Create ONE finished handwritten educational notes page, page 19 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “19 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): ABSTRACT CLASS vs INTERFACE
EASY DEFINITION (place directly below the title): An abstract class is an incomplete base class. An interface is a contract that tells what a class can do.
LAYOUT BLUEPRINT: Reference-matched three-column table with 10 easy rows and a choice guide.

EXACT PAGE CONTENT
  PANEL 1 — FEATURE COMPARISON
  - Definition — abstract class: base class that cannot be created directly; interface: contract/capability implemented by classes.
  - Keyword — abstract class uses abstract; interface uses interface.
  - Methods — abstract class may have abstract and normal methods; interface may have abstract, default, static, and private methods.
  - Variables — abstract class may have instance fields; interface fields are constants (public static final).
  - Constructor — abstract class can have constructors; interface cannot.
  - Inheritance — extend one class; implement multiple interfaces.
  - Access — class members can use different access levels; interface abstract methods are public.
  - Use — shared state/base behavior versus a common capability.
  - Example — Animal base class versus Drawable contract.
  - Modern Java — interfaces can also contain useful default helper behavior.
  Visual instruction: Columns Feature | Abstract Class | Interface; ten numbered rows.
  PANEL 2 — SIMPLE CHOICE
  - Need shared fields and base setup? Choose an abstract class.
  - Need one class to promise several abilities? Choose interfaces.
  - Need only to reuse a helper? First consider a separate helper object (composition).

CODE BOXES (copy exactly, preserve punctuation)
  abstract class Animal {
    abstract void sound();
  }

  interface Drawable {
    void draw();
  }

FLOWCHART / DIAGRAM
Shared base state? → Abstract class. Common ability/multiple roles? → Interface.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• A class can extend one class and implement many interfaces.
• Since Java 8 interfaces may have default/static methods; since Java 9 they may have private helpers.

CHECK YOUR UNDERSTANDING (small bordered box)
? When would you choose an interface instead of an abstract class?

SUMMARY (lower-right cloud outline)
✓ Abstract class = shared base.
✓ Interface = common contract or ability.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “19 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```

## Page 20 — Object CLASS + equals + hashCode

```text
Create ONE finished handwritten educational notes page, page 20 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “20 / 65” at bottom center.
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
TITLE (large uppercase, centered, double-underlined): Object CLASS + equals + hashCode
EASY DEFINITION (place directly below the title): Object is the top parent of Java classes. Its common methods help compare, describe, and identify objects.
LAYOUT BLUEPRINT: Method table and two-object equality drawing.

EXACT PAGE CONTENT
  PANEL 1 — COMMON Object METHODS
  - toString() returns a text description useful for logs and debugging.
  - equals() answers whether two objects should be treated as logically equal.
  - hashCode() gives a number used by hash collections.
  - getClass() returns the object's runtime class.
  Visual instruction: Table Method | Easy meaning | Example use.
  PANEL 2 — == vs equals
  - == compares primitive values directly.
  - For objects, == asks whether two references point to the same object.
  - equals asks whether objects represent the same logical value when implemented that way.
  - String overrides equals, so use it for String value comparison.
  PANEL 3 — THE RULE
  - If two objects are equal, they must have the same hash code.
  - Override equals and hashCode together.
  - Do not change equality fields while an object is inside HashSet or used as a HashMap key.

CODE BOXES (copy exactly, preserve punctuation)
  String a = new String("Java");
  String b = new String("Java");

  a == b;       // false: different objects
  a.equals(b);  // true: same text

FLOWCHART / DIAGRAM
Compare references? → ==. Compare object meaning? → equals → matching hashCode rule.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• toString should never reveal passwords or secret data.
• Records automatically create useful equals, hashCode, and toString methods.

CHECK YOUR UNDERSTANDING (small bordered box)
? Why should equals and hashCode be overridden together?

SUMMARY (lower-right cloud outline)
✓ == checks identity for objects; equals checks logical value.
✓ Equal objects need equal hash codes.

FINAL PRE-RENDER AUDIT
1. Confirm canvas width is smaller than height and the whole A4 sheet is visible.
2. Compare every heading and bullet with the supplied content: no omission, duplication, fragment, or invented line.
3. Read code character-by-character: case, braces, line breaks, punctuation, and statement scope must match.
4. Confirm no instruction words leaked onto the page and body text remains sentence case.
5. Confirm version facts cannot visually attach to the wrong feature.
6. Confirm footer is exactly “20 / 65” and “Java Backend • Easy Notes”, with nothing else.
Only render after all six checks pass. The page should look like the supplied reference sheet with modern, technically correct content.

```
