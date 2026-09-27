# Image Prompts — Batch 1

## Page 01 — WHAT IS JAVA BACKEND DEVELOPMENT?

```text
Create ONE finished handwritten educational notes page, page 01 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “01 / 65” at bottom center.
- Avoid: typeset font, calligraphy, illegible pseudo-text, misspelled code, 3D effects, decorative illustrations unrelated to learning, undefined expert jargon, long academic paragraphs.

MODULE: Module 1 — Starting Java
TITLE (large uppercase, centered, double-underlined): WHAT IS JAVA BACKEND DEVELOPMENT?
EASY DEFINITION (place directly below the title): Backend development means writing the hidden part of an application that receives requests, applies rules, saves data, and sends results.
LAYOUT BLUEPRINT: Top: simple real-life example. Middle: request journey. Bottom: frontend/backend comparison.

EXACT PAGE CONTENT
  PANEL 1 — A SIMPLE EXAMPLE
  - When you place an online order, the screen you see is the frontend.
  - The backend checks the product, calculates the total, saves the order, and returns an order number.
  - Java is a popular language for building this backend part.
  Visual instruction: Draw phone screen on the left and a Java server plus database on the right.
  PANEL 2 — REQUEST JOURNEY
  - 1. A user clicks a button.
  - 2. The frontend sends a request through the internet.
  - 3. The Java backend checks the request and performs the work.
  - 4. The database stores or returns data.
  - 5. The backend sends a response to the user.
  Visual instruction: Five boxes: User → Frontend → Java Backend → Database → Response.
  PANEL 3 — MAIN BACKEND JOBS
  - Accept data safely.
  - Follow business rules.
  - Store and read information.
  - Protect private data.
  - Handle errors and stay available.

CODE BOXES (copy exactly, preserve punctuation)
  No separate code box.

FLOWCHART / DIAGRAM
User action → HTTP request → Controller → Service → Database → JSON response.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• The backend is not normally visible, but it does most of the application's work.
• A database stores information; Java code decides what should happen.

CHECK YOUR UNDERSTANDING (small bordered box)
? Explain what happens after a user clicks 'Place Order'.

SUMMARY (lower-right cloud outline)
✓ Frontend shows; backend works.
✓ Java backend connects user requests with business rules and data.

Final quality gate: verify title, technical terms, arrows, code punctuation, page number, and every supplied sentence before rendering. The result should look like the supplied reference sheet, but with modern, technically correct content.

```

## Page 02 — INSTALL JAVA + RUN YOUR FIRST PROGRAM

```text
Create ONE finished handwritten educational notes page, page 02 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “02 / 65” at bottom center.
- Avoid: typeset font, calligraphy, illegible pseudo-text, misspelled code, 3D effects, decorative illustrations unrelated to learning, undefined expert jargon, long academic paragraphs.

MODULE: Module 1 — Starting Java
TITLE (large uppercase, centered, double-underlined): INSTALL JAVA + RUN YOUR FIRST PROGRAM
EASY DEFINITION (place directly below the title): A Java program is text written in a .java file. The JDK gives us the tools needed to compile and run it.
LAYOUT BLUEPRINT: Top: setup checklist. Middle: Hello World code. Bottom: compile and run flow.

EXACT PAGE CONTENT
  PANEL 1 — WHAT YOU NEED
  - Install a supported JDK such as Java 17 or Java 21.
  - Use an editor or IDE such as IntelliJ IDEA, Eclipse, or VS Code.
  - Check installation with java --version and javac --version.
  - Create a file named Hello.java.
  Visual instruction: Checklist with JDK, IDE, terminal, source file.
  PANEL 2 — UNDERSTAND THE PROGRAM
  - class Hello creates a class named Hello.
  - main is the starting method of a simple Java program.
  - System.out.println prints text on the screen.
  - Java names and uppercase/lowercase letters must match exactly.
  Visual instruction: Arrows from each line of code to its plain meaning.
  PANEL 3 — COMPILE AND RUN
  - javac Hello.java checks the code and creates Hello.class.
  - java Hello asks the Java runtime to execute the compiled class.
  - A compiler error means the code must be corrected before it can run.

CODE BOXES (copy exactly, preserve punctuation)
  public class Hello {
    public static void main(String[] args) {
      System.out.println("Hello, Java!");
    }
  }

FLOWCHART / DIAGRAM
Hello.java → javac Hello.java → Hello.class → java Hello → Hello, Java!

IMPORTANT POINTS (lower-left, purple-underlined heading)
• The public class name and file name should match.
• Run java Hello, not java Hello.class.

CHECK YOUR UNDERSTANDING (small bordered box)
? What is the difference between javac and java?

SUMMARY (lower-right cloud outline)
✓ Write source code, compile it, then run it.
✓ main is the starting point of this example.

Final quality gate: verify title, technical terms, arrows, code punctuation, page number, and every supplied sentence before rendering. The result should look like the supplied reference sheet, but with modern, technically correct content.

```

