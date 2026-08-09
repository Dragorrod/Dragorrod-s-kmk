from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class DragorrodsDoWhateverYouWantChallengesArchipelagoOptions:
    dragorrods_do_whatever_you_want_challenges_no_quite_what_you_want: DragorrodsDoWhateverYouWantChallengesNoQuiteWhatYouWant


class DragorrodsDoWhateverYouWantChallengesGame(Game):
    name = "Dragorrod's Do Whatever You Want Challenges"
    platform = KeymastersKeepGamePlatforms.META

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = DragorrodsDoWhateverYouWantChallengesArchipelagoOptions

    @property
    def no_quite_what_you_want(self) -> bool:
        return bool(self.archipelago_options.dragorrods_do_whatever_you_want_challenges_no_quite_what_you_want.value)

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Do whatever you want for 15 minutes",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=8,
            ),
            GameObjectiveTemplate(
                label="Do whatever you want for 30 minutes",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=12,
            ),
            GameObjectiveTemplate(
                label="Do whatever you want for 1 hour",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=5,
            ),
            GameObjectiveTemplate(
                label="Do whatever you want for 2 hours",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=2,
            ),
            GameObjectiveTemplate(
                label="Do whatever you want for 3 hours",
                data=dict(),
                is_time_consuming=True,
                is_difficult=False,
                weight=1,
            ),
        ]

        if self.no_quite_what_you_want:
            templates.extend([
                GameObjectiveTemplate(
                    label="Do whatever you want out of your house for 30 minutes",
                    data=dict(),
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Do whatever you want on the sofa for 30 minutes",
                    data=dict(),
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Do whatever you want without electronics for 30 minutes",
                    data=dict(),
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Do whatever you want in your bed for 30 minutes",
                    data=dict(),
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Do whatever you want sitting on the ground for 30 minutes",
                    data=dict(),
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
            ])

        return templates


# Archipelago Options

class DragorrodsDoWhateverYouWantChallengesNoQuiteWhatYouWant(Toggle):
    """
    Want challenges that are not quite just whatever you want?
    """

    display_name = "Dragorrod's Do Whatever You Want Challenges No Quite What You Want"
