"""Build the approved beginner-friendly 65-page Java backend notes script."""
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
pages: list[dict] = []


def panel(heading: str, copy: list[str], visual: str = "") -> dict:
    return {"heading": heading, "copy": copy, "visual": visual}


def page(
    number: int,
    module: str,
    title: str,
    definition: str,
    layout: str,
    panels: list[dict],
    *,
    code: list[str] | None = None,
    flowchart: str = "",
    important: list[str],
    summary: list[str],
    interview: list[str],
) -> None:
    pages.append({
        "page": number,
        "module": module,
        "title": title,
        "objective": definition,
        "layout": layout,
        "panels": panels,
        "code": code or [],
        "flowchart": flowchart,
        "important": important,
        "summary": summary,
        "interview_checks": interview,
    })


page(1, "Module 1 — Starting Java", "WHAT IS JAVA BACKEND DEVELOPMENT?",
"Backend development means writing the hidden part of an application that receives requests, applies rules, saves data, and sends results.",
"Top: simple real-life example. Middle: request journey. Bottom: frontend/backend comparison.", [
 panel("A SIMPLE EXAMPLE", ["When you place an online order, the screen you see is the frontend.", "The backend checks the product, calculates the total, saves the order, and returns an order number.", "Java is a popular language for building this backend part."], "Draw phone screen on the left and a Java server plus database on the right."),
 panel("REQUEST JOURNEY", ["1. A user clicks a button.", "2. The frontend sends a request through the internet.", "3. The Java backend checks the request and performs the work.", "4. The database stores or returns data.", "5. The backend sends a response to the user."], "Five boxes: User → Frontend → Java Backend → Database → Response."),
 panel("MAIN BACKEND JOBS", ["Accept data safely.", "Follow business rules.", "Store and read information.", "Protect private data.", "Handle errors and stay available."])
 ], flowchart="User action → HTTP request → Controller → Service → Database → JSON response.",
 important=["The backend is not normally visible, but it does most of the application's work.", "A database stores information; Java code decides what should happen."],
 summary=["Frontend shows; backend works.", "Java backend connects user requests with business rules and data."],
 interview=["Explain what happens after a user clicks 'Place Order'."])

page(2, "Module 1 — Starting Java", "INSTALL JAVA + RUN YOUR FIRST PROGRAM",
"A Java program is text written in a .java file. The JDK gives us the tools needed to compile and run it.",
"Top: setup checklist. Middle: Hello World code. Bottom: compile and run flow.", [
 panel("WHAT YOU NEED", ["Install a supported JDK such as Java 17 or Java 21.", "Use an editor or IDE such as IntelliJ IDEA, Eclipse, or VS Code.", "Check installation with java --version and javac --version.", "Create a file named Hello.java."] , "Checklist with JDK, IDE, terminal, source file."),
 panel("UNDERSTAND THE PROGRAM", ["class Hello creates a class named Hello.", "main is the starting method of a simple Java program.", "System.out.println prints text on the screen.", "Java names and uppercase/lowercase letters must match exactly."], "Arrows from each line of code to its plain meaning."),
 panel("COMPILE AND RUN", ["javac Hello.java checks the code and creates Hello.class.", "java Hello asks the Java runtime to execute the compiled class.", "A compiler error means the code must be corrected before it can run."])
 ], code=["public class Hello {\n  public static void main(String[] args) {\n    System.out.println(\"Hello, Java!\");\n  }\n}"],
 flowchart="Hello.java → javac Hello.java → Hello.class → java Hello → Hello, Java!",
 important=["The public class name and file name should match.", "Run java Hello, not java Hello.class."],
 summary=["Write source code, compile it, then run it.", "main is the starting point of this example."],
 interview=["What is the difference between javac and java?"])

page(3, "Module 1 — Starting Java", "JDK vs JRE vs JVM",
"JDK, JRE, and JVM are three connected parts that help us build and run Java programs.",
"Reference-style three-column comparison table with a small flow below.", [
 panel("EASY COMPARISON", ["JDK — Java Development Kit. It contains tools for writing, compiling, and running Java programs.", "JRE — Java Runtime Environment. It means the runtime libraries and JVM needed to run Java code.", "JVM — Java Virtual Machine. It reads Java bytecode and runs it on the computer.", "Modern Java usually provides a complete JDK; custom runtimes can also be created."], "Three columns: Part | Full form | Main job | Used by."),
 panel("HOW THEY WORK TOGETHER", ["The compiler javac changes source code into bytecode.", "Bytecode is stored in a .class file.", "The JVM changes bytecode into instructions the computer can execute.", "A JVM is made for a particular operating system, but Java bytecode is portable."])
 ], flowchart="Program.java → JDK compiler → Program.class bytecode → JVM → computer output.",
 important=["JDK is used to develop; JVM is used to execute.", "Bytecode is the reason the same Java program can run on different systems with a suitable JVM."],
 summary=["JDK builds Java programs.", "JVM runs Java bytecode."],
 interview=["Why is Java called platform-independent?"])

page(4, "Module 1 — Starting Java", "STRUCTURE OF A JAVA PROGRAM",
"A Java program is organized using packages, imports, classes, fields, methods, and statements.",
"Large labeled code example on left; meaning table on right.", [
 panel("MAIN PARTS", ["package tells where the class belongs.", "import lets us use a class from another package by its short name.", "class is a blueprint that groups data and behavior.", "field stores data inside an object.", "method performs a task.", "statement is one instruction and normally ends with a semicolon."], "Label each part on the code example with colored arrows."),
 panel("NAMING STYLE", ["Class names use PascalCase: OrderService.", "Methods and variables use camelCase: calculateTotal.", "Constants normally use UPPER_SNAKE_CASE: MAX_SIZE.", "Good names explain purpose better than short names like x or data1."])
 ], code=["package com.example.shop;\n\nimport java.math.BigDecimal;\n\npublic class Product {\n  private String name;\n\n  public String getName() {\n    return name;\n  }\n}"],
 flowchart="Package contains classes → class contains fields and methods → method contains statements.",
 important=["Java code is read from top-level classes, but program work happens inside methods.", "Braces { } group code; indentation makes the groups easy to see."],
 summary=["A class groups related data and actions.", "Clear structure and names make code easy to understand."],
 interview=["Name the field and method in the Product example."])

page(5, "Module 1 — Starting Java", "VARIABLES + DATA TYPES",
"A variable is a named place that holds a value. Its data type tells Java what kind of value it may hold.",
"Top definition and boxes. Middle primitive table. Bottom reference example.", [
 panel("VARIABLE PARTS", ["Declaration: int age; tells Java the name and type.", "Assignment: age = 25; puts a value into the variable.", "Initialization: int age = 25; does both at once.", "A variable can change unless it is declared final."], "Draw a labeled box: type | name | value."),
 panel("8 PRIMITIVE TYPES", ["Whole numbers: byte, short, int, long.", "Decimal numbers: float, double.", "Single character: char.", "True or false: boolean.", "Primitives directly represent simple values."], "Table Type | Example | Simple use."),
 panel("REFERENCE TYPES", ["String, arrays, and objects are reference types.", "A reference points to an object rather than directly containing the whole object.", "null means the reference currently points to no object."])
 ], code=["int quantity = 3;\ndouble price = 49.5;\nboolean available = true;\nchar grade = 'A';\nString name = \"Book\";"],
 flowchart="Choose meaning → choose suitable type → give clear name → assign value.",
 important=["Use long suffix L and float suffix F when needed.", "For money, BigDecimal is safer than double because decimal values must be exact."],
 summary=["A variable has a type, name, and value.", "Primitive and reference types store different kinds of information."],
 interview=["Which type would you choose for age, name, and a yes/no answer?"])

page(6, "Module 1 — Starting Java", "OPERATORS IN JAVA",
"An operator is a symbol that tells Java to calculate, compare, assign, or check values.",
"Reference-style rows: operator group, symbols, example, result.", [
 panel("OPERATOR GROUPS", ["Arithmetic: +, -, *, /, % perform calculations.", "Assignment: =, +=, -= store or update a value.", "Comparison: ==, !=, >, <, >=, <= produce true or false.", "Logical: && means AND, || means OR, ! means NOT.", "Increment/decrement: ++ and -- add or remove one."], "Table Group | Symbols | Example | Result."),
 panel("ORDER OF WORK", ["Parentheses run first and make the intention clear.", "Multiplication/division normally happen before addition/subtraction.", "Short-circuit AND stops when the left side is false.", "Short-circuit OR stops when the left side is true."])
 ], code=["int total = 10 + 5 * 2;       // 20\nboolean adult = age >= 18;\nboolean allowed = active && adult;\nint remainder = 10 % 3;          // 1"],
 flowchart="Values → operator → result; comparison result → boolean true/false.",
 important=["Use .equals() to compare String values; == compares object references.", "Add parentheses when an expression may be hard to read."],
 summary=["Operators work with values.", "Comparison and logical operators help make decisions."],
 interview=["What is the result of 10 + 5 * 2, and why?"])

page(7, "Module 1 — Starting Java", "TYPE CASTING + USER INPUT",
"Type casting changes a value from one type to another. Input lets a program receive a value from a user or another source.",
"Left: widening/narrowing arrows. Right: Scanner example and safety notes.", [
 panel("TYPE CASTING", ["Widening conversion moves a smaller type to a larger compatible type automatically: int to long.", "Narrowing conversion moves a larger type to a smaller type and needs an explicit cast.", "Narrowing can lose decimal parts or overflow the target range.", "Casting does not turn unrelated objects into each other."], "Small-to-large green arrow; large-to-small orange warning arrow."),
 panel("READING INPUT", ["Scanner can read values from the console in a beginner program.", "nextLine reads a line of text; nextInt reads an integer.", "Real web applications receive input from HTTP requests instead of the console.", "All outside input must be checked before it is trusted."])
 ], code=["int count = 10;\nlong bigger = count;          // widening\ndouble price = 19.95;\nint whole = (int) price;      // 19\n\nScanner in = new Scanner(System.in);\nString name = in.nextLine();"],
 flowchart="Outside value → read → convert if needed → validate → use.",
 important=["A cast can lose information; use it only when the allowed range is known.", "Input validation prevents wrong values from entering the program."],
 summary=["Widening is usually safe; narrowing may lose data.", "Read input, then validate it."],
 interview=["Why does converting double 19.95 to int produce 19?"])

page(8, "Module 1 — Starting Java", "IF, ELSE + SWITCH",
"Conditional statements let a program choose different work based on a true or false condition.",
"Top if/else flowchart. Middle examples. Bottom switch table.", [
 panel("IF / ELSE", ["if runs a block when its condition is true.", "else if checks another condition when earlier ones were false.", "else runs when no earlier condition matched.", "Conditions should be clear and should not perform hidden work."], "Decision diamond: condition? true path / false path."),
 panel("SWITCH", ["switch compares one value with several possible cases.", "Arrow-style cases avoid accidental fall-through.", "A default case handles values not listed.", "Use if for ranges/complex conditions and switch for clear named choices."])
 ], code=["if (age >= 18) {\n  System.out.println(\"Adult\");\n} else {\n  System.out.println(\"Minor\");\n}", "String message = switch (status) {\n  case PAID -> \"Ready to ship\";\n  case NEW -> \"Waiting for payment\";\n  default -> \"Check order\";\n};"],
 flowchart="Start → check condition → choose one path → continue after decision.",
 important=["Use braces even for short blocks; they prevent mistakes during later changes.", "Keep the normal path simple by rejecting invalid input early."],
 summary=["if chooses by a condition.", "switch chooses among known values."],
 interview=["When is switch clearer than a long if/else chain?"])

page(9, "Module 1 — Starting Java", "LOOPS: FOR, WHILE + DO-WHILE",
"A loop repeats a block of code until a condition says it should stop.",
"Three-column comparison with one flow diagram and loop-control notes.", [
 panel("THREE LOOPS", ["for is useful when the number of repetitions is known.", "enhanced for reads each item from an array or collection.", "while checks the condition before every repetition.", "do-while runs once before checking its condition."], "Columns Loop | Best use | Small example."),
 panel("LOOP CONTROL", ["break immediately leaves the loop.", "continue skips the rest of the current repetition.", "A loop needs progress toward stopping, or it may run forever.", "Avoid changing a normal collection while using an enhanced for loop over it."])
 ], code=["for (int i = 0; i < 3; i++) {\n  System.out.println(i);\n}\n\nfor (String name : names) {\n  System.out.println(name);\n}"],
 flowchart="Initialize → check condition → run body → update → check again → finish.",
 important=["An off-by-one error repeats one time too many or too few.", "Use meaningful loop names and small loop bodies."],
 summary=["Loops repeat work.", "The condition and update decide when a loop stops."],
 interview=["What is the difference between while and do-while?"])

