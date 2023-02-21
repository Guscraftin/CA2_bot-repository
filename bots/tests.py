import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Author, Bot


class BotModelTests(TestCase):

    def test_bot_was_added_in_the_future(self):
        """
        was_joined_recently() returns False for Bot whose add_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_bot = Bot(add_date=time)
        self.assertIs(future_bot.was_published_recently(), False)

    def test_bot_was_added_recently(self):
        """
        was_published_recently() returns False for Bot whose add_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_bot = Bot(add_date=time)
        self.assertIs(old_bot.was_published_recently(), False)

    def test_bot_was_added_in_the_past(self):
        """
        was_published_recently() returns True for Bot whose add_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_bot = Bot(add_date=time)
        self.assertIs(recent_bot.was_published_recently(), True)


def create_author(author_name, join_date):
    """
    Create an author with the given arguments and joined the
    given number of `join_date` offset to now (negative for bots added
    in the past, positive for bots that have yet to be added).
    """
    time = timezone.now() + datetime.timedelta(days=join_date)
    return Author.objects.create(author_name=author_name, join_date=time)


def create_bot(author, bot_name, add_date, votes, description):
    """
    Create a bot with the given arguments and added the
    given number of `add_date` offset to now (negative for bots added
    in the past, positive for bots that have yet to be added).
    """
    time = timezone.now() + datetime.timedelta(days=add_date)
    return Bot.objects.create(author=author, bot_name=bot_name, add_date=time, votes=votes, description=description)


class BotIndexViewTests(TestCase):
    def test_no_bots(self):
        """
        If no bots exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('bots:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No bots are available.")
        self.assertQuerysetEqual(response.context['latest_bot_list'], [])

    def test_past_bot(self):
        """
        Bots with an add_date in the past are displayed on the
        index page.
        """
        author = create_author(author_name="John", join_date=0)
        bot = create_bot(author=author, bot_name="Past bot.", add_date=-30, votes=0, description="")
        response = self.client.get(reverse('bots:index'))
        self.assertQuerysetEqual(
            response.context['latest_bot_list'],
            [bot],
        )

    def test_future_bot(self):
        """
        Bots with an add_date in the future aren't displayed on
        the index page.
        """
        author = create_author(author_name="John", join_date=0)
        create_bot(author=author, bot_name="Future bots.", add_date=30, votes=0, description="")
        response = self.client.get(reverse('bots:index'))
        self.assertContains(response, "No bots are available.")
        self.assertQuerysetEqual(response.context['latest_bot_list'], [])

    def test_future_bot_and_past_bot(self):
        """
        Even if both past and future bots exist, only past bots
        are displayed.
        """
        author = create_author(author_name="John", join_date=0)
        bot = create_bot(author=author, bot_name="Past question.", add_date=-30, votes=0, description="")
        create_bot(author=author, bot_name="Future question.", add_date=30, votes=0, description="")
        response = self.client.get(reverse('bots:index'))
        self.assertQuerysetEqual(
            response.context['latest_bot_list'],
            [bot],
        )

    def test_two_past_bots(self):
        """
        The bots index page may display multiple bots.
        """
        author = create_author(author_name="John", join_date=0)
        bot1 = create_bot(author=author, bot_name="Past question 1.", add_date=-30, votes=0, description="")
        bot2 = create_bot(author=author, bot_name="Past question 2.", add_date=-5, votes=0, description="")
        response = self.client.get(reverse('bots:index'))
        self.assertQuerysetEqual(
            response.context['latest_bot_list'],
            [bot2, bot1],
        )


class BotDetailViewTests(TestCase):
    def test_future_author(self):
        """
        The detail view of a bot with a add_date in the future
        returns a 404 not found.
        """
        author = create_author(author_name="John", join_date=0)
        future_bot = create_bot(author=author, bot_name="Future bot.", add_date=5, votes=0, description="")
        url = reverse('bots:detail', args=(future_bot.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_author(self):
        """
        The detail view of an author with a join_date in the past
        displays the bot's text.
        """
        author = create_author(author_name="John", join_date=0)
        past_bot = create_bot(author=author, bot_name="Past bot.", add_date=-5, votes=0, description="")
        url = reverse('bots:detail', args=(past_bot.id,))
        response = self.client.get(url)
        self.assertContains(response, past_bot.bot_name)
