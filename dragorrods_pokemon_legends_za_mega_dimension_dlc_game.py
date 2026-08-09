from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class DragorrodsPokemonLegendsZAMegaDimensionDLCArchipelagoOptions:
    dragorrods_legends_za_mega_dimension_include_shiny_challenges: DragorrodsLegendsZAMegaDimensionIncludeShinyChallenges


class DragorrodsPokemonLegendsZAMegaDimensionDLCGame(Game):
    name = "Dragorrod's Pokemon Legends Z-A: Mega Dimension DLC"
    platform = KeymastersKeepGamePlatforms.SW

    platforms_other = None

    is_adult_only_or_unrated = False

    options_cls = DragorrodsPokemonLegendsZAMegaDimensionDLCArchipelagoOptions

    @property
    def include_shiny_challenges(self) -> bool:
        return bool(self.archipelago_options.dragorrods_legends_za_mega_dimension_include_shiny_challenges.value)

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates: List[GameObjectiveTemplate] = [
            GameObjectiveTemplate(
                label="Get the gold ball in 2 wild hyperspace 1 star",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=16,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 3 wild hyperspace 1 star",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=24,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 4 wild hyperspace 1 star",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=16,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 2 wild hyperspace 2 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=16,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 3 wild hyperspace 2 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=24,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 4 wild hyperspace 2 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=16,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 2 wild hyperspace 3 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=16,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 3 wild hyperspace 3 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=24,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 4 wild hyperspace 3 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=16,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 2 wild hyperspace 4 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=16,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 3 wild hyperspace 4 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=24,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 4 wild hyperspace 4 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=16,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 2 Battle hyperspace 2 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 3 Battle hyperspace 2 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 4 Battle hyperspace 2 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 2 Battle hyperspace 3 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 3 Battle hyperspace 3 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 4 Battle hyperspace 3 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 2 Battle hyperspace 4 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 3 Battle hyperspace 4 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=10,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 4 Battle hyperspace 4 stars",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=6,
            ),
            GameObjectiveTemplate(
                label="Defeat 1 rogue mega evolution hyperspace",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=48,
            ),
            GameObjectiveTemplate(
                label="Defeat 2 rogue mega evolution hyperspace",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=40,
            ),
            GameObjectiveTemplate(
                label="Defeat 3 rogue mega evolution hyperspace",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=24,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 1 hyperspace 5 stars (special scan)",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 2 hyperspace 5 stars (special scan)",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=30,
            ),
            GameObjectiveTemplate(
                label="Get the gold ball in 3 hyperspace 5 stars (special scan)",
                data=dict(),
                is_time_consuming=False,
                is_difficult=False,
                weight=20,
            ),
        ]

        if self.include_shiny_challenges:
            shiny_types: List[str] = [
                "Bug",
                "Dark",
                "Dragon",
                "Electric",
                "Fairy",
                "Fighting",
                "Fire",
                "Flying",
                "Ghost",
                "Grass",
                "Ground",
                "Ice",
                "Normal",
                "Poison",
                "Psychic",
                "Rock",
                "Steel",
                "Water",
            ]

            for pokemon_type in shiny_types:
                templates.append(
                    GameObjectiveTemplate(
                        label=f"Get a shiny {pokemon_type.lower()} type or craft 3 sparkly donut",
                        data=dict(),
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=1,
                    )
                )

        return templates


# Archipelago Options

class DragorrodsLegendsZAMegaDimensionIncludeShinyChallenges(Toggle):
    """
    Include challenges asking you to get shiny pokemon or make sparkly donuts?
    """

    display_name = "Dragorrod's Pokemon Legends Z-A Mega Dimension DLC Include Shiny Challenges"
