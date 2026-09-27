# Reference Style and Teaching Analysis

## What will be preserved

- **A4 portrait, one teaching topic per sheet:** every page can be understood by itself and still connects to the next page.
- **Clear visual hierarchy:** large purple uppercase title, decorative underline, teal/purple subheads, navy body text.
- **Simple definitions:** introduce the topic in normal words before showing technical details.
- **Topic-driven layouts:** comparison tables for alternatives; numbered rows for concepts; small code beside its meaning; arrows that show what happens next.
- **Learning aids:** tiny examples, “Important Points,” a check-your-understanding question, and a cloud-shaped summary.
- **Human character:** warm paper, hand-drawn rules, slightly variable lettering and arrows, but clean enough to read easily.

## Content rule for the 65-page edition

No work experience or framework knowledge is assumed. Every page follows this order:

1. What is it? — one easy definition.
2. Why is it used? — a familiar example.
3. How does it work? — a table, code box, or flowchart.
4. What should I remember? — two or three important points.
5. Can I explain it? — one simple question and a summary cloud.

New words are explained before later pages use them. Sentences stay short and direct. Advanced topics such as transactions, security, Kafka, caching, and Kubernetes remain included, but each starts from its basic purpose.

## Accuracy improvements over the reference

The reference's teaching style is the target, but outdated facts are not copied. These notes use **Java 17/21 and Spring Boot 3.x**:

- Interfaces may contain abstract methods, `default` and `static` methods (Java 8+), and `private` helper methods (Java 9+).
- Interface fields are implicitly `public static final`.
- “100% abstraction” is an old shortcut, not a dependable modern difference.
- Static interface methods have had bodies since Java 8, not Java 16.

Every generated page must be checked for accurate wording, readable code, correct arrows, A4 portrait shape, and consistent handwriting before approval.

## Standard page grammar

1. **Header (top 8%):** title and small module label.
2. **Easy definition (next 7%):** one or two plain-language sentences.
3. **Teaching area (next 65%):** 2–4 bordered panels, a table, small example, or flowchart.
4. **Recall area (next 15%):** important points + understanding check + summary cloud.
5. **Footer (last 5%):** page number and small “Java Backend • Easy Notes” label.
