# Dragorrod's Real World Scavenger Hunts
#
# Adapted from "Real-World Scavenger Hunt" (real_world_scavenger_hunt_game.py / ScavengerHuntGame),
# originally written for Keymaster's Keep by its original author. Thank you for the template this
# game is built on!

from __future__ import annotations

from typing import List

from dataclasses import dataclass

from Options import DefaultOnToggle, Toggle

from ..game import Game
from ..game_objective_template import GameObjectiveTemplate

from ..enums import KeymastersKeepGamePlatforms


@dataclass
class DragorrodsRealWorldScavengerHuntsArchipelagoOptions:
    dragorrods_real_world_scavenger_hunts_include_photography: DragorrodsRealWorldScavengerHuntsIncludePhotography
    dragorrods_real_world_scavenger_hunts_include_location_hunting: DragorrodsRealWorldScavengerHuntsIncludeLocationHunting
    dragorrods_real_world_scavenger_hunts_include_object_collection: DragorrodsRealWorldScavengerHuntsIncludeObjectCollection
    dragorrods_real_world_scavenger_hunts_include_interaction_challenges: DragorrodsRealWorldScavengerHuntsIncludeInteractionChallenges
    dragorrods_real_world_scavenger_hunts_include_nature_exploration: DragorrodsRealWorldScavengerHuntsIncludeNatureExploration
    dragorrods_real_world_scavenger_hunts_include_community_engagement: DragorrodsRealWorldScavengerHuntsIncludeCommunityEngagement
    dragorrods_real_world_scavenger_hunts_allow_architecture_style_challenge: DragorrodsRealWorldScavengerHuntsAllowArchitectureStyleChallenge