page(10, "Module 1 — Starting Java", "ARRAYS",
"An array stores a fixed number of values of the same type in numbered positions.",
"Top array drawing with indexes. Middle operations. Bottom 1D/2D comparison.", [
 panel("HOW AN ARRAY WORKS", ["The first position has index 0.", "An array of length 5 has indexes 0 through 4.", "length gives the number of positions.", "Reading an index outside the range causes ArrayIndexOutOfBoundsException."] , "Five boxes labeled values with indexes 0,1,2,3,4 below."),
 panel("CREATE AND USE", ["The size is fixed when the array is created.", "Primitive array positions receive default primitive values.", "Object array positions start as null.", "Use ArrayList when the number of items must easily grow or shrink."])
 ], code=["int[] scores = {80, 92, 75};\nint first = scores[0];\nscores[2] = 78;\n\nfor (int score : scores) {\n  System.out.println(score);\n}"],
 flowchart="Create size → fill positions → read/update by index → loop through values.",
 important=["Array length is scores.length, not scores.length().", "A two-dimensional array is an array whose elements are arrays."],
 summary=["Arrays store same-type values in fixed positions.", "Array indexes start at zero."],
 interview=["What are the valid indexes of an array with length 4?"])

page(11, "Module 1 — Starting Java", "METHODS + PARAMETERS",
"A method is a named block of code that performs one task and can be used again.",
"Large method anatomy with labels; call flow beneath.", [
 panel("METHOD PARTS", ["Access modifier controls where it can be called.", "Return type tells what value comes back; void means no value.", "Method name should describe the action.", "Parameters are input names in the method definition.", "Arguments are actual values given when calling it."], "Label public, int, add, parameters, body, return."),
 panel("WHY METHODS HELP", ["They divide a large problem into small steps.", "One tested method can be reused.", "A short method is easier to read and change.", "Method overloading allows the same name with different parameter lists."])
 ], code=["public int add(int a, int b) {\n  int result = a + b;\n  return result;\n}\n\nint total = add(4, 6);"],
 flowchart="Caller gives arguments → method parameters receive copied values → body runs → return value goes to caller.",
 important=["Java passes every argument by value; an object argument copies the reference value.", "A method should usually do one clearly named job."],
 summary=["Parameters bring values in; return sends a value out.", "Methods organize and reuse logic."],
 interview=["What is the difference between a parameter and an argument?"])

page(12, "Module 1 — Starting Java", "CLASS vs OBJECT",
"A class is a blueprint. An object is one real instance created from that blueprint.",
"Reference-style comparison table and two-object memory drawing.", [
 panel("EASY COMPARISON", ["Class: describes fields and methods shared by a kind of thing.", "Object: has its own field values and can use the class methods.", "One class can create many objects.", "The new keyword normally creates an object and calls a constructor."], "Two columns Class | Object with definition, creation, memory, example."),
 panel("STATE + BEHAVIOR", ["State means the current data, such as account balance.", "Behavior means actions, such as deposit or withdraw.", "Each BankAccount object can have a different balance.", "Methods protect how state is changed."])
 ], code=["class Car {\n  String color;\n  void drive() {\n    System.out.println(\"Moving\");\n  }\n}\n\nCar redCar = new Car();\nredCar.color = \"Red\";"],
 flowchart="Class blueprint → new → object 1 and object 2, each with separate field values.",
 important=["A variable such as redCar stores a reference to the object.", "Two references can point to the same object."],
 summary=["Class describes; object exists.", "Objects combine data and actions."],
 interview=["Can one class create many objects? Give an example."])

page(13, "Module 1 — Starting Java", "CONSTRUCTORS, this + static",
"A constructor prepares a new object. this means the current object. static belongs to the class rather than one object.",
"Three horizontal parts with object creation flow.", [
 panel("CONSTRUCTOR", ["A constructor has the same name as the class and no return type.", "It runs when new creates an object.", "It should place the object in a valid starting state.", "Constructors can be overloaded with different parameter lists."] , "new Product(...) arrow into constructor then ready object."),
 panel("this", ["this.name means the name field of the current object.", "It is useful when a parameter and field have the same name.", "this(...) calls another constructor and must be the first constructor statement."]),
 panel("static", ["A static field is shared by all objects of the class.", "A static method can be called using the class name.", "A static method cannot directly use instance fields because no current object is selected."])
 ], code=["class Product {\n  static int count = 0;\n  private String name;\n\n  Product(String name) {\n    this.name = name;\n    count++;\n  }\n}"],
 flowchart="new Product(\"Book\") → constructor validates/sets fields → object is ready; shared count increases.",
 important=["Java supplies a no-argument default constructor only when no constructor is written.", "Do not use static as a replacement for proper objects and dependencies."],
 summary=["Constructor creates a valid starting object.", "this is current object; static is class-level."],
 interview=["Why is this.name = name used in a constructor?"])

page(14, "Module 1 — Starting Java", "ACCESS MODIFIERS + PACKAGES",
"Access modifiers control where a class member can be used. Packages group related classes and avoid name conflicts.",
"Large four-row visibility table plus package tree.", [
 panel("VISIBILITY", ["private: only inside the same class.", "no modifier (package-private): classes in the same package.", "protected: same package and qualifying subclasses.", "public: available from other packages when the class is accessible."], "Table Modifier | Same class | Same package | Subclass | Other package."),
 panel("PACKAGES", ["A package name usually follows a reversed internet-domain style: com.example.shop.", "The folder structure normally follows the package name.", "import gives a short way to refer to a class from another package.", "java.lang classes such as String are imported automatically."])
 ], code=["package com.example.shop.order;\n\npublic class Order {\n  private double total;\n\n  public double getTotal() {\n    return total;\n  }\n}"],
 flowchart="Application → feature package → related classes; public API outside, private details inside.",
 important=["Choose the smallest visibility that the design needs.", "private data is accessed through meaningful methods, not automatically through a setter for every field."],
 summary=["Modifiers protect access.", "Packages organize related code."],
 interview=["What is the difference between private and public?"])

page(15, "Module 2 — Object-Oriented Java", "OOP CONCEPTS — ONE EASY VIEW",
"Object-oriented programming organizes software around objects that contain data and actions.",
"Reference-style five-row grid with definition, small example, and benefit.", [
 panel("1. ENCAPSULATION", ["Keep data and the methods that safely change it together.", "Example: BankAccount keeps balance private and provides deposit().", "Benefit: protects valid data."] , "Row arrow → Data protection."),
 panel("2. ABSTRACTION", ["Show what an object can do and hide unnecessary internal steps.", "Example: pay() hides payment-provider details.", "Benefit: simpler use."] , "Row arrow → Hides complexity."),
 panel("3. INHERITANCE", ["A child class receives accessible behavior from a parent class.", "Example: Dog extends Animal.", "Benefit: shared behavior when there is a true IS-A relation."] , "Animal → Dog."),
 panel("4. POLYMORPHISM", ["The same method call can behave differently for different objects.", "Example: shape.draw() works for Circle and Rectangle.", "Benefit: flexible code."] , "Shape branches to Circle/Rectangle."),
 panel("5. ASSOCIATION", ["Objects can use or contain other objects.", "Example: Order has Customer and LineItem objects.", "Benefit: models relationships."])
 ], flowchart="Real thing → class model → data + methods → collaborating objects.",
 important=["OOP is not only writing classes; it is placing responsibilities in clear objects.", "Prefer simple object relationships over deep inheritance trees."],
 summary=["OOP groups state and behavior.", "Four main ideas are encapsulation, abstraction, inheritance, and polymorphism."],
 interview=["Explain each OOP concept using one simple example."])


page(16, "Module 2 — Object-Oriented Java", "ENCAPSULATION + DATA HIDING",
"Encapsulation means keeping an object's data private and allowing it to change only through safe methods.",
"Top definition. Middle bad/good comparison. Bottom account example.", [
 panel("WHY HIDE DATA?", ["Public fields can be changed to any value from anywhere.", "Private fields stop outside code from changing data directly.", "Public methods can check a value before changing the field.", "This keeps the object in a valid state."], "Open box with unsafe arrows versus protected box with one checked entrance."),
 panel("GETTERS AND SETTERS", ["A getter returns a value when callers need to read it.", "A setter changes a value, but it should validate the new value.", "Not every field needs both a getter and setter.", "A meaningful method such as withdraw(amount) is clearer than setBalance(value)."])
 ], code=["class BankAccount {\n  private double balance;\n\n  public void deposit(double amount) {\n    if (amount <= 0) throw new IllegalArgumentException();\n    balance += amount;\n  }\n\n  public double getBalance() { return balance; }\n}"],
 flowchart="Caller → public method → validation → private field changes safely.",
 important=["Encapsulation is more than private fields; it protects rules.", "Expose actions the object supports, not all internal details."],
 summary=["Private data + safe methods = encapsulation.", "The object protects its own valid state."],
 interview=["Why is withdraw(amount) better than a public balance field?"])

page(17, "Module 2 — Object-Oriented Java", "INHERITANCE + IS-A RELATIONSHIP",
"Inheritance lets one class receive behavior from another class when the child is truly a type of the parent.",
"Parent/child diagram, syntax, and use/do-not-use comparison.", [
 panel("PARENT AND CHILD", ["The parent or superclass contains common behavior.", "The child or subclass uses extends and may add or change behavior.", "A Dog IS-A Animal, so the relationship can make sense.", "Constructors are not inherited, but a child constructor can call super(...)."], "Animal top box; Dog and Cat child boxes."),
 panel("WHEN TO USE", ["Use inheritance when every child can safely be used wherever the parent is expected.", "Do not use inheritance only to copy some code.", "A Car is not an Engine; a Car HAS-A Engine, so composition is better.", "Java classes can extend only one class."])
 ], code=["class Animal {\n  void eat() { System.out.println(\"Eating\"); }\n}\n\nclass Dog extends Animal {\n  void bark() { System.out.println(\"Woof\"); }\n}"],
 flowchart="General parent → common behavior → specialized child adds behavior.",
 important=["private parent fields are not directly accessible in the child.", "Favor composition when there is no clear IS-A relationship."],
 summary=["Inheritance shares behavior through an IS-A relation.", "A child should respect the parent's promise."],
 interview=["Is Car extends Engine a good design? Why or why not?"])

page(18, "Module 2 — Object-Oriented Java", "POLYMORPHISM: OVERLOADING vs OVERRIDING",
"Polymorphism means 'many forms': one name or contract can work in more than one way.",
"Reference-style two-column comparison and runtime object diagram.", [
 panel("METHOD OVERLOADING", ["Same method name, different parameter list.", "Usually written in the same class.", "The compiler selects the method using the argument types.", "Return type alone cannot create a valid overload."], "Compile-time label with two add methods."),
 panel("METHOD OVERRIDING", ["A child class gives a new implementation of an inherited method.", "Name and parameter list match the parent method.", "@Override lets the compiler check our intention.", "The real object type chooses the method while the program runs."], "Animal reference points to Dog object; sound() prints Woof."),
 panel("WHY IT HELPS", ["Code can use a general type such as PaymentMethod.", "Different objects perform pay() in their own way.", "The caller does not need a large if/else for every concrete type."])
 ], code=["int add(int a, int b) { return a + b; }\ndouble add(double a, double b) { return a + b; }", "Animal animal = new Dog();\nanimal.sound(); // Dog version runs"],
 flowchart="General reference → actual object → overridden method runs.",
 important=["Overloading is chosen at compile time; overriding is chosen at runtime.", "Use @Override whenever a method is intended to override."],
 summary=["Overloading changes parameters.", "Overriding changes inherited behavior."],
 interview=["Give one difference between overloading and overriding."])

page(19, "Module 2 — Object-Oriented Java", "ABSTRACT CLASS vs INTERFACE",
"An abstract class is an incomplete base class. An interface is a contract that tells what a class can do.",
"Reference-matched three-column table with 10 easy rows and a choice guide.", [
 panel("FEATURE COMPARISON", ["Definition — abstract class: base class that cannot be created directly; interface: contract/capability implemented by classes.", "Keyword — abstract class uses abstract; interface uses interface.", "Methods — abstract class may have abstract and normal methods; interface may have abstract, default, static, and private methods.", "Variables — abstract class may have instance fields; interface fields are constants (public static final).", "Constructor — abstract class can have constructors; interface cannot.", "Inheritance — extend one class; implement multiple interfaces.", "Access — class members can use different access levels; interface abstract methods are public.", "Use — shared state/base behavior versus a common capability.", "Example — Animal base class versus Drawable contract.", "Modern Java — interfaces can also contain useful default helper behavior."], "Columns Feature | Abstract Class | Interface; ten numbered rows."),
 panel("SIMPLE CHOICE", ["Need shared fields and base setup? Choose an abstract class.", "Need one class to promise several abilities? Choose interfaces.", "Need only to reuse a helper? First consider a separate helper object (composition)."])
 ], code=["abstract class Animal {\n  abstract void sound();\n}\n\ninterface Drawable {\n  void draw();\n}"],
 flowchart="Shared base state? → Abstract class. Common ability/multiple roles? → Interface.",
 important=["A class can extend one class and implement many interfaces.", "Since Java 8 interfaces may have default/static methods; since Java 9 they may have private helpers."],
 summary=["Abstract class = shared base.", "Interface = common contract or ability."],
 interview=["When would you choose an interface instead of an abstract class?"])

