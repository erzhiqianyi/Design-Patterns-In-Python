import unittest

from notebook.note_book import Note, NoteBook


class NoteMatchTestCase(unittest.TestCase):

    def test_match(self):
        n1 = Note('hello first')
        match = n1.match('hello')
        self.assertTrue(match)

    def test_not_match(self):
        n2 = Note('hello again')
        match = n2.match('second')
        self.assertFalse(match)


class NewNotebookTestCase(unittest.TestCase):

    def setUp(self):
        self.notebook = NoteBook()

    def test_new_note(self):
        memo = 'hello world'
        self.notebook.new_note(memo)
        self.assertEqual(len(self.notebook.notes), 1)
        note = self.notebook.notes[0]
        self.assertEqual(memo, note.memo)

    def test_new_note_tags(self):
        memo = 'hello world'
        tags = ['first']
        self.notebook.new_note(memo, tags=tags)
        self.assertEqual(len(self.notebook.notes), 1)
        note = self.notebook.notes[0]
        self.assertEqual(memo, note.memo)
        self.assertEqual(tags, note.tags)


class SearchNotebookTestCase(unittest.TestCase):

    def setUp(self):
        self.notebook = NoteBook()
        self.notebook.new_note('hello world')
        self.notebook.new_note('hello world again')
        self.notebook.new_note('hello world again and again')
        self.notebook.new_note('hello again')

    def test_search_notes(self):
        notes = self.notebook.search('hello')
        self.assertEqual(len(notes), 4)

    def test_search_notes_no_matches(self):
        notes = self.notebook.search('goodbye')
        self.assertEqual(len(notes), 0)


class ModifyMemoTestCase(unittest.TestCase):
    def setUp(self):
        self.momo = 'hello world'
        self.notebook = NoteBook()
        self.notebook.new_note(self.momo)

    def test_modify_memo(self):
        notes = self.notebook.search(self.momo)
        self.assertEqual(len(self.notebook.notes), 1)
        note = notes[0]
        new_memo = 'new memo'
        modify = self.notebook.modify_memo(note.id, new_memo)
        self.assertTrue(modify)
        note = self.notebook._find_note(note.id)
        self.assertEqual(new_memo, note.memo)


class ModifyTagsTestCase(unittest.TestCase):
    def setUp(self):
        self.momo = 'hello world'
        self.notebook = NoteBook()
        self.notebook.new_note(self.momo)

    def test_modify_tags(self):
        notes = self.notebook.search(self.momo)
        self.assertEqual(len(self.notebook.notes), 1)
        note = notes[0]
        new_tags = ['new', 'tags']
        modify = self.notebook.modify_tags(note.id, new_tags)
        self.assertTrue(modify)
        note = self.notebook._find_note(note.id)
        self.assertEqual(new_tags, note.tags)

if __name__ == '__main__':
    unittest.main()