## Page 03 — JDK vs JRE vs JVM

```text
Create ONE finished handwritten educational notes page, page 03 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “03 / 65” at bottom center.
- Avoid: typeset font, calligraphy, illegible pseudo-text, misspelled code, 3D effects, decorative illustrations unrelated to learning, undefined expert jargon, long academic paragraphs.

MODULE: Module 1 — Starting Java
TITLE (large uppercase, centered, double-underlined): JDK vs JRE vs JVM
EASY DEFINITION (place directly below the title): JDK, JRE, and JVM are three connected parts that help us build and run Java programs.
LAYOUT BLUEPRINT: Reference-style three-column comparison table with a small flow below.

EXACT PAGE CONTENT
  PANEL 1 — EASY COMPARISON
  - JDK — Java Development Kit. It contains tools for writing, compiling, and running Java programs.
  - JRE — Java Runtime Environment. It means the runtime libraries and JVM needed to run Java code.
  - JVM — Java Virtual Machine. It reads Java bytecode and runs it on the computer.
  - Modern Java usually provides a complete JDK; custom runtimes can also be created.
  Visual instruction: Three columns: Part | Full form | Main job | Used by.
  PANEL 2 — HOW THEY WORK TOGETHER
  - The compiler javac changes source code into bytecode.
  - Bytecode is stored in a .class file.
  - The JVM changes bytecode into instructions the computer can execute.
  - A JVM is made for a particular operating system, but Java bytecode is portable.

CODE BOXES (copy exactly, preserve punctuation)
  No separate code box.

FLOWCHART / DIAGRAM
Program.java → JDK compiler → Program.class bytecode → JVM → computer output.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• JDK is used to develop; JVM is used to execute.
• Bytecode is the reason the same Java program can run on different systems with a suitable JVM.

CHECK YOUR UNDERSTANDING (small bordered box)
? Why is Java called platform-independent?

SUMMARY (lower-right cloud outline)
✓ JDK builds Java programs.
✓ JVM runs Java bytecode.

Final quality gate: verify title, technical terms, arrows, code punctuation, page number, and every supplied sentence before rendering. The result should look like the supplied reference sheet, but with modern, technically correct content.

```

## Page 04 — STRUCTURE OF A JAVA PROGRAM

