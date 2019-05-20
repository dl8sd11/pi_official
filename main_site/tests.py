from django.test import TestCase
from django.urls import reverse
from .models import Question

def create_question(asker="Tester",title="test",cat="Meow",content="Not a real question"):
    reply = Question(asker="Tester",cat="Meow",content="test")
    reply.submit()
    return reply

class QuestionModelTests(TestCase):
    def test_reply_empty_string(self):
        """
        seen be False when response is empty
        """
        empty_reply = create_question()
        empty_reply.reply("")
        self.assertIs(empty_reply.seen,False)

    def test_reply_not_empty_string(self):
        """
        seen be True when response is not empty
        """
        not_empty_reply = create_question()
        not_empty_reply.reply("Wong")
        self.assertIs(not_empty_reply.seen,True)

    def test_unreply(self):
        """
        seen be True when response is not empty
        """
        unreply_question = create_question()
        unreply_question.submit()
        self.assertIs(unreply_question.seen,False)


class ResponseQuestionViewTests(TestCase):
    def test_id_not_exist(self):
        """
        If the given id not exist return 404
        """
        response = self.client.get(reverse('response_questions',args=[40404]))
        self.assertEqual(response.status_code, 404)

    def test_id_exist(self):
        """
        If the given id exist return reply form with question
        """
        query_question = create_question()
        response = self.client.get(reverse('response_questions',args=[query_question.id]))
        self.assertEqual(response.context['question'],query_question)