page(20, "Module 2 — Object-Oriented Java", "Object CLASS + equals + hashCode",
"Object is the top parent of Java classes. Its common methods help compare, describe, and identify objects.",
"Method table and two-object equality drawing.", [
 panel("COMMON Object METHODS", ["toString() returns a text description useful for logs and debugging.", "equals() answers whether two objects should be treated as logically equal.", "hashCode() gives a number used by hash collections.", "getClass() returns the object's runtime class."] , "Table Method | Easy meaning | Example use."),
 panel("== vs equals", ["== compares primitive values directly.", "For objects, == asks whether two references point to the same object.", "equals asks whether objects represent the same logical value when implemented that way.", "String overrides equals, so use it for String value comparison."]),
 panel("THE RULE", ["If two objects are equal, they must have the same hash code.", "Override equals and hashCode together.", "Do not change equality fields while an object is inside HashSet or used as a HashMap key."])
 ], code=["String a = new String(\"Java\");\nString b = new String(\"Java\");\n\na == b;       // false: different objects\na.equals(b);  // true: same text"],
 flowchart="Compare references? → ==. Compare object meaning? → equals → matching hashCode rule.",
 important=["toString should never reveal passwords or secret data.", "Records automatically create useful equals, hashCode, and toString methods."],
 summary=["== checks identity for objects; equals checks logical value.", "Equal objects need equal hash codes."],
 interview=["Why should equals and hashCode be overridden together?"])

page(21, "Module 2 — Object-Oriented Java", "STRING, STRINGBUILDER + STRING POOL",
"String represents text. String objects are immutable, meaning their text cannot be changed after creation.",
"Top string pool drawing. Middle method examples. Bottom comparison table.", [
 panel("STRING IMMUTABILITY", ["A String operation returns a new String instead of changing the old one.", "Immutability makes String safe to share and suitable as a map key.", "String literals with the same text can share one object in the string pool.", "new String(...) normally creates a separate object."] , "Two literal references point to one pooled 'Java'; new String points outside."),
 panel("USEFUL METHODS", ["length gives character count.", "equals compares text; equalsIgnoreCase ignores letter case.", "substring takes part of the text.", "trim/strip removes surrounding whitespace.", "split separates text into parts."]),
 panel("BUILDING TEXT", ["Repeated + inside a loop can create many temporary String objects.", "StringBuilder is mutable and efficient for building text on one thread.", "StringBuffer is synchronized and is less commonly needed."])
 ], code=["String name = \"Java\";\nString upper = name.toUpperCase();\n\nStringBuilder text = new StringBuilder();\ntext.append(\"Order: \").append(42);\nString result = text.toString();"],
 flowchart="Original String → operation → new String; StringBuilder → many appends → final String.",
 important=["Use equals, not ==, for String content.", "A String can be empty (\"\") or null; they are different."],
 summary=["String is immutable text.", "StringBuilder is useful for repeated text building."],
 interview=["Why does name.toUpperCase() not change the original String?"])

page(22, "Module 2 — Object-Oriented Java", "WRAPPER CLASSES, ENUMS + RECORDS",
"Wrapper classes turn primitive values into objects; enums define fixed choices; records define small data carriers.",
"Three reference-style rows with definition, example, and use.", [
 panel("WRAPPER CLASSES", ["Integer wraps int, Long wraps long, Double wraps double, and Boolean wraps boolean.", "Generics and collections use objects, so List<Integer> is used instead of List<int>.", "Autoboxing converts primitive to wrapper; unboxing converts back.", "A wrapper may be null, which can cause a problem during unboxing."], "int 5 ↔ Integer object."),
 panel("ENUM", ["An enum lists a fixed set of named values.", "It is safer than passing random text for a known choice.", "Enums may contain fields, constructors, and methods.", "Example states: NEW, PAID, SHIPPED."]),
 panel("RECORD", ["A record is a short way to create a data-focused class.", "It creates a constructor, accessors, equals, hashCode, and toString.", "Its fields cannot be reassigned, but an object stored inside can still be mutable."])
 ], code=["enum OrderStatus { NEW, PAID, SHIPPED }\n\nrecord UserResponse(long id, String name) {}\n\nList<Integer> scores = List.of(10, 20);"],
 flowchart="Simple number → wrapper when object is needed; fixed choices → enum; small data result → record.",
 important=["Compare enum values with ==.", "Do not use a wrapper as a field when a primitive clearly cannot be absent."],
 summary=["Wrappers provide object forms of primitives.", "Enums name fixed choices; records carry data concisely."],
 interview=["Why does List<int> not work, but List<Integer> does?"])

page(23, "Module 2 — Object-Oriented Java", "EXCEPTIONS + try-catch-finally",
"An exception is an object that tells us something unexpected stopped the normal flow of a program.",
"Throwable tree on top; try/catch flow and good practices below.", [
 panel("EXCEPTION FAMILY", ["Throwable is the top type.", "Error usually represents a serious JVM/system problem an application does not normally handle.", "Exception represents problems application code may report or handle.", "RuntimeException is unchecked; other common Exception types are checked by the compiler."], "Tree Throwable → Error and Exception → RuntimeException."),
 panel("TRY, CATCH, FINALLY", ["try contains code that may fail.", "catch handles a matching exception.", "finally runs after try/catch for cleanup in normal cases.", "Do not use a wide catch(Exception) unless that boundary can handle it properly."]),
 panel("GOOD ERROR HANDLING", ["Catch an exception only when you can recover, add useful context, or translate it.", "Keep the original cause when creating another exception.", "Never ignore an exception with an empty catch block.", "Do not show stack traces or database details to API users."])
 ], code=["try {\n  int value = Integer.parseInt(input);\n  System.out.println(value);\n} catch (NumberFormatException ex) {\n  System.out.println(\"Please enter a number\");\n} finally {\n  System.out.println(\"Finished\");\n}"],
 flowchart="Normal work → problem thrown → matching catch → continue or return safe error.",
 important=["Checked exceptions must be caught or declared; unchecked exceptions do not have that compiler rule.", "Exceptions should not be used as normal loop or decision logic."],
 summary=["Exceptions describe failed program flow.", "Handle them at a place that can make a useful decision."],
 interview=["What is the job of try, catch, and finally?"])

page(24, "Module 2 — Object-Oriented Java", "CUSTOM EXCEPTIONS + RESOURCE SAFETY",
"A custom exception gives a failure a clear application meaning. Try-with-resources closes resources automatically.",
"Left exception translation ladder; right resource lifecycle.", [
 panel("CUSTOM EXCEPTION", ["Create one when the failure has a useful domain meaning such as OrderNotFound.", "Give it a clear name and useful safe information.", "Pass the original exception as the cause when translating a lower-level failure.", "Do not create a different exception class for every tiny message."] , "Database error → OrderLoadException → safe API response."),
 panel("TRY-WITH-RESOURCES", ["Files, streams, and database resources must be closed.", "A resource implementing AutoCloseable can be declared inside try(...).", "Java closes resources automatically, even when work throws an exception.", "Resources close in reverse order of creation."])
 ], code=["class OrderNotFoundException extends RuntimeException {\n  OrderNotFoundException(long id) {\n    super(\"Order not found: \" + id);\n  }\n}", "try (var reader = Files.newBufferedReader(path)) {\n  return reader.readLine();\n}"],
 flowchart="Open resource → use resource → success or exception → automatic close.",
 important=["Garbage collection does not replace closing files and database connections.", "Public error messages must not expose secrets or internal system details."],
 summary=["Custom exceptions give failures clear meaning.", "Try-with-resources makes cleanup reliable."],
 interview=["Why is try-with-resources safer than manually closing a file?"])

page(25, "Module 2 — Object-Oriented Java", "GENERICS — TYPE-SAFE REUSABLE CODE",
"Generics let one class or method work with different types while the compiler still checks type safety.",
"Before/after boxes and type parameter anatomy.", [
 panel("WHY GENERICS?", ["Without generics, an Object container needs casts and may fail at runtime.", "With Box<String>, the compiler knows only String values belong there.", "A type parameter such as T is a placeholder for a real type.", "Generics make collections and reusable APIs safer."] , "Object box with unsafe cast versus Box<String> with compiler check."),
 panel("COMMON FORMS", ["Class: Box<T>.", "Two types: Map<K,V> for key and value.", "Method: <T> T first(List<T> items).", "Bound: <T extends Number> accepts Number subtypes."]),
 panel("IMPORTANT LIMIT", ["List<Integer> is not a child of List<Number>.", "Most generic type details are removed at runtime; this is called type erasure.", "Primitive types cannot be type arguments; use wrappers such as Integer."])
 ], code=["class Box<T> {\n  private T value;\n  void set(T value) { this.value = value; }\n  T get() { return value; }\n}\n\nBox<String> box = new Box<>();"],
 flowchart="Write generic T once → use as String, Integer, Order, and other reference types.",
 important=["Avoid raw List or Box because it removes useful compiler checks.", "Use clear type names such as T, K, V, or descriptive names in complex code."],
 summary=["Generics provide reusable code with type safety.", "The compiler catches many wrong-type mistakes early."],
 interview=["What problem does Box<T> solve compared with storing Object?"])

page(26, "Module 2 — Object-Oriented Java", "WILDCARDS + PECS",
"A wildcard ? means an unknown type. It helps a method accept a safe family of generic types.",
"Producer/consumer two-column table with arrows and small examples.", [
 panel("? extends — PRODUCER", ["List<? extends Number> means a list of some Number subtype.", "We can safely read its items as Number.", "We cannot safely add an Integer because the real list might be List<Double>.", "Remember: a producer gives values to us."] , "List<Integer>/List<Double> arrows into read Number."),
 panel("? super — CONSUMER", ["List<? super Integer> means a list that can receive Integer values.", "We may add an Integer safely.", "When reading, only Object is guaranteed.", "Remember: a consumer accepts values from us."]),
 panel("PECS RULE", ["Producer Extends, Consumer Super.", "Use exact List<T> when the method both reads and writes T.", "Use a named T when parameter and return types must be connected."])
 ], code=["double sum(List<? extends Number> values) {\n  return values.stream()\n      .mapToDouble(Number::doubleValue).sum();\n}\n\nvoid addId(List<? super Long> out) {\n  out.add(10L);\n}"],
 flowchart="Only read T? → extends. Only add T? → super. Read and add T? → exact type.",
 important=["Wildcards are mainly useful in method/API boundaries.", "Do not return complicated wildcard types unless callers truly need them."],
 summary=["extends is good for reading.", "super is good for adding."],
 interview=["Explain PECS in one sentence."])

page(27, "Module 2 — Object-Oriented Java", "COLLECTIONS FRAMEWORK OVERVIEW",
"A collection stores and organizes a group of objects. Different collection types provide different rules.",
"Large hierarchy tree and four-question choice guide.", [
 panel("MAIN INTERFACES", ["List keeps item positions and allows duplicates.", "Set keeps unique items.", "Queue keeps items waiting to be processed.", "Deque works at both ends and can act as queue or stack.", "Map stores key-value pairs and is not a child of Collection."], "Iterable → Collection → List/Set/Queue → Deque; separate Map branch."),
 panel("CHOOSE BY NEED", ["Need position/order and duplicates? List.", "Need uniqueness? Set.", "Need lookup by key? Map.", "Need first/next work item? Queue.", "Need sorted data? Choose a sorted implementation such as TreeSet/TreeMap."]),
 panel("INTERFACE + IMPLEMENTATION", ["Declare the general interface when possible: List<String>.", "Choose an implementation for behavior: new ArrayList<>().", "Most normal collections are not safe for changing from many threads at once."])
 ], code=["List<String> names = new ArrayList<>();\nSet<String> uniqueNames = new HashSet<>();\nMap<Long, String> nameById = new HashMap<>();"],
 flowchart="What rule do the items need? → List / Set / Queue / Map → choose implementation.",
 important=["Collections store objects, so primitives use wrappers.", "Ordering, uniqueness, and thread safety are part of correctness."],
 summary=["Collection type describes the rule for stored items.", "Choose by behavior, not habit."],
 interview=["When would you choose Set instead of List?"])

page(28, "Module 2 — Object-Oriented Java", "LIST, SET, QUEUE + DEQUE",
"List, Set, Queue, and Deque are collection interfaces made for different ways of storing and reading items.",
"Four reference-style rows: meaning, implementations, example, caution.", [
 panel("LIST", ["ArrayList uses a resizable array and is the common general choice.", "It gives fast index access; middle insert/remove may shift items.", "LinkedList uses linked nodes and has slow index access."] , "Array boxes with index numbers."),
 panel("SET", ["HashSet gives expected fast membership checks and no sorted order.", "LinkedHashSet keeps insertion order.", "TreeSet keeps sorted order.", "Uniqueness depends on equals and hashCode (or comparison for sorted sets)."]),
 panel("QUEUE + DEQUE", ["Queue normally processes the next item first.", "offer adds, poll removes, and peek reads the head without removing.", "ArrayDeque is a good normal queue/stack implementation.", "PriorityQueue returns the highest-priority head, not fully sorted iteration."])
 ], code=["List<String> list = new ArrayList<>();\nlist.add(\"A\");\n\nSet<String> set = new HashSet<>();\nset.add(\"A\");\n\nDeque<String> jobs = new ArrayDeque<>();\njobs.offerLast(\"email\");"],
 flowchart="Items → need position? List; unique? Set; processing order? Queue/Deque.",
 important=["ArrayList is often faster than LinkedList in real programs because arrays use memory efficiently.", "Do not depend on HashSet iteration order."],
 summary=["List = position; Set = unique; Queue = next item.", "Implementation decides ordering and speed."],
 interview=["What do offer, poll, and peek do?"])

