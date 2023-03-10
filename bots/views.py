from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import *

from .models import Bot


# All views of the application "bots", ie all functions used when opening a page of this application.


class IndexView(generic.ListView):
    """
    This is the main view for bot discord directory
    """
    template_name = 'bots/index.html'
    context_object_name = 'latest_bot_list'

    def get_queryset(self):
        """
        Return the last ten added bots (not including those set to be
        published in the future).
        """
        return Bot.objects.filter(
            add_date__lte=timezone.now()
        ).order_by('-votes')[:10]


class DetailView(generic.DetailView):
    """
    This is the view that allows you to see the details of a bot
    """
    model = Bot
    template_name = 'bots/detail/detail.html'

    def get_queryset(self):
        """
        Excludes any bots that aren't added yet.
        """
        return Bot.objects.filter(add_date__lte=timezone.now())


class AddView(generic.FormView):
    """
    This is the view to add a new bot
    """
    template_name = 'bots/add/add.html'
    form_class = AddBotForm
    success_url = '/'

    def form_valid(self, form):
        bot = form.addBot(self.request.user)
        return HttpResponseRedirect(reverse('bots:detail', args=(bot.id,)))


class VoteView(generic.View):
    """
    This is the view to vote to a bot (no visible)
    """
    model = Bot

    def get(self, request, *args, **kwargs):
        """
        Returns all the information of a bot
        """
        bot_id = self.kwargs.get('pk')
        bot = Bot.objects.get(id=bot_id)
        bot.votes += 1
        bot.save()
        return HttpResponseRedirect(reverse('bots:detail', args=(bot_id,)))


class UpdateView(generic.UpdateView):
    """
    This is the view to update the bot
    """
    model = Bot
    template_name = "bots/update/update.html"
    form_class = UpdateBotForm

    def get_success_url(self):
        """
        Redirects the page to the DetailView when the user has validated the form
        """
        return reverse('bots:detail', args=(self.kwargs.get('pk'),))


class RemoveView(generic.DeleteView):
    """
    This is the view to confirm the deletion of a bot
    """
    model = Bot
    template_name = 'bots/remove/remove.html'
    success_url = '/'


