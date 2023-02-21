from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import *

from .models import Bot, Author


class IndexView(generic.ListView):
    template_name = 'bots/index.html'
    context_object_name = 'latest_bot_list'

    def get_queryset(self):
        """
        Return the last ten added bots (not including those set to be
        published in the future).
        """
        return Bot.objects.filter(
            add_date__lte=timezone.now()
        ).order_by('-add_date')[:10]


class DetailView(generic.DetailView):
    model = Bot
    template_name = 'bots/detail.html'

    def get_queryset(self):
        """
        Excludes any bots that aren't added yet.
        """
        return Bot.objects.filter(add_date__lte=timezone.now())


class AddView(generic.CreateView):
    model = Bot
    template_name = 'bots/add.html'
    form_class = AddBotForm
    success_url = "/bots"


class VoteView(generic.View):
    model = Bot

    def get(self, request, *args, **kwargs):
        bot_id = self.kwargs.get('pk')
        bot = Bot.objects.get(id=bot_id)
        bot.votes += 1
        bot.save()
        return HttpResponseRedirect(reverse('bots:detail', args=(bot_id,)))


class UpdateView(generic.UpdateView):
    model = Bot
    template_name = "bots/update.html"
    form_class = UpdateBotForm

    def get_success_url(self):
        return reverse('bots:detail', args=(self.kwargs.get('pk'),))


class RemoveView(generic.DeleteView):
    model = Bot
    template_name = 'bots/remove.html'
    success_url = "/bots"


