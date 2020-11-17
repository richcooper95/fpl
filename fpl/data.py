import fetch
import process
import pandas as pd
from typing import Callable

import error

class H2HLeague:
    """Class representing the H2H league.
    """

    DISPLAY = {
        "rank": "Rank",
        "entry_name": "Team",
        "player_name": "Manager",
        "matches_won": "Won",
        "matches_lost": "Lost",
        "matches_drawn": "Drawn",
    }

    INTERNAL = list(DISPLAY.keys()) + [
        "last_rank",
        "entry",
        "total",
    ]

    def __init__(
        self,
        id: int,
        name: str,
        start_event: int,
        standings_df: pd.DataFrame,
    ) -> None:
        """Class constructor.

        Keyword Arguments:
            id {int} -- The H2H League ID.
            name {str} -- The name of this league.
            start_event {int}
                -- The event (Gameweek) in which this league started.
            standings_df {pd.DataFrame}
                -- The Pandas DataFrame for league results.
        """
        self.id: int = id
        self.name: str = name
        self.start_event: int = start_event
        self.standings_df: pd.DataFrame = standings_df


    def __repr__(self) -> str:
        """Instance string representation."""
        # TODO: The DataFrame repr is very long - neaten this up
        classname = self.__class__.__name__
        parts = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
        return f"{classname}({', '.join(parts)})"


    @property
    def display_df(self):
        """Return a filtered standings DataFrame for display on the app.

        Returns:
            pd.DataFrame -- The filtered DataFrame for display.
        """
        df = self.standings_df[list(self.DISPLAY.keys())]
        return df.rename(columns=self.DISPLAY)


    @classmethod
    def create(cls, get_func: Callable[[None], dict]) -> "H2HLeague":
        """Create a League instance.

        Arguments:
            get_func {Callable[None, dict]}
                -- The function to call to get the raw JSON data from the FPL
                   API.
        """
        # TODO: Better error handling here - what happens when:
        #  - the 'get' function raises an exception?
        #  - the JSON structure isn't as expected (e.g. field names changed)?
        json_data = get_func()

        try:
            standings_df = pd.DataFrame(json_data["standings"]["results"])
            standings_df = standings_df[cls.INTERNAL]
        except Exception as exc:
            msg = f"Error in structure of downloaded JSON: {exc}"
            raise error.JSONError(msg) from exc

        return cls(
            json_data["league"]["id"],
            json_data["league"]["name"],
            json_data["league"]["start_event"],
            standings_df,
        )


class Bootstrap:
    """Class representing the bootstrap data.
    """
    def __init__(
        self,
        elements_df: pd.DataFrame,
        events_df: pd.DataFrame,
        phases_df: pd.DataFrame,
        pl_teams_df: pd.DataFrame,
        element_types_df: pd.DataFrame,
    ) -> None:
        """Class constructor.

        Keyword Arguments:
            elements_df {pd.DataFrame}
                -- The Pandas DataFrame for the elements (players).
            events_df {pd.DataFrame}
                -- The Pandas DataFrame for the events (Gameweeks).
            phases_df {pd.DataFrame}
                -- The Pandas DataFrame for the phases (months).
            pl_teams_df {pd.DataFrame}
                -- The Pandas DataFrame for the PL teams.
            element_types_df {pd.DataFrame}
                -- The Pandas DataFrame for the element (player) types.
        """
        self.elements_df: pd.DataFrame = elements_df
        self.events_df: pd.DataFrame = events_df
        self.phases_df: pd.DataFrame = phases_df
        self.pl_teams_df: pd.DataFrame = pl_teams_df
        self.element_types_df: pd.DataFrame = element_types_df


    def __repr__(self) -> str:
        """Instance string representation."""
        # TODO: The DataFrame repr is very long - neaten this up (with type?)
        classname = self.__class__.__name__
        parts = [f"{k}={type(v)}" for k, v in self.__dict__.items()]
        return f"{classname}({', '.join(parts)})"


    @classmethod
    def create(cls, get_func: Callable[[None], dict]) -> "Elements":
        """Create an Elements instance.

        Arguments:
            get_func {Callable[None, dict]}
                -- The function to call to get the raw JSON data from the FPL
                   API.
        """
        # TODO: Better error handling here - what happens when:
        #  - the 'get' function raises an exception?
        #  - the JSON structure isn't as expected (e.g. field names changed)?
        json_data = get_func()

        try:
            elements_df = pd.DataFrame(json_data["elements"])
            elements_df = elements_df[cls.INTERNAL]
        except Exception as exc:
            msg = f"Error in structure of downloaded JSON: {exc}"
            raise error.JSONError(msg) from exc

        return cls(
            elements_df,
        )