page(29, "Module 2 — Object-Oriented Java", "Map + HashMap INTERNALS",
"A Map stores a value under a unique key. HashMap uses a key's hashCode and equals methods to find its entry.",
"Top map picture. Middle put/get flow. Bottom implementation comparison.", [
 panel("MAP BASICS", ["put(key,value) adds or replaces a value.", "get(key) returns the matching value or null when none is found.", "containsKey checks whether a key exists.", "Keys are unique; different keys may point to equal values."] , "ID keys on left point to Customer values on right."),
 panel("HOW HashMap FINDS A KEY", ["1. Call key.hashCode().", "2. Use the hash to choose a bucket.", "3. Check equals among keys in that bucket.", "4. Return/replace/add the matching entry.", "Different keys may have the same hash; this is called a collision."] , "Bucket array with two keys in one bucket."),
 panel("OTHER MAPS", ["LinkedHashMap keeps insertion or configured access order.", "TreeMap keeps keys sorted.", "ConcurrentHashMap supports safe concurrent operations and does not allow null keys/values."])
 ], code=["Map<Long, String> users = new HashMap<>();\nusers.put(10L, \"Asha\");\nString name = users.get(10L);"],
 flowchart="Key → hashCode → bucket → equals check → value.",
 important=["Do not change fields used by a key's equals/hashCode while it is in the map.", "HashMap allows one null key, but using null often makes code less clear."],
 summary=["Map connects keys to values.", "hashCode narrows the search; equals confirms the key."],
 interview=["What happens when two different keys have the same hash code?"])

page(30, "Module 2 — Object-Oriented Java", "Comparable vs Comparator",
"Comparable defines a type's natural order. Comparator defines a separate chosen order.",
"Two-column comparison table and sorting examples.", [
 panel("COMPARABLE", ["The class implements Comparable<T>.", "It defines compareTo(T other).", "It is used for one main natural order.", "Example: sort Product naturally by product code."] , "Class owns one natural-order arrow."),
 panel("COMPARATOR", ["It is a separate object/function.", "It defines compare(a,b).", "A type can have many comparators.", "Example: sort Product by price, name, or newest date."]),
 panel("RETURN VALUE", ["Negative means first value comes before second.", "Zero means equal in this ordering.", "Positive means first comes after second.", "Use Comparator.comparing instead of subtracting numbers, which can overflow."])
 ], code=["Comparator<Product> byPrice =\n    Comparator.comparing(Product::getPrice);\n\nproducts.sort(byPrice.thenComparing(Product::getName));"],
 flowchart="Need one natural order? → Comparable. Need a situation-specific order? → Comparator.",
 important=["TreeSet and TreeMap use comparison to decide sorted uniqueness.", "Comparator can be reversed and chained with thenComparing."],
 summary=["Comparable lives in the class.", "Comparator supplies one outside ordering."],
 interview=["How can the same products be sorted by both name and price?"])


page(31, "Module 3 — Useful Modern Java", "LAMBDAS + FUNCTIONAL INTERFACES",
"A lambda is a short way to provide a piece of behavior. A functional interface is an interface with one abstract method.",
"Anonymous class to lambda transformation; four-interface table below.", [
 panel("FROM LONG TO SHORT", ["Before lambdas, a small behavior often needed an anonymous class.", "A lambda writes parameters, an arrow ->, and the action.", "The lambda receives its meaning from a functional interface type.", "Use @FunctionalInterface to clearly mark the intended contract."] , "Long anonymous class shrinks into (x) -> action."),
 panel("COMMON INTERFACES", ["Predicate<T>: takes T and returns true/false.", "Function<T,R>: changes T into R.", "Consumer<T>: accepts T and returns nothing.", "Supplier<T>: takes nothing and returns T."], "Table Interface | Shape | Method | Easy example."),
 panel("METHOD REFERENCE", ["A method reference is a shorter lambda that calls an existing method.", "name -> print(name) can become System.out::println.", "Keep lambdas short; move larger logic to a named method."])
 ], code=["Predicate<Integer> adultAge = age -> age >= 18;\nFunction<String, Integer> length = String::length;\nConsumer<String> print = System.out::println;\nSupplier<UUID> newId = UUID::randomUUID;"],
 flowchart="Input → lambda behavior → output; target interface explains input/output types.",
 important=["A lambda may use a local variable only when it is final or effectively final.", "Do not hide large business logic inside one long lambda."],
 summary=["Lambda passes behavior as a value.", "Functional interfaces give lambdas a clear type."],
 interview=["What are Predicate and Function used for?"])

page(32, "Module 3 — Useful Modern Java", "STREAM API — FILTER, MAP + COLLECT",
"A stream is a pipeline that reads data from a source, transforms it, and produces a result.",
"Large conveyor-belt pipeline with intermediate/terminal table.", [
 panel("STREAM PIPELINE", ["Source: a collection, array, or other data source.", "filter keeps items that match a condition.", "map changes each item into another value.", "sorted orders items; distinct removes duplicates.", "A terminal operation such as toList, count, or collect produces the result."], "Orders → filter paid → map IDs → sorted → list."),
 panel("LAZY WORK", ["Intermediate operations are lazy: they wait until a terminal operation starts.", "A stream is normally used once.", "A stream does not store the items; the source stores them.", "Avoid changing shared outside data inside a stream operation."]),
 panel("USEFUL OPERATIONS", ["anyMatch asks whether any item matches.", "findFirst returns an Optional result.", "flatMap opens and combines nested groups.", "groupingBy groups items using a selected value."])
 ], code=["List<String> names = users.stream()\n    .filter(User::isActive)\n    .map(User::getName)\n    .sorted()\n    .toList();"],
 flowchart="Collection → filter → map → sort → terminal result.",
 important=["Use a normal loop when it is clearer than a stream.", "Parallel streams are not automatically faster and are poor for ordinary blocking database/API calls."],
 summary=["Streams describe a data-processing pipeline.", "Intermediate steps are lazy; a terminal step starts the work."],
 interview=["What is the difference between filter and map?"])

page(33, "Module 3 — Useful Modern Java", "Optional + DATE/TIME API",
"Optional represents a result that may be present or absent. java.time classes represent dates and time clearly.",
"Left Optional railway; right time-type choice table.", [
 panel("OPTIONAL", ["Optional.of(value) holds a non-null value.", "Optional.empty() represents no value.", "Use map, orElseGet, and orElseThrow instead of immediately calling get().", "It is most useful as a method return type when absence is normal."] , "Present track → map; empty track → fallback/throw."),
 panel("TIME TYPES", ["LocalDate: a date such as 2026-09-27.", "LocalTime: time of day without a date.", "LocalDateTime: date and time but no zone/offset.", "Instant: one exact moment on the global timeline.", "ZonedDateTime: date/time with time-zone rules.", "Duration measures time; Period measures calendar dates."] , "Type | Contains | Easy use table."),
 panel("TESTABLE TIME", ["Use Clock as a dependency when code needs the current time.", "Store global event times as Instant/UTC in many backend systems.", "Convert to a user's zone when displaying time."])
 ], code=["User user = repository.findById(id)\n    .orElseThrow(() -> new UserNotFound(id));\n\nInstant now = clock.instant();\nLocalDate today = LocalDate.now(clock);"],
 flowchart="Could result be absent? → Optional return. Need exact event moment? → Instant. Human calendar date? → LocalDate.",
 important=["orElse creates its fallback immediately; orElseGet creates it only when needed.", "LocalDateTime alone does not identify one global moment."],
 summary=["Optional clearly shows possible absence.", "Choose a time type that contains the information you need."],
 interview=["What is the difference between Instant and LocalDateTime?"])

page(34, "Module 3 — Useful Modern Java", "FILES + INPUT/OUTPUT STREAMS",
"Input means reading data; output means writing data. Java streams move bytes or characters between a program and another place.",
"Byte/character comparison and file read/write lifecycle.", [
 panel("BYTE vs CHARACTER", ["InputStream and OutputStream work with raw bytes, useful for images and binary files.", "Reader and Writer work with characters, useful for text.", "Buffered versions reduce expensive small read/write operations.", "Files utility methods provide simple operations for paths and small files."] , "Binary file → byte stream; text file → reader/writer."),
 panel("PATH + FILES", ["Path represents a file-system path.", "Files.exists checks existence.", "Files.readString/writeString are convenient for small text files.", "Large files should be streamed instead of fully loaded into memory."]),
 panel("SAFE USE", ["Use try-with-resources so open files close.", "Choose the correct character encoding, commonly UTF-8.", "Validate file names/paths when they come from users to prevent path traversal."])
 ], code=["Path path = Path.of(\"notes.txt\");\nFiles.writeString(path, \"Hello\", UTF_8);\nString text = Files.readString(path, UTF_8);\n\ntry (var lines = Files.lines(path)) {\n  lines.forEach(System.out::println);\n}"],
 flowchart="Path → open → read/write in chunks → close automatically.",
 important=["A file is outside Java heap memory, but loaded file contents use heap memory.", "Never trust a user-provided file path without validation."],
 summary=["Byte streams handle binary; character streams handle text.", "Close resources and choose encoding explicitly."],
 interview=["When would you use Reader instead of InputStream?"])

page(35, "Module 3 — Useful Modern Java", "THREADS + CONCURRENCY BASICS",
"A thread is one path of work inside a program. Concurrency means several tasks can make progress during the same time period.",
"Thread lifecycle on top; race-condition timeline below.", [
 panel("WHY THREADS?", ["A server handles many user requests, often using many threads.", "Concurrency can improve responsiveness and throughput.", "More threads do not always mean more speed; CPU and other resources are limited.", "Call start() to begin a new thread; directly calling run() is a normal method call."] , "Thread states: NEW → RUNNABLE → WAITING/BLOCKED → TERMINATED."),
 panel("RACE CONDITION", ["A race happens when threads read/write shared data without safe coordination.", "count++ is read, add, and write—not one guaranteed atomic step.", "Two threads may both read 10 and both write 11, losing one update.", "Prefer immutable/local data before adding locks."] , "Two-thread timeline showing lost update."),
 panel("SAFE TOOLS", ["synchronized allows one thread at a time in a protected section and makes changes visible.", "volatile helps visibility for one variable but does not make count++ atomic.", "AtomicInteger provides atomic operations for a single integer value."])
 ], code=["private final AtomicInteger count = new AtomicInteger();\n\nvoid increment() {\n  count.incrementAndGet();\n}"],
 flowchart="Shared mutable data? → avoid sharing if possible → otherwise choose atomic value or protected critical section.",
 important=["sleep pauses a thread but does not release a lock it holds.", "Interruption is a cooperative request for a thread to stop/wake, not a forced kill."],
 summary=["Threads allow concurrent work.", "Shared changing data needs a safety plan."],
 interview=["Why is volatile not enough for count++?"])

page(36, "Module 3 — Useful Modern Java", "EXECUTORS + CompletableFuture",
"An Executor manages worker threads for us. CompletableFuture represents work that may finish later.",
"Executor queue diagram and future composition railway.", [
 panel("EXECUTOR", ["Submit a Runnable when no result is needed.", "Submit a Callable<T> when a result is needed.", "A thread pool reuses a limited number of worker threads.", "A bounded queue prevents unlimited waiting tasks from filling memory.", "Shut down an executor when its owner stops."] , "Tasks → bounded queue → worker threads → results."),
 panel("CompletableFuture", ["supplyAsync starts work that returns a value.", "thenApply changes a completed value.", "thenCompose starts a next async step and avoids a nested future.", "thenCombine joins independent results.", "exceptionally can provide a fallback for a failure."]),
 panel("LIMITS", ["Always use timeouts for remote work.", "Choose an intentional executor for blocking work.", "Async code does not make a slow database faster.", "Modern virtual threads make many blocking tasks cheaper, but downstream limits still matter."])
 ], code=["CompletableFuture<User> user =\n    CompletableFuture.supplyAsync(() -> loadUser(id), pool);\n\nreturn user.thenApply(UserResponse::from)\n           .orTimeout(1, SECONDS);"],
 flowchart="Submit task → queue → worker executes → future completes → next step or error path.",
 important=["A very large pool can overload the database or another service.", "thenApply maps a value; thenCompose connects another future."],
 summary=["Executors control thread resources.", "CompletableFuture connects work that finishes later."],
 interview=["What is the difference between thenApply and thenCompose?"])

