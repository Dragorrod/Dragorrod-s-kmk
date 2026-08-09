from __future__ import annotations

from typing import List
from dataclasses import dataclass

from Options import Range

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate
from ..enums import KeymastersKeepGamePlatforms


@dataclass
class FarmTogether2ArchipelagoOptions:
    farm_together_2_farm_level: FarmTogether2FarmLevel


class FarmTogether2FarmLevel(Range):
    """What is your current Farm Level in Farm Together 2?"""
    display_name = "Farm Level"
    range_start = 1
    range_end = 250
    default = 10


class FarmTogether2Game(Game):
    name = "Dragorrod's Farm Together 2"
    platform = KeymastersKeepGamePlatforms.PC

    platforms_other = [
        KeymastersKeepGamePlatforms.XONE,
        KeymastersKeepGamePlatforms.PS5,
        KeymastersKeepGamePlatforms.SW,
    ]

    is_adult_only_or_unrated = False
    options_cls = FarmTogether2ArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        return []

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        templates = []

        # --- Gather X Lettuce (level 1+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Lettuce",
            data={"AMOUNT": (self.amounts_lettuce_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 1 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Lettuce",
            data={"AMOUNT": (self.amounts_lettuce_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 1 else 0,
        ))

        # --- Gather X Purple Sweet Asparagus (level 138+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Purple Sweet Asparagus",
            data={"AMOUNT": (self.amounts_purple_sweet_asparagus_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 138 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Purple Sweet Asparagus",
            data={"AMOUNT": (self.amounts_purple_sweet_asparagus_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 138 else 0,
        ))

        # --- Gather X Lombardy Cabbage (level 9+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Lombardy Cabbage",
            data={"AMOUNT": (self.amounts_lombardy_cabbage_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 9 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Lombardy Cabbage",
            data={"AMOUNT": (self.amounts_lombardy_cabbage_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 9 else 0,
        ))

        # --- Unlock Green Cabbage or Gather X Green Cabbage (level 29+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Green Cabbage or Gather AMOUNT Green Cabbage",
            data={"AMOUNT": (self.amounts_green_cabbage_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 29 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Green Cabbage or Gather AMOUNT Green Cabbage",
            data={"AMOUNT": (self.amounts_green_cabbage_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 29 else 0,
        ))

        # --- Unlock Savoy Cabbage or Gather X Savoy Cabbage (level 47+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Savoy Cabbage or Gather AMOUNT Savoy Cabbage",
            data={"AMOUNT": (self.amounts_savoy_cabbage_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 47 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Savoy Cabbage or Gather AMOUNT Savoy Cabbage",
            data={"AMOUNT": (self.amounts_savoy_cabbage_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 47 else 0,
        ))

        # --- Unlock Napa Cabbage or Gather X Napa Cabbage (level 83+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Napa Cabbage or Gather AMOUNT Napa Cabbage",
            data={"AMOUNT": (self.amounts_napa_cabbage_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 83 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Napa Cabbage or Gather AMOUNT Napa Cabbage",
            data={"AMOUNT": (self.amounts_napa_cabbage_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 83 else 0,
        ))

        # --- Gather X Common Spinach (level 42+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Common Spinach",
            data={"AMOUNT": (self.amounts_common_spinach_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 42 else 0,
        ))

        # --- Unlock Red Spinach or Gather X Red Spinach (level 78+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Red Spinach or Gather AMOUNT Red Spinach",
            data={"AMOUNT": (self.amounts_red_spinach_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 78 else 0,
        ))

        # --- Complete X Level1 silver quest (level 62+) ---
        templates.append(GameObjectiveTemplate(
            label="Complete AMOUNT Level1 silver quest",
            data={"AMOUNT": (self.amounts_level1_silver_quest_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 62 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Complete AMOUNT Level1 silver quest",
            data={"AMOUNT": (self.amounts_level1_silver_quest_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 62 else 0,
        ))

        # --- Complete X Level2 silver quest (level 62+) ---
        templates.append(GameObjectiveTemplate(
            label="Complete AMOUNT Level2 silver quest",
            data={"AMOUNT": (self.amounts_level2_silver_quest_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 62 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Complete AMOUNT Level2 silver quest",
            data={"AMOUNT": (self.amounts_level2_silver_quest_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 62 else 0,
        ))

        # --- Complete X Level3 silver quest (level 62+) ---
        templates.append(GameObjectiveTemplate(
            label="Complete AMOUNT Level3 silver quest",
            data={"AMOUNT": (self.amounts_level3_silver_quest_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 62 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Complete AMOUNT Level3 silver quest",
            data={"AMOUNT": (self.amounts_level3_silver_quest_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 62 else 0,
        ))

        # --- Complete X Level4 silver quest (level 62+) ---
        templates.append(GameObjectiveTemplate(
            label="Complete AMOUNT Level4 silver quest",
            data={"AMOUNT": (self.amounts_level4_silver_quest_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 62 else 0,
        ))

        # --- Buy a new expansion (level 1+) ---
        templates.append(GameObjectiveTemplate(
            label="Buy a new expansion",
            data={},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 1 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Buy a new expansion",
            data={},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 1 else 0,
        ))

        # --- Complete X NPC requests (level 10+) ---
        templates.append(GameObjectiveTemplate(
            label="Complete AMOUNT NPC requests",
            data={"AMOUNT": (self.amounts_npc_requests_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 10 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Complete AMOUNT NPC requests",
            data={"AMOUNT": (self.amounts_npc_requests_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 10 else 0,
        ))

        # --- Upgrade Vegetable Shop or empty gem inventory (level 5+) ---
        templates.append(GameObjectiveTemplate(
            label="Upgrade Vegetable Shop or empty gem inventory",
            data={},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 5 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Upgrade Vegetable Shop or empty gem inventory",
            data={},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 5 else 0,
        ))

        # --- Upgrade Fruit Stand or empty gem inventory (level 5+) ---
        templates.append(GameObjectiveTemplate(
            label="Upgrade Fruit Stand or empty gem inventory",
            data={},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 5 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Upgrade Fruit Stand or empty gem inventory",
            data={},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 5 else 0,
        ))

        # --- Upgrade Fish Stand or empty gem inventory (level 6+) ---
        templates.append(GameObjectiveTemplate(
            label="Upgrade Fish Stand or empty gem inventory",
            data={},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 6 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Upgrade Fish Stand or empty gem inventory",
            data={},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 6 else 0,
        ))

        # --- Upgrade Bakery or empty gem inventory (level 9+) ---
        templates.append(GameObjectiveTemplate(
            label="Upgrade Bakery or empty gem inventory",
            data={},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 9 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Upgrade Bakery or empty gem inventory",
            data={},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 9 else 0,
        ))

        # --- Upgrade Grocery Store or empty gem inventory (level 10+) ---
        templates.append(GameObjectiveTemplate(
            label="Upgrade Grocery Store or empty gem inventory",
            data={},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 10 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Upgrade Grocery Store or empty gem inventory",
            data={},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 10 else 0,
        ))

        # --- Upgrade Flower Shop or empty gem inventory (level 14+) ---
        templates.append(GameObjectiveTemplate(
            label="Upgrade Flower Shop or empty gem inventory",
            data={},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 14 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Upgrade Flower Shop or empty gem inventory",
            data={},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 14 else 0,
        ))

        # --- Upgrade Mushroom Stand or empty gem inventory (level 5+) ---
        templates.append(GameObjectiveTemplate(
            label="Upgrade Mushroom Stand or empty gem inventory",
            data={},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 5 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Upgrade Mushroom Stand or empty gem inventory",
            data={},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 5 else 0,
        ))

        # --- Upgrade Arts&Craft Story or empty gem inventory (level 5+) ---
        templates.append(GameObjectiveTemplate(
            label="Upgrade Arts&Craft Story or empty gem inventory",
            data={},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 5 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Upgrade Arts&Craft Story or empty gem inventory",
            data={},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 5 else 0,
        ))

        # --- Gather X Corn (level 1+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Corn",
            data={"AMOUNT": (self.amounts_corn_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 1 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Corn",
            data={"AMOUNT": (self.amounts_corn_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 1 else 0,
        ))

        # --- Gather X Junin Corn (level 18+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Junin Corn",
            data={"AMOUNT": (self.amounts_junin_corn_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 18 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Junin Corn",
            data={"AMOUNT": (self.amounts_junin_corn_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 18 else 0,
        ))

        # --- Unlock Strawberry Red Corn or Gather X Strawberry Red Corn (level 39+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Strawberry Red Corn or Gather AMOUNT Strawberry Red Corn",
            data={"AMOUNT": (self.amounts_strawberry_red_corn_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 39 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Strawberry Red Corn or Gather AMOUNT Strawberry Red Corn",
            data={"AMOUNT": (self.amounts_strawberry_red_corn_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 39 else 0,
        ))

        # --- Gather X Wheat (level 12+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Wheat",
            data={"AMOUNT": (self.amounts_wheat_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 12 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Wheat",
            data={"AMOUNT": (self.amounts_wheat_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 12 else 0,
        ))

        # --- Gather X Rye (level 17+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Rye",
            data={"AMOUNT": (self.amounts_rye_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 17 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Rye",
            data={"AMOUNT": (self.amounts_rye_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 17 else 0,
        ))

        # --- Unlock Barley or Gather X Barley (level 38+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Barley or Gather AMOUNT Barley",
            data={"AMOUNT": (self.amounts_barley_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 38 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Barley or Gather AMOUNT Barley",
            data={"AMOUNT": (self.amounts_barley_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 38 else 0,
        ))

        # --- Gather X Arborio Rice (level 90+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Arborio Rice",
            data={"AMOUNT": (self.amounts_arborio_rice_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 90 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Arborio Rice",
            data={"AMOUNT": (self.amounts_arborio_rice_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 90 else 0,
        ))

        # --- Unlock Basmati Rice or Gather X Basmati Rice (level 127+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Basmati Rice or Gather AMOUNT Basmati Rice",
            data={"AMOUNT": (self.amounts_basmati_rice_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 127 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Basmati Rice or Gather AMOUNT Basmati Rice",
            data={"AMOUNT": (self.amounts_basmati_rice_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 127 else 0,
        ))

        # --- Unlock Black Japonica Rice or Gather X Black Japonica Rice (level 158+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Black Japonica Rice or Gather AMOUNT Black Japonica Rice",
            data={"AMOUNT": (self.amounts_black_japonica_rice_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 158 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Black Japonica Rice or Gather AMOUNT Black Japonica Rice",
            data={"AMOUNT": (self.amounts_black_japonica_rice_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 158 else 0,
        ))

        # --- Gather X Carrot (level 1+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Carrot",
            data={"AMOUNT": (self.amounts_carrot_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 1 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Carrot",
            data={"AMOUNT": (self.amounts_carrot_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 1 else 0,
        ))

        # --- Gather X Cosmic Purple Carrot (level 21+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Cosmic Purple Carrot",
            data={"AMOUNT": (self.amounts_cosmic_purple_carrot_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 21 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Cosmic Purple Carrot",
            data={"AMOUNT": (self.amounts_cosmic_purple_carrot_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 21 else 0,
        ))

        # --- Unlock Kyoto Carrot or Gather X Kyoto Carrot (level 32+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Kyoto Carrot or Gather AMOUNT Kyoto Carrot",
            data={"AMOUNT": (self.amounts_kyoto_carrot_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 32 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Kyoto Carrot or Gather AMOUNT Kyoto Carrot",
            data={"AMOUNT": (self.amounts_kyoto_carrot_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 32 else 0,
        ))

        # --- Unlock Lobbericher Carrot or Gather X Lobbericher Carrot (level 50+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Lobbericher Carrot or Gather AMOUNT Lobbericher Carrot",
            data={"AMOUNT": (self.amounts_lobbericher_carrot_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 50 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Lobbericher Carrot or Gather AMOUNT Lobbericher Carrot",
            data={"AMOUNT": (self.amounts_lobbericher_carrot_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 50 else 0,
        ))

        # --- Unlock Lunar White Carrot or Gather X Lunar White Carrot (level 89+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Lunar White Carrot or Gather AMOUNT Lunar White Carrot",
            data={"AMOUNT": (self.amounts_lunar_white_carrot_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 89 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Lunar White Carrot or Gather AMOUNT Lunar White Carrot",
            data={"AMOUNT": (self.amounts_lunar_white_carrot_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 89 else 0,
        ))

        # --- Gather X Beet (level 2+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Beet",
            data={"AMOUNT": (self.amounts_beet_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 2 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Beet",
            data={"AMOUNT": (self.amounts_beet_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 2 else 0,
        ))

        # --- Gather X Golden Beet (level 23+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Golden Beet",
            data={"AMOUNT": (self.amounts_golden_beet_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 23 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Golden Beet",
            data={"AMOUNT": (self.amounts_golden_beet_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 23 else 0,
        ))

        # --- Unlock Turnip or Gather X Turnip (level 43+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Turnip or Gather AMOUNT Turnip",
            data={"AMOUNT": (self.amounts_turnip_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 43 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Turnip or Gather AMOUNT Turnip",
            data={"AMOUNT": (self.amounts_turnip_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 43 else 0,
        ))

        # --- Gather X Potato (level 3+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Potato",
            data={"AMOUNT": (self.amounts_potato_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 3 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Potato",
            data={"AMOUNT": (self.amounts_potato_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 3 else 0,
        ))

        # --- Gather X Carolina Potato (level 22+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Carolina Potato",
            data={"AMOUNT": (self.amounts_carolina_potato_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 22 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Carolina Potato",
            data={"AMOUNT": (self.amounts_carolina_potato_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 22 else 0,
        ))

        # --- Gather X Vitelotte Potato (level 27+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Vitelotte Potato",
            data={"AMOUNT": (self.amounts_vitelotte_potato_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 27 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Vitelotte Potato",
            data={"AMOUNT": (self.amounts_vitelotte_potato_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 27 else 0,
        ))

        # --- Gather X Zucchini (level 4+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Zucchini",
            data={"AMOUNT": (self.amounts_zucchini_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 4 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Zucchini",
            data={"AMOUNT": (self.amounts_zucchini_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 4 else 0,
        ))

        # --- Unlock Lodge Zucchini or Gather X Lodge Zucchini (level 30+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Lodge Zucchini or Gather AMOUNT Lodge Zucchini",
            data={"AMOUNT": (self.amounts_lodge_zucchini_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 30 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Lodge Zucchini or Gather AMOUNT Lodge Zucchini",
            data={"AMOUNT": (self.amounts_lodge_zucchini_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 30 else 0,
        ))

        # --- Gather X Cucumber (level 30+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Cucumber",
            data={"AMOUNT": (self.amounts_cucumber_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 30 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Cucumber",
            data={"AMOUNT": (self.amounts_cucumber_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 30 else 0,
        ))

        # --- Gather X Pumpkin (level 15+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Pumpkin",
            data={"AMOUNT": (self.amounts_pumpkin_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 15 else 0,
        ))

        # --- Gather X Acorn Pumpkin (level 34+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Acorn Pumpkin",
            data={"AMOUNT": (self.amounts_acorn_pumpkin_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 34 else 0,
        ))

        # --- Unlock Baby Boo Pumpkin or Gather X Baby Boo Pumpkin (level 60+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Baby Boo Pumpkin or Gather AMOUNT Baby Boo Pumpkin",
            data={"AMOUNT": (self.amounts_baby_boo_pumpkin_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 60 else 0,
        ))

        # --- Gather X Eggplant (level 18+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Eggplant",
            data={"AMOUNT": (self.amounts_eggplant_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 18 else 0,
        ))

        # --- Gather X Chinese Eggplant (level 31+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Chinese Eggplant",
            data={"AMOUNT": (self.amounts_chinese_eggplant_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 31 else 0,
        ))

        # --- Unlock Albino Eggplant or Gather X Albino Eggplant (level 47+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Albino Eggplant or Gather AMOUNT Albino Eggplant",
            data={"AMOUNT": (self.amounts_albino_eggplant_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 47 else 0,
        ))

        # --- Gather X Jersey Asparagus (level 115+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Jersey Asparagus",
            data={"AMOUNT": (self.amounts_jersey_asparagus_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 115 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Jersey Asparagus",
            data={"AMOUNT": (self.amounts_jersey_asparagus_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 115 else 0,
        ))

        # --- Unlock Mary Washington Asparagus or Gather X Mary Washington Asparagus (level 171+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Mary Washington Asparagus or Gather AMOUNT Mary Washington Asparagus",
            data={"AMOUNT": (self.amounts_mary_washington_asparagus_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 171 else 0,
        ))

        # --- Gather X Lentil (level 11+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Lentil",
            data={"AMOUNT": (self.amounts_lentil_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 11 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Lentil",
            data={"AMOUNT": (self.amounts_lentil_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 11 else 0,
        ))

        # --- Gather X Chickpea (level 26+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Chickpea",
            data={"AMOUNT": (self.amounts_chickpea_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 26 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Chickpea",
            data={"AMOUNT": (self.amounts_chickpea_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 26 else 0,
        ))

        # --- Gather X White Garlic (level 57+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT White Garlic",
            data={"AMOUNT": (self.amounts_white_garlic_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 57 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT White Garlic",
            data={"AMOUNT": (self.amounts_white_garlic_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 57 else 0,
        ))

        # --- Unlock Red Garlic or Gather X Red Garlic (level 80+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Red Garlic or Gather AMOUNT Red Garlic",
            data={"AMOUNT": (self.amounts_red_garlic_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 80 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Red Garlic or Gather AMOUNT Red Garlic",
            data={"AMOUNT": (self.amounts_red_garlic_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 80 else 0,
        ))

        # --- Unlock Black Garlic or Gather X Black Garlic (level 103+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Black Garlic or Gather AMOUNT Black Garlic",
            data={"AMOUNT": (self.amounts_black_garlic_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 103 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Black Garlic or Gather AMOUNT Black Garlic",
            data={"AMOUNT": (self.amounts_black_garlic_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 103 else 0,
        ))

        # --- Gather X French Bean (level 99+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT French Bean",
            data={"AMOUNT": (self.amounts_french_bean_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 99 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT French Bean",
            data={"AMOUNT": (self.amounts_french_bean_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 99 else 0,
        ))

        # --- Gather X Soy Bean (level 118+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Soy Bean",
            data={"AMOUNT": (self.amounts_soy_bean_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 118 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Soy Bean",
            data={"AMOUNT": (self.amounts_soy_bean_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 118 else 0,
        ))

        # --- Unlock Hyacinth Bean or Gather X Hyacinth Bean (level 133+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Hyacinth Bean or Gather AMOUNT Hyacinth Bean",
            data={"AMOUNT": (self.amounts_hyacinth_bean_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 133 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Hyacinth Bean or Gather AMOUNT Hyacinth Bean",
            data={"AMOUNT": (self.amounts_hyacinth_bean_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 133 else 0,
        ))

        # --- Unlock Broad Bean or Gather X Broad Bean (level 165+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Broad Bean or Gather AMOUNT Broad Bean",
            data={"AMOUNT": (self.amounts_broad_bean_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 165 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Broad Bean or Gather AMOUNT Broad Bean",
            data={"AMOUNT": (self.amounts_broad_bean_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 165 else 0,
        ))

        # --- Gather X Tomato (level 7+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Tomato",
            data={"AMOUNT": (self.amounts_tomato_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 7 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Tomato",
            data={"AMOUNT": (self.amounts_tomato_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 7 else 0,
        ))

        # --- Gather X Honeycomb Tomato (level 24+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Honeycomb Tomato",
            data={"AMOUNT": (self.amounts_honeycomb_tomato_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 24 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Honeycomb Tomato",
            data={"AMOUNT": (self.amounts_honeycomb_tomato_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 24 else 0,
        ))

        # --- Unlock Cherokee Tomato or Gather X Cherokee Tomato (level 46+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Cherokee Tomato or Gather AMOUNT Cherokee Tomato",
            data={"AMOUNT": (self.amounts_cherokee_tomato_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 46 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Cherokee Tomato or Gather AMOUNT Cherokee Tomato",
            data={"AMOUNT": (self.amounts_cherokee_tomato_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 46 else 0,
        ))

        # --- Gather X Beefsteak Tomato (level 26+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Beefsteak Tomato",
            data={"AMOUNT": (self.amounts_beefsteak_tomato_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 26 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Beefsteak Tomato",
            data={"AMOUNT": (self.amounts_beefsteak_tomato_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 26 else 0,
        ))

        # --- Unlock Yellow Beefsteak Tomato or Gather X Yellow Beefsteak Tomato (level 53+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Yellow Beefsteak Tomato or Gather AMOUNT Yellow Beefsteak Tomato",
            data={"AMOUNT": (self.amounts_yellow_beefsteak_tomato_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 53 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Yellow Beefsteak Tomato or Gather AMOUNT Yellow Beefsteak Tomato",
            data={"AMOUNT": (self.amounts_yellow_beefsteak_tomato_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 53 else 0,
        ))

        # --- Unlock Black Beefsteak Tomato or Gather X Black Beefsteak Tomato (level 41+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Black Beefsteak Tomato or Gather AMOUNT Black Beefsteak Tomato",
            data={"AMOUNT": (self.amounts_black_beefsteak_tomato_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 41 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Black Beefsteak Tomato or Gather AMOUNT Black Beefsteak Tomato",
            data={"AMOUNT": (self.amounts_black_beefsteak_tomato_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 41 else 0,
        ))

        # --- Gather X Cherry Tomato (level 36+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Cherry Tomato",
            data={"AMOUNT": (self.amounts_cherry_tomato_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 36 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Cherry Tomato",
            data={"AMOUNT": (self.amounts_cherry_tomato_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 36 else 0,
        ))

        # --- Unlock Yellow Cherry Tomato or Gather X Yellow Cherry Tomato (level 49+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Yellow Cherry Tomato or Gather AMOUNT Yellow Cherry Tomato",
            data={"AMOUNT": (self.amounts_yellow_cherry_tomato_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 49 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Yellow Cherry Tomato or Gather AMOUNT Yellow Cherry Tomato",
            data={"AMOUNT": (self.amounts_yellow_cherry_tomato_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 49 else 0,
        ))

        # --- Unlock Black Cherry Tomato or Gather X Black Cherry Tomato (level 65+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Black Cherry Tomato or Gather AMOUNT Black Cherry Tomato",
            data={"AMOUNT": (self.amounts_black_cherry_tomato_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 65 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Black Cherry Tomato or Gather AMOUNT Black Cherry Tomato",
            data={"AMOUNT": (self.amounts_black_cherry_tomato_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 65 else 0,
        ))

        # --- Gather X Red Pepper (level 5+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Red Pepper",
            data={"AMOUNT": (self.amounts_red_pepper_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 5 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Red Pepper",
            data={"AMOUNT": (self.amounts_red_pepper_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 5 else 0,
        ))

        # --- Gather X Yellow Pepper (level 29+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Yellow Pepper",
            data={"AMOUNT": (self.amounts_yellow_pepper_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 29 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Yellow Pepper",
            data={"AMOUNT": (self.amounts_yellow_pepper_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 29 else 0,
        ))

        # --- Unlock Green Pepper or Gather X Green Pepper (level 44+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Green Pepper or Gather AMOUNT Green Pepper",
            data={"AMOUNT": (self.amounts_green_pepper_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 44 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Green Pepper or Gather AMOUNT Green Pepper",
            data={"AMOUNT": (self.amounts_green_pepper_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 44 else 0,
        ))

        # --- Gather X Spanish Peanut (level 8+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Spanish Peanut",
            data={"AMOUNT": (self.amounts_spanish_peanut_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 8 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Spanish Peanut",
            data={"AMOUNT": (self.amounts_spanish_peanut_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 8 else 0,
        ))

        # --- Gather X Virginia Peanut (level 155+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Virginia Peanut",
            data={"AMOUNT": (self.amounts_virginia_peanut_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 155 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Virginia Peanut",
            data={"AMOUNT": (self.amounts_virginia_peanut_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 155 else 0,
        ))

        # --- Gather X Melon (level 10+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Melon",
            data={"AMOUNT": (self.amounts_melon_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 10 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Melon",
            data={"AMOUNT": (self.amounts_melon_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 10 else 0,
        ))

        # --- Gather X Watermelon (level 20+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Watermelon",
            data={"AMOUNT": (self.amounts_watermelon_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 20 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Watermelon",
            data={"AMOUNT": (self.amounts_watermelon_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 20 else 0,
        ))

        # --- Unlock Canary Melon or Gather X Canary Melon (level 41+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Canary Melon or Gather AMOUNT Canary Melon",
            data={"AMOUNT": (self.amounts_canary_melon_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 41 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Canary Melon or Gather AMOUNT Canary Melon",
            data={"AMOUNT": (self.amounts_canary_melon_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 41 else 0,
        ))

        # --- Gather X Cantaloupe Melon (level 7+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Cantaloupe Melon",
            data={"AMOUNT": (self.amounts_cantaloupe_melon_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 7 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Cantaloupe Melon",
            data={"AMOUNT": (self.amounts_cantaloupe_melon_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 7 else 0,
        ))

        # --- Gather X Concord Grape (level 25+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Concord Grape",
            data={"AMOUNT": (self.amounts_concord_grape_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 25 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Concord Grape",
            data={"AMOUNT": (self.amounts_concord_grape_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 25 else 0,
        ))

        # --- Gather X Thompson Grape (level 39+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Thompson Grape",
            data={"AMOUNT": (self.amounts_thompson_grape_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 39 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Thompson Grape",
            data={"AMOUNT": (self.amounts_thompson_grape_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 39 else 0,
        ))

        # --- Unlock Cabernet Grape or Gather X Cabernet Grape (level 48+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Cabernet Grape or Gather AMOUNT Cabernet Grape",
            data={"AMOUNT": (self.amounts_cabernet_grape_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 48 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Cabernet Grape or Gather AMOUNT Cabernet Grape",
            data={"AMOUNT": (self.amounts_cabernet_grape_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 48 else 0,
        ))

        # --- Unlock Crimson Grape or Gather X Crimson Grape (level 62+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Crimson Grape or Gather AMOUNT Crimson Grape",
            data={"AMOUNT": (self.amounts_crimson_grape_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 62 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Crimson Grape or Gather AMOUNT Crimson Grape",
            data={"AMOUNT": (self.amounts_crimson_grape_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 62 else 0,
        ))

        # --- Gather X Strawberry (level 38+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Strawberry",
            data={"AMOUNT": (self.amounts_strawberry_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 38 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Strawberry",
            data={"AMOUNT": (self.amounts_strawberry_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 38 else 0,
        ))

        # --- Unlock Pineberry or Gather X Pineberry (level 74+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Pineberry or Gather AMOUNT Pineberry",
            data={"AMOUNT": (self.amounts_pineberry_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 74 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Pineberry or Gather AMOUNT Pineberry",
            data={"AMOUNT": (self.amounts_pineberry_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 74 else 0,
        ))

        # --- Gather X Black Peppercorn (level 80+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Black Peppercorn",
            data={"AMOUNT": (self.amounts_black_peppercorn_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 80 else 0,
        ))

        # --- Unlock Green Peppercorn or Gather X Green Peppercorn (level 101+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Green Peppercorn or Gather AMOUNT Green Peppercorn",
            data={"AMOUNT": (self.amounts_green_peppercorn_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 101 else 0,
        ))

        # --- Unlock Pink Peppercorn or Gather X Pink Peppercorn (level 127+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Pink Peppercorn or Gather AMOUNT Pink Peppercorn",
            data={"AMOUNT": (self.amounts_pink_peppercorn_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 127 else 0,
        ))

        # --- Gather X Flat Parsley (level 125+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Flat Parsley",
            data={"AMOUNT": (self.amounts_flat_parsley_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 125 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Flat Parsley",
            data={"AMOUNT": (self.amounts_flat_parsley_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 125 else 0,
        ))

        # --- Unlock Curley Parsley or Gather X Curley Parsley (level 155+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Curley Parsley or Gather AMOUNT Curley Parsley",
            data={"AMOUNT": (self.amounts_curley_parsley_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 155 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Curley Parsley or Gather AMOUNT Curley Parsley",
            data={"AMOUNT": (self.amounts_curley_parsley_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 155 else 0,
        ))

        # --- Unlock Coriander or Gather X Coriander (level 185+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Coriander or Gather AMOUNT Coriander",
            data={"AMOUNT": (self.amounts_coriander_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 185 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Coriander or Gather AMOUNT Coriander",
            data={"AMOUNT": (self.amounts_coriander_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 185 else 0,
        ))

        # --- Gather X Gold Pineapple (level 86+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Gold Pineapple",
            data={"AMOUNT": (self.amounts_gold_pineapple_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 86 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Gold Pineapple",
            data={"AMOUNT": (self.amounts_gold_pineapple_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 86 else 0,
        ))

        # --- Unlock Mauritius Pineapple or Gather X Mauritius Pineapple (level 111+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Mauritius Pineapple or Gather AMOUNT Mauritius Pineapple",
            data={"AMOUNT": (self.amounts_mauritius_pineapple_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 111 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Mauritius Pineapple or Gather AMOUNT Mauritius Pineapple",
            data={"AMOUNT": (self.amounts_mauritius_pineapple_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 111 else 0,
        ))

        # --- Unlock Red Pineapple or Gather X Red Pineapple (level 142+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Red Pineapple or Gather AMOUNT Red Pineapple",
            data={"AMOUNT": (self.amounts_red_pineapple_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 142 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Red Pineapple or Gather AMOUNT Red Pineapple",
            data={"AMOUNT": (self.amounts_red_pineapple_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 142 else 0,
        ))

        # --- Gather X Apple (level 1+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Apple",
            data={"AMOUNT": (self.amounts_apple_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 1 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Apple",
            data={"AMOUNT": (self.amounts_apple_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 1 else 0,
        ))

        # --- Gather X Royal Gala Apple (level 24+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Royal Gala Apple",
            data={"AMOUNT": (self.amounts_royal_gala_apple_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 24 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Royal Gala Apple",
            data={"AMOUNT": (self.amounts_royal_gala_apple_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 24 else 0,
        ))

        # --- Unlock Reinette Apple or Gather X Reinette Apple (level 36+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Reinette Apple or Gather AMOUNT Reinette Apple",
            data={"AMOUNT": (self.amounts_reinette_apple_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 36 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Reinette Apple or Gather AMOUNT Reinette Apple",
            data={"AMOUNT": (self.amounts_reinette_apple_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 36 else 0,
        ))

        # --- Unlock Granny Smith Apple or Gather X Granny Smith Apple (level 68+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Granny Smith Apple or Gather AMOUNT Granny Smith Apple",
            data={"AMOUNT": (self.amounts_granny_smith_apple_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 68 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Granny Smith Apple or Gather AMOUNT Granny Smith Apple",
            data={"AMOUNT": (self.amounts_granny_smith_apple_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 68 else 0,
        ))

        # --- Unlock Golden Apple or Gather X Golden Apple (level 89+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Golden Apple or Gather AMOUNT Golden Apple",
            data={"AMOUNT": (self.amounts_golden_apple_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 89 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Golden Apple or Gather AMOUNT Golden Apple",
            data={"AMOUNT": (self.amounts_golden_apple_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 89 else 0,
        ))

        # --- Gather X Lemon (level 2+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Lemon",
            data={"AMOUNT": (self.amounts_lemon_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 2 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Lemon",
            data={"AMOUNT": (self.amounts_lemon_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 2 else 0,
        ))

        # --- Unlock Orange or Gather X Orange (level 22+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Orange or Gather AMOUNT Orange",
            data={"AMOUNT": (self.amounts_orange_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 22 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Orange or Gather AMOUNT Orange",
            data={"AMOUNT": (self.amounts_orange_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 22 else 0,
        ))

        # --- Unlock Lime or Gather X Lime (level 31+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Lime or Gather AMOUNT Lime",
            data={"AMOUNT": (self.amounts_lime_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 31 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Lime or Gather AMOUNT Lime",
            data={"AMOUNT": (self.amounts_lime_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 31 else 0,
        ))

        # --- Unlock Tangerine or Gather X Tangerine (level 61+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Tangerine or Gather AMOUNT Tangerine",
            data={"AMOUNT": (self.amounts_tangerine_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 61 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Tangerine or Gather AMOUNT Tangerine",
            data={"AMOUNT": (self.amounts_tangerine_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 61 else 0,
        ))

        # --- Unlock Yuzu or Gather X Yuzu (level 82+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Yuzu or Gather AMOUNT Yuzu",
            data={"AMOUNT": (self.amounts_yuzu_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 82 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Yuzu or Gather AMOUNT Yuzu",
            data={"AMOUNT": (self.amounts_yuzu_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 82 else 0,
        ))

        # --- Unlock Blood Tangerine or Gather X Blood Tangerine (level 96+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Blood Tangerine or Gather AMOUNT Blood Tangerine",
            data={"AMOUNT": (self.amounts_blood_tangerine_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 96 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Blood Tangerine or Gather AMOUNT Blood Tangerine",
            data={"AMOUNT": (self.amounts_blood_tangerine_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 96 else 0,
        ))

        # --- Gather X Pear (level 4+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Pear",
            data={"AMOUNT": (self.amounts_pear_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 4 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Pear",
            data={"AMOUNT": (self.amounts_pear_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 4 else 0,
        ))

        # --- Gather X Peach (level 13+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Peach",
            data={"AMOUNT": (self.amounts_peach_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 13 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Peach",
            data={"AMOUNT": (self.amounts_peach_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 13 else 0,
        ))

        # --- Gather X Apricot (level 28+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Apricot",
            data={"AMOUNT": (self.amounts_apricot_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 28 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Apricot",
            data={"AMOUNT": (self.amounts_apricot_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 28 else 0,
        ))

        # --- Gather X Prickly Pear (level 37+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Prickly Pear",
            data={"AMOUNT": (self.amounts_prickly_pear_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 37 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Prickly Pear",
            data={"AMOUNT": (self.amounts_prickly_pear_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 37 else 0,
        ))

        # --- Gather X Plum (level 45+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Plum",
            data={"AMOUNT": (self.amounts_plum_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 45 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Plum",
            data={"AMOUNT": (self.amounts_plum_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 45 else 0,
        ))

        # --- Unlock Quince or Gather X Quince (level 73+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Quince or Gather AMOUNT Quince",
            data={"AMOUNT": (self.amounts_quince_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 73 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Quince or Gather AMOUNT Quince",
            data={"AMOUNT": (self.amounts_quince_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 73 else 0,
        ))

        # --- Gather X Wonderful Pomegranate (level 96+) ---
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Wonderful Pomegranate",
            data={"AMOUNT": (self.amounts_wonderful_pomegranate_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 96 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Gather AMOUNT Wonderful Pomegranate",
            data={"AMOUNT": (self.amounts_wonderful_pomegranate_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 96 else 0,
        ))

        # --- Unlock Purple Heart Pomegranate or Gather X Purple Heart Pomegranate (level 121+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Purple Heart Pomegranate or Gather AMOUNT Purple Heart Pomegranate",
            data={"AMOUNT": (self.amounts_purple_heart_pomegranate_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 121 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Purple Heart Pomegranate or Gather AMOUNT Purple Heart Pomegranate",
            data={"AMOUNT": (self.amounts_purple_heart_pomegranate_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 121 else 0,
        ))

        # --- Unlock Haku Botan Pomegranate or Gather X Haku Botan Pomegranate (level 150+) ---
        templates.append(GameObjectiveTemplate(
            label="Unlock Haku Botan Pomegranate or Gather AMOUNT Haku Botan Pomegranate",
            data={"AMOUNT": (self.amounts_haku_botan_pomegranate_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 150 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Unlock Haku Botan Pomegranate or Gather AMOUNT Haku Botan Pomegranate",
            data={"AMOUNT": (self.amounts_haku_botan_pomegranate_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 150 else 0,
        ))

        # --- Add 5 Leghorn Chicken and gather X times from them (level 1+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Leghorn Chicken and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_leghorn_chicken_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 1 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Leghorn Chicken and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_leghorn_chicken_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 1 else 0,
        ))

        # --- Add 5 New Hampshire Chicken and gather X times from them (level 13+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 New Hampshire Chicken and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_new_hampshire_chicken_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 13 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 New Hampshire Chicken and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_new_hampshire_chicken_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 13 else 0,
        ))

        # --- Add 5 Australorp Chicken and gather X times from them (level 22+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Australorp Chicken and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_australorp_chicken_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 22 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Australorp Chicken and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_australorp_chicken_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 22 else 0,
        ))

        # --- Add 5 Jersey Giant Chicken and gather X times from them (level 36+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Jersey Giant Chicken and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_jersey_giant_chicken_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 36 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Jersey Giant Chicken and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_jersey_giant_chicken_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 36 else 0,
        ))

        # --- Add 5 Orpington Chicken and gather X times from them (level 45+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Orpington Chicken and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_orpington_chicken_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 45 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Orpington Chicken and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_orpington_chicken_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 45 else 0,
        ))

        # --- Add 5 Serama Bantam Chicken and gather X times from them (level 59+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Serama Bantam Chicken and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_serama_bantam_chicken_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 59 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Serama Bantam Chicken and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_serama_bantam_chicken_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 59 else 0,
        ))

        # --- Add 5 Landrace Pig and gather X times from them (level 6+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Landrace Pig and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_landrace_pig_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 6 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Landrace Pig and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_landrace_pig_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 6 else 0,
        ))

        # --- Add 5 Hampshire Pig and gather X times from them (level 20+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Hampshire Pig and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_hampshire_pig_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 20 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Hampshire Pig and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_hampshire_pig_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 20 else 0,
        ))

        # --- Add 5 Large Black Pig and gather X times from them (level 35+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Large Black Pig and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_large_black_pig_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 35 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Large Black Pig and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_large_black_pig_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 35 else 0,
        ))

        # --- Add 5 Hereford Pig and gather X times from them (level 55+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Hereford Pig and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_hereford_pig_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 55 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Hereford Pig and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_hereford_pig_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 55 else 0,
        ))

        # --- Add 5 Duroc Pig and gather X times from them (level 65+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Duroc Pig and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_duroc_pig_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 65 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Duroc Pig and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_duroc_pig_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 65 else 0,
        ))

        # --- Add 5 Kunekune Pig and gather X times from them (level 85+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Kunekune Pig and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_kunekune_pig_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 85 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Kunekune Pig and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_kunekune_pig_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 85 else 0,
        ))

        # --- Add 5 Holstein Cow and gather X times from them (level 19+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Holstein Cow and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_holstein_cow_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 19 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Holstein Cow and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_holstein_cow_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 19 else 0,
        ))

        # --- Add 5 Jersey Cow and gather X times from them (level 33+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Jersey Cow and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_jersey_cow_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 33 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Jersey Cow and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_jersey_cow_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 33 else 0,
        ))

        # --- Add 5 Belted Cow and gather X times from them (level 44+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Belted Cow and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_belted_cow_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 44 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Belted Cow and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_belted_cow_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 44 else 0,
        ))

        # --- Add 5 Ayrshire Cow and gather X times from them (level 61+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Ayrshire Cow and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_ayrshire_cow_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 61 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Ayrshire Cow and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_ayrshire_cow_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 61 else 0,
        ))

        # --- Add 5 Girolando Cow and gather X times from them (level 84+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Girolando Cow and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_girolando_cow_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 84 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Girolando Cow and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_girolando_cow_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 84 else 0,
        ))

        # --- Add 5 Tyrol Grey Cow and gather X times from them (level 103+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Tyrol Grey Cow and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_tyrol_grey_cow_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 103 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Tyrol Grey Cow and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_tyrol_grey_cow_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 103 else 0,
        ))

        # --- Add 5 Alpine Goat and gather X times from them (level 56+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Alpine Goat and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_alpine_goat_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 56 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Alpine Goat and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_alpine_goat_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 56 else 0,
        ))

        # --- Add 5 Black Bengal Goat and gather X times from them (level 76+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Black Bengal Goat and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_black_bengal_goat_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 76 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Black Bengal Goat and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_black_bengal_goat_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 76 else 0,
        ))

        # --- Add 5 Saanen Goat and gather X times from them (level 99+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Saanen Goat and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_saanen_goat_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 99 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Saanen Goat and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_saanen_goat_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 99 else 0,
        ))

        # --- Add 5 Australian Brown Goat and gather X times from them (level 120+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Australian Brown Goat and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_australian_brown_goat_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 120 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Australian Brown Goat and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_australian_brown_goat_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 120 else 0,
        ))

        # --- Add 5 Nigerian Dwarf Goat and gather X times from them (level 133+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Nigerian Dwarf Goat and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_nigerian_dwarf_goat_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 133 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Nigerian Dwarf Goat and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_nigerian_dwarf_goat_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 133 else 0,
        ))

        # --- Add 5 Hampshire Sheep and gather X times from them (level 34+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Hampshire Sheep and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_hampshire_sheep_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 34 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Hampshire Sheep and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_hampshire_sheep_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 34 else 0,
        ))

        # --- Add 5 Merino Sheep and gather X times from them (level 51+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Merino Sheep and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_merino_sheep_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 51 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Merino Sheep and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_merino_sheep_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 51 else 0,
        ))

        # --- Add 5 Gotland Sheep and gather X times from them (level 63+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Gotland Sheep and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_gotland_sheep_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 63 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Gotland Sheep and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_gotland_sheep_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 63 else 0,
        ))

        # --- Add 5 Romanov Sheep and gather X times from them (level 82+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Romanov Sheep and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_romanov_sheep_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 82 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Romanov Sheep and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_romanov_sheep_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 82 else 0,
        ))

        # --- Add 5 Jacob Sheep and gather X times from them (level 92+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Jacob Sheep and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_jacob_sheep_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 92 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Jacob Sheep and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_jacob_sheep_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 92 else 0,
        ))

        # --- Add 5 Dutch Rabbit and gather X times from them (level 72+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Dutch Rabbit and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_dutch_rabbit_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 72 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Dutch Rabbit and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_dutch_rabbit_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 72 else 0,
        ))

        # --- Add 5 Netherland Dwarf Rabbit and gather X times from them (level 97+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Netherland Dwarf Rabbit and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_netherland_dwarf_rabbit_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 97 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Netherland Dwarf Rabbit and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_netherland_dwarf_rabbit_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 97 else 0,
        ))

        # --- Add 5 Alaska Rabbit and gather X times from them (level 123+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Alaska Rabbit and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_alaska_rabbit_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 123 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Alaska Rabbit and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_alaska_rabbit_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 123 else 0,
        ))

        # --- Add 5 Flemish Giant Rabbit and gather X times from them (level 150+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Flemish Giant Rabbit and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_flemish_giant_rabbit_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 150 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Flemish Giant Rabbit and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_flemish_giant_rabbit_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 150 else 0,
        ))

        # --- Add 5 Suri Alpaca and gather X times from them (level 86+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Suri Alpaca and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_suri_alpaca_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 86 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Suri Alpaca and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_suri_alpaca_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 86 else 0,
        ))

        # --- Add 5 Huacaya Alpaca and gather X times from them (level 127+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Huacaya Alpaca and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_huacaya_alpaca_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 127 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Huacaya Alpaca and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_huacaya_alpaca_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 127 else 0,
        ))

        # --- Add 5 Llama and gather X times from them (level 176+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Llama and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_llama_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 176 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Llama and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_llama_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 176 else 0,
        ))

        # --- Add 5 Abacot Ranger Duck and gather X times from them (level 47+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Abacot Ranger Duck and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_abacot_ranger_duck_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 47 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Abacot Ranger Duck and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_abacot_ranger_duck_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 47 else 0,
        ))

        # --- Add 5 Pekin Duck and gather X times from them (level 65+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Pekin Duck and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_pekin_duck_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 65 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Pekin Duck and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_pekin_duck_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 65 else 0,
        ))

        # --- Add 5 Duckling and gather X times from them (level 79+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Duckling and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_duckling_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 79 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Duckling and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_duckling_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 79 else 0,
        ))

        # --- Add 5 Magpie Duck and gather X times from them (level 97+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Magpie Duck and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_magpie_duck_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 97 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Magpie Duck and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_magpie_duck_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 97 else 0,
        ))

        # --- Add 5 Cayuga Duck and gather X times from them (level 115+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Cayuga Duck and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_cayuga_duck_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 115 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Cayuga Duck and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_cayuga_duck_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 115 else 0,
        ))

        # --- Add 5 Clownfish and gather X times from them (level 1+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Clownfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_clownfish_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 1 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Clownfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_clownfish_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 1 else 0,
        ))

        # --- Add 5 Amber Clownfish and gather X times from them (level 12+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Amber Clownfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_amber_clownfish_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 12 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Amber Clownfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_amber_clownfish_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 12 else 0,
        ))

        # --- Add 5 Ebony Clownfish and gather X times from them (level 24+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Ebony Clownfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_ebony_clownfish_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 24 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Ebony Clownfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_ebony_clownfish_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 24 else 0,
        ))

        # --- Add 5 Surgeonfish and gather X times from them (level 21+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Surgeonfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_surgeonfish_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 21 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Surgeonfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_surgeonfish_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 21 else 0,
        ))

        # --- Add 5 Platinum Surgeonfish and gather X times from them (level 40+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Platinum Surgeonfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_platinum_surgeonfish_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 40 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Platinum Surgeonfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_platinum_surgeonfish_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 40 else 0,
        ))

        # --- Add 5 Bronze Surgeonfish and gather X times from them (level 55+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Bronze Surgeonfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_bronze_surgeonfish_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 55 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Bronze Surgeonfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_bronze_surgeonfish_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 55 else 0,
        ))

        # --- Add 5 Sardine and gather X times from them (level 36+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Sardine and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_sardine_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 36 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Sardine and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_sardine_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 36 else 0,
        ))

        # --- Add 5 Pacific Sardinella and gather X times from them (level 68+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Pacific Sardinella and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_pacific_sardinella_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 68 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Pacific Sardinella and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_pacific_sardinella_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 68 else 0,
        ))

        # --- Add 5 White Sardine and gather X times from them (level 101+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 White Sardine and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_white_sardine_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 101 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 White Sardine and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_white_sardine_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 101 else 0,
        ))

        # --- Add 5 Salmon and gather X times from them (level 6+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Salmon and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_salmon_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 6 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Salmon and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_salmon_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 6 else 0,
        ))

        # --- Add 5 Crimson Salmon and gather X times from them (level 16+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Crimson Salmon and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_crimson_salmon_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 16 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Crimson Salmon and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_crimson_salmon_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 16 else 0,
        ))

        # --- Add 5 Viridian Salmon and gather X times from them (level 25+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Viridian Salmon and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_viridian_salmon_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 25 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Viridian Salmon and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_viridian_salmon_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 25 else 0,
        ))

        # --- Add 5 Trout and gather X times from them (level 18+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Trout and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_trout_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 18 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Trout and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_trout_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 18 else 0,
        ))

        # --- Add 5 Coral Trout and gather X times from them (level 32+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Coral Trout and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_coral_trout_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 32 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Coral Trout and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_coral_trout_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 32 else 0,
        ))

        # --- Add 5 Brass Trout and gather X times from them (level 48+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Brass Trout and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_brass_trout_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 48 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Brass Trout and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_brass_trout_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 48 else 0,
        ))

        # --- Add 5 Blowfish and gather X times from them (level 10+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Blowfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_blowfish_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 10 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Blowfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_blowfish_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 10 else 0,
        ))

        # --- Add 5 Cocoa Blowfish and gather X times from them (level 27+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Cocoa Blowfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_cocoa_blowfish_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 27 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Cocoa Blowfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_cocoa_blowfish_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 27 else 0,
        ))

        # --- Add 5 Cerulean Blowfish and gather X times from them (level 48+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Cerulean Blowfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_cerulean_blowfish_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 48 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Cerulean Blowfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_cerulean_blowfish_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 48 else 0,
        ))

        # --- Add 5 Slinger Seabream and gather X times from them (level 52+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Slinger Seabream and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_slinger_seabream_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 52 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Slinger Seabream and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_slinger_seabream_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 52 else 0,
        ))

        # --- Add 5 Hottentot Seabream and gather X times from them (level 87+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Hottentot Seabream and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_hottentot_seabream_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 87 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Hottentot Seabream and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_hottentot_seabream_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 87 else 0,
        ))

        # --- Add 5 Seventyfour Seabream and gather X times from them (level 123+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Seventyfour Seabream and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_seventyfour_seabream_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 123 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Seventyfour Seabream and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_seventyfour_seabream_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 123 else 0,
        ))

        # --- Add 5 Silver Hake and gather X times from them (level 64+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Silver Hake and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_silver_hake_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 64 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Silver Hake and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_silver_hake_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 64 else 0,
        ))

        # --- Add 5 Swordfish and gather X times from them (level 14+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Swordfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_swordfish_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 14 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Swordfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_swordfish_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 14 else 0,
        ))

        # --- Add 5 Topaz Swordfish and gather X times from them (level 35+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Topaz Swordfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_topaz_swordfish_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 35 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Topaz Swordfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_topaz_swordfish_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 35 else 0,
        ))

        # --- Add 5 Emerald Swordfish and gather X times from them (level 53+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Emerald Swordfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_emerald_swordfish_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 53 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Emerald Swordfish and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_emerald_swordfish_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 53 else 0,
        ))

        # --- Add 5 Vermillion Snapper and gather X times from them (level 81+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Vermillion Snapper and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_vermillion_snapper_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 81 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Vermillion Snapper and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_vermillion_snapper_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 81 else 0,
        ))

        # --- Add 5 Black Snapper and gather X times from them (level 113+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Black Snapper and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_black_snapper_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 113 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Black Snapper and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_black_snapper_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 113 else 0,
        ))

        # --- Add 5 Yellowtail Snapper and gather X times from them (level 142+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Yellowtail Snapper and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_yellowtail_snapper_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 142 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Yellowtail Snapper and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_yellowtail_snapper_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 142 else 0,
        ))

        # --- Add 5 Ginrin Koi and gather X times from them (level 100+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Ginrin Koi and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_ginrin_koi_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 100 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Ginrin Koi and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_ginrin_koi_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 100 else 0,
        ))

        # --- Add 5 Utsuri Koi and gather X times from them (level 133+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Utsuri Koi and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_utsuri_koi_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 133 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Utsuri Koi and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_utsuri_koi_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 133 else 0,
        ))

        # --- Add 5 Shusui Koi and gather X times from them (level 165+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Shusui Koi and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_shusui_koi_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 165 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Shusui Koi and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_shusui_koi_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 165 else 0,
        ))

        # --- Add 5 Rose and gather X times from them (level 1+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Rose and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_rose_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 1 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Rose and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_rose_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 1 else 0,
        ))

        # --- Add 5 Ramanas Rose and gather X times from them (level 13+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Ramanas Rose and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_ramanas_rose_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 13 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Ramanas Rose and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_ramanas_rose_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 13 else 0,
        ))

        # --- Add 5 Damask Rose and gather X times from them (level 26+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Damask Rose and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_damask_rose_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 26 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Damask Rose and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_damask_rose_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 26 else 0,
        ))

        # --- Add 5 Provence Rose and gather X times from them (level 39+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Provence Rose and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_provence_rose_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 39 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Provence Rose and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_provence_rose_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 39 else 0,
        ))

        # --- Add 5 Grandiflora Rose and gather X times from them (level 55+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Grandiflora Rose and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_grandiflora_rose_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 55 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Grandiflora Rose and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_grandiflora_rose_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 55 else 0,
        ))

        # --- Add 5 Bizet Carnation and gather X times from them (level 20+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Bizet Carnation and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_bizet_carnation_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 20 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Bizet Carnation and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_bizet_carnation_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 20 else 0,
        ))

        # --- Add 5 Domingo Carnation and gather X times from them (level 36+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Domingo Carnation and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_domingo_carnation_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 36 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Domingo Carnation and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_domingo_carnation_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 36 else 0,
        ))

        # --- Add 5 White Liberty Carnation and gather X times from them (level 48+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 White Liberty Carnation and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_white_liberty_carnation_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 48 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 White Liberty Carnation and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_white_liberty_carnation_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 48 else 0,
        ))

        # --- Add 5 Daisy and gather X times from them (level 5+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Daisy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_daisy_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 5 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Daisy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_daisy_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 5 else 0,
        ))

        # --- Add 5 Shasta Daisy and gather X times from them (level 19+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Shasta Daisy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_shasta_daisy_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 19 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Shasta Daisy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_shasta_daisy_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 19 else 0,
        ))

        # --- Add 5 Swan River Daisy and gather X times from them (level 28+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Swan River Daisy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_swan_river_daisy_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 28 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Swan River Daisy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_swan_river_daisy_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 28 else 0,
        ))

        # --- Add 5 Cape Daisy and gather X times from them (level 40+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Cape Daisy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_cape_daisy_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 40 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Cape Daisy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_cape_daisy_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 40 else 0,
        ))

        # --- Add 5 African Daisy and gather X times from them (level 75+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 African Daisy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_african_daisy_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 75 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 African Daisy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_african_daisy_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 75 else 0,
        ))

        # --- Add 5 Sunforest Sunflower and gather X times from them (level 81+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Sunforest Sunflower and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_sunforest_sunflower_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 81 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Sunforest Sunflower and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_sunforest_sunflower_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 81 else 0,
        ))

        # --- Add 5 Earthwalker Sunflower and gather X times from them (level 107+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Earthwalker Sunflower and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_earthwalker_sunflower_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 107 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Earthwalker Sunflower and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_earthwalker_sunflower_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 107 else 0,
        ))

        # --- Add 5 Italian White Sunflower and gather X times from them (level 136+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Italian White Sunflower and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_italian_white_sunflower_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 136 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Italian White Sunflower and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_italian_white_sunflower_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 136 else 0,
        ))

        # --- Add 5 Strawberry Blonde Sunflower and gather X times from them (level 165+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Strawberry Blonde Sunflower and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_strawberry_blonde_sunflower_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 165 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Strawberry Blonde Sunflower and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_strawberry_blonde_sunflower_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 165 else 0,
        ))

        # --- Add 5 China Pink Tulip and gather X times from them (level 9+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 China Pink Tulip and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_china_pink_tulip_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 9 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 China Pink Tulip and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_china_pink_tulip_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 9 else 0,
        ))

        # --- Add 5 Orange Princess Tulip and gather X times from them (level 31+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Orange Princess Tulip and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_orange_princess_tulip_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 31 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Orange Princess Tulip and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_orange_princess_tulip_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 31 else 0,
        ))

        # --- Add 5 Arabian Mystery Tulip and gather X times from them (level 42+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Arabian Mystery Tulip and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_arabian_mystery_tulip_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 42 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Arabian Mystery Tulip and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_arabian_mystery_tulip_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 42 else 0,
        ))

        # --- Add 5 Sevilla Tulip and gather X times from them (level 56+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Sevilla Tulip and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_sevilla_tulip_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 56 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Sevilla Tulip and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_sevilla_tulip_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 56 else 0,
        ))

        # --- Add 5 Blue Diamond Tulips and gather X times from them (level 68+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Blue Diamond Tulips and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_blue_diamond_tulips_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 68 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Blue Diamond Tulips and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_blue_diamond_tulips_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 68 else 0,
        ))

        # --- Add 5 Celestial Morning Glory and gather X times from them (level 49+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Celestial Morning Glory and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_celestial_morning_glory_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 49 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Celestial Morning Glory and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_celestial_morning_glory_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 49 else 0,
        ))

        # --- Add 5 Noah Morning Glory and gather X times from them (level 62+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Noah Morning Glory and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_noah_morning_glory_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 62 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Noah Morning Glory and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_noah_morning_glory_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 62 else 0,
        ))

        # --- Add 5 Silk Morning Glory and gather X times from them (level 77+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Silk Morning Glory and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_silk_morning_glory_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 77 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Silk Morning Glory and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_silk_morning_glory_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 77 else 0,
        ))

        # --- Add 5 Pearly Morning Glory and gather X times from them (level 91+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Pearly Morning Glory and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_pearly_morning_glory_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 91 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Pearly Morning Glory and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_pearly_morning_glory_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 91 else 0,
        ))

        # --- Add 5 Poppy and gather X times from them (level 33+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Poppy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_poppy_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 33 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Poppy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_poppy_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 33 else 0,
        ))

        # --- Add 5 Iceland Poppy and gather X times from them (level 42+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Iceland Poppy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_iceland_poppy_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 42 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Iceland Poppy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_iceland_poppy_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 42 else 0,
        ))

        # --- Add 5 California Poppy and gather X times from them (level 57+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 California Poppy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_california_poppy_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 57 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 California Poppy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_california_poppy_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 57 else 0,
        ))

        # --- Add 5 Arabian Poppy and gather X times from them (level 66+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Arabian Poppy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_arabian_poppy_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 66 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Arabian Poppy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_arabian_poppy_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 66 else 0,
        ))

        # --- Add 5 Flanders Poppy and gather X times from them (level 82+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Flanders Poppy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_flanders_poppy_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 82 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Flanders Poppy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_flanders_poppy_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 82 else 0,
        ))

        # --- Add 5 Lauren's Grape Poppy and gather X times from them (level 197+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Lauren's Grape Poppy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_lauren_s_grape_poppy_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 197 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Lauren's Grape Poppy and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_lauren_s_grape_poppy_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 197 else 0,
        ))

        # --- Add 5 Caldera Red Geranium and gather X times from them (level 71+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Caldera Red Geranium and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_caldera_red_geranium_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 71 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Caldera Red Geranium and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_caldera_red_geranium_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 71 else 0,
        ))

        # --- Add 5 Cranesbill Geranium and gather X times from them (level 92+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Cranesbill Geranium and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_cranesbill_geranium_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 92 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Cranesbill Geranium and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_cranesbill_geranium_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 92 else 0,
        ))

        # --- Add 5 Horizon White Geranium and gather X times from them (level 109+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Horizon White Geranium and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_horizon_white_geranium_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 109 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Horizon White Geranium and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_horizon_white_geranium_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 109 else 0,
        ))

        # --- Add 5 Blue Sky Noon Geranium and gather X times from them (level 142+) ---
        templates.append(GameObjectiveTemplate(
            label="Add 5 Blue Sky Noon Geranium and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_blue_sky_noon_geranium_normal, 1)},
            is_time_consuming=False,
            is_difficult=False,
            weight=1 if self.farm_level >= 142 else 0,
        ))
        templates.append(GameObjectiveTemplate(
            label="Add 5 Blue Sky Noon Geranium and gather AMOUNT times from them",
            data={"AMOUNT": (self.amounts_blue_sky_noon_geranium_tc, 1)},
            is_time_consuming=True,
            is_difficult=False,
            weight=1 if self.farm_level >= 142 else 0,
        ))

        return templates

    # -------------------------------------------------------------------------
    # Helpers
    # -------------------------------------------------------------------------

    @property
    def farm_level(self) -> int:
        return self.archipelago_options.farm_together_2_farm_level.value

    @staticmethod
    def _amount_range(min_val: int, max_val: int, max_tc: int) -> List[int]:
        """
        If max_tc <= 24: every integer from min_val to max_val.
        Otherwise: min_val, next multiple of 10, steps of 10, max_val.
        """
        if min_val >= max_val:
            return [min_val]
        if max_tc <= 24:
            return list(range(min_val, max_val + 1))
        result = [min_val]
        first_step = ((min_val // 10) + 1) * 10
        if first_step < max_val:
            result.append(first_step)
            current = first_step + 10
            while current < max_val:
                result.append(current)
                current += 10
        result.append(max_val)
        return result

    # -------------------------------------------------------------------------
    # Amount pools
    # -------------------------------------------------------------------------

    def amounts_lettuce_normal(self) -> List[int]:
        return [17, 20, 30, 40, 50, 60, 70, 80, 90, 99]

    def amounts_lettuce_tc(self) -> List[int]:
        return [17, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 792]

    def amounts_purple_sweet_asparagus_normal(self) -> List[int]:
        return [15, 20, 30, 40, 50, 60, 70, 80, 89]

    def amounts_purple_sweet_asparagus_tc(self) -> List[int]:
        return [15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710]

    def amounts_lombardy_cabbage_normal(self) -> List[int]:
        return [24, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 143]

    def amounts_lombardy_cabbage_tc(self) -> List[int]:
        return [24, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140]

    def amounts_green_cabbage_normal(self) -> List[int]:
        return [3, 10, 17]

    def amounts_green_cabbage_tc(self) -> List[int]:
        return [3, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 134]

    def amounts_savoy_cabbage_normal(self) -> List[int]:
        return [5, 10, 20, 29]

    def amounts_savoy_cabbage_tc(self) -> List[int]:
        return [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 228]

    def amounts_napa_cabbage_normal(self) -> List[int]:
        return [47, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 279]

    def amounts_napa_cabbage_tc(self) -> List[int]:
        return [47, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440, 1450, 1460, 1470, 1480, 1490, 1500, 1510, 1520, 1530, 1540, 1550, 1560, 1570, 1580, 1590, 1600, 1610, 1620, 1630, 1640, 1650, 1660, 1670, 1680, 1690, 1700, 1710, 1720, 1730, 1740, 1750, 1760, 1770, 1780, 1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100, 2110, 2120, 2130, 2140, 2150, 2160, 2170, 2180, 2190, 2200, 2210, 2220, 2230, 2232]

    def amounts_common_spinach_tc(self) -> List[int]:
        return [1, 10, 20, 26]

    def amounts_red_spinach_tc(self) -> List[int]:
        return [1, 10, 20, 29]

    def amounts_level1_silver_quest_normal(self) -> List[int]:
        return [1, 2]

    def amounts_level1_silver_quest_tc(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_level2_silver_quest_normal(self) -> List[int]:
        return [1]

    def amounts_level2_silver_quest_tc(self) -> List[int]:
        return [1, 2, 3]

    def amounts_level3_silver_quest_normal(self) -> List[int]:
        return [1]

    def amounts_level3_silver_quest_tc(self) -> List[int]:
        return [1, 2]

    def amounts_level4_silver_quest_tc(self) -> List[int]:
        return [1, 2]

    def amounts_npc_requests_normal(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_npc_requests_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    def amounts_corn_normal(self) -> List[int]:
        return [6, 10, 20, 30, 33]

    def amounts_corn_tc(self) -> List[int]:
        return [6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 264]

    def amounts_junin_corn_normal(self) -> List[int]:
        return [11, 20, 30, 40, 50, 60, 63]

    def amounts_junin_corn_tc(self) -> List[int]:
        return [11, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 504]

    def amounts_strawberry_red_corn_normal(self) -> List[int]:
        return [12, 20, 30, 40, 50, 60, 70, 74]

    def amounts_strawberry_red_corn_tc(self) -> List[int]:
        return [12, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 588]

    def amounts_wheat_normal(self) -> List[int]:
        return [4, 10, 20, 26]

    def amounts_wheat_tc(self) -> List[int]:
        return [4, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 211]

    def amounts_rye_normal(self) -> List[int]:
        return [4, 10, 20, 23]

    def amounts_rye_tc(self) -> List[int]:
        return [4, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 185]

    def amounts_barley_normal(self) -> List[int]:
        return [6, 10, 20, 30, 36]

    def amounts_barley_tc(self) -> List[int]:
        return [6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 288]

    def amounts_arborio_rice_normal(self) -> List[int]:
        return [7, 10, 20, 30, 40, 43]

    def amounts_arborio_rice_tc(self) -> List[int]:
        return [7, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 343]

    def amounts_basmati_rice_normal(self) -> List[int]:
        return [7, 10, 20, 30, 40, 41]

    def amounts_basmati_rice_tc(self) -> List[int]:
        return [7, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 329]

    def amounts_black_japonica_rice_normal(self) -> List[int]:
        return [9, 10, 20, 30, 40, 50, 56]

    def amounts_black_japonica_rice_tc(self) -> List[int]:
        return [9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 448]

    def amounts_carrot_normal(self) -> List[int]:
        return [11, 20, 30, 40, 50, 60, 66]

    def amounts_carrot_tc(self) -> List[int]:
        return [11, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 528]

    def amounts_cosmic_purple_carrot_normal(self) -> List[int]:
        return [19, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 112]

    def amounts_cosmic_purple_carrot_tc(self) -> List[int]:
        return [19, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 893]

    def amounts_kyoto_carrot_normal(self) -> List[int]:
        return [32, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 189]

    def amounts_kyoto_carrot_tc(self) -> List[int]:
        return [32, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440, 1450, 1460, 1470, 1480, 1490, 1500, 1510, 1512]

    def amounts_lobbericher_carrot_normal(self) -> List[int]:
        return [60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360]

    def amounts_lobbericher_carrot_tc(self) -> List[int]:
        return [60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440, 1450, 1460, 1470, 1480, 1490, 1500, 1510, 1520, 1530, 1540, 1550, 1560, 1570, 1580, 1590, 1600, 1610, 1620, 1630, 1640, 1650, 1660, 1670, 1680, 1690, 1700, 1710, 1720, 1730, 1740, 1750, 1760, 1770, 1780, 1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100, 2110, 2120, 2130, 2140, 2150, 2160, 2170, 2180, 2190, 2200, 2210, 2220, 2230, 2240, 2250, 2260, 2270, 2280, 2290, 2300, 2310, 2320, 2330, 2340, 2350, 2360, 2370, 2380, 2390, 2400, 2410, 2420, 2430, 2440, 2450, 2460, 2470, 2480, 2490, 2500, 2510, 2520, 2530, 2540, 2550, 2560, 2570, 2580, 2590, 2600, 2610, 2620, 2630, 2640, 2650, 2660, 2670, 2680, 2690, 2700, 2710, 2720, 2730, 2740, 2750, 2760, 2770, 2780, 2790, 2800, 2810, 2820, 2830, 2840, 2850, 2860, 2870, 2880]

    def amounts_lunar_white_carrot_normal(self) -> List[int]:
        return [74, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 446]

    def amounts_lunar_white_carrot_tc(self) -> List[int]:
        return [74, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440, 1450, 1460, 1470, 1480, 1490, 1500, 1510, 1520, 1530, 1540, 1550, 1560, 1570, 1580, 1590, 1600, 1610, 1620, 1630, 1640, 1650, 1660, 1670, 1680, 1690, 1700, 1710, 1720, 1730, 1740, 1750, 1760, 1770, 1780, 1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100, 2110, 2120, 2130, 2140, 2150, 2160, 2170, 2180, 2190, 2200, 2210, 2220, 2230, 2240, 2250, 2260, 2270, 2280, 2290, 2300, 2310, 2320, 2330, 2340, 2350, 2360, 2370, 2380, 2390, 2400, 2410, 2420, 2430, 2440, 2450, 2460, 2470, 2480, 2490, 2500, 2510, 2520, 2530, 2540, 2550, 2560, 2570, 2580, 2590, 2600, 2610, 2620, 2630, 2640, 2650, 2660, 2670, 2680, 2690, 2700, 2710, 2720, 2730, 2740, 2750, 2760, 2770, 2780, 2790, 2800, 2810, 2820, 2830, 2840, 2850, 2860, 2870, 2880, 2890, 2900, 2910, 2920, 2930, 2940, 2950, 2960, 2970, 2980, 2990, 3000, 3010, 3020, 3030, 3040, 3050, 3060, 3070, 3080, 3090, 3100, 3110, 3120, 3130, 3140, 3150, 3160, 3170, 3180, 3190, 3200, 3210, 3220, 3230, 3240, 3250, 3260, 3270, 3280, 3290, 3300, 3310, 3320, 3330, 3340, 3350, 3360, 3370, 3380, 3390, 3400, 3410, 3420, 3430, 3440, 3450, 3460, 3470, 3480, 3490, 3500, 3510, 3520, 3530, 3540, 3550, 3560, 3564]

    def amounts_beet_normal(self) -> List[int]:
        return [9, 10, 20, 30, 40, 50, 54]

    def amounts_beet_tc(self) -> List[int]:
        return [9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 432]

    def amounts_golden_beet_normal(self) -> List[int]:
        return [2, 9]

    def amounts_golden_beet_tc(self) -> List[int]:
        return [2, 10, 20, 30, 40, 50, 60, 70, 74]

    def amounts_turnip_normal(self) -> List[int]:
        return [2, 10, 12]

    def amounts_turnip_tc(self) -> List[int]:
        return [2, 10, 20, 30, 40, 50, 60, 70, 80, 90, 98]

    def amounts_potato_normal(self) -> List[int]:
        return [5, 10, 20, 29]

    def amounts_potato_tc(self) -> List[int]:
        return [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 234]

    def amounts_carolina_potato_normal(self) -> List[int]:
        return [12, 20, 30, 40, 50, 60, 70, 72]

    def amounts_carolina_potato_tc(self) -> List[int]:
        return [12, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 576]

    def amounts_vitelotte_potato_normal(self) -> List[int]:
        return [12, 20, 30, 40, 50, 60, 70, 74]

    def amounts_vitelotte_potato_tc(self) -> List[int]:
        return [12, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 592]

    def amounts_zucchini_normal(self) -> List[int]:
        return [14, 20, 30, 40, 50, 60, 70, 80, 84]

    def amounts_zucchini_tc(self) -> List[int]:
        return [14, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 672]

    def amounts_lodge_zucchini_normal(self) -> List[int]:
        return [33, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

    def amounts_lodge_zucchini_tc(self) -> List[int]:
        return [33, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440, 1450, 1460, 1470, 1480, 1490, 1500, 1510, 1520, 1530, 1540, 1550, 1560, 1570, 1580, 1590, 1600]

    def amounts_cucumber_normal(self) -> List[int]:
        return [5, 10, 20, 30]

    def amounts_cucumber_tc(self) -> List[int]:
        return [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240]

    def amounts_pumpkin_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def amounts_acorn_pumpkin_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    def amounts_baby_boo_pumpkin_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

    def amounts_eggplant_tc(self) -> List[int]:
        return [1, 10, 20, 28]

    def amounts_chinese_eggplant_tc(self) -> List[int]:
        return [1, 10, 20, 30, 38]

    def amounts_albino_eggplant_tc(self) -> List[int]:
        return [1, 10, 20, 30, 40, 49]

    def amounts_jersey_asparagus_normal(self) -> List[int]:
        return [16, 20, 30, 40, 50, 60, 70, 80, 90, 94]

    def amounts_jersey_asparagus_tc(self) -> List[int]:
        return [16, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750]

    def amounts_mary_washington_asparagus_tc(self) -> List[int]:
        return [15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 724]

    def amounts_lentil_normal(self) -> List[int]:
        return [3, 10, 16]

    def amounts_lentil_tc(self) -> List[int]:
        return [3, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 126]

    def amounts_chickpea_normal(self) -> List[int]:
        return [3, 10, 18]

    def amounts_chickpea_tc(self) -> List[int]:
        return [3, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 144]

    def amounts_white_garlic_normal(self) -> List[int]:
        return [4, 10, 20, 25]

    def amounts_white_garlic_tc(self) -> List[int]:
        return [4, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 201]

    def amounts_red_garlic_normal(self) -> List[int]:
        return [6, 10, 20, 30, 34]

    def amounts_red_garlic_tc(self) -> List[int]:
        return [6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270]

    def amounts_black_garlic_normal(self) -> List[int]:
        return [7, 10, 20, 30, 40, 42]

    def amounts_black_garlic_tc(self) -> List[int]:
        return [7, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 339]

    def amounts_french_bean_normal(self) -> List[int]:
        return [41, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 245]

    def amounts_french_bean_tc(self) -> List[int]:
        return [41, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440, 1450, 1460, 1470, 1480, 1490, 1500, 1510, 1520, 1530, 1540, 1550, 1560, 1570, 1580, 1590, 1600, 1610, 1620, 1630, 1640, 1650, 1660, 1670, 1680, 1690, 1700, 1710, 1720, 1730, 1740, 1750, 1760, 1770, 1780, 1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1962]

    def amounts_soy_bean_normal(self) -> List[int]:
        return [43, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 256]

    def amounts_soy_bean_tc(self) -> List[int]:
        return [43, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440, 1450, 1460, 1470, 1480, 1490, 1500, 1510, 1520, 1530, 1540, 1550, 1560, 1570, 1580, 1590, 1600, 1610, 1620, 1630, 1640, 1650, 1660, 1670, 1680, 1690, 1700, 1710, 1720, 1730, 1740, 1750, 1760, 1770, 1780, 1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2048]

    def amounts_hyacinth_bean_normal(self) -> List[int]:
        return [61, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 368]

    def amounts_hyacinth_bean_tc(self) -> List[int]:
        return [61, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440, 1450, 1460, 1470, 1480, 1490, 1500, 1510, 1520, 1530, 1540, 1550, 1560, 1570, 1580, 1590, 1600, 1610, 1620, 1630, 1640, 1650, 1660, 1670, 1680, 1690, 1700, 1710, 1720, 1730, 1740, 1750, 1760, 1770, 1780, 1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100, 2110, 2120, 2130, 2140, 2150, 2160, 2170, 2180, 2190, 2200, 2210, 2220, 2230, 2240, 2250, 2260, 2270, 2280, 2290, 2300, 2310, 2320, 2330, 2340, 2350, 2360, 2370, 2380, 2390, 2400, 2410, 2420, 2430, 2440, 2450, 2460, 2470, 2480, 2490, 2500, 2510, 2520, 2530, 2540, 2550, 2560, 2570, 2580, 2590, 2600, 2610, 2620, 2630, 2640, 2650, 2660, 2670, 2680, 2690, 2700, 2710, 2720, 2730, 2740, 2750, 2760, 2770, 2780, 2790, 2800, 2810, 2820, 2830, 2840, 2850, 2860, 2870, 2880, 2890, 2900, 2910, 2920, 2930, 2940, 2942]

    def amounts_broad_bean_normal(self) -> List[int]:
        return [88, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 525]

    def amounts_broad_bean_tc(self) -> List[int]:
        return [88, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440, 1450, 1460, 1470, 1480, 1490, 1500, 1510, 1520, 1530, 1540, 1550, 1560, 1570, 1580, 1590, 1600, 1610, 1620, 1630, 1640, 1650, 1660, 1670, 1680, 1690, 1700, 1710, 1720, 1730, 1740, 1750, 1760, 1770, 1780, 1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100, 2110, 2120, 2130, 2140, 2150, 2160, 2170, 2180, 2190, 2200, 2210, 2220, 2230, 2240, 2250, 2260, 2270, 2280, 2290, 2300, 2310, 2320, 2330, 2340, 2350, 2360, 2370, 2380, 2390, 2400, 2410, 2420, 2430, 2440, 2450, 2460, 2470, 2480, 2490, 2500, 2510, 2520, 2530, 2540, 2550, 2560, 2570, 2580, 2590, 2600, 2610, 2620, 2630, 2640, 2650, 2660, 2670, 2680, 2690, 2700, 2710, 2720, 2730, 2740, 2750, 2760, 2770, 2780, 2790, 2800, 2810, 2820, 2830, 2840, 2850, 2860, 2870, 2880, 2890, 2900, 2910, 2920, 2930, 2940, 2950, 2960, 2970, 2980, 2990, 3000, 3010, 3020, 3030, 3040, 3050, 3060, 3070, 3080, 3090, 3100, 3110, 3120, 3130, 3140, 3150, 3160, 3170, 3180, 3190, 3200, 3210, 3220, 3230, 3240, 3250, 3260, 3270, 3280, 3290, 3300, 3310, 3320, 3330, 3340, 3350, 3360, 3370, 3380, 3390, 3400, 3410, 3420, 3430, 3440, 3450, 3460, 3470, 3480, 3490, 3500, 3510, 3520, 3530, 3540, 3550, 3560, 3570, 3580, 3590, 3600, 3610, 3620, 3630, 3640, 3650, 3660, 3670, 3680, 3690, 3700, 3710, 3720, 3730, 3740, 3750, 3760, 3770, 3780, 3790, 3800, 3810, 3820, 3830, 3840, 3850, 3860, 3870, 3880, 3890, 3900, 3910, 3920, 3930, 3940, 3950, 3960, 3970, 3980, 3990, 4000, 4010, 4020, 4030, 4040, 4050, 4060, 4070, 4080, 4090, 4100, 4110, 4120, 4130, 4140, 4150, 4160, 4170, 4180, 4190, 4200]

    def amounts_tomato_normal(self) -> List[int]:
        return [4, 10, 20, 26]

    def amounts_tomato_tc(self) -> List[int]:
        return [4, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 204]

    def amounts_honeycomb_tomato_normal(self) -> List[int]:
        return [6, 10, 20, 30, 34]

    def amounts_honeycomb_tomato_tc(self) -> List[int]:
        return [6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 272]

    def amounts_cherokee_tomato_normal(self) -> List[int]:
        return [8, 10, 20, 30, 40, 50]

    def amounts_cherokee_tomato_tc(self) -> List[int]:
        return [8, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 403]

    def amounts_beefsteak_tomato_normal(self) -> List[int]:
        return [5, 10, 20, 29]

    def amounts_beefsteak_tomato_tc(self) -> List[int]:
        return [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 236]

    def amounts_yellow_beefsteak_tomato_normal(self) -> List[int]:
        return [6, 10, 20, 30, 38]

    def amounts_yellow_beefsteak_tomato_tc(self) -> List[int]:
        return [6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 302]

    def amounts_black_beefsteak_tomato_normal(self) -> List[int]:
        return [6, 10, 20, 30, 35]

    def amounts_black_beefsteak_tomato_tc(self) -> List[int]:
        return [6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 282]

    def amounts_cherry_tomato_normal(self) -> List[int]:
        return [12, 20, 30, 40, 50, 60, 69]

    def amounts_cherry_tomato_tc(self) -> List[int]:
        return [12, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 552]

    def amounts_yellow_cherry_tomato_normal(self) -> List[int]:
        return [12, 20, 30, 40, 50, 60, 70, 71]

    def amounts_yellow_cherry_tomato_tc(self) -> List[int]:
        return [12, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 566]

    def amounts_black_cherry_tomato_normal(self) -> List[int]:
        return [14, 20, 30, 40, 50, 60, 70, 80, 84]

    def amounts_black_cherry_tomato_tc(self) -> List[int]:
        return [14, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 675]

    def amounts_red_pepper_normal(self) -> List[int]:
        return [9, 10, 20, 30, 40, 50, 56]

    def amounts_red_pepper_tc(self) -> List[int]:
        return [9, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450]

    def amounts_yellow_pepper_normal(self) -> List[int]:
        return [5, 10, 20, 29]

    def amounts_yellow_pepper_tc(self) -> List[int]:
        return [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 234]

    def amounts_green_pepper_normal(self) -> List[int]:
        return [11, 20, 30, 40, 50, 60, 65]

    def amounts_green_pepper_tc(self) -> List[int]:
        return [11, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 518]

    def amounts_spanish_peanut_normal(self) -> List[int]:
        return [6, 10, 20, 30, 36]

    def amounts_spanish_peanut_tc(self) -> List[int]:
        return [6, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 288]

    def amounts_virginia_peanut_normal(self) -> List[int]:
        return [55, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330]

    def amounts_virginia_peanut_tc(self) -> List[int]:
        return [55, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440, 1450, 1460, 1470, 1480, 1490, 1500, 1510, 1520, 1530, 1540, 1550, 1560, 1570, 1580, 1590, 1600, 1610, 1620, 1630, 1640, 1650, 1660, 1670, 1680, 1690, 1700, 1710, 1720, 1730, 1740, 1750, 1760, 1770, 1780, 1790, 1800, 1810, 1820, 1830, 1840, 1850, 1860, 1870, 1880, 1890, 1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020, 2030, 2040, 2050, 2060, 2070, 2080, 2090, 2100, 2110, 2120, 2130, 2140, 2150, 2160, 2170, 2180, 2190, 2200, 2210, 2220, 2230, 2240, 2250, 2260, 2270, 2280, 2290, 2300, 2310, 2320, 2330, 2340, 2350, 2360, 2370, 2380, 2390, 2400, 2410, 2420, 2430, 2440, 2450, 2460, 2470, 2480, 2490, 2500, 2510, 2520, 2530, 2540, 2550, 2560, 2570, 2580, 2590, 2600, 2610, 2620, 2630, 2640]

    def amounts_melon_normal(self) -> List[int]:
        return [3, 10, 20]

    def amounts_melon_tc(self) -> List[int]:
        return [3, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]

    def amounts_watermelon_normal(self) -> List[int]:
        return [3, 10, 15]

    def amounts_watermelon_tc(self) -> List[int]:
        return [3, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

    def amounts_canary_melon_normal(self) -> List[int]:
        return [38, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230]

    def amounts_canary_melon_tc(self) -> List[int]:
        return [38, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400, 410, 420, 430, 440, 450, 460, 470, 480, 490, 500, 510, 520, 530, 540, 550, 560, 570, 580, 590, 600, 610, 620, 630, 640, 650, 660, 670, 680, 690, 700, 710, 720, 730, 740, 750, 760, 770, 780, 790, 800, 810, 820, 830, 840, 850, 860, 870, 880, 890, 900, 910, 920, 930, 940, 950, 960, 970, 980, 990, 1000, 1010, 1020, 1030, 1040, 1050, 1060, 1070, 1080, 1090, 1100, 1110, 1120, 1130, 1140, 1150, 1160, 1170, 1180, 1190, 1200, 1210, 1220, 1230, 1240, 1250, 1260, 1270, 1280, 1290, 1300, 1310, 1320, 1330, 1340, 1350, 1360, 1370, 1380, 1390, 1400, 1410, 1420, 1430, 1440, 1450, 1460, 1470, 1480, 1490, 1500, 1510, 1520, 1530, 1540, 1550, 1560, 1570, 1580, 1590, 1600, 1610, 1620, 1630, 1640, 1650, 1660, 1670, 1680, 1690, 1700, 1710, 1720, 1730, 1740, 1750, 1760, 1770, 1780, 1790, 1800, 1810, 1820, 1830, 1836]

    def amounts_cantaloupe_melon_normal(self) -> List[int]:
        return [2, 10, 13]

    def amounts_cantaloupe_melon_tc(self) -> List[int]:
        return [2, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 102]

    def amounts_concord_grape_normal(self) -> List[int]:
        return [1, 9]

    def amounts_concord_grape_tc(self) -> List[int]:
        return [1, 10, 20, 30, 40, 50, 60, 70]

    def amounts_thompson_grape_normal(self) -> List[int]:
        return [2, 10, 11]

    def amounts_thompson_grape_tc(self) -> List[int]:
        return [2, 10, 20, 30, 40, 50, 60, 70, 80, 88]

    def amounts_cabernet_grape_normal(self) -> List[int]:
        return [2, 10, 12]

    def amounts_cabernet_grape_tc(self) -> List[int]:
        return [2, 10, 20, 30, 40, 50, 60, 70, 80, 90, 99]

    def amounts_crimson_grape_normal(self) -> List[int]:
        return [2, 10, 14]

    def amounts_crimson_grape_tc(self) -> List[int]:
        return [2, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 113]

    def amounts_strawberry_normal(self) -> List[int]:
        return [1, 7]

    def amounts_strawberry_tc(self) -> List[int]:
        return [1, 10, 20, 30, 40, 50, 58]

    def amounts_pineberry_normal(self) -> List[int]:
        return [2, 10, 11]

    def amounts_pineberry_tc(self) -> List[int]:
        return [2, 10, 20, 30, 40, 50, 60, 70, 80, 90, 92]

    def amounts_black_peppercorn_tc(self) -> List[int]:
        return [2, 10, 20, 30, 40, 50, 60, 70, 80, 90]

    def amounts_green_peppercorn_tc(self) -> List[int]:
        return [2, 10, 20, 30, 40, 50, 60, 70, 80, 83]

    def amounts_pink_peppercorn_tc(self) -> List[int]:
        return [2, 10, 20, 30, 40, 50, 60, 70, 80, 82]

    def amounts_flat_parsley_normal(self) -> List[int]:
        return [3, 10, 20]

    def amounts_flat_parsley_tc(self) -> List[int]:
        return [3, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 162]

    def amounts_curley_parsley_normal(self) -> List[int]:
        return [4, 10, 20, 23]

    def amounts_curley_parsley_tc(self) -> List[int]:
        return [4, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180]

    def amounts_coriander_normal(self) -> List[int]:
        return [5, 10, 20, 30, 33]

    def amounts_coriander_tc(self) -> List[int]:
        return [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260]

    def amounts_gold_pineapple_normal(self) -> List[int]:
        return [4, 10, 20, 24]

    def amounts_gold_pineapple_tc(self) -> List[int]:
        return [4, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 192]

    def amounts_mauritius_pineapple_normal(self) -> List[int]:
        return [4, 10, 20, 23]

    def amounts_mauritius_pineapple_tc(self) -> List[int]:
        return [4, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 182]

    def amounts_red_pineapple_normal(self) -> List[int]:
        return [4, 10, 20, 23]

    def amounts_red_pineapple_tc(self) -> List[int]:
        return [4, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 182]

    def amounts_apple_normal(self) -> List[int]:
        return [20, 30, 40, 50, 60, 70, 80]

    def amounts_apple_tc(self) -> List[int]:
        return [20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300, 310, 320, 330, 340, 350, 360, 370, 380, 390, 400]

    def amounts_royal_gala_apple_normal(self) -> List[int]:
        return [10, 20, 30, 40]

    def amounts_royal_gala_apple_tc(self) -> List[int]:
        return [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

    def amounts_reinette_apple_normal(self) -> List[int]:
        return [10, 20, 30, 40]

    def amounts_reinette_apple_tc(self) -> List[int]:
        return [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

    def amounts_granny_smith_apple_normal(self) -> List[int]:
        return [10, 20, 30, 40]

    def amounts_granny_smith_apple_tc(self) -> List[int]:
        return [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

    def amounts_golden_apple_normal(self) -> List[int]:
        return [5, 10, 20]

    def amounts_golden_apple_tc(self) -> List[int]:
        return [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    def amounts_lemon_normal(self) -> List[int]:
        return [10, 20, 30, 40]

    def amounts_lemon_tc(self) -> List[int]:
        return [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

    def amounts_orange_normal(self) -> List[int]:
        return [15, 20, 30, 40, 50, 60]

    def amounts_orange_tc(self) -> List[int]:
        return [15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]

    def amounts_lime_normal(self) -> List[int]:
        return [15, 20, 30, 40, 50, 60]

    def amounts_lime_tc(self) -> List[int]:
        return [15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]

    def amounts_tangerine_normal(self) -> List[int]:
        return [10, 20, 30, 40]

    def amounts_tangerine_tc(self) -> List[int]:
        return [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

    def amounts_yuzu_normal(self) -> List[int]:
        return [10, 20, 30, 40]

    def amounts_yuzu_tc(self) -> List[int]:
        return [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

    def amounts_blood_tangerine_normal(self) -> List[int]:
        return [15, 20, 30, 40, 50, 60]

    def amounts_blood_tangerine_tc(self) -> List[int]:
        return [15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]

    def amounts_pear_normal(self) -> List[int]:
        return [5, 10, 20]

    def amounts_pear_tc(self) -> List[int]:
        return [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    def amounts_peach_normal(self) -> List[int]:
        return [10, 20, 30, 40]

    def amounts_peach_tc(self) -> List[int]:
        return [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

    def amounts_apricot_normal(self) -> List[int]:
        return [10, 20, 30, 40]

    def amounts_apricot_tc(self) -> List[int]:
        return [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

    def amounts_prickly_pear_normal(self) -> List[int]:
        return [10, 20, 30, 40]

    def amounts_prickly_pear_tc(self) -> List[int]:
        return [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

    def amounts_plum_normal(self) -> List[int]:
        return [5, 10, 20]

    def amounts_plum_tc(self) -> List[int]:
        return [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    def amounts_quince_normal(self) -> List[int]:
        return [5, 10, 20]

    def amounts_quince_tc(self) -> List[int]:
        return [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    def amounts_wonderful_pomegranate_normal(self) -> List[int]:
        return [10, 20, 30, 40]

    def amounts_wonderful_pomegranate_tc(self) -> List[int]:
        return [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

    def amounts_purple_heart_pomegranate_normal(self) -> List[int]:
        return [10, 20, 30, 40]

    def amounts_purple_heart_pomegranate_tc(self) -> List[int]:
        return [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200]

    def amounts_haku_botan_pomegranate_normal(self) -> List[int]:
        return [15, 20, 30, 40, 50, 60]

    def amounts_haku_botan_pomegranate_tc(self) -> List[int]:
        return [15, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190, 200, 210, 220, 230, 240, 250, 260, 270, 280, 290, 300]

    def amounts_leghorn_chicken_normal(self) -> List[int]:
        return [3, 4, 5, 6, 7, 8, 9]

    def amounts_leghorn_chicken_tc(self) -> List[int]:
        return [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

    def amounts_new_hampshire_chicken_normal(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_new_hampshire_chicken_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def amounts_australorp_chicken_normal(self) -> List[int]:
        return [1, 2, 3]

    def amounts_australorp_chicken_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def amounts_jersey_giant_chicken_normal(self) -> List[int]:
        return [1, 2]

    def amounts_jersey_giant_chicken_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8]

    def amounts_orpington_chicken_normal(self) -> List[int]:
        return [1, 2]

    def amounts_orpington_chicken_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6]

    def amounts_serama_bantam_chicken_normal(self) -> List[int]:
        return [2, 3, 4, 5, 6]

    def amounts_serama_bantam_chicken_tc(self) -> List[int]:
        return [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    def amounts_landrace_pig_normal(self) -> List[int]:
        return [1, 2, 3]

    def amounts_landrace_pig_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def amounts_hampshire_pig_normal(self) -> List[int]:
        return [1, 2]

    def amounts_hampshire_pig_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8]

    def amounts_large_black_pig_normal(self) -> List[int]:
        return [1]

    def amounts_large_black_pig_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5]

    def amounts_hereford_pig_normal(self) -> List[int]:
        return [1, 2]

    def amounts_hereford_pig_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6]

    def amounts_duroc_pig_normal(self) -> List[int]:
        return [1, 2]

    def amounts_duroc_pig_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8]

    def amounts_kunekune_pig_normal(self) -> List[int]:
        return [1, 2, 3]

    def amounts_kunekune_pig_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def amounts_holstein_cow_normal(self) -> List[int]:
        return [1]

    def amounts_holstein_cow_tc(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_jersey_cow_normal(self) -> List[int]:
        return [1]

    def amounts_jersey_cow_tc(self) -> List[int]:
        return [1, 2, 3]

    def amounts_belted_cow_normal(self) -> List[int]:
        return [1]

    def amounts_belted_cow_tc(self) -> List[int]:
        return [1, 2, 3]

    def amounts_ayrshire_cow_normal(self) -> List[int]:
        return [1]

    def amounts_ayrshire_cow_tc(self) -> List[int]:
        return [1, 2, 3]

    def amounts_girolando_cow_normal(self) -> List[int]:
        return [1]

    def amounts_girolando_cow_tc(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_tyrol_grey_cow_normal(self) -> List[int]:
        return [1]

    def amounts_tyrol_grey_cow_tc(self) -> List[int]:
        return [1, 2, 3]

    def amounts_alpine_goat_normal(self) -> List[int]:
        return [1]

    def amounts_alpine_goat_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5]

    def amounts_black_bengal_goat_normal(self) -> List[int]:
        return [1]

    def amounts_black_bengal_goat_tc(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_saanen_goat_normal(self) -> List[int]:
        return [1]

    def amounts_saanen_goat_tc(self) -> List[int]:
        return [1, 2, 3]

    def amounts_australian_brown_goat_normal(self) -> List[int]:
        return [1]

    def amounts_australian_brown_goat_tc(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_nigerian_dwarf_goat_normal(self) -> List[int]:
        return [1]

    def amounts_nigerian_dwarf_goat_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5]

    def amounts_hampshire_sheep_normal(self) -> List[int]:
        return [1]

    def amounts_hampshire_sheep_tc(self) -> List[int]:
        return [1, 2]

    def amounts_merino_sheep_normal(self) -> List[int]:
        return [1]

    def amounts_merino_sheep_tc(self) -> List[int]:
        return [1, 2]

    def amounts_romanov_sheep_normal(self) -> List[int]:
        return [1]

    def amounts_romanov_sheep_tc(self) -> List[int]:
        return [1, 2]

    def amounts_dutch_rabbit_normal(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_dutch_rabbit_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    def amounts_netherland_dwarf_rabbit_normal(self) -> List[int]:
        return [1, 2, 3]

    def amounts_netherland_dwarf_rabbit_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def amounts_alaska_rabbit_normal(self) -> List[int]:
        return [1, 2]

    def amounts_alaska_rabbit_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6]

    def amounts_flemish_giant_rabbit_normal(self) -> List[int]:
        return [1, 2]

    def amounts_flemish_giant_rabbit_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8]

    def amounts_abacot_ranger_duck_normal(self) -> List[int]:
        return [1]

    def amounts_abacot_ranger_duck_tc(self) -> List[int]:
        return [1, 2]

    def amounts_duckling_normal(self) -> List[int]:
        return [1]

    def amounts_duckling_tc(self) -> List[int]:
        return [1, 2]

    def amounts_clownfish_normal(self) -> List[int]:
        return [2, 3, 4]

    def amounts_clownfish_tc(self) -> List[int]:
        return [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    def amounts_amber_clownfish_normal(self) -> List[int]:
        return [2, 3, 4]

    def amounts_amber_clownfish_tc(self) -> List[int]:
        return [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    def amounts_ebony_clownfish_normal(self) -> List[int]:
        return [2, 3, 4]

    def amounts_ebony_clownfish_tc(self) -> List[int]:
        return [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    def amounts_surgeonfish_normal(self) -> List[int]:
        return [1, 2]

    def amounts_surgeonfish_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def amounts_platinum_surgeonfish_normal(self) -> List[int]:
        return [1, 2]

    def amounts_platinum_surgeonfish_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def amounts_bronze_surgeonfish_normal(self) -> List[int]:
        return [1, 2]

    def amounts_bronze_surgeonfish_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def amounts_sardine_normal(self) -> List[int]:
        return [1, 2]

    def amounts_sardine_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8]

    def amounts_pacific_sardinella_normal(self) -> List[int]:
        return [1, 2]

    def amounts_pacific_sardinella_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8]

    def amounts_white_sardine_normal(self) -> List[int]:
        return [2, 3, 4]

    def amounts_white_sardine_tc(self) -> List[int]:
        return [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

    def amounts_salmon_normal(self) -> List[int]:
        return [1]

    def amounts_salmon_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5]

    def amounts_crimson_salmon_normal(self) -> List[int]:
        return [1]

    def amounts_crimson_salmon_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5]

    def amounts_viridian_salmon_normal(self) -> List[int]:
        return [1]

    def amounts_viridian_salmon_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5]

    def amounts_trout_normal(self) -> List[int]:
        return [1]

    def amounts_trout_tc(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_coral_trout_normal(self) -> List[int]:
        return [1]

    def amounts_coral_trout_tc(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_brass_trout_normal(self) -> List[int]:
        return [1]

    def amounts_brass_trout_tc(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_blowfish_normal(self) -> List[int]:
        return [1]

    def amounts_blowfish_tc(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_cocoa_blowfish_normal(self) -> List[int]:
        return [1]

    def amounts_cocoa_blowfish_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6]

    def amounts_cerulean_blowfish_normal(self) -> List[int]:
        return [1]

    def amounts_cerulean_blowfish_tc(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_slinger_seabream_normal(self) -> List[int]:
        return [1]

    def amounts_slinger_seabream_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6]

    def amounts_hottentot_seabream_normal(self) -> List[int]:
        return [1]

    def amounts_hottentot_seabream_tc(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_seventyfour_seabream_normal(self) -> List[int]:
        return [1]

    def amounts_seventyfour_seabream_tc(self) -> List[int]:
        return [1, 2, 3]

    def amounts_swordfish_normal(self) -> List[int]:
        return [1]

    def amounts_swordfish_tc(self) -> List[int]:
        return [1, 2]

    def amounts_topaz_swordfish_normal(self) -> List[int]:
        return [1]

    def amounts_topaz_swordfish_tc(self) -> List[int]:
        return [1, 2]

    def amounts_emerald_swordfish_normal(self) -> List[int]:
        return [1]

    def amounts_emerald_swordfish_tc(self) -> List[int]:
        return [1, 2]

    def amounts_vermillion_snapper_normal(self) -> List[int]:
        return [1]

    def amounts_vermillion_snapper_tc(self) -> List[int]:
        return [1, 2]

    def amounts_black_snapper_normal(self) -> List[int]:
        return [1]

    def amounts_black_snapper_tc(self) -> List[int]:
        return [1, 2]

    def amounts_yellowtail_snapper_normal(self) -> List[int]:
        return [1]

    def amounts_yellowtail_snapper_tc(self) -> List[int]:
        return [1, 2]

    def amounts_ginrin_koi_normal(self) -> List[int]:
        return [1]

    def amounts_ginrin_koi_tc(self) -> List[int]:
        return [1, 2]

    def amounts_utsuri_koi_normal(self) -> List[int]:
        return [1]

    def amounts_utsuri_koi_tc(self) -> List[int]:
        return [1, 2]

    def amounts_rose_normal(self) -> List[int]:
        return [1, 2, 3]

    def amounts_rose_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def amounts_ramanas_rose_normal(self) -> List[int]:
        return [1, 2]

    def amounts_ramanas_rose_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8]

    def amounts_damask_rose_normal(self) -> List[int]:
        return [1]

    def amounts_damask_rose_tc(self) -> List[int]:
        return [1, 2, 3]

    def amounts_provence_rose_normal(self) -> List[int]:
        return [1]

    def amounts_provence_rose_tc(self) -> List[int]:
        return [1, 2]

    def amounts_grandiflora_rose_normal(self) -> List[int]:
        return [1, 2]

    def amounts_grandiflora_rose_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6]

    def amounts_daisy_normal(self) -> List[int]:
        return [1]

    def amounts_daisy_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5]

    def amounts_shasta_daisy_normal(self) -> List[int]:
        return [1]

    def amounts_shasta_daisy_tc(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_cape_daisy_normal(self) -> List[int]:
        return [1]

    def amounts_cape_daisy_tc(self) -> List[int]:
        return [1, 2]

    def amounts_african_daisy_normal(self) -> List[int]:
        return [1, 2]

    def amounts_african_daisy_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6]

    def amounts_sunforest_sunflower_normal(self) -> List[int]:
        return [1]

    def amounts_sunforest_sunflower_tc(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_earthwalker_sunflower_normal(self) -> List[int]:
        return [1]

    def amounts_earthwalker_sunflower_tc(self) -> List[int]:
        return [1, 2]

    def amounts_strawberry_blonde_sunflower_normal(self) -> List[int]:
        return [1]

    def amounts_strawberry_blonde_sunflower_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5]

    def amounts_china_pink_tulip_normal(self) -> List[int]:
        return [1]

    def amounts_china_pink_tulip_tc(self) -> List[int]:
        return [1, 2, 3]

    def amounts_orange_princess_tulip_normal(self) -> List[int]:
        return [1, 2]

    def amounts_orange_princess_tulip_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6]

    def amounts_arabian_mystery_tulip_normal(self) -> List[int]:
        return [1]

    def amounts_arabian_mystery_tulip_tc(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_sevilla_tulip_normal(self) -> List[int]:
        return [1]

    def amounts_sevilla_tulip_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5]

    def amounts_blue_diamond_tulips_normal(self) -> List[int]:
        return [1]

    def amounts_blue_diamond_tulips_tc(self) -> List[int]:
        return [1, 2, 3]

    def amounts_poppy_normal(self) -> List[int]:
        return [1, 2, 3]

    def amounts_poppy_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    def amounts_iceland_poppy_normal(self) -> List[int]:
        return [1]

    def amounts_iceland_poppy_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5]

    def amounts_california_poppy_normal(self) -> List[int]:
        return [1]

    def amounts_california_poppy_tc(self) -> List[int]:
        return [1, 2, 3, 4]

    def amounts_arabian_poppy_normal(self) -> List[int]:
        return [1]

    def amounts_arabian_poppy_tc(self) -> List[int]:
        return [1, 2, 3, 4, 5]

    def amounts_flanders_poppy_normal(self) -> List[int]:
        return [1]

    def amounts_flanders_poppy_tc(self) -> List[int]:
        return [1, 2]

    def amounts_lauren_s_grape_poppy_normal(self) -> List[int]:
        return [1]

    def amounts_lauren_s_grape_poppy_tc(self) -> List[int]:
        return [1, 2, 3]

    def amounts_caldera_red_geranium_normal(self) -> List[int]:
        return [1]

    def amounts_caldera_red_geranium_tc(self) -> List[int]:
        return [1, 2]

    def amounts_cranesbill_geranium_normal(self) -> List[int]:
        return [1]

    def amounts_cranesbill_geranium_tc(self) -> List[int]:
        return [1, 2, 3]

    def amounts_horizon_white_geranium_normal(self) -> List[int]:
        return [1]

    def amounts_horizon_white_geranium_tc(self) -> List[int]:
        return [1, 2]

    def amounts_blue_sky_noon_geranium_normal(self) -> List[int]:
        return [1]

    def amounts_blue_sky_noon_geranium_tc(self) -> List[int]:
        return [1, 2]

    def amounts_gotland_sheep_normal(self) -> List[int]:
        return [1]

    def amounts_gotland_sheep_tc(self) -> List[int]:
        return [1]

    def amounts_jacob_sheep_normal(self) -> List[int]:
        return [1]

    def amounts_jacob_sheep_tc(self) -> List[int]:
        return [1]

    def amounts_suri_alpaca_normal(self) -> List[int]:
        return [1]

    def amounts_suri_alpaca_tc(self) -> List[int]:
        return [1]

    def amounts_huacaya_alpaca_normal(self) -> List[int]:
        return [1]

    def amounts_huacaya_alpaca_tc(self) -> List[int]:
        return [1]

    def amounts_llama_normal(self) -> List[int]:
        return [1]

    def amounts_llama_tc(self) -> List[int]:
        return [1]

    def amounts_pekin_duck_normal(self) -> List[int]:
        return [1]

    def amounts_pekin_duck_tc(self) -> List[int]:
        return [1]

    def amounts_magpie_duck_normal(self) -> List[int]:
        return [1]

    def amounts_magpie_duck_tc(self) -> List[int]:
        return [1]

    def amounts_cayuga_duck_normal(self) -> List[int]:
        return [1]

    def amounts_cayuga_duck_tc(self) -> List[int]:
        return [1]

    def amounts_silver_hake_normal(self) -> List[int]:
        return [1]

    def amounts_silver_hake_tc(self) -> List[int]:
        return [1]

    def amounts_shusui_koi_normal(self) -> List[int]:
        return [1]

    def amounts_shusui_koi_tc(self) -> List[int]:
        return [1]

    def amounts_bizet_carnation_normal(self) -> List[int]:
        return [1]

    def amounts_bizet_carnation_tc(self) -> List[int]:
        return [1]

    def amounts_domingo_carnation_normal(self) -> List[int]:
        return [1]

    def amounts_domingo_carnation_tc(self) -> List[int]:
        return [1]

    def amounts_white_liberty_carnation_normal(self) -> List[int]:
        return [1]

    def amounts_white_liberty_carnation_tc(self) -> List[int]:
        return [1]

    def amounts_swan_river_daisy_normal(self) -> List[int]:
        return [1]

    def amounts_swan_river_daisy_tc(self) -> List[int]:
        return [1]

    def amounts_italian_white_sunflower_normal(self) -> List[int]:
        return [1]

    def amounts_italian_white_sunflower_tc(self) -> List[int]:
        return [1]

    def amounts_celestial_morning_glory_normal(self) -> List[int]:
        return [1]

    def amounts_celestial_morning_glory_tc(self) -> List[int]:
        return [1]

    def amounts_noah_morning_glory_normal(self) -> List[int]:
        return [1]

    def amounts_noah_morning_glory_tc(self) -> List[int]:
        return [1]

    def amounts_silk_morning_glory_normal(self) -> List[int]:
        return [1]

    def amounts_silk_morning_glory_tc(self) -> List[int]:
        return [1]

    def amounts_pearly_morning_glory_normal(self) -> List[int]:
        return [1]

    def amounts_pearly_morning_glory_tc(self) -> List[int]:
        return [1]
