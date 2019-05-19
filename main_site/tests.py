from django.test import TestCase
from .models import Question

class QuestionModelTests(TestCase):
    def test_reply_empty_string(self):
        """
        seen be False when response is empty
        """
        empty_reply = Question(asker="Tester",cat="Meow",content="test")
        empty_reply.submit()
        empty_reply.reply("")
        self.assertIs(empty_reply.seen,False)

    def test_reply_not_empty_string(self):
        """
        seen be True when response is not empty
        """
        empty_reply = Question(asker="Tester",cat="Meow",content="test")
        empty_reply.submit()
        empty_reply.reply("Wong")
        self.assertIs(empty_reply.seen,True)

    def test_unreply(self):
        """
        seen be True when response is not empty
        """
        empty_reply = Question(asker="Tester",cat="Meow",content="test")
        empty_reply.submit()
        self.assertIs(empty_reply.seen,False)