page(37, "Module 3 — Useful Modern Java", "JVM MEMORY + GARBAGE COLLECTION",
"The JVM uses several memory areas. Garbage collection automatically frees heap objects that are no longer reachable.",
"Large labeled memory map and reachable-object drawing.", [
 panel("MEMORY AREAS", ["Heap: most objects and arrays; shared by threads.", "Stack: each thread's method calls and local working values.", "Metaspace: class information in native memory.", "Code cache: machine code created by the JIT compiler.", "Direct/native memory: buffers, thread stacks, and native libraries outside the heap."] , "One process split into heap, per-thread stacks, metaspace, code cache, native."),
 panel("GARBAGE COLLECTION", ["GC starts from roots such as active thread stacks and static references.", "Objects reachable from roots stay alive.", "Unreachable objects may be collected.", "GC manages memory, but it does not close files or database connections for us."] , "Green reachable graph and faded unreachable island."),
 panel("COMMON PROBLEMS", ["StackOverflowError often comes from endless/deep recursion.", "OutOfMemoryError means a memory area could not provide more space.", "An unbounded cache or list can keep unwanted objects reachable.", "Use measurements, GC logs, thread dumps, heap dumps, and Java Flight Recorder to investigate."])
 ], flowchart="Create object → reachable while used → no path from roots → eligible for collection.",
 important=["A Java memory leak means unwanted objects are still reachable.", "Do not call System.gc() as a normal fix."],
 summary=["Heap stores objects; stacks hold thread method work.", "GC removes unreachable objects."],
 interview=["Can Java have a memory leak even with garbage collection?"])

page(38, "Module 4 — Design, Build + Web Basics", "SOLID PRINCIPLES — EASY VERSION",
"SOLID is a set of five design ideas that help code stay understandable and easier to change.",
"Five reference-style rows with simple definition and example.", [
 panel("S — SINGLE RESPONSIBILITY", ["A class should have one main reason to change.", "OrderService should not also generate PDFs and send every email."] , "Large mixed class splits into focused helpers."),
 panel("O — OPEN/CLOSED", ["Add a new behavior with a safe extension instead of repeatedly changing stable code.", "PaymentStrategy can gain a new payment type."]),
 panel("L — LISKOV SUBSTITUTION", ["A child implementation must keep the promise of its parent type.", "A subtype should not surprise callers by rejecting valid parent operations."]),
 panel("I — INTERFACE SEGREGATION", ["Prefer small useful interfaces over one huge interface.", "A reader should not be forced to implement write methods."]),
 panel("D — DEPENDENCY INVERSION", ["Business code depends on a useful contract, not directly on vendor/database details.", "CheckoutService depends on PaymentGateway."])
 ], code=["class CheckoutService {\n  private final PaymentGateway gateway;\n\n  CheckoutService(PaymentGateway gateway) {\n    this.gateway = gateway;\n  }\n}"],
 flowchart="Find responsibility → find change point → create smallest clear boundary → test the behavior.",
 important=["SOLID is guidance, not a rule to create the maximum number of classes.", "Create an abstraction only when it makes the design clearer."],
 summary=["SOLID helps separate responsibilities and changes.", "Simple code is more important than blindly following a pattern."],
 interview=["Explain one SOLID principle with a simple example."])

page(39, "Module 4 — Design, Build + Web Basics", "COMMON DESIGN PATTERNS",
"A design pattern is a common way to solve a problem that appears again and again in software.",
"Four pattern cards with problem, shape, and backend example.", [
 panel("FACTORY", ["Problem: the program must choose which object to create.", "Factory keeps creation/selection in one place.", "Example: NotificationFactory returns EmailSender or SmsSender."] , "Input type → Factory → chosen object."),
 panel("BUILDER", ["Problem: an object has many optional construction values.", "Builder names each value and creates the final object.", "Example: building an HTTP request or test data."]),
 panel("STRATEGY", ["Problem: one task has several interchangeable ways.", "Each strategy follows one contract.", "Example: CardPayment and UpiPayment implement PaymentStrategy."]),
 panel("ADAPTER + DECORATOR", ["Adapter changes an external API into the interface our app expects.", "Decorator wraps an object to add logging, caching, metrics, or retry.", "Spring often uses proxies with decorator-like behavior."])
 ], code=["PaymentStrategy strategy = strategies.get(type);\nPaymentResult result = strategy.pay(command);"],
 flowchart="Repeated design problem → understand trade-offs → choose smallest useful pattern → keep code readable.",
 important=["Patterns are names for solutions, not goals by themselves.", "Singleton means one instance in a particular container/context, not one object in the whole distributed system."],
 summary=["Patterns give developers a shared design language.", "Use one only when it makes the problem simpler."],
 interview=["What problem does the Strategy pattern solve?"])

page(40, "Module 4 — Design, Build + Web Basics", "MAVEN, PROJECT STRUCTURE + GIT",
"Maven builds Java projects and manages libraries. Git records code changes and helps a team work together.",
"Maven lifecycle at top, project tree and Git flow below.", [
 panel("MAVEN", ["pom.xml describes the project, dependencies, plugins, and settings.", "A dependency is a library the code uses.", "A plugin performs build work.", "Common flow: validate → compile → test → package → verify → install.", "Maven Wrapper (mvnw) helps a team use the intended Maven version."] , "Long lifecycle arrow."),
 panel("PROJECT STRUCTURE", ["src/main/java contains application Java code.", "src/main/resources contains configuration/templates/static resources.", "src/test/java contains tests.", "target contains generated build output and should not be committed.", "Grouping code by business feature often keeps related work together."]),
 panel("GIT FLOW", ["Create a small branch/change, make focused commits, and open a pull request.", "Automated checks and review run before merging.", "Never commit passwords, secret keys, target output, or personal IDE files."])
 ], code=["./mvnw clean verify\n./mvnw spring-boot:run\ngit status\ngit add .\ngit commit -m \"Add order validation\""],
 flowchart="Source + pom.xml → compile → test → package JAR → deploy; Git commit → review → main.",
 important=["Use dependency:tree to understand library version conflicts.", "A secret remains in old Git history even after deleting it from the latest file."],
 summary=["Maven makes builds repeatable.", "Git records and reviews code changes."],
 interview=["What is the difference between a Maven dependency and plugin?"])

page(41, "Module 4 — Design, Build + Web Basics", "HTTP, URL + JSON BASICS",
"HTTP is the request-response language used by web clients and servers. JSON is a common text format for request and response data.",
"Large HTTP request/response cards and method table.", [
 panel("HTTP REQUEST", ["Method says the action: GET, POST, PUT, PATCH, DELETE.", "URL identifies the address/resource.", "Headers carry extra information such as content type or authorization.", "Body carries data when needed, often JSON."] , "Request card with method, path, headers, body labels."),
 panel("HTTP RESPONSE", ["Status code explains the result.", "Headers describe the response.", "Body carries returned data or an error.", "Common codes: 200 OK, 201 Created, 204 No Content, 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 500 Server Error."]),
 panel("JSON", ["JSON objects use { } and name-value pairs.", "JSON arrays use [ ].", "Strings use double quotes.", "JSON has no comments and does not know Java class types by itself."])
 ], code=["POST /orders HTTP/1.1\nContent-Type: application/json\n\n{\n  \"productId\": 10,\n  \"quantity\": 2\n}"],
 flowchart="Client builds HTTP request → server processes → server sends status + headers + optional JSON.",
 important=["HTTPS is HTTP protected by TLS encryption in transit.", "A 401 means authentication is needed/failed; 403 means the known user is not allowed."],
 summary=["HTTP carries requests and responses.", "JSON carries structured text data."],
 interview=["What are the four main parts of an HTTP request?"])

page(42, "Module 4 — Design, Build + Web Basics", "DATABASE + SQL CRUD",
"A relational database stores information in tables. SQL is the language used to create, read, update, and delete that information.",
"Table anatomy on top; CRUD four-row examples below.", [
 panel("TABLE BASICS", ["A table represents one kind of information, such as customers.", "A row represents one record.", "A column represents one property and has a data type.", "A primary key uniquely identifies a row.", "A foreign key links a row to another table."] , "Customer table with row, column, primary key labels."),
 panel("CRUD", ["CREATE data: INSERT.", "READ data: SELECT.", "UPDATE data: UPDATE.", "DELETE data: DELETE.", "WHERE chooses which rows are affected."]),
 panel("SAFE VALUES", ["Use SQL parameters instead of joining user input into SQL text.", "Database constraints such as NOT NULL, UNIQUE, CHECK, and FOREIGN KEY protect valid data.", "Application validation gives friendly errors; database constraints protect every writer."])
 ], code=["INSERT INTO customer(name, email) VALUES (?, ?);\n\nSELECT id, name FROM customer WHERE email = ?;\n\nUPDATE customer SET name = ? WHERE id = ?;\n\nDELETE FROM customer WHERE id = ?;"],
 flowchart="Application sends parameterized SQL → database checks constraints → rows change/result returns.",
 important=["UPDATE or DELETE without the intended WHERE can affect every row.", "NULL means missing/unknown; check it with IS NULL, not = NULL."],
 summary=["Tables contain rows and columns.", "CRUD means create, read, update, and delete."],
 interview=["What is the purpose of a primary key and foreign key?"])

page(43, "Module 4 — Design, Build + Web Basics", "SQL FILTERING, GROUPING + JOINS",
"Filtering chooses rows, grouping summarizes rows, and joins combine related rows from tables.",
"Top logical query order. Middle joins drawing. Bottom aggregate example.", [
 panel("FILTER + GROUP", ["WHERE filters individual rows.", "GROUP BY places matching values into groups.", "COUNT, SUM, AVG, MIN, and MAX summarize data.", "HAVING filters completed groups.", "ORDER BY sorts the final result."] , "Rows → WHERE → groups → HAVING → ordered result."),
 panel("JOINS", ["INNER JOIN returns rows with a match on both sides.", "LEFT JOIN keeps every left row and uses NULL where no right match exists.", "The ON condition explains how rows are related.", "Joining one-to-many data can produce several result rows for one parent."] , "Customers and Orders key rows connected; show inner/left results."),
 panel("LOGICAL ORDER", ["FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT.", "Knowing this order explains why a selected alias may not be usable in WHERE."])
 ], code=["SELECT c.id, c.name, COUNT(o.id) AS order_count\nFROM customer c\nLEFT JOIN orders o ON o.customer_id = c.id\nWHERE c.active = TRUE\nGROUP BY c.id, c.name\nHAVING COUNT(o.id) >= 2\nORDER BY order_count DESC;"],
 flowchart="Choose tables → join → filter rows → group → filter groups → select → sort.",
 important=["A condition on the right table in WHERE can accidentally remove unmatched LEFT JOIN rows.", "Select only the columns the application needs."],
 summary=["WHERE filters rows; HAVING filters groups.", "Joins combine related table data."],
 interview=["What is the difference between INNER JOIN and LEFT JOIN?"])

page(44, "Module 4 — Design, Build + Web Basics", "INDEXES + ACID TRANSACTIONS",
"An index helps a database find rows faster. A transaction groups database work into one reliable unit.",
"B-tree picture on left; ACID four-box diagram and transfer flow on right.", [
 panel("DATABASE INDEX", ["An index is an extra ordered structure built from selected columns.", "It can speed up filtering, joining, and sorting.", "It uses storage and makes inserts/updates/deletes do extra work.", "A composite index contains more than one column; column order matters.", "Use the database query plan to check whether an index helps."] , "Book index analogy and small B-tree."),
 panel("ACID", ["Atomicity: all transaction steps succeed or all are undone.", "Consistency: constraints/rules remain valid.", "Isolation: concurrent transactions do not see unsafe partial work.", "Durability: committed data survives expected failures."] , "Four boxes around money transfer."),
 panel("ISOLATION IDEA", ["Concurrent users may read/change the same rows.", "Isolation levels choose which changes can be seen and what conflicts may happen.", "Keep transactions short so locks and database connections are not held too long."])
 ], code=["BEGIN;\nUPDATE account SET balance = balance - 100 WHERE id = 1;\nUPDATE account SET balance = balance + 100 WHERE id = 2;\nCOMMIT;"],
 flowchart="Begin → perform related SQL → success? commit : rollback.",
 important=["More indexes are not always better; they cost space and write time.", "A transaction does not automatically include a remote API or message broker."],
 summary=["Indexes trade write/storage cost for faster reads.", "Transactions protect a group of database changes."],
 interview=["What does Atomicity mean in a bank transfer?"])

page(45, "Module 4 — Design, Build + Web Basics", "JDBC + CONNECTION POOL",
"JDBC is Java's basic API for talking to relational databases. A connection pool reuses a limited set of database connections.",
"JDBC sequence on top; pool checkout/return below.", [
 panel("JDBC PARTS", ["DataSource provides database connections.", "Connection represents one database session.", "PreparedStatement holds parameterized SQL.", "ResultSet lets code read returned rows.", "SQLException describes a database-access failure."] , "Java → DataSource → Connection → PreparedStatement → DB → ResultSet."),
 panel("PREPARED STATEMENT", ["SQL structure and input values are kept separate.", "This is the normal defense against SQL injection for values.", "Each ? placeholder receives a typed value.", "Close Connection, Statement, and ResultSet with try-with-resources."]),
 panel("CONNECTION POOL", ["Opening a physical connection is expensive, so a pool reuses connections.", "A request borrows a connection and closing it returns it to the pool.", "Pool size is limited because the database has limited capacity.", "Slow queries/long transactions can exhaust the pool."])
 ], code=["try (Connection c = dataSource.getConnection();\n     PreparedStatement ps = c.prepareStatement(\n         \"SELECT name FROM customer WHERE id = ?\")) {\n  ps.setLong(1, id);\n  try (ResultSet rs = ps.executeQuery()) {\n    if (rs.next()) return rs.getString(\"name\");\n  }\n}"],
 flowchart="Borrow connection → prepare/bind → execute → read result → close returns connection.",
 important=["Never build SQL by directly joining untrusted input into the query.", "A larger connection pool can overload the database instead of fixing slow SQL."],
 summary=["JDBC sends safe SQL and reads results.", "A pool treats connections as limited reusable resources."],
 interview=["Why should JDBC code use PreparedStatement?"])