```text
Create ONE finished handwritten educational notes page, page 04 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “04 / 65” at bottom center.
- Avoid: typeset font, calligraphy, illegible pseudo-text, misspelled code, 3D effects, decorative illustrations unrelated to learning, undefined expert jargon, long academic paragraphs.

MODULE: Module 1 — Starting Java
TITLE (large uppercase, centered, double-underlined): STRUCTURE OF A JAVA PROGRAM
EASY DEFINITION (place directly below the title): A Java program is organized using packages, imports, classes, fields, methods, and statements.
LAYOUT BLUEPRINT: Large labeled code example on left; meaning table on right.

EXACT PAGE CONTENT
  PANEL 1 — MAIN PARTS
  - package tells where the class belongs.
  - import lets us use a class from another package by its short name.
  - class is a blueprint that groups data and behavior.
  - field stores data inside an object.
  - method performs a task.
  - statement is one instruction and normally ends with a semicolon.
  Visual instruction: Label each part on the code example with colored arrows.
  PANEL 2 — NAMING STYLE
  - Class names use PascalCase: OrderService.
  - Methods and variables use camelCase: calculateTotal.
  - Constants normally use UPPER_SNAKE_CASE: MAX_SIZE.
  - Good names explain purpose better than short names like x or data1.

CODE BOXES (copy exactly, preserve punctuation)
  package com.example.shop;

  import java.math.BigDecimal;

  public class Product {
    private String name;

    public String getName() {
      return name;
    }
  }

FLOWCHART / DIAGRAM
Package contains classes → class contains fields and methods → method contains statements.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Java code is read from top-level classes, but program work happens inside methods.
• Braces { } group code; indentation makes the groups easy to see.

CHECK YOUR UNDERSTANDING (small bordered box)
? Name the field and method in the Product example.

SUMMARY (lower-right cloud outline)
✓ A class groups related data and actions.
✓ Clear structure and names make code easy to understand.

Final quality gate: verify title, technical terms, arrows, code punctuation, page number, and every supplied sentence before rendering. The result should look like the supplied reference sheet, but with modern, technically correct content.

```

## Page 05 — VARIABLES + DATA TYPES

```text
Create ONE finished handwritten educational notes page, page 05 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “05 / 65” at bottom center.
- Avoid: typeset font, calligraphy, illegible pseudo-text, misspelled code, 3D effects, decorative illustrations unrelated to learning, undefined expert jargon, long academic paragraphs.

MODULE: Module 1 — Starting Java
TITLE (large uppercase, centered, double-underlined): VARIABLES + DATA TYPES
EASY DEFINITION (place directly below the title): A variable is a named place that holds a value. Its data type tells Java what kind of value it may hold.
LAYOUT BLUEPRINT: Top definition and boxes. Middle primitive table. Bottom reference example.

EXACT PAGE CONTENT
  PANEL 1 — VARIABLE PARTS
  - Declaration: int age; tells Java the name and type.
  - Assignment: age = 25; puts a value into the variable.
  - Initialization: int age = 25; does both at once.
  - A variable can change unless it is declared final.
  Visual instruction: Draw a labeled box: type | name | value.
  PANEL 2 — 8 PRIMITIVE TYPES
  - Whole numbers: byte, short, int, long.
  - Decimal numbers: float, double.
  - Single character: char.
  - True or false: boolean.
  - Primitives directly represent simple values.
  Visual instruction: Table Type | Example | Simple use.
  PANEL 3 — REFERENCE TYPES
  - String, arrays, and objects are reference types.
  - A reference points to an object rather than directly containing the whole object.
  - null means the reference currently points to no object.

CODE BOXES (copy exactly, preserve punctuation)
  int quantity = 3;
  double price = 49.5;
  boolean available = true;
  char grade = 'A';
  String name = "Book";

FLOWCHART / DIAGRAM
Choose meaning → choose suitable type → give clear name → assign value.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Use long suffix L and float suffix F when needed.
• For money, BigDecimal is safer than double because decimal values must be exact.

CHECK YOUR UNDERSTANDING (small bordered box)
? Which type would you choose for age, name, and a yes/no answer?

SUMMARY (lower-right cloud outline)
✓ A variable has a type, name, and value.
✓ Primitive and reference types store different kinds of information.

Final quality gate: verify title, technical terms, arrows, code punctuation, page number, and every supplied sentence before rendering. The result should look like the supplied reference sheet, but with modern, technically correct content.

```

