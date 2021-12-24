import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from polls.models import Question


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        test for was_published_recenetly() method
        :return: false for Questions  whose publish_date are in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(publish_date=time)
        self.assertIs(future_question.was_published_recenetly(), False)

    def test_was_published_recently_with_old_question(self):
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(publish_date=time)
        self.assertIs(old_question.was_published_recenetly(), False)

    def test_was_published_recently_with_recent_question(self):
        time = timezone.now() - datetime.timedelta(hours=23, seconds=59, minutes=59)
        recent_question = Question(publish_date=time)
        self.assertIs(recent_question.was_published_recenetly(), True)


def create_question(question, days):
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question=question, publish_date=time)


class QuestionIndexViewTests(TestCase):
    def test_no_questions(self):
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_past_question(self):
        """
        Questions with publish date in the past are displayed on index page
        :return:
        """
        question = create_question("Past Question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], question)

    def test_future_question(self):
        """
        Questions with publish date in the future are not displayed on index page
        :return:
        """

        create_question("Future 2Question.", days=30)
        response = self.client.get(reverse('polls:index'))
        self.assertContains(response, "No polls are available")
        self.assertQuerysetEqual(response.context['latest_question_list'], [])

    def test_future_a_and_past_question(self):
        """
        Even if both  future and past questions exist, only past questions are displayed
        :return:
        """
        create_question("Future 2Question.", days=30)
        past_question = create_question("Past Question.", days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerysetEqual(response.context['latest_question_list'], [past_question])

    def test_future_and_past_question(self):

        pass


class QuestionDetailViewTests(TestCase):
    def future_question(self):
        """
        The detail view of a question with a publish date in the future returns 404
        :return:
        """
        question = create_question("Future Question.", days=30)
        response = self.client.get(reverse('polls:detail', args=(question.id, )))
        self.assertEqual(response.status_code, 404)