page(46, "Module 5 — JPA, Spring + Spring Boot", "JPA + HIBERNATE BASICS",
"JPA is a Java standard for mapping objects to relational data. Hibernate is a common tool that implements JPA.",
"Object/table mapping picture and entity lifecycle below.", [
 panel("ORM IDEA", ["ORM means Object-Relational Mapping.", "A Java entity class maps to a database table.", "An entity object maps to a row; fields map to columns.", "JPA defines annotations/APIs; Hibernate performs the work.", "JPA saves boilerplate but does not remove the need to understand SQL."] , "Order object fields align with orders table columns."),
 panel("ENTITY BASICS", ["@Entity marks a persistent class.", "@Id marks its identity/primary key.", "@GeneratedValue asks a configured strategy to create an ID.", "Entities need an accessible no-argument constructor for JPA.", "Use a transaction when changing stored data."]),
 panel("ENTITY STATES", ["Transient: new object not managed/saved.", "Managed: tracked by the persistence context.", "Detached: no longer tracked.", "Removed: marked for deletion.", "Dirty checking writes changes made to managed entities."] , "State circles with persist, detach, remove arrows.")
 ], code=["@Entity\n@Table(name = \"product\")\nclass Product {\n  @Id\n  private Long id;\n\n  private String name;\n  private BigDecimal price;\n}"],
 flowchart="Entity object → EntityManager/Hibernate → generated SQL → database row.",
 important=["Do not expose JPA entities directly as API response objects.", "flush sends pending SQL but transaction commit makes it durable."],
 summary=["JPA maps objects and tables.", "Hibernate tracks managed entities and executes SQL."],
 interview=["What is the difference between JPA and Hibernate?"])

page(47, "Module 5 — JPA, Spring + Spring Boot", "JPA RELATIONSHIPS, FETCHING + N+1",
"JPA relationships map links between entities. Fetching decides when related data is loaded.",
"Relationship symbols on top; N+1 query timeline and fixes below.", [
 panel("RELATIONSHIPS", ["@OneToOne: one row relates to one row.", "@OneToMany: one parent relates to many children.", "@ManyToOne: many children point to one parent.", "@ManyToMany: many on both sides, usually through a join table.", "The owning side controls the foreign key/join mapping."] , "Customer 1 → many Orders; Order 1 → many LineItems."),
 panel("LAZY vs EAGER", ["Lazy means related data loads when it is accessed.", "Eager means it is requested with the entity, but exact SQL still matters.", "Neither choice is correct for every use case.", "Choose a fetch plan for the data one screen/API needs."]),
 panel("N+1 PROBLEM", ["One query loads N parent rows.", "Reading each lazy child list causes up to N more queries.", "Fix choices include fetch join, EntityGraph, DTO projection, or batch fetching.", "Loading everything eagerly can create another performance problem."] , "One parent query followed by N red child queries."),
 panel("CASCADE", ["Cascade passes operations such as persist/remove from parent to related entities.", "orphanRemoval deletes a child removed from an owned collection.", "Use both only when object lifecycle ownership is clear."])
 ], code=["@OneToMany(mappedBy = \"order\", cascade = PERSIST)\nprivate List<LineItem> items = new ArrayList<>();"],
 flowchart="API data need → choose projection/fetch plan → run query → count queries and rows.",
 important=["A collection fetch join and pagination can produce wrong/expensive results; often page parent IDs first.", "Keep both sides of a bidirectional relationship consistent."],
 summary=["Mappings describe relationships and ownership.", "N+1 means one starting query plus many repeated queries."],
 interview=["What is the N+1 problem and one way to fix it?"])

page(48, "Module 5 — JPA, Spring + Spring Boot", "SPRING, IoC + DEPENDENCY INJECTION",
"Spring is a Java framework that creates and connects application objects. IoC means Spring controls this object setup.",
"Without/with Spring comparison and constructor injection example.", [
 panel("WITHOUT SPRING", ["A class directly creates its dependencies using new.", "Object setup becomes spread across the application.", "Replacing a real dependency with a test version becomes harder."] , "OrderService → new OrderRepository/new EmailClient."),
 panel("WITH SPRING IoC", ["We describe which classes are Spring beans.", "ApplicationContext creates the bean objects.", "It finds their dependencies and connects them.", "It also manages lifecycle and may add proxy behavior."] , "Container creates Repository and injects it into Service."),
 panel("CONSTRUCTOR INJECTION", ["Required dependencies appear in the constructor.", "They can be final and are available when the object is created.", "A plain unit test can call the constructor directly.", "Too many constructor parameters may mean a class has too many jobs."])
 ], code=["@Service\nclass OrderService {\n  private final OrderRepository orders;\n\n  OrderService(OrderRepository orders) {\n    this.orders = orders;\n  }\n}"],
 flowchart="Spring reads configuration/components → creates beans → finds constructor needs → injects dependencies.",
 important=["An object created manually with new is not automatically managed by Spring.", "Constructor injection is usually clearer than hidden field injection."],
 summary=["IoC gives object setup to the container.", "Dependency injection supplies the objects a class needs."],
 interview=["Why is constructor injection useful?"])

page(49, "Module 5 — JPA, Spring + Spring Boot", "SPRING BEANS + COMMON ANNOTATIONS",
"A Spring bean is an object created and managed by the Spring container.",
"Annotation family tree and bean creation flow.", [
 panel("STEREOTYPE ANNOTATIONS", ["@Component: general Spring-managed component.", "@Service: application/business service.", "@Repository: data-access component; also supports exception translation.", "@Controller: MVC controller that may return views.", "@RestController: controller whose methods normally return response bodies such as JSON."], "@Component branches to specialized stereotypes."),
 panel("EXPLICIT BEANS", ["@Configuration marks a class containing bean configuration.", "@Bean marks a method whose returned object becomes a bean.", "This is useful for third-party classes we cannot annotate.", "A single constructor normally does not need @Autowired."]),
 panel("MULTIPLE BEANS", ["When two beans match one type, Spring needs help choosing.", "@Primary marks the normal choice.", "@Qualifier names the intended role.", "Injecting a Map<String, Strategy> can support many strategies."])
 ], code=["@Configuration\nclass AppConfig {\n  @Bean\n  Clock clock() {\n    return Clock.systemUTC();\n  }\n}"],
 flowchart="Component scan or @Bean → bean definition → object created → dependencies injected → ready.",
 important=["The annotation name communicates purpose but does not automatically make business design correct.", "Circular constructor dependencies usually show responsibilities that should be redesigned."],
 summary=["A bean is a container-managed object.", "Scanning and @Bean methods register beans."],
 interview=["When would you use @Bean instead of @Component?"])

page(50, "Module 5 — JPA, Spring + Spring Boot", "BEAN LIFECYCLE, SCOPES + PROXIES",
"Bean lifecycle describes how Spring creates, prepares, uses, and destroys a bean. Scope describes how many bean objects exist.",
"Lifecycle conveyor, scope table, and proxy wrapper picture.", [
 panel("LIFECYCLE", ["Spring reads a bean definition.", "It creates the object and injects dependencies.", "Bean post-processors can inspect or wrap it.", "@PostConstruct runs after setup.", "The bean is used.", "@PreDestroy runs during a normal container shutdown."] , "Definition → create → inject → initialize → use → destroy."),
 panel("SCOPES", ["singleton: one bean per ApplicationContext; the normal scope.", "prototype: a new bean when requested from the container.", "request: one bean per web request.", "session: one bean per web session.", "Singleton beans serve many threads, so avoid request-specific mutable fields."] , "Scope | Lifetime | Simple use table."),
 panel("PROXY", ["Spring can return a wrapper called a proxy around a bean.", "The proxy adds transactions, security, caching, or async behavior.", "A call from a method to another method on this may skip the proxy.", "That is why self-invoked @Transactional may not work as expected."] , "Caller → Proxy → target bean; internal arrow bypasses proxy.")
 ], flowchart="Caller → proxy extra behavior → real method → proxy finishes behavior → result.",
 important=["Singleton means one per container, not one in the whole cluster.", "Do not start slow work or unmanaged threads inside a bean constructor."],
 summary=["Spring controls bean creation and cleanup.", "Proxies add framework behavior around method calls."],
 interview=["Why can self-invocation bypass @Transactional?"])

page(51, "Module 5 — JPA, Spring + Spring Boot", "SPRING BOOT + AUTO-CONFIGURATION",
"Spring Boot makes Spring applications faster to start by providing useful defaults, dependency starters, and automatic configuration.",
"@SpringBootApplication branches and conditional decision flow.", [
 panel("WHAT BOOT PROVIDES", ["Starter dependencies collect common libraries, such as spring-boot-starter-web.", "Auto-configuration suggests beans based on libraries, properties, and existing beans.", "An embedded server lets a web app run as one executable JAR.", "Actuator adds optional production health and metric endpoints."] , "Spring Boot box: starters, auto-config, server, actuator."),
 panel("@SpringBootApplication", ["It includes configuration support.", "It starts component scanning from its package downward.", "It enables Boot's auto-configuration selection.", "Place the main class near the top package so features are scanned."]),
 panel("CONDITIONAL SETUP", ["Is a required class present?", "Is a property enabled?", "Did the application already define its own bean?", "When a user bean exists, auto-configuration often backs off.", "The condition report helps explain why a configuration matched."] , "Decision diamonds ending Create default bean / Back off.")
 ], code=["@SpringBootApplication\npublic class ShopApplication {\n  public static void main(String[] args) {\n    SpringApplication.run(ShopApplication.class, args);\n  }\n}"],
 flowchart="Classpath + properties + user beans → conditions → auto-configured beans → running application.",
 important=["Auto-configuration is conditional setup, not magic.", "Do not exclude an auto-configuration before understanding what condition matched."],
 summary=["Boot supplies sensible conditional defaults.", "The application can replace defaults when needed."],
 interview=["What three ideas are combined by @SpringBootApplication?"])

page(52, "Module 5 — JPA, Spring + Spring Boot", "CONFIGURATION + PROFILES",
"Configuration means values that may change between environments without changing the Java code.",
"One JAR to three environments and typed properties card.", [
 panel("EXTERNAL CONFIG", ["application.properties or application.yml provides defaults.", "Environment variables and command-line values can override configuration.", "Use the same built artifact in development, test, and production.", "Inject each environment's URLs, limits, and feature values during deployment."] , "One JAR flows to dev/stage/prod; each supplies config."),
 panel("PROFILES", ["A profile activates environment- or purpose-specific configuration/beans.", "Example: application-dev.yml.", "Profiles may be combined, so test the real combination.", "Do not use profiles for every small business feature choice."]),
 panel("TYPED PROPERTIES", ["@ConfigurationProperties maps a group of values to a typed class/record.", "Validation can stop startup when a required value is missing.", "This is clearer than many scattered @Value fields.", "Secrets belong in a secret manager/platform secret, never Git."])
 ], code=["@ConfigurationProperties(prefix = \"payment\")\npublic record PaymentProperties(\n    String baseUrl,\n    Duration timeout) {}", "payment:\n  base-url: https://api.example.com\n  timeout: 2s"],
 flowchart="Config sources → precedence/override → typed binding → validation → bean uses safe values.",
 important=["Never log all environment values because they may contain secrets.", "Configuration changes environment behavior; the artifact stays unchanged."],
 summary=["External configuration keeps code and environment values separate.", "Typed properties make configuration clear and testable."],
 interview=["Why should production secrets not be stored in application.yml in Git?"])

page(53, "Module 5 — JPA, Spring + Spring Boot", "SPRING MVC REQUEST LIFECYCLE",
"Spring MVC receives an HTTP request, finds the correct controller method, converts data, and creates an HTTP response.",
"Full-page numbered request sequence with component notes.", [
 panel("BEFORE CONTROLLER", ["1. The embedded server accepts the request.", "2. Servlet Filters run for concerns such as security and request IDs.", "3. DispatcherServlet acts as Spring MVC's front controller.", "4. HandlerMapping finds a matching controller method.", "5. Argument resolvers and message converters create method parameters."] , "Client → Server/Filters → DispatcherServlet → Controller."),
 panel("CONTROLLER + SERVICE", ["6. JSON may be converted into a request DTO.", "7. Validation runs when requested.", "8. The controller calls an application service.", "9. The service applies rules and uses repositories.", "10. The controller returns a result or ResponseEntity."]),
 panel("RESPONSE", ["11. A message converter changes the response object into JSON.", "12. Exception handlers translate known failures into safe error responses.", "13. The response passes back through filters to the client."])
 ], code=["@RestController\n@RequestMapping(\"/products\")\nclass ProductController {\n  @GetMapping(\"/{id}\")\n  ProductResponse get(@PathVariable long id) {\n    return service.get(id);\n  }\n}"],
 flowchart="Client → filters → DispatcherServlet → mapping/binding → controller → service → repository → JSON response.",
 important=["Controllers are singleton beans, so do not store one user's request data in controller fields.", "Spring MVC normally uses the servlet blocking model; WebFlux is a separate reactive stack."],
 summary=["DispatcherServlet coordinates the MVC request.", "Controllers adapt HTTP to application calls."],
 interview=["What happens between incoming JSON and a controller parameter?"])