## Page 06 — OPERATORS IN JAVA

```text
Create ONE finished handwritten educational notes page, page 06 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “06 / 65” at bottom center.
- Avoid: typeset font, calligraphy, illegible pseudo-text, misspelled code, 3D effects, decorative illustrations unrelated to learning, undefined expert jargon, long academic paragraphs.

MODULE: Module 1 — Starting Java
TITLE (large uppercase, centered, double-underlined): OPERATORS IN JAVA
EASY DEFINITION (place directly below the title): An operator is a symbol that tells Java to calculate, compare, assign, or check values.
LAYOUT BLUEPRINT: Reference-style rows: operator group, symbols, example, result.

EXACT PAGE CONTENT
  PANEL 1 — OPERATOR GROUPS
  - Arithmetic: +, -, *, /, % perform calculations.
  - Assignment: =, +=, -= store or update a value.
  - Comparison: ==, !=, >, <, >=, <= produce true or false.
  - Logical: && means AND, || means OR, ! means NOT.
  - Increment/decrement: ++ and -- add or remove one.
  Visual instruction: Table Group | Symbols | Example | Result.
  PANEL 2 — ORDER OF WORK
  - Parentheses run first and make the intention clear.
  - Multiplication/division normally happen before addition/subtraction.
  - Short-circuit AND stops when the left side is false.
  - Short-circuit OR stops when the left side is true.

CODE BOXES (copy exactly, preserve punctuation)
  int total = 10 + 5 * 2;       // 20
  boolean adult = age >= 18;
  boolean allowed = active && adult;
  int remainder = 10 % 3;          // 1

FLOWCHART / DIAGRAM
Values → operator → result; comparison result → boolean true/false.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Use .equals() to compare String values; == compares object references.
• Add parentheses when an expression may be hard to read.

CHECK YOUR UNDERSTANDING (small bordered box)
? What is the result of 10 + 5 * 2, and why?

SUMMARY (lower-right cloud outline)
✓ Operators work with values.
✓ Comparison and logical operators help make decisions.

Final quality gate: verify title, technical terms, arrows, code punctuation, page number, and every supplied sentence before rendering. The result should look like the supplied reference sheet, but with modern, technically correct content.

```

## Page 07 — TYPE CASTING + USER INPUT

```text
Create ONE finished handwritten educational notes page, page 07 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “07 / 65” at bottom center.
- Avoid: typeset font, calligraphy, illegible pseudo-text, misspelled code, 3D effects, decorative illustrations unrelated to learning, undefined expert jargon, long academic paragraphs.

MODULE: Module 1 — Starting Java
TITLE (large uppercase, centered, double-underlined): TYPE CASTING + USER INPUT
EASY DEFINITION (place directly below the title): Type casting changes a value from one type to another. Input lets a program receive a value from a user or another source.
LAYOUT BLUEPRINT: Left: widening/narrowing arrows. Right: Scanner example and safety notes.

EXACT PAGE CONTENT
  PANEL 1 — TYPE CASTING
  - Widening conversion moves a smaller type to a larger compatible type automatically: int to long.
  - Narrowing conversion moves a larger type to a smaller type and needs an explicit cast.
  - Narrowing can lose decimal parts or overflow the target range.
  - Casting does not turn unrelated objects into each other.
  Visual instruction: Small-to-large green arrow; large-to-small orange warning arrow.
  PANEL 2 — READING INPUT
  - Scanner can read values from the console in a beginner program.
  - nextLine reads a line of text; nextInt reads an integer.
  - Real web applications receive input from HTTP requests instead of the console.
  - All outside input must be checked before it is trusted.

CODE BOXES (copy exactly, preserve punctuation)
  int count = 10;
  long bigger = count;          // widening
  double price = 19.95;
  int whole = (int) price;      // 19

  Scanner in = new Scanner(System.in);
  String name = in.nextLine();

FLOWCHART / DIAGRAM
Outside value → read → convert if needed → validate → use.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• A cast can lose information; use it only when the allowed range is known.
• Input validation prevents wrong values from entering the program.

CHECK YOUR UNDERSTANDING (small bordered box)
? Why does converting double 19.95 to int produce 19?

SUMMARY (lower-right cloud outline)
✓ Widening is usually safe; narrowing may lose data.
✓ Read input, then validate it.

Final quality gate: verify title, technical terms, arrows, code punctuation, page number, and every supplied sentence before rendering. The result should look like the supplied reference sheet, but with modern, technically correct content.

```

