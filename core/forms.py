from django import forms
from axelrod import strategies
from .models import Tournament, TournamentDefinition

ALL_STRATEGIES = (
    strategies.basic_strategies +
    strategies.ordinary_strategies +
    strategies.cheating_strategies
)

STRATEGY_CHOICES = [(a.__name__, a.__name__) for a in ALL_STRATEGIES]


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['status', 'tournament_definition']


class TournamentDefinitionForm(forms.ModelForm):
    players = forms.MultipleChoiceField(
        choices=STRATEGY_CHOICES,
        widget=forms.SelectMultiple(attrs={'class': 'multiselect'}))

    class Meta:
        model = TournamentDefinition
        fields = ['name', 'players']

    def clean_players(self):
        return ",".join(self.cleaned_data['players'])