class DragorrodsRealWorldScavengerHuntsGame(Game):
    name = "Dragorrod's Real World Scavenger Hunts"
    platform = KeymastersKeepGamePlatforms.META

    platforms_other = []

    is_adult_only_or_unrated = False

    options_cls = DragorrodsRealWorldScavengerHuntsArchipelagoOptions

    def optional_game_constraint_templates(self) -> List[GameObjectiveTemplate]:
        constraints = []

        constraints.extend([
            GameObjectiveTemplate(
                label="Complete this objective within LOCATION_TYPE areas only",
                data={"LOCATION_TYPE": (self.location_restrictions, 1)},
                is_time_consuming=False,
                is_difficult=False,
            ),
            GameObjectiveTemplate(
                label="Complete this objective using TRANSPORTATION_METHOD",
                data={"TRANSPORTATION_METHOD": (self.transportation_methods, 1)},
                is_time_consuming=False,
                is_difficult=False,
            ),
            GameObjectiveTemplate(
                label="Complete this objective with COMPANION_TYPE",
                data={"COMPANION_TYPE": (self.companion_types, 1)},
                is_time_consuming=False,
                is_difficult=False,
            ),
            GameObjectiveTemplate(
                label="Complete this objective during WEATHER_CONDITION",
                data={"WEATHER_CONDITION": (self.weather_conditions, 1)},
                is_time_consuming=True,
                is_difficult=False,
            ),
        ])

        return constraints

    def game_objective_templates(self) -> List[GameObjectiveTemplate]:
        game_objective_templates: List[GameObjectiveTemplate] = list()

        # Photography Challenges
        if self.include_photography:
            photo_templates = [
                GameObjectiveTemplate(
                    label="Capture a photo of CHALLENGE_PHOTO during SPECIFIC_TIME",
                    data={
                        "CHALLENGE_PHOTO": (self.challenge_photos, 1),
                        "SPECIFIC_TIME": (self.specific_times, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=True,
                    weight=1,
                ),
            ]

            photo_templates.extend([
                GameObjectiveTemplate(
                    label="Take a photo of PHOTO_SUBJECT",
                    data={"PHOTO_SUBJECT": (self.photo_subjects, 1)},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Create a photo series of SERIES_COUNT PHOTO_THEME photos",
                    data={
                        "SERIES_COUNT": (self.photo_series_counts_normal, 1),
                        "PHOTO_THEME": (self.photo_themes, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Create a photo series of SERIES_COUNT PHOTO_THEME photos",
                    data={
                        "SERIES_COUNT": (self.photo_series_counts_tc, 1),
                        "PHOTO_THEME": (self.photo_themes, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Document COLOR_COUNT different examples of COLOR_TYPE objects",
                    data={
                        "COLOR_COUNT": (self.color_counts_normal, 1),
                        "COLOR_TYPE": (self.colors, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Document COLOR_COUNT different examples of COLOR_TYPE objects",
                    data={
                        "COLOR_COUNT": (self.color_counts_tc, 1),
                        "COLOR_TYPE": (self.colors, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
            ])

            if self.allow_architecture_style_challenge:
                photo_templates.extend([
                    GameObjectiveTemplate(
                        label="Photograph ARCHITECTURE_COUNT different ARCHITECTURE_STYLE buildings",
                        data={
                            "ARCHITECTURE_COUNT": (self.architecture_counts_normal, 1),
                            "ARCHITECTURE_STYLE": (self.architecture_styles, 1)
                        },
                        is_time_consuming=False,
                        is_difficult=False,
                        weight=4,
                    ),
                    GameObjectiveTemplate(
                        label="Photograph ARCHITECTURE_COUNT different ARCHITECTURE_STYLE buildings",
                        data={
                            "ARCHITECTURE_COUNT": (self.architecture_counts_tc, 1),
                            "ARCHITECTURE_STYLE": (self.architecture_styles, 1)
                        },
                        is_time_consuming=True,
                        is_difficult=False,
                        weight=4,
                    ),
                ])

            game_objective_templates.extend(photo_templates)

        # Location Hunting
        if self.include_location_hunting:
            location_templates = [
                GameObjectiveTemplate(
                    label="Visit LANDMARK_COUNT historical landmarks",
                    data={"LANDMARK_COUNT": (self.landmark_counts_normal, 1)},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Visit LANDMARK_COUNT historical landmarks",
                    data={"LANDMARK_COUNT": (self.landmark_counts_tc, 1)},
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Explore REGION_COUNT different neighborhoods or regions",
                    data={"REGION_COUNT": (self.region_counts_normal, 1)},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Explore REGION_COUNT different neighborhoods or regions",
                    data={"REGION_COUNT": (self.region_counts_tc, 1)},
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
            ]

            location_templates.extend([
                GameObjectiveTemplate(
                    label="Find and visit LOCATION_TYPE",
                    data={"LOCATION_TYPE": (self.discoverable_locations, 1)},
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Locate ADDRESS_COUNT addresses with ADDRESS_FEATURE",
                    data={
                        "ADDRESS_COUNT": (self.address_counts_normal, 1),
                        "ADDRESS_FEATURE": (self.address_features, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Locate ADDRESS_COUNT addresses with ADDRESS_FEATURE",
                    data={
                        "ADDRESS_COUNT": (self.address_counts_tc, 1),
                        "ADDRESS_FEATURE": (self.address_features, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Visit SHOP_COUNT different SHOP_TYPE establishments",
                    data={
                        "SHOP_COUNT": (self.shop_counts_normal, 1),
                        "SHOP_TYPE": (self.shop_types, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Visit SHOP_COUNT different SHOP_TYPE establishments",
                    data={
                        "SHOP_COUNT": (self.shop_counts_tc, 1),
                        "SHOP_TYPE": (self.shop_types, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Find (and visit if possible) MUSEUM_COUNT MUSEUM_TYPE museums or galleries",
                    data={
                        "MUSEUM_COUNT": (self.museum_counts_normal, 1),
                        "MUSEUM_TYPE": (self.museum_types, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Find (and visit if possible) MUSEUM_COUNT MUSEUM_TYPE museums or galleries",
                    data={
                        "MUSEUM_COUNT": (self.museum_counts_tc, 1),
                        "MUSEUM_TYPE": (self.museum_types, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
            ])

            game_objective_templates.extend(location_templates)

        # Object Collection
        if self.include_object_collection:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Collect ITEM_COUNT different COLLECTIBLE_CATEGORY items",
                    data={
                        "ITEM_COUNT": (self.item_counts_normal, 1),
                        "COLLECTIBLE_CATEGORY": (self.collectible_categories, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Collect ITEM_COUNT different COLLECTIBLE_CATEGORY items",
                    data={
                        "ITEM_COUNT": (self.item_counts_tc, 1),
                        "COLLECTIBLE_CATEGORY": (self.collectible_categories, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Find and document SPECIMEN_COUNT SPECIMEN_TYPE specimens",
                    data={
                        "SPECIMEN_COUNT": (self.specimen_counts_normal, 1),
                        "SPECIMEN_TYPE": (self.specimen_types, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Find and document SPECIMEN_COUNT SPECIMEN_TYPE specimens",
                    data={
                        "SPECIMEN_COUNT": (self.specimen_counts_tc, 1),
                        "SPECIMEN_TYPE": (self.specimen_types, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Gather MATERIAL_COUNT samples of NATURAL_MATERIAL",
                    data={
                        "MATERIAL_COUNT": (self.material_counts_normal, 1),
                        "NATURAL_MATERIAL": (self.natural_materials, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Gather MATERIAL_COUNT samples of NATURAL_MATERIAL",
                    data={
                        "MATERIAL_COUNT": (self.material_counts_tc, 1),
                        "NATURAL_MATERIAL": (self.natural_materials, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Locate TREASURE_COUNT pieces of URBAN_TREASURE",
                    data={
                        "TREASURE_COUNT": (self.treasure_counts_normal, 1),
                        "URBAN_TREASURE": (self.urban_treasures, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Locate TREASURE_COUNT pieces of URBAN_TREASURE",
                    data={
                        "TREASURE_COUNT": (self.treasure_counts_tc, 1),
                        "URBAN_TREASURE": (self.urban_treasures, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Find VINTAGE_COUNT VINTAGE_ITEM at thrift stores or markets",
                    data={
                        "VINTAGE_COUNT": (self.vintage_counts_normal, 1),
                        "VINTAGE_ITEM": (self.vintage_items, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Find VINTAGE_COUNT VINTAGE_ITEM at thrift stores or markets",
                    data={
                        "VINTAGE_COUNT": (self.vintage_counts_tc, 1),
                        "VINTAGE_ITEM": (self.vintage_items, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
            ])

        # Interaction Challenges
        if self.include_interaction_challenges:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Engage in CONVERSATION_COUNT conversations with PERSON_TYPE",
                    data={
                        "CONVERSATION_COUNT": (self.conversation_counts_normal, 1),
                        "PERSON_TYPE": (self.person_types, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Engage in CONVERSATION_COUNT conversations with PERSON_TYPE",
                    data={
                        "CONVERSATION_COUNT": (self.conversation_counts_tc, 1),
                        "PERSON_TYPE": (self.person_types, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Learn SKILL_COUNT basic phrases in LOCAL_LANGUAGE",
                    data={
                        "SKILL_COUNT": (self.skill_counts_normal, 1),
                        "LOCAL_LANGUAGE": (self.local_languages, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Learn SKILL_COUNT basic phrases in LOCAL_LANGUAGE",
                    data={
                        "SKILL_COUNT": (self.skill_counts_tc, 1),
                        "LOCAL_LANGUAGE": (self.local_languages, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Volunteer VOLUNTEER_HOURS hours for VOLUNTEER_CAUSE",
                    data={
                        "VOLUNTEER_HOURS": (self.volunteer_hours_normal, 1),
                        "VOLUNTEER_CAUSE": (self.volunteer_causes, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=1,
                ),
                GameObjectiveTemplate(
                    label="Volunteer VOLUNTEER_HOURS hours for VOLUNTEER_CAUSE",
                    data={
                        "VOLUNTEER_HOURS": (self.volunteer_hours_tc, 1),
                        "VOLUNTEER_CAUSE": (self.volunteer_causes, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
            ])

        # Nature Exploration
        if self.include_nature_exploration:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Identify SPECIES_COUNT different WILDLIFE_TYPE species",
                    data={
                        "SPECIES_COUNT": (self.species_counts_normal, 1),
                        "WILDLIFE_TYPE": (self.wildlife_types, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Identify SPECIES_COUNT different WILDLIFE_TYPE species",
                    data={
                        "SPECIES_COUNT": (self.species_counts_tc, 1),
                        "WILDLIFE_TYPE": (self.wildlife_types, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Explore TRAIL_COUNT different TRAIL_TYPE",
                    data={
                        "TRAIL_COUNT": (self.trail_counts_normal, 1),
                        "TRAIL_TYPE": (self.trail_types, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Explore TRAIL_COUNT different TRAIL_TYPE",
                    data={
                        "TRAIL_COUNT": (self.trail_counts_tc, 1),
                        "TRAIL_TYPE": (self.trail_types, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Document PLANT_COUNT PLANT_CATEGORY plants",
                    data={
                        "PLANT_COUNT": (self.plant_counts_normal, 1),
                        "PLANT_CATEGORY": (self.plant_categories, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Document PLANT_COUNT PLANT_CATEGORY plants",
                    data={
                        "PLANT_COUNT": (self.plant_counts_tc, 1),
                        "PLANT_CATEGORY": (self.plant_categories, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Visit PARK_COUNT different PARK_TYPE areas",
                    data={
                        "PARK_COUNT": (self.park_counts_normal, 1),
                        "PARK_TYPE": (self.park_types, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Visit PARK_COUNT different PARK_TYPE areas",
                    data={
                        "PARK_COUNT": (self.park_counts_tc, 1),
                        "PARK_TYPE": (self.park_types, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Observe and record WEATHER_COUNT different weather patterns",
                    data={"WEATHER_COUNT": (self.weather_pattern_counts_normal, 1)},
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=2,
                ),
                GameObjectiveTemplate(
                    label="Observe and record WEATHER_COUNT different weather patterns",
                    data={"WEATHER_COUNT": (self.weather_pattern_counts_tc, 1)},
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=2,
                ),
            ])

        # Community Engagement
        if self.include_community_engagement:
            game_objective_templates.extend([
                GameObjectiveTemplate(
                    label="Support LOCAL_BUSINESS_COUNT local BUSINESS_TYPE businesses",
                    data={
                        "LOCAL_BUSINESS_COUNT": (self.local_business_counts_normal, 1),
                        "BUSINESS_TYPE": (self.business_types, 1)
                    },
                    is_time_consuming=False,
                    is_difficult=False,
                    weight=3,
                ),
                GameObjectiveTemplate(
                    label="Support LOCAL_BUSINESS_COUNT local BUSINESS_TYPE businesses",
                    data={
                        "LOCAL_BUSINESS_COUNT": (self.local_business_counts_tc, 1),
                        "BUSINESS_TYPE": (self.business_types, 1)
                    },
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=3,
                ),
                GameObjectiveTemplate(
                    label="Help with COMMUNITY_PROJECT",
                    data={"COMMUNITY_PROJECT": (self.community_projects, 1)},
                    is_time_consuming=True,
                    is_difficult=False,
                    weight=1,
                ),
            ])

        return game_objective_templates

    # Property checks
    @property
    def include_photography(self) -> bool:
        return self.archipelago_options.dragorrods_real_world_scavenger_hunts_include_photography.value

    @property
    def include_location_hunting(self) -> bool:
        return self.archipelago_options.dragorrods_real_world_scavenger_hunts_include_location_hunting.value

    @property
    def include_object_collection(self) -> bool:
        return self.archipelago_options.dragorrods_real_world_scavenger_hunts_include_object_collection.value

    @property
    def include_interaction_challenges(self) -> bool:
        return self.archipelago_options.dragorrods_real_world_scavenger_hunts_include_interaction_challenges.value

    @property
    def include_nature_exploration(self) -> bool:
        return self.archipelago_options.dragorrods_real_world_scavenger_hunts_include_nature_exploration.value

    @property
    def include_community_engagement(self) -> bool:
        return self.archipelago_options.dragorrods_real_world_scavenger_hunts_include_community_engagement.value

    @property
    def allow_architecture_style_challenge(self) -> bool:
        return bool(self.archipelago_options.dragorrods_real_world_scavenger_hunts_allow_architecture_style_challenge.value)

    # Data lists
    @staticmethod
    def photo_subjects() -> List[str]:
        return [
            "Colorful graffiti", "An interesting door", "A vintage sign",
            "A dog out for a walk", "A busy playground", "A food truck", "Public art",
            "A unique building", "A garden", "A bridge",
            "Street vendor stalls", "A clock tower", "A fountain", "A mural",
            "Multiple dogs on a walk", "Animals being fed in a park",
            "A pet playing outside", "Street art", "A protest sign",
            "A uniquely decorated vehicle", "A craft stall", "A flag"
        ]

    @staticmethod
    def challenge_photos() -> List[str]:
        return [
            "A moving vehicle", "A person mid-jump", "Water in motion", "A flying bird",
            "Rush hour crowds", "Wind affecting objects", "A reflection in puddles",
            "A spinning wheel", "A bouncing ball", "A falling leaf", "A flowing stream",
            "A swinging pendulum", "A rotating sign", "A fluttering flag", "A rippling water",
            "A person running", "A cyclist in motion", "A dog catching a frisbee", "A cat pouncing",
            "A bird taking flight", "A busy intersection", "A crowded market", "A cafe",
            "A moving escalator", "A revolving door", "Steam rising from coffee",
            "Rain drops or Snow falling", "Wind blowing object(s)", "Waves crashing",
            "A fountain spraying", "A waterfall cascading", "A fire burning",
            "A person's shadow in motion", "Multiple exposures of movement", "Motion blur effects",
            "A soap bubble floating", "A coin being flipped", "Dice being rolled", "Cards being shuffled",
            "A clock's second hand moving", "A timer counting down", "Someone typing on keyboard",
            "A printer in action", "A barista making coffee"
        ]

    @staticmethod
    def photo_themes() -> List[str]:
        return [
            "Doors and Entrances", "Street Signs", "Public Transportation", "Local Wildlife",
            "Food and Dining", "Architectural Details", "Green Spaces",
            "Street Art", "Community Gathering Spots", "Vintage Elements", "Modern Design"
        ]

    @staticmethod
    def colors() -> List[str]:
        return [
            "Red", "Blue", "Yellow", "Green", "Purple", "Orange", "Pink", "Turquoise",
            "Gold", "Silver", "Black", "White", "Brown", "Maroon", "Navy", "Teal"
        ]

    @staticmethod
    def architecture_styles() -> List[str]:
        return [
            "Victorian", "Modern", "Art Deco", "Colonial", "Industrial", "Mid-Century",
            "Gothic", "Contemporary", "Brutalist", "Traditional", "Craftsman", "Mediterranean"
        ]

    @staticmethod
    def discoverable_locations() -> List[str]:
        return [
            "A hidden garden", "A historic plaque", "A community bulletin board",
            "A local landmark", "A scenic viewpoint", "A unique shop", "A street market",
            "A public library", "A community center", "A park with playground",
            "A coffee shop with local art", "A bookstore", "A thrift store",
            "A secret alley", "A hidden staircase", "A tucked-away cafe",
            "An abandoned building", "A graffiti tunnel", "A pocket park", "A memorial bench",
            "A community garden", "A food co-op", "A maker space", "A recording studio",
            "A pottery studio", "A dance studio", "A martial arts dojo", "A climbing gym",
            "A vintage arcade", "A comic book store", "A used record shop",
            "A camera store", "A musical instrument shop", "A specialty spice shop", "A tea house",
            "A wine bar", "A craft brewery", "A distillery", "A cheese shop", "A chocolate shop",
            "A bakery", "A farmers market vendor", "A fish market",
            "A butcher shop", "A florist", "A plant nursery",
            "A community workshop", "A co-working space", "A pop-up shop", "A mobile vendor",
            "A seasonal stand", "A historic house", "A heritage building", "A old church",
            "A train station or bus terminal", "A water tower", "A bridge underpass",
            "A pedestrian overpass", "A observation deck", "A scenic overlook",
            "A rock formation", "A waterfall", "A creek crossing", "A pond", "A marsh",
            "A meadow", "A grove of trees", "A giant tree", "A herb garden"
        ]

    @staticmethod
    def address_features() -> List[str]:
        return [
            "Interesting house numbers", "Unique mailboxes", "Colorful front doors",
            "Garden displays", "Window decorations", "Porch decorations",
            "Street number murals", "Historic markers"
        ]

    @staticmethod
    def shop_types() -> List[str]:
        return [
            "Local cafes", "Independent bookstores", "Thrift shops", "Art galleries",
            "Farmers markets", "Food trucks", "Antique stores", "Craft shops",
            "Music stores", "Specialty food shops", "Shopping Malls", "Community markets"
        ]

    @staticmethod
    def collectible_categories() -> List[str]:
        return [
            "Interesting rocks", "Unique leaves", "Event flyers", "Postcards",
            "Stickers", "Maps", "Brochures", "Tickets", "Feathers", "Shells", "Coins",
            "Bottle caps", "Trading cards", "Keychains", "Magnets", "Pins",
            "Sugar packets", "Tea bags", "Coasters", "Napkins with logos",
            "Library bookmarks", "Museum brochures", "Wine corks", "Beer caps",
            "Coffee sleeves", "Local newspaper clippings", "Public transit transfers",
            "Paint Sample Papers", "Stone fragments", "Sand samples", "Soil samples",
            "Bark pieces", "Seed pods", "Pine cones", "Acorns", "Nuts", "Berries (safe ones)",
            "Flower petals", "Grass samples", "Moss specimens", "Lichen samples",
            "Interesting shaped stones", "Smooth pebbles", "Colored glass",
            "Driftwood or interesting wood pieces", "Animal tracks (photos)",
            "Nest materials", "Spider webs"
        ]

    @staticmethod
    def specimen_types() -> List[str]:
        return [
            "Tree species", "Flower varieties", "Bird species", "Insect types",
            "Cloud formations", "Rock types", "Lichen or Moss", "Grass types",
            "Weed varieties", "Shrub types", "Bush varieties", "Herb varieties",
            "Wildflower species", "Garden flower types", "Native plants", "Invasive species",
            "Fruit tree varieties", "Nut tree species", "Coniferous trees", "Deciduous trees",
            "Evergreen varieties", "Flowering trees", "Bug varieties", "Mammals species",
            "Rodent species", "Urban wildlife", "Domesticated animals", "Reptile species",
            "Fish species"
        ]

    @staticmethod
    def natural_materials() -> List[str]:
        return [
            "Different soil types", "Various sand types", "Water samples",
            "Seed pods", "Pine cones", "Bark textures", "Stone varieties"
        ]

    @staticmethod
    def urban_treasures() -> List[str]:
        return [
            "Interesting manhole covers", "Unique street art", "Historic markers",
            "Architectural details", "Vintage elements", "Community messages",
            "Local memorial plaques", "Unusual door handles", "Decorative window shutters",
            "Ornate fire escapes", "Vintage street lamps", "Old neon signs",
            "Historic building cornerstones", "Date stones in buildings", "Carved building details",
            "Interesting chimneys", "Decorative ironwork", "Stained glass windows",
            "Mosaic tiles", "Brick patterns", "Stone carvings", "Metal sculptures",
            "Bridge decorations", "Utility box art", "Fence art", "Wall textures",
            "Interesting shadows", "Light patterns", "Reflection art", "Mirror installations",
            "Aromatic gardens", "Community message boards", "Time capsule markers",
            "Survey markers", "Mile markers", "Seasonal installations"
        ]

    @staticmethod
    def vintage_items() -> List[str]:
        return [
            "Old books", "Vintage postcards", "Retro clothing", "Antique tools",
            "Vintage jewelry", "Classic records", "Antique buttons", "Vintage fabric",
            "Retro toys", "Classic board games", "Vintage puzzles", "Old playing cards",
            "Antique dishes", "Vintage glassware", "Retro kitchen utensils", "Old typewriters",
            "Vintage cameras", "Classic radios", "Old televisions", "Vintage phones",
            "Retro appliances", "Antique furniture", "Vintage lamps", "Old clocks",
            "Antique mirrors", "Vintage frames", "Old suitcases/luggage", "Vintage hats",
            "Retro accessories", "Antique watches", "Vintage purses", "Old wallets",
            "Retro sunglasses", "Antique pins", "Retro containers", "Military surplus items",
            "Vintage uniforms", "Retro collectibles", "Classic movie posters",
            "Antique instruments", "Vintage sports equipment", "Old gaming items",
            "Retro technology", "Old educational materials", "Antique religious items",
            "Vintage holiday decorations"
        ]

    @staticmethod
    def person_types() -> List[str]:
        return [
            "Local shop owners", "Dog walkers", "Gardeners",
            "Public transit operators", "Food vendors", "Artists",
            "Library staff", "Park workers", "Museum guides", "Neighbors",
            "Postal workers", "Delivery drivers", "Security guards", "Construction workers",
            "Maintenance staff", "Cleaning crews", "Landscapers",
            "Bus drivers", "Cyclists", "Joggers", "Students", "Crossing guards",
            "Bakers", "Baristas", "Bartenders", "Servers",
            "Store clerks", "Cashiers", "Sales associates"
        ]

    @staticmethod
    def local_languages() -> List[str]:
        return [
            "Spanish", "French", "Mandarin", "Sign Language", "Local dialect",
            "German", "Italian", "Portuguese", "Arabic", "Japanese", "Korean", "Hindi"
        ]

    @staticmethod
    def volunteer_causes() -> List[str]:
        return [
            "Environmental cleanup", "Community garden", "Food bank", "Animal shelter",
            "Elder care", "Youth programs", "Literacy programs", "Local arts",
            "Community events", "Habitat restoration", "Homeless support", "Education support"
        ]

    @staticmethod
    def wildlife_types() -> List[str]:
        return [
            "Birds", "Squirrels", "Insects", "Urban wildlife", "Garden creatures",
            "Park animals", "Pond life", "Tree dwellers", "Ground animals"
        ]

    @staticmethod
    def trail_types() -> List[str]:
        return [
            "Walking trails", "Bike paths", "Nature trails", "Historic routes",
            "Scenic walkways", "Urban trails", "Park loops"
        ]

    @staticmethod
    def plant_categories() -> List[str]:
        return [
            "Native plants", "Garden plants", "Trees", "Shrubs", "Herbs",
            "Grasses", "Flowering plants", "Fruit plants"
        ]

    @staticmethod
    def park_types() -> List[str]:
        return [
            "City parks", "Neighborhood parks", "Nature preserves", "Botanical gardens",
            "Community gardens", "Pocket parks", "Recreation areas", "Green spaces"
        ]

    @staticmethod
    def museum_types() -> List[str]:
        return [
            "Art", "History", "Science", "Natural history", "Cultural",
            "Community", "Children's", "Technology"
        ]

    @staticmethod
    def business_types() -> List[str]:
        return [
            "Restaurants", "Shops", "Services", "Markets", "Cafes", "Bookstores",
            "Art studios", "Craft stores", "Food producers", "Entertainment venues"
        ]

    @staticmethod
    def community_projects() -> List[str]:
        return [
            "Community garden maintenance", "Neighborhood cleanup", "Local event organization",
            "Public art project", "History documentation", "Environmental improvement",
            "Youth program support", "Elder assistance", "Cultural preservation"
        ]

    @staticmethod
    def location_restrictions() -> List[str]:
        return [
            "Within walking distance", "Public transportation accessible", "Downtown area",
            "Residential neighborhoods", "Parks and nature areas", "Cultural districts"
        ]

    @staticmethod
    def transportation_methods() -> List[str]:
        return [
            "Walking only", "Bicycle", "Public transit", "Car", "Combination methods",
            "Eco-friendly transport", "Different method each day"
        ]

    @staticmethod
    def companion_types() -> List[str]:
        return [
            "Solo exploration", "Solo exploration", "Solo exploration",
            "Solo exploration", "Solo exploration", "Solo exploration",
            "With family", "With friends", "With community group",
            "With pets", "Meeting new people", "Guided group"
        ]

    @staticmethod
    def weather_conditions() -> List[str]:
        return [
            "Sunny weather", "Rainy or Snowy day", "Overcast skies",
            "Windy conditions", "Any weather", "Perfect weather"
        ]

    @staticmethod
    def specific_times() -> List[str]:
        return [
            "Golden hour", "Blue hour", "Rush hour", "Early morning", "Late evening",
            "Midday", "Lunch time", "Weekend morning"
        ]

    # Counts (split into "normal" / "tc" pairs so the top value of every count
    # requires the "Long Objectives" global setting to be enabled)
    @staticmethod
    def photo_series_counts_normal() -> List[int]:
        return [3, 5]

    @staticmethod
    def photo_series_counts_tc() -> List[int]:
        return [7]

    @staticmethod
    def color_counts_normal() -> List[int]:
        return [3]

    @staticmethod
    def color_counts_tc() -> List[int]:
        return [6]

    @staticmethod
    def architecture_counts_normal() -> List[int]:
        return [2, 3, 4]

    @staticmethod
    def architecture_counts_tc() -> List[int]:
        return [5]

    @staticmethod
    def landmark_counts_normal() -> List[int]:
        return [2, 3, 4]

    @staticmethod
    def landmark_counts_tc() -> List[int]:
        return [5]

    @staticmethod
    def region_counts_normal() -> List[int]:
        return [3, 4]

    @staticmethod
    def region_counts_tc() -> List[int]:
        return [5]

    @staticmethod
    def address_counts_normal() -> List[int]:
        return [3, 5]

    @staticmethod
    def address_counts_tc() -> List[int]:
        return [7]

    @staticmethod
    def shop_counts_normal() -> List[int]:
        return [1, 2, 3]

    @staticmethod
    def shop_counts_tc() -> List[int]:
        return [4]

    @staticmethod
    def item_counts_normal() -> List[int]:
        return [3, 5]

    @staticmethod
    def item_counts_tc() -> List[int]:
        return [7]

    @staticmethod
    def specimen_counts_normal() -> List[int]:
        return [2, 4]

    @staticmethod
    def specimen_counts_tc() -> List[int]:
        return [5]

    @staticmethod
    def material_counts_normal() -> List[int]:
        return [3, 5]

    @staticmethod
    def material_counts_tc() -> List[int]:
        return [7]

    @staticmethod
    def treasure_counts_normal() -> List[int]:
        return [2, 3]

    @staticmethod
    def treasure_counts_tc() -> List[int]:
        return [5]

    @staticmethod
    def vintage_counts_normal() -> List[int]:
        return [2]

    @staticmethod
    def vintage_counts_tc() -> List[int]:
        return [4]

    @staticmethod
    def conversation_counts_normal() -> List[int]:
        return [3, 5, 7]

    @staticmethod
    def conversation_counts_tc() -> List[int]:
        return [9]

    @staticmethod
    def skill_counts_normal() -> List[int]:
        return [5]

    @staticmethod
    def skill_counts_tc() -> List[int]:
        return [10]

    @staticmethod
    def volunteer_hours_normal() -> List[int]:
        return [1, 2, 3]

    @staticmethod
    def volunteer_hours_tc() -> List[int]:
        return [4]

    @staticmethod
    def species_counts_normal() -> List[int]:
        return [2, 4]

    @staticmethod
    def species_counts_tc() -> List[int]:
        return [6]

    @staticmethod
    def trail_counts_normal() -> List[int]:
        return [1, 2, 3]

    @staticmethod
    def trail_counts_tc() -> List[int]:
        return [4]

    @staticmethod
    def plant_counts_normal() -> List[int]:
        return [3, 5]

    @staticmethod
    def plant_counts_tc() -> List[int]:
        return [7]

    @staticmethod
    def park_counts_normal() -> List[int]:
        return [1, 2, 3]

    @staticmethod
    def park_counts_tc() -> List[int]:
        return [4]

    @staticmethod
    def weather_pattern_counts_normal() -> List[int]:
        return [2, 4]

    @staticmethod
    def weather_pattern_counts_tc() -> List[int]:
        return [6]

    @staticmethod
    def museum_counts_normal() -> List[int]:
        return [2]

    @staticmethod
    def museum_counts_tc() -> List[int]:
        return [4]

    @staticmethod
    def local_business_counts_normal() -> List[int]:
        return [2, 3, 4]

    @staticmethod
    def local_business_counts_tc() -> List[int]:
        return [5]


# Archipelago Options
class DragorrodsRealWorldScavengerHuntsIncludePhotography(DefaultOnToggle):
    """Include photography and visual documentation objectives."""
    display_name = "Dragorrod's Real World Scavenger Hunts Include Photography"

class DragorrodsRealWorldScavengerHuntsIncludeLocationHunting(DefaultOnToggle):
    """Include location discovery and exploration objectives."""
    display_name = "Dragorrod's Real World Scavenger Hunts Include Location Hunting"

class DragorrodsRealWorldScavengerHuntsIncludeObjectCollection(DefaultOnToggle):
    """Include item collection and specimen gathering objectives."""
    display_name = "Dragorrod's Real World Scavenger Hunts Include Object Collection"

class DragorrodsRealWorldScavengerHuntsIncludeInteractionChallenges(Toggle):
    """Include social interaction and communication objectives."""
    display_name = "Dragorrod's Real World Scavenger Hunts Include Interaction Challenges"

class DragorrodsRealWorldScavengerHuntsIncludeNatureExploration(DefaultOnToggle):
    """Include wildlife observation and nature study objectives."""
    display_name = "Dragorrod's Real World Scavenger Hunts Include Nature Exploration"

class DragorrodsRealWorldScavengerHuntsIncludeCommunityEngagement(Toggle):
    """Include community participation and local support objectives."""
    display_name = "Dragorrod's Real World Scavenger Hunts Include Community Engagement"

class DragorrodsRealWorldScavengerHuntsAllowArchitectureStyleChallenge(Toggle):
    """Include the objective asking you to photograph buildings of a specific, named architecture style?"""
    display_name = "Dragorrod's Real World Scavenger Hunts Allow Architecture Style Challenge"