## Page 08 — IF, ELSE + SWITCH

```text
Create ONE finished handwritten educational notes page, page 08 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “08 / 65” at bottom center.
- Avoid: typeset font, calligraphy, illegible pseudo-text, misspelled code, 3D effects, decorative illustrations unrelated to learning, undefined expert jargon, long academic paragraphs.

MODULE: Module 1 — Starting Java
TITLE (large uppercase, centered, double-underlined): IF, ELSE + SWITCH
EASY DEFINITION (place directly below the title): Conditional statements let a program choose different work based on a true or false condition.
LAYOUT BLUEPRINT: Top if/else flowchart. Middle examples. Bottom switch table.

EXACT PAGE CONTENT
  PANEL 1 — IF / ELSE
  - if runs a block when its condition is true.
  - else if checks another condition when earlier ones were false.
  - else runs when no earlier condition matched.
  - Conditions should be clear and should not perform hidden work.
  Visual instruction: Decision diamond: condition? true path / false path.
  PANEL 2 — SWITCH
  - switch compares one value with several possible cases.
  - Arrow-style cases avoid accidental fall-through.
  - A default case handles values not listed.
  - Use if for ranges/complex conditions and switch for clear named choices.

CODE BOXES (copy exactly, preserve punctuation)
  if (age >= 18) {
    System.out.println("Adult");
  } else {
    System.out.println("Minor");
  }

  String message = switch (status) {
    case PAID -> "Ready to ship";
    case NEW -> "Waiting for payment";
    default -> "Check order";
  };

FLOWCHART / DIAGRAM
Start → check condition → choose one path → continue after decision.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Use braces even for short blocks; they prevent mistakes during later changes.
• Keep the normal path simple by rejecting invalid input early.

CHECK YOUR UNDERSTANDING (small bordered box)
? When is switch clearer than a long if/else chain?

SUMMARY (lower-right cloud outline)
✓ if chooses by a condition.
✓ switch chooses among known values.

Final quality gate: verify title, technical terms, arrows, code punctuation, page number, and every supplied sentence before rendering. The result should look like the supplied reference sheet, but with modern, technically correct content.

```

## Page 09 — LOOPS: FOR, WHILE + DO-WHILE

```text
Create ONE finished handwritten educational notes page, page 09 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “09 / 65” at bottom center.
- Avoid: typeset font, calligraphy, illegible pseudo-text, misspelled code, 3D effects, decorative illustrations unrelated to learning, undefined expert jargon, long academic paragraphs.

MODULE: Module 1 — Starting Java
TITLE (large uppercase, centered, double-underlined): LOOPS: FOR, WHILE + DO-WHILE
EASY DEFINITION (place directly below the title): A loop repeats a block of code until a condition says it should stop.
LAYOUT BLUEPRINT: Three-column comparison with one flow diagram and loop-control notes.

EXACT PAGE CONTENT
  PANEL 1 — THREE LOOPS
  - for is useful when the number of repetitions is known.
  - enhanced for reads each item from an array or collection.
  - while checks the condition before every repetition.
  - do-while runs once before checking its condition.
  Visual instruction: Columns Loop | Best use | Small example.
  PANEL 2 — LOOP CONTROL
  - break immediately leaves the loop.
  - continue skips the rest of the current repetition.
  - A loop needs progress toward stopping, or it may run forever.
  - Avoid changing a normal collection while using an enhanced for loop over it.

CODE BOXES (copy exactly, preserve punctuation)
  for (int i = 0; i < 3; i++) {
    System.out.println(i);
  }

  for (String name : names) {
    System.out.println(name);
  }

FLOWCHART / DIAGRAM
Initialize → check condition → run body → update → check again → finish.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• An off-by-one error repeats one time too many or too few.
• Use meaningful loop names and small loop bodies.

CHECK YOUR UNDERSTANDING (small bordered box)
? What is the difference between while and do-while?

SUMMARY (lower-right cloud outline)
✓ Loops repeat work.
✓ The condition and update decide when a loop stops.

Final quality gate: verify title, technical terms, arrows, code punctuation, page number, and every supplied sentence before rendering. The result should look like the supplied reference sheet, but with modern, technically correct content.

```