page(54, "Module 5 — JPA, Spring + Spring Boot", "REST CONTROLLERS + API DESIGN",
"A REST API exposes resources through HTTP methods, URLs, status codes, headers, and representations such as JSON.",
"Resource URL examples, HTTP method table, status-code guide.", [
 panel("RESOURCE URLS", ["Use nouns: /orders and /orders/42.", "Avoid action names such as /getOrder when GET already describes the action.", "A nested path such as /orders/42/items can show clear ownership.", "Query parameters filter, sort, search, or paginate a collection."] , "Cross out /getOrders; green /orders/{id}."),
 panel("METHOD MEANING", ["GET reads without changing the intended resource state.", "POST creates or starts an operation.", "PUT replaces a resource at a known URL.", "PATCH changes part of a resource.", "DELETE removes a resource."]),
 panel("GOOD RESPONSES", ["200 for normal success with a body.", "201 + Location when a resource is created.", "204 for success without a body.", "400 for invalid request, 404 for missing resource, 409 for state conflict.", "500 for an unexpected server problem—not for client mistakes."]),
 panel("IDEMPOTENCY", ["Repeating an idempotent request has the same intended server effect.", "GET, PUT, and DELETE are defined as idempotent in meaning.", "A critical POST can use an idempotency key stored with its result so a retry does not create the action twice."])
 ], code=["@PostMapping\nResponseEntity<OrderResponse> create(\n    @Valid @RequestBody CreateOrderRequest request) {\n  OrderResponse result = service.create(request);\n  return ResponseEntity.created(uri(result.id())).body(result);\n}"],
 flowchart="HTTP method + resource URL → validate → perform use case → choose status + headers + JSON.",
 important=["REST design uses HTTP meaning, not only JSON fields.", "A client timeout does not prove the server operation failed; retry safety matters."],
 summary=["URLs name resources; methods name actions.", "Status codes clearly tell the result."],
 interview=["What should POST /orders return after creating an order?"])

page(55, "Module 5 — JPA, Spring + Spring Boot", "DTOs + VALIDATION",
"A DTO is an object used to carry input or output across a boundary. Validation checks whether received data follows required rules.",
"Entity/DTO boundary diagram and three validation layers.", [
 panel("WHY DTOs?", ["A request DTO contains only fields the client is allowed to send.", "A response DTO contains only fields the API should show.", "JPA entities contain persistence details and may load extra data during JSON conversion.", "Separate DTOs let the database model and API change at different speeds."] , "JSON ↔ DTO | safe boundary | service/entity ↔ database."),
 panel("JAKARTA VALIDATION", ["@NotNull: value must exist.", "@NotBlank: text must contain non-space characters.", "@Size: text/collection length range.", "@Positive, @Min, @Max: number rules.", "@Email and @Pattern: format checks.", "@Valid checks nested request objects."] , "Annotation | Easy meaning | Example table."),
 panel("THREE LAYERS", ["DTO validation checks shape and simple input rules.", "Service/domain checks current business rules, such as enough stock.", "Database constraints protect final stored truth and concurrent writers.", "The same rule should have a clear owner, even when defenses exist at several layers."])
 ], code=["public record CreateUserRequest(\n    @NotBlank String name,\n    @Email @NotBlank String email,\n    @Min(18) int age) {}"],
 flowchart="JSON → bind DTO → validate fields → service business rules → database constraints.",
 important=["Never trust a client-supplied owner ID or role when it should come from authenticated identity.", "Do not return JPA entities directly from controllers."],
 summary=["DTOs protect API boundaries.", "Validation happens from input shape to business rule to database truth."],
 interview=["Why should an API use DTOs instead of returning entities?"])


page(56, "Module 6 — Complete Spring Backend", "GLOBAL ERROR HANDLING",
"Global error handling changes application exceptions into one clear, safe, and consistent API error format.",
"Exception-to-response ladder and ProblemDetail card.", [
 panel("WHY CENTRAL HANDLING?", ["Without it, every controller repeats try/catch code.", "@RestControllerAdvice holds handlers used by many controllers.", "@ExceptionHandler chooses a response for a known exception type.", "Unknown failures return a general 500 message while detailed information stays in protected logs."] , "Controller exceptions funnel into one advice component."),
 panel("ERROR RESPONSE", ["status: HTTP status number.", "code/type: stable machine-readable error name.", "title/detail: safe human explanation.", "fieldErrors: invalid input fields when useful.", "traceId: value that helps support find the matching logs.", "instance/path: the failed request location."] , "ProblemDetail-shaped JSON card."),
 panel("COMMON MAPPING", ["Bad JSON/DTO validation → 400.", "Missing resource → 404.", "Wrong current state or duplicate unique value → 409.", "Unauthenticated → 401; not allowed → 403.", "Unexpected bug → safe 500."])
 ], code=["@RestControllerAdvice\nclass ApiErrors {\n  @ExceptionHandler(OrderNotFound.class)\n  ProblemDetail notFound(OrderNotFound ex) {\n    var error = ProblemDetail.forStatus(404);\n    error.setTitle(\"Order not found\");\n    error.setProperty(\"code\", \"ORDER_NOT_FOUND\");\n    return error;\n  }\n}"],
 flowchart="Exception → matching handler → status + safe body + trace ID → client; detailed cause → protected log.",
 important=["Never return stack traces, SQL statements, passwords, or internal class names to a client.", "Keep error codes stable even when the human message changes."],
 summary=["One handler keeps API errors consistent.", "Public errors are safe; internal logs keep useful details."],
 interview=["What information should and should not appear in an API error?"])

page(57, "Module 6 — Complete Spring Backend", "SPRING DATA JPA REPOSITORIES",
"Spring Data JPA creates repository implementations from interfaces, reducing repeated data-access code.",
"Repository interface to proxy to EntityManager flow and query choice ladder.", [
 panel("REPOSITORY BASICS", ["JpaRepository<Entity,IdType> provides save, findById, delete, paging, and more.", "Spring creates a proxy object that implements the interface.", "findById returns Optional because the row may not exist.", "Collection queries normally return an empty collection, not null."] , "Interface → Spring Data proxy → EntityManager → database."),
 panel("QUERY METHODS", ["A simple method name can become a query: findByEmail.", "Combine fields carefully: findByStatusAndCreatedAtBefore.", "@Query writes JPQL using entity and field names.", "Native SQL uses table/column names and database features.", "Complex reports may be clearer in a custom read repository."] , "Simple derived → @Query → Specification/custom ladder."),
 panel("PAGING + PROJECTION", ["Pageable asks for page number, size, and sorting.", "Page includes content and a count; Slice only knows whether a next part exists.", "A projection returns only fields needed by the screen/API.", "Always use deterministic sorting, including a unique tie-breaker."])
 ], code=["interface OrderRepository extends JpaRepository<Order, UUID> {\n  List<Order> findByStatus(OrderStatus status);\n\n  @Query(\"select o from Order o where o.customer.id = :id\")\n  Page<Order> findForCustomer(UUID id, Pageable page);\n}"],
 flowchart="Call repository method → derive/read query → proxy executes through JPA → result/projection returns.",
 important=["Generated repository methods still run real SQL; inspect SQL and query plans.", "Changing a managed entity in a transaction is saved by dirty checking without calling save again."],
 summary=["Spring Data creates common repository code.", "Method names and @Query define reads."],
 interview=["What implementation class do you write for a normal Spring Data repository interface?"])

page(58, "Module 6 — Complete Spring Backend", "@Transactional + LOCKING",
"A transaction makes related database changes succeed or fail as one unit. @Transactional asks Spring to manage that boundary.",
"Proxy transaction flow, rollback rules, and two-user version drawing.", [
 panel("HOW @Transactional WORKS", ["A Spring proxy starts or joins a transaction before the method.", "Repository operations use that transaction.", "Normal completion commits it.", "A matching failure rolls it back.", "The normal default rolls back for RuntimeException/Error, not every checked exception."] , "Caller → transaction proxy → begin → method → commit/rollback."),
 panel("GOOD BOUNDARY", ["Put the transaction around one application use case.", "Keep it short.", "Avoid slow network calls while holding database locks/connections when the design allows.", "Private/self-invoked methods may skip proxy behavior."]),
 panel("CONCURRENT UPDATE", ["Optimistic locking uses an @Version field.", "Two users read version 3; the first update creates version 4.", "The second update using version 3 fails instead of silently overwriting.", "Pessimistic locking asks the database to block conflicting access and must be used carefully."] , "Two users read v3; first wins v4; second gets conflict."),
 panel("PROPAGATION IDEA", ["REQUIRED joins an existing transaction or starts one; it is the normal default.", "REQUIRES_NEW pauses the outer transaction and starts an independent one.", "Independent commits can change the all-or-nothing behavior, so choose deliberately."])
 ], code=["@Transactional\npublic void pay(UUID orderId) {\n  Order order = orders.findById(orderId)\n      .orElseThrow(OrderNotFound::new);\n  order.markPaid();\n}"],
 flowchart="Proxy call → begin/join transaction → work → success commit | exception rule rollback.",
 important=["Catching an exception and returning normally may allow commit.", "A retry after an optimistic conflict must read the newest state and safely repeat the use case."],
 summary=["@Transactional manages a local database unit of work.", "Version checks prevent silent lost updates."],
 interview=["Why may @Transactional not work on a method called through this?"])

page(59, "Module 6 — Complete Spring Backend", "SPRING SECURITY BASICS",
"Security first proves who the caller is (authentication), then checks what that caller may do (authorization).",
"Two-gate drawing, security filter chain, and 401/403 comparison.", [
 panel("TWO QUESTIONS", ["Authentication: Who are you?", "Authorization: Are you allowed to do this action on this resource?", "A logged-in user may still be forbidden from another user's order.", "Use least privilege: give only needed permissions."] , "Identity gate → permission/ownership gate → controller."),
 panel("FILTER CHAIN", ["Spring Security runs filters before the controller.", "A filter reads a session, bearer token, or other credentials.", "AuthenticationManager/Provider checks the evidence.", "A successful Authentication is stored in SecurityContext.", "Authorization rules decide whether the request may continue."] , "Request → security filters → authentication → authorization → MVC."),
 panel("401 vs 403", ["401: no valid authentication; the caller must authenticate.", "403: identity is known but does not have permission.", "404 may sometimes hide whether a protected resource exists.", "Test allowed and denied cases."]),
 panel("PASSWORDS", ["Store an adaptive one-way hash such as bcrypt or Argon2, never plain passwords.", "Rate-limit login attempts.", "Never log passwords or access tokens.", "Use HTTPS so credentials are protected in transit."])
 ], code=["@Bean\nSecurityFilterChain security(HttpSecurity http) throws Exception {\n  return http\n      .authorizeHttpRequests(auth -> auth\n          .requestMatchers(\"/public/**\").permitAll()\n          .anyRequest().authenticated())\n      .build();\n}"],
 flowchart="Credentials → verify identity → create Authentication → check role/ownership → allow or 401/403.",
 important=["Do not trust a role or user ID sent in an ordinary client header.", "Authorization must also check resource ownership when needed."],
 summary=["Authentication proves identity.", "Authorization checks permission."],
 interview=["What is the difference between 401 and 403?"])

page(60, "Module 6 — Complete Spring Backend", "JWT, CORS + CSRF",
"JWT is a signed token format. CORS controls browser cross-origin reading. CSRF protects against unwanted requests using automatically sent credentials.",
"JWT anatomy on top; CORS/CSRF comparison table below.", [
 panel("JWT", ["A JWT has header.payload.signature.", "Header and payload are encoded, not secret; a holder can read them.", "The server verifies allowed algorithm, signature, issuer, audience, and expiry.", "Short-lived access tokens limit damage.", "Do not put passwords or unnecessary private data in claims."] , "Three colored token sections and validation checklist."),
 panel("CORS", ["Browsers normally restrict one website from reading another origin's response.", "The server can allow trusted origins, methods, and headers.", "CORS is not login, authorization, or a server-to-server firewall.", "Credentialed CORS cannot use a wildcard allowed origin."]),
 panel("CSRF", ["Browsers automatically send some credentials, especially cookies.", "A malicious page can cause an unwanted state-changing request using them.", "CSRF tokens and SameSite cookie rules are common defenses.", "A bearer-only stateless API has a different CSRF model, but token storage must still be protected from XSS."])
 ], code=["Authorization: Bearer <access-token>\n\nVerify: algorithm → signature → issuer → audience → expiry → authorities"],
 flowchart="Client gets token → sends bearer token → server verifies cryptography/claims → authorizes action.",
 important=["A valid signature alone is not enough; issuer, audience, and time claims matter.", "JWT signing does not encrypt its payload."],
 summary=["JWT carries signed claims, not secret text.", "CORS and CSRF solve different browser security problems."],
 interview=["Can anyone read a normal JWT payload, and what prevents changing it?"])

