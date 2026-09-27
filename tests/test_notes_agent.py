import unittest

from notes_agent.prompts import compile_prompt
from notes_agent.repository import load_pages, load_style
from notes_agent.validation import validate_pages
from notes_agent.workflow import _assert_batch_unlocked, batch_count, batch_pages


class ContentTests(unittest.TestCase):
    def test_exactly_sixty_five_continuous_pages(self):
        pages = load_pages()
        self.assertEqual(list(range(1, 66)), [page.page for page in pages])
        self.assertEqual([], validate_pages(pages))

    def test_seven_batches_and_final_five_pages(self):
        self.assertEqual(7, batch_count())
        self.assertEqual([1, 10], [batch_pages(1)[0].page, batch_pages(1)[-1].page])
        self.assertEqual([61, 65], [batch_pages(7)[0].page, batch_pages(7)[-1].page])
        self.assertEqual(5, len(batch_pages(7)))

    def test_beginner_prompt_uses_sixty_five_page_contract(self):
        page = load_pages()[18]
        prompt = compile_prompt(page, load_style())
        self.assertIn("ABSTRACT CLASS vs INTERFACE", prompt)
        self.assertIn("page 19 of 65", prompt)
        self.assertIn("19 / 65", prompt)
        self.assertIn("complete beginner", prompt)
        self.assertIn("Since Java 8", prompt)
        self.assertIn("PORTRAIT IS NON-NEGOTIABLE", prompt)
        self.assertIn("STYLE DIRECTIONS ARE NOT PAGE CONTENT", prompt)
        self.assertIn("JAVA CODE IS CASE-SENSITIVE", prompt)
        self.assertIn("PRESERVE CODE STRUCTURE", prompt)
        self.assertIn("EXACT FOOTER", prompt)
        self.assertIn("FINAL PRE-RENDER AUDIT", prompt)

    def test_every_page_starts_with_short_easy_definition(self):
        for page in load_pages():
            self.assertTrue(page.objective)
            self.assertLessEqual(len(page.objective.split()), 35)

    def test_human_gate_blocks_script_and_next_batch(self):
        pending = {"script": {"status": "review_pending"}, "pages": {}}
        with self.assertRaisesRegex(ValueError, "written script"):
            _assert_batch_unlocked(pending, 1)

        state = {
            "script": {"status": "approved"},
            "pages": {str(n): {"status": "approved"} for n in range(1, 10)},
        }
        with self.assertRaisesRegex(ValueError, r"blocked pages: \[10\]"):
            _assert_batch_unlocked(state, 2)
        state["pages"]["10"] = {"status": "approved"}
        _assert_batch_unlocked(state, 2)


if __name__ == "__main__":
    unittest.main()