## Page 10 — ARRAYS

```text
Create ONE finished handwritten educational notes page, page 10 of 65.

HARD OUTPUT RULES
- A4 portrait, 210:297, high resolution, full page visible, no crop, no desk or hand in frame.
- Warm off-white real paper. Exceptionally neat HUMAN HANDWRITING—not a typeset infographic.
- This page is for a complete beginner. Use the supplied easy wording; never replace it with advanced jargon.
- All supplied wording and code must be spelled exactly and remain readable. Do not invent paragraphs.
- Main body ink: deep navy blue. Main title: purple/magenta, uppercase, centered, double-underlined.
- Secondary headings: teal green or purple with a short decorative underline. Borders: thin black or navy hand-drawn straight lines.
- Writing character: neat human handwritten print with slight right slant and natural variation; compact but readable.
- Thin hand-drawn boxes, straight ruled tables, green arrows/check marks, purple underlines.
- Keep 4% safe margins. Put small page number “10 / 65” at bottom center.
- Avoid: typeset font, calligraphy, illegible pseudo-text, misspelled code, 3D effects, decorative illustrations unrelated to learning, undefined expert jargon, long academic paragraphs.

MODULE: Module 1 — Starting Java
TITLE (large uppercase, centered, double-underlined): ARRAYS
EASY DEFINITION (place directly below the title): An array stores a fixed number of values of the same type in numbered positions.
LAYOUT BLUEPRINT: Top array drawing with indexes. Middle operations. Bottom 1D/2D comparison.

EXACT PAGE CONTENT
  PANEL 1 — HOW AN ARRAY WORKS
  - The first position has index 0.
  - An array of length 5 has indexes 0 through 4.
  - length gives the number of positions.
  - Reading an index outside the range causes ArrayIndexOutOfBoundsException.
  Visual instruction: Five boxes labeled values with indexes 0,1,2,3,4 below.
  PANEL 2 — CREATE AND USE
  - The size is fixed when the array is created.
  - Primitive array positions receive default primitive values.
  - Object array positions start as null.
  - Use ArrayList when the number of items must easily grow or shrink.

CODE BOXES (copy exactly, preserve punctuation)
  int[] scores = {80, 92, 75};
  int first = scores[0];
  scores[2] = 78;

  for (int score : scores) {
    System.out.println(score);
  }

FLOWCHART / DIAGRAM
Create size → fill positions → read/update by index → loop through values.

IMPORTANT POINTS (lower-left, purple-underlined heading)
• Array length is scores.length, not scores.length().
• A two-dimensional array is an array whose elements are arrays.

CHECK YOUR UNDERSTANDING (small bordered box)
? What are the valid indexes of an array with length 4?

SUMMARY (lower-right cloud outline)
✓ Arrays store same-type values in fixed positions.
✓ Array indexes start at zero.

Final quality gate: verify title, technical terms, arrows, code punctuation, page number, and every supplied sentence before rendering. The result should look like the supplied reference sheet, but with modern, technically correct content.

```