page(61, "Module 6 — Complete Spring Backend", "TESTING: JUNIT, MOCKITO + SPRING",
"A test runs code with a known setup and checks that the result matches expected behavior.",
"Testing pyramid, AAA example, and test-type table.", [
 panel("TESTING LEVELS", ["Unit test: one small class/rule without Spring or real infrastructure.", "Slice test: one Spring area such as MVC or JPA.", "Integration test: several real parts working together, often with a real database container.", "End-to-end test: a complete important user journey.", "Many fast small tests plus fewer broad tests give useful confidence."] , "Pyramid unit → slice/integration → end-to-end."),
 panel("ARRANGE, ACT, ASSERT", ["Arrange creates input and starting state.", "Act performs one behavior.", "Assert checks the visible result.", "A good test name describes the rule.", "Tests should be deterministic and not depend on order or sleep timing."]),
 panel("TOOLS", ["JUnit 5 supplies @Test, setup, parameterized tests, and assertions.", "Mockito creates mocks for collaborator interfaces at a unit boundary.", "@WebMvcTest checks routing, JSON, validation, security, and controller behavior.", "@DataJpaTest checks repositories/JPA.", "@SpringBootTest loads the complete application context.", "Testcontainers can start real PostgreSQL, Kafka, or Redis for tests."])
 ], code=["@Test\nvoid rejectsNegativeQuantity() {\n  var order = new Order();\n\n  var error = assertThrows(IllegalArgumentException.class,\n      () -> order.add(product, -1));\n\n  assertEquals(\"Quantity must be positive\", error.getMessage());\n}"],
 flowchart="Rule/risk → choose smallest trustworthy test boundary → arrange → act → assert.",
 important=["Do not use @SpringBootTest for a simple pure Java unit test.", "Mocks are useful at boundaries; mocking every object makes tests fragile."],
 summary=["Small tests give fast feedback.", "Broader tests prove framework and infrastructure wiring."],
 interview=["When would you use @WebMvcTest instead of @SpringBootTest?"])

page(62, "Module 6 — Complete Spring Backend", "LOGGING, METRICS + TRACING",
"Observability means understanding a running system through logs, metrics, and traces.",
"Three-column signal comparison and one request correlation flow.", [
 panel("THREE SIGNALS", ["Logs record individual events with useful context.", "Metrics are numbers measured over time, such as request count and latency.", "Traces show one request's path through services and database calls.", "Use metrics to detect, traces to locate, and logs to explain."] , "Columns Signal | Answers | Example."),
 panel("GOOD LOGGING", ["Use structured fields such as traceId, orderId, operation, and outcome.", "ERROR is a real failure, WARN is unexpected/degraded, INFO is a useful milestone, DEBUG is detailed diagnosis.", "Log a failure at the boundary that handles it instead of at every layer.", "Never log passwords, tokens, or full sensitive request bodies."]),
 panel("METRICS + HEALTH", ["RED metrics: request Rate, Error rate, and Duration.", "Use percentiles such as p95/p99; an average can hide slow requests.", "Do not use userId/orderId as metric labels because they create too many time series.", "Actuator can expose health and metrics.", "Readiness means able to receive traffic; liveness means restart may help."]),
 panel("TRACING", ["A trace ID connects work for one request.", "Spans measure controller, database, HTTP, or message steps.", "Propagate trace information across service and message boundaries."])
 ], code=["log.info(\"Order created orderId={} total={}\",\n    order.id(), order.total());"],
 flowchart="Request with trace ID → controller span → DB/client spans → metrics + structured logs → dashboard/debug.",
 important=["Health endpoints must be protected and reveal little detail publicly.", "High-cardinality metric labels can cause high cost and poor performance."],
 summary=["Metrics tell when, traces tell where, logs explain details.", "All signals should share request correlation."],
 interview=["Why is orderId good in a log but bad as a metric label?"])

page(63, "Module 7 — Production + Distributed Systems", "CACHING + REDIS",
"A cache stores a temporary copy of data so later reads can return faster. Redis is a common remote in-memory data store.",
"Cache-aside numbered flow and problem/solution cards.", [
 panel("CACHE-ASIDE", ["1. Application asks the cache for a key.", "2. On a hit, return the cached value.", "3. On a miss, read the database.", "4. Store the result in cache with an expiry time (TTL).", "5. Return the result.", "After a database update, invalidate or safely update the cached copy."] , "App → Redis hit; miss → DB → Redis → app."),
 panel("KEY + TTL", ["A key includes every input that changes the result, such as tenant and product ID.", "TTL limits how long stale data and unused keys stay.", "Add small random TTL variation so many keys do not expire together.", "Cache null/missing results briefly only when it safely reduces repeated load."]),
 panel("COMMON PROBLEMS", ["Stale data: cache and database differ.", "Stampede: many requests miss one hot key and all hit the database.", "Penetration: repeated missing/random keys reach the database.", "Redis outage: fallback may overload the database, so use timeouts and capacity limits."]),
 panel("SPRING CACHE", ["@Cacheable reads/stores results; @CacheEvict removes; @CachePut updates.", "These annotations use proxies, so self-invocation can bypass them.", "A cache action and database transaction are not automatically one atomic operation."])
 ], code=["@Cacheable(cacheNames = \"products\", key = \"#id\")\npublic ProductResponse getProduct(long id) {\n  return repository.findById(id).map(mapper::toResponse)\n      .orElseThrow(ProductNotFound::new);\n}"],
 flowchart="Request → cache hit return | miss → single loader → database → cache with TTL → return.",
 important=["Cache is normally a temporary copy; the database remains the source of truth.", "A cache makes reads faster but adds freshness and failure decisions."],
 summary=["Cache trades freshness/complexity for speed and lower database load.", "Keys, TTL, invalidation, and fallback belong to one design."],
 interview=["What is a cache stampede and one way to reduce it?"])

page(64, "Module 7 — Production + Distributed Systems", "MESSAGING, KAFKA + OUTBOX",
"Messaging lets one part of a system send work or events without waiting for the receiver to finish immediately.",
"Broker flow, Kafka/RabbitMQ table, and outbox reliability diagram.", [
 panel("BASIC FLOW", ["Producer creates a message.", "Broker stores/routes it.", "Consumer receives and processes it.", "Acknowledgement/offset tells the broker how far processing succeeded.", "Messages may be delivered more than once, so consumer work should be idempotent."] , "Producer → broker → consumer → database; retry/DLQ side path."),
 panel("KAFKA vs RABBITMQ", ["Kafka: a retained ordered log split into partitions; consumers can replay using offsets.", "RabbitMQ: exchanges route messages to queues; consumers acknowledge queue deliveries.", "Kafka order exists inside one partition.", "A Kafka consumer group shares partitions among its members.", "Choose based on replay, ordering, routing, throughput, and team operations—not trend."] , "Comparison table Model | Replay | Ordering | Common use."),
 panel("SAFE MESSAGE", ["Include eventId, type, version, time, correlation ID, and payload.", "An event describes a fact that happened: OrderCreated.", "A command asks an owner to do something: ReserveStock.", "Use compatible schema changes and do not publish secrets/entire ORM entities."]),
 panel("OUTBOX PATTERN", ["Problem: database save succeeds but broker publish fails, or the reverse.", "In one database transaction, save business data and an outbox row.", "A relay later publishes the outbox event and retries safely.", "Duplicates are still possible, so consumers store processed event IDs or use an idempotent update."] , "Transaction bracket around Order + Outbox → relay → broker.")
 ], code=["BEGIN;\nINSERT INTO orders(id, status) VALUES (?, 'CREATED');\nINSERT INTO outbox(event_id, type, payload) VALUES (?, 'OrderCreated', ?);\nCOMMIT;"],
 flowchart="Local transaction [business row + outbox] → relay → broker → idempotent consumer → acknowledge.",
 important=["A dead-letter queue holds failed messages but still needs alerts, investigation, and safe replay.", "Exactly-once claims are limited to particular boundaries; prove the final business effect."],
 summary=["Messaging separates work in time.", "Outbox avoids an unsafe database-and-broker dual write."],
 interview=["What problem does the transactional outbox solve?"])

page(65, "Module 7 — Production + Distributed Systems", "MICROSERVICES TO DEPLOYMENT — COMPLETE MAP",
"A microservice is an independently deployable service built around a business capability. Production delivery packages, tests, deploys, and operates it safely.",
"Full-page simple architecture with numbered order flow and compact production checklist.", [
 panel("SERVICE BOUNDARIES", ["Start with clear business modules; distribution adds network failures and operational work.", "A service owns its business rules and data writes.", "Synchronous HTTP gives an immediate result but connects availability/latency.", "Asynchronous events allow later reactions but require duplicate and eventual-consistency handling.", "Keep a modular monolith when independent deployment does not justify microservice cost."] , "Gateway → Order, Payment, Inventory; each owns data."),
 panel("RESILIENCE", ["Timeout stops waiting after a budget.", "Retry repeats only transient, safe/idempotent work with backoff and jitter.", "Circuit breaker temporarily fails fast while a dependency recovers.", "Bulkhead limits capacity used by one dependency.", "Saga coordinates service-local transactions and compensation; compensation is a new business action, not database rollback."] , "CLOSED → OPEN → HALF_OPEN breaker plus short Saga arrow."),
 panel("DOCKER + CI/CD + KUBERNETES", ["Docker image is an immutable package; a container is a running instance.", "Run as non-root, inject secrets/config at runtime, set memory limits with JVM headroom, and handle SIGTERM gracefully.", "CI compiles, tests, scans, and publishes one image.", "CD promotes the same image digest through environments.", "Kubernetes Deployment manages Pods; Service gives stable networking.", "Readiness removes an unready Pod from traffic; liveness restarts a stuck one."] , "Commit → CI → image registry → Kubernetes Pods."),
 panel("END-TO-END ORDER", ["1 Client POST /orders with authentication and idempotency key.", "2 Controller validates DTO; service applies rules.", "3 Transaction saves Order + outbox event.", "4 API returns 201 Created.", "5 Relay publishes OrderCreated.", "6 Inventory/notification consumers handle it idempotently.", "7 Logs, metrics, and traces follow every step.", "8 Docker/Kubernetes run several healthy copies."] , "Numbered full architecture flow."),
 panel("FINAL REVISION RULE", ["For every topic ask: What is it? Why is it used? Where is it in the request? What can fail? How is it tested and observed?", "When debugging: define symptom → check metrics/change → follow trace → read correlated logs → test one theory → fix and add a regression test."])
 ], flowchart="Client → Gateway/Security → Controller → Service → PostgreSQL [Order+Outbox] → response; Relay → Kafka → consumers; telemetry receives signals from all.",
 important=["Do not create microservices only because they are popular.", "Every network arrow needs authentication, timeout, failure behavior, and observability.", "Deploy the same tested artifact; change environment configuration outside it."],
 summary=["Simple boundaries first; distribute only for a reason.", "Reliable backends combine correct code, safe data, security, tests, delivery, and observation.", "Trace one request and one event from start to finish."],
 interview=["Using the order flow, explain what happens if the client retries after the database committed but before it received the response."])


# PAGE_CALLS


def write_outputs() -> None:
    payload = {
        "edition": "Beginner-friendly Java 17/21 + Spring Boot 3.x",
        "audience": "Anyone learning Java backend development, including complete beginners",
        "page_count": len(pages),
        "pages": pages,
    }
    (ROOT / "content" / "pages.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    lines = [
        "# Java + Spring Boot Backend — 65-Page Easy Handwritten Notes Script",
        "",
        "> Audience: anyone learning Java backend development. No work experience is assumed.",
        "> Rule: define first, explain in normal words, show a small example, then summarize.",
        "",
    ]
    current_module = None
    for item in pages:
        if item["module"] != current_module:
            current_module = item["module"]
            lines.extend([f"# {current_module}", ""])
        lines.extend([
            f"## Page {item['page']:02d} — {item['title']}", "",
            f"**Easy definition:** {item['objective']}", "",
            f"**Layout:** {item['layout']}", "",
        ])
        for block in item["panels"]:
            lines.extend([f"### {block['heading']}", ""])
            lines.extend(f"- {copy}" for copy in block["copy"])
            if block.get("visual"):
                lines.append(f"- **Visual:** {block['visual']}")
            lines.append("")
        if item["code"]:
            lines.extend(["### Small example", ""])
            for snippet in item["code"]:
                lines.extend(["```java", snippet, "```", ""])
        if item["flowchart"]:
            lines.extend(["### Flowchart", "", item["flowchart"], ""])
        lines.extend(["### Important points", ""])
        lines.extend(f"- {copy}" for copy in item["important"])
        lines.extend(["", "### Check your understanding", ""])
        lines.extend(f"- {copy}" for copy in item["interview_checks"])
        lines.extend(["", "### Summary cloud", ""])
        lines.extend(f"- ✓ {copy}" for copy in item["summary"])
        lines.extend(["", "---", ""])
    (ROOT / "content" / "master-script.md").write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    write_outputs()
