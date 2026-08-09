from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import Toggle, OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class DragorrodsShinyHuntingArchipelagoOptions:
    dragorrods_shiny_hunting_include_training_challenges: DragorrodsShinyHuntingIncludeTrainingChallenges
    dragorrods_shiny_hunting_include_soft_reset_challenges: DragorrodsShinyHuntingIncludeSoftResetChallenges
    dragorrods_shiny_hunting_include_games: DragorrodsShinyHuntingIncludeGames


class DragorrodsShinyHuntingGame(Game):
    name = "Dragorrod's Shiny Hunting"
    platform = KeymastersKeepGamePlatforms.META

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = DragorrodsShinyHuntingArchipelagoOptions

    @property
    def include_training(self) -> bool:
        return bool(self.archipelago_options.dragorrods_shiny_hunting_include_training_challenges.value)

    @property
    def include_soft_reset(self) -> bool:
        return bool(self.archipelago_options.dragorrods_shiny_hunting_include_soft_reset_challenges.value)

    @property
    def included_games(self) -> set:
        return set(self.archipelago_options.dragorrods_shiny_hunting_include_games.value)

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        # (label, weight, game, is_difficult, is_training, is_soft_reset)
        entries = [
            ("Legends Z-A - Hyperspace Lumiose: Get a shiny or craft 6 sparkly donut", 6, "Legends Z-A", False, False, False),
            ("Legends Z-A - Overworld Encounter: Get a shiny or spend 2 hours looking", 1, "Legends Z-A", True, False, False),
            ("Legends Arceus - Massive Mass Outbreak: Get a shiny or fully explore 3 MMO", 3, "Legends Arceus", False, False, False),
            ("Legends Arceus - Mass Outbreak: Get a shiny or fully explore 5 MO", 3, "Legends Arceus", False, False, False),
            ("Legends Arceus - Overworld Encounter: Get a shiny or spend 2 hours looking", 1, "Legends Arceus", True, False, False),
            ("Scarlet/Violet - Mass Outbreak: Get a shiny or gather 2 herba mystica", 4, "Scarlet/Violet", False, False, False),
            ("Scarlet/Violet - Egg: Get a shiny or hatch 100 eggs", 2, "Scarlet/Violet", False, False, False),
            ("Scarlet/Violet - Overworld Encounter: Get a shiny or spend 2 hours looking", 1, "Scarlet/Violet", True, False, False),
            ("Let's Go - Chain: Get a shiny or spend 1 hour looking with max chain on", 6, "Let's Go", False, False, False),
            ("Sword/Shield - Chain: Get a shiny or do 100 encounters", 1, "Sword/Shield", False, False, False),
            ("Sword/Shield - Egg: Get a shiny or hatch 100 eggs", 2, "Sword/Shield", False, False, False),
            ("Sword/Shield - Dynamax: Get a shiny or do 4 dynamax adventures", 3, "Sword/Shield", False, False, False),
            ("Sword/Shield - Encounter Reset: Get a shiny or spend 2 hours resetting", 1, "Sword/Shield", True, False, True),
            ("Diamond/Pearl - Pokeradar: Get a shiny or spend 2 hours trying", 4, "Brilliant Diamond/Shining Pearl", False, False, False),
            ("Diamond/Pearl - Egg: Get a shiny or hatch 100 eggs", 2, "Brilliant Diamond/Shining Pearl", False, False, False),
            ("Diamond/Pearl - Encounter Reset: Get a shiny or spend 2 hours resetting", 1, "Brilliant Diamond/Shining Pearl", True, False, True),
            ("Evolve a shiny pokemon or train to level 100 with a good moveset in Legends Z-A", 2, "Legends Z-A", False, True, False),
            ("Evolve a shiny pokemon or train to beat the path of solitude with a shiny pokemon in Legends Arceus", 2, "Legends Arceus", False, True, False),
            ("Evolve a shiny pokemon or train to level 100 with a good moveset in Scarlet/Violet", 2, "Scarlet/Violet", True, True, False),
            ("Evolve a shiny pokemon or train to beat the master of the specie in Let's Go", 2, "Let's Go", False, True, False),
            ("Evolve a shiny pokemon or train to level 100 with a good moveset in Sword/Shield", 2, "Sword/Shield", True, True, False),
            ("Evolve a shiny pokemon or train to level 100 with a good moveset in Diamond/Pearl", 2, "Brilliant Diamond/Shining Pearl", True, True, False),
        ]

        included_games: set = self.included_games

        templates: List[GameObjectiveTemplate] = []

        for label, weight, game, is_difficult, is_training, is_soft_reset in entries:
            if game not in included_games:
                continue

            if is_training and not self.include_training:
                continue

            if is_soft_reset and not self.include_soft_reset:
                continue

            templates.append(
                GameObjectiveTemplate(
                    label=label,
                    data=dict(),
                    is_time_consuming=False,
                    is_difficult=is_difficult,
                    weight=weight,
                )
            )

        return templates


# Archipelago Options

class DragorrodsShinyHuntingIncludeTrainingChallenges(Toggle):
    """
    Indicate whether to include challenges that makes you evolve or train shiny Pokemon
    """

    display_name = "Dragorrod's Shiny Hunting Include Training Challenges"


class DragorrodsShinyHuntingIncludeSoftResetChallenges(Toggle):
    """
    Indicate whether to include challenges that requires soft resetting the game over and over
    """

    display_name = "Dragorrod's Shiny Hunting Include Soft Reset Challenges"


class DragorrodsShinyHuntingIncludeGames(OptionSet):
    """
    Indicates which Pokemon games to include shiny hunting challenges for.
    """

    display_name = "Dragorrod's Shiny Hunting Include Games"

    valid_keys = frozenset(
        {
            "Legends Z-A",
            "Legends Arceus",
            "Scarlet/Violet",
            "Let's Go",
            "Sword/Shield",
            "Brilliant Diamond/Shining Pearl",
        }
    )

    default = valid_keys
