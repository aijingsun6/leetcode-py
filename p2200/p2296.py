from collections import deque


class TextEditor:
    left = deque([])
    right = deque([])

    def __init__(self):
        self.left = deque([])
        self.right = deque([])

    def addText(self, text: str) -> None:
        for e in text:
            self.left.append(e)

    def deleteText(self, k: int) -> int:
        c = min(k, len(self.left))
        for i in range(c):
            self.left.pop()
        return c

    def cur_str(self) -> str:
        c = min(10, len(self.left))
        q = deque([])
        s = ""
        for i in range(c):
            e = self.left.pop()
            q.appendleft(e)
            s = e + s
        while len(q) > 0:
            e = q.popleft()
            self.left.append(e)
        return s

    def cursorLeft(self, k: int) -> str:
        c = min(k, len(self.left))
        for i in range(c):
            e = self.left.pop()
            self.right.appendleft(e)
        return self.cur_str()

    def cursorRight(self, k: int) -> str:
        c = min(k, len(self.right))
        for i in range(c):
            e = self.right.popleft()
            self.left.append(e)
        return self.cur_str()

import unittest
class TestTextEditor(unittest.TestCase):
    def test(self):
        textEditor = TextEditor()
        textEditor.addText("leetcode") # leetcode|
        r=textEditor.deleteText(4)     # leet|
        self.assertEqual(4, r)

        textEditor.addText("practice") # leetpractice|
        s = textEditor.cursorRight(3)  # leetpractice|
        self.assertEqual("etpractice", s)

        s = textEditor.cursorLeft(8) # leet|practice
        self.assertEqual("leet", s)

        r = textEditor.deleteText(10) # |practice
        self.assertEqual(4, r)

        s = textEditor.cursorLeft(2) # |practice
        self.assertEqual("", s)

        s = textEditor.cursorRight(6) # practi|ce
        self.assertEqual("practi", s)
        pass

if __name__ == '__main__':
    unittest.main()