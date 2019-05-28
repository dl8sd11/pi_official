from django.test import TestCase
from django.urls import reverse
from .models import Question
from .burn_side import BurnSide


def create_question(asker="Tester", title="test",
                    cat="Meow", content="Not a real question"):
    reply = Question(asker="Tester", cat="Meow", content="test", order=1)
    reply.submit()
    return reply


class QuestionModelTests(TestCase):
    def test_reply_empty_string(self):
        """
        seen be False when response is empty
        """
        empty_reply = create_question()
        empty_reply.reply("")
        self.assertIs(empty_reply.seen, False)

    def test_reply_not_empty_string(self):
        """
        seen be True when response is not empty
        """
        not_empty_reply = create_question()
        not_empty_reply.reply("Wong")
        self.assertIs(not_empty_reply.seen, True)

    def test_unreply(self):
        """
        seen be True when response is not empty
        """
        unreply_question = create_question()
        unreply_question.submit()
        self.assertIs(unreply_question.seen, False)


class ResponseQuestionViewTests(TestCase):
    def test_id_not_exist(self):
        """
        If the given id not exist return 404
        """
        response = self.client.get(reverse('response_questions', args=[40404]))
        self.assertEqual(response.status_code,  404)

    def test_id_exist(self):
        """
        If the given id exist return reply form with question
        """
        query_question = create_question()
        response = self.client.get(reverse('response_questions',
                                   args=[query_question.id]))
        self.assertEqual(response.context['question'], query_question)


class BurnSideTests(TestCase):
    def test_prime_n(self):
        """
        n is prime
        """
        agent = BurnSide(7, 3)
        self.assertIn("198.0000000000", agent.solve())

    def test_composite_n(self):
        """
        n is composite
        """
        agent = BurnSide(6, 6)
        self.assertIn("4291.0000000000", agent.solve())

    def test_neg_n(self):
        """
        n is neg
        """
        agent = BurnSide(-8, 4)
        self.assertIn("-0.0656747818", agent.solve())

    def test_zero_n(self):
        """
        n is zero
        """
        agent = BurnSide(0, 4)
        self.assertIn("0.0000000000", agent.solve())

    def test_zero_k(self):
        """
        k is zero
        """
        agent = BurnSide(5, 0)
        self.assertIn("0.0000000000", agent.solve())

    def test_neg_k(self):
        """
        k is neg
        """
        agent = BurnSide(12, -4)
        self.assertIn("696166.0000000000", agent.solve())
