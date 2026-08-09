from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import Toggle, OptionList

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class DragorrodsJoin7AsyncsChallengesArchipelagoOptions:
    dragorrods_join_7_asyncs_challenges_bucket_related_challenges: DragorrodsJoin7AsyncsChallengesBucketRelatedChallenges
    dragorrods_join_7_asyncs_challenges_specific_games_challenge: DragorrodsJoin7AsyncsChallengesSpecificGamesChallenge
    dragorrods_join_7_asyncs_challenges_specific_games_list: DragorrodsJoin7AsyncsChallengesSpecificGamesList


class DragorrodsJoin7AsyncsChallengesGame(Game):
    name = "Dragorrod's Join 7+ Asyncs Challenges"
    platform = KeymastersKeepGamePlatforms.META

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = DragorrodsJoin7AsyncsChallengesArchipelagoOptions

    @property
    def include_bucket_related(self) -> bool:
        return bool(self.archipelago_options.dragorrods_join_7_asyncs_challenges_bucket_related_challenges.value)

    @property
    def include_specific_games(self) -> bool:
        return bool(self.archipelago_options.dragorrods_join_7_asyncs_challenges_specific_games_challenge.value)

    def specific_games(self) -> List[str]:
        return sorted(self.archipelago_options.dragorrods_join_7_asyncs_challenges_specific_games_list.value)

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Send 10 checks in one session",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Send 20 checks in one session",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Send a macguffin",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Send a progression item",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Send a hint",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Send a trap",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Send a filler",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Send a useful",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Send 5 macguffin in one game",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Send 5 progression item in one game",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Send 2 hints in one game",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Send 2 hints to one game but from 2 different games",
                data=dict(),
                is_time_consuming=True,
                is_difficult=True,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Send 2 traps to the same player",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Send 5 fillers",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Send 3 useful",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Send a progression in 4 different asyncs",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Send a progression in 3 different asyncs",
                data=dict(),
                is_time_consuming=False,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Send a progression in 2 different asyncs",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Send a hint in 4 different asyncs",
                data=dict(),
                is_time_consuming=True,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Send a hint in 3 different asyncs",
                data=dict(),
                is_time_consuming=True,
                is_difficult=True,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Send a hint in 2 different asyncs",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Hint a macguffin",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Hint a progression",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Hint a location you don't want to do",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=4,
            ),
            GameObjectiveTemplate(
                label="Help someone with a simon puzzle",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Help someone with a KMK check",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Have someone do one of your checks for you",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=2,
            ),
        ]

        if self.include_specific_games:
            templates.extend([
                GameObjectiveTemplate(
                    label="Bring a new or claim a GAME",
                    data={"GAME": (self.specific_games, 1)},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=10,
                ),
                GameObjectiveTemplate(
                    label="Claim a GAME or bring one to a new async with half the settings set to random",
                    data={"GAME": (self.specific_games, 1)},
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=6,
                ),
                GameObjectiveTemplate(
                    label="Claim a GAME or bring one to a new async with all settings on default",
                    data={"GAME": (self.specific_games, 1)},
                    is_time_consuming=False,
                    is_difficult=True,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Claim a GAME or bring one to a new async with prog balancing 0",
                    data={"GAME": (self.specific_games, 1)},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=4,
                ),
                GameObjectiveTemplate(
                    label="Goal GAME in any async",
                    data={"GAME": (self.specific_games, 1)},
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Fully BK all your current GAME, if none, complete a solo of GAME",
                    data={"GAME": (self.specific_games, 1)},
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=4,
                ),
            ])

            if self.include_bucket_related:
                templates.append(
                    GameObjectiveTemplate(
                        label="Do a solo GAME and send it to the bucket",
                        data={"GAME": (self.specific_games, 1)},
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=4,
                    )
                )

        if self.include_bucket_related:
            templates.extend([
                GameObjectiveTemplate(
                    label="Host a small quick async and send yamls to the bucket",
                    data=dict(),
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label='Create a meta yaml that only affects "null" and send to the bucket',
                    data=dict(),
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Ask Dragorrod to make you a 2 bucket yaml world you can play and finish it",
                    data=dict(),
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
            ])

        return templates


# Archipelago Options

class DragorrodsJoin7AsyncsChallengesBucketRelatedChallenges(Toggle):
    """
    Indicates whether challenges related to the bucket can be selected.
    """

    display_name = "Dragorrod's Join 7+ Asyncs Challenges Bucket Related Challenges"


class DragorrodsJoin7AsyncsChallengesSpecificGamesChallenge(Toggle):
    """
    Indicates whether challenges that reference a specific game from your list can be selected.
    """

    display_name = "Dragorrod's Join 7+ Asyncs Challenges Specific Games Challenge"


class DragorrodsJoin7AsyncsChallengesSpecificGamesList(OptionList):
    """
    The list of games that can be randomly selected for specific games challenges.

    Only used when Dragorrod's Join 7+ Asyncs Challenges Specific Games Challenge is enabled.
    """

    display_name = "Dragorrod's Join 7+ Asyncs Challenges Specific Games List"

    default = ["Game1", "Game2", "Game3"]
