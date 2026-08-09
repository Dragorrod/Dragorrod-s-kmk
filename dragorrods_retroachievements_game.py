from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import OptionSet

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class DragorrodsRetroachievementsArchipelagoOptions:
    dragorrods_retroachievements_games: DragorrodsRetroachievementsGames


class DragorrodsRetroachievementsGame(Game):
    name = "Dragorrod's Retroachievements"
    platform = KeymastersKeepGamePlatforms.META

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = DragorrodsRetroachievementsArchipelagoOptions

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        return [
            GameObjectiveTemplate(
                label="Earn 1 achievement of GAME",
                data={"GAME": (self.games, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Earn 2 achievements of GAME",
                data={"GAME": (self.games, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Earn 3 achievements of GAME",
                data={"GAME": (self.games, 1)},
                is_time_consuming=False,
                is_difficult=False,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Earn 4 achievements of GAME",
                data={"GAME": (self.games, 1)},
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Earn 5 achievements of GAME",
                data={"GAME": (self.games, 1)},
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
            GameObjectiveTemplate(
                label="Earn 5% of your remaining achievements of GAME",
                data={"GAME": (self.games, 1)},
                is_time_consuming=False,
                is_difficult=True,
                weight=15,
            ),
            GameObjectiveTemplate(
                label="Earn 10% of your remaining achievements of GAME",
                data={"GAME": (self.games, 1)},
                is_time_consuming=True,
                is_difficult=True,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Earn 5% of all achievements of GAME",
                data={"GAME": (self.games, 1)},
                is_time_consuming=True,
                is_difficult=True,
                weight=3,
            ),
            GameObjectiveTemplate(
                label="Earn 10% of all achievements of GAME",
                data={"GAME": (self.games, 1)},
                is_time_consuming=True,
                is_difficult=True,
                weight=1,
            ),
        ]

    def games(self) -> List[str]:
        return sorted(self.archipelago_options.dragorrods_retroachievements_games.value)


# Archipelago Options

class DragorrodsRetroachievementsGames(OptionSet):
    """
    Indicates which games the player owns and wants to hunt achievements for.
    """

    display_name = "Dragorrod's Retroachievements Games"

    default = [
        "[PLATFORM] Game 1",
        "[PLATFORM] Game 2",
        "[PLATFORM] Game 3",
    ]
