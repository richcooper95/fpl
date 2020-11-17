import requests
import streamlit as st

import error

__all__ = (
    "get_entry_json",
    "get_element_json",
    "get_league_json",
    "get_league_matches_json",
    "get_entry_event_picks_json",
    "get_entry_history_json",
)

BASE_URL = "https://fantasy.premierleague.com/api/"

def _get_from_url(url):
    """Return JSON string from URL.
    """
    try:
        # Catch all fetch-related exceptions in one block.
        response = requests.get(url)
        response.raise_for_status() # checks status is success
        response = response.json()
    except Exception as exc:
        msg = f"Error fetching JSON data from URL: {url}: {exc}"
        raise error.FetchError(msg) from exc

    return response


@st.cache(persist=True)
def get_bootstrap_json():
    """Returns JSON data for the given team (entry).

    Data is structured as follows:
        {
            total_players: int,
            events: [
                {
                    id: int,
                    name: str,
                    deadline_time: str,
                    average_entry_score: int,
                    finished: bool,
                    data_checked: bool,
                    highest_scoring_entry: int,
                    highest_score: int,
                    is_previous: bool,
                    is_current: bool,
                    is_next: bool,
                    chip_plays: [
                        {
                            chip_name: str,
                            num_played: int
                        },
                        ...
                    ],
                    most_selected: int,
                    most_transferred_in: int,
                    top_element: int,
                    top_element_info: {
                        id: int,
                        points: int
                    },
                    transfers_made: int,
                    most_captained: int,
                    most_vice_captained: int,
                    <irrelevant fields omitted>
                },
                ...
            ],
            game_settings: {
                <irrelevant fields omitted>
            },
            phases: [
                {
                    id: int,
                    name: str,
                    start_event: int,
                    stop_event: int
                },
                ...
            ],
            teams: [
                code: int,
                id: int,
                name: str,
                short_name: str,
                <irrelevant fields omitted>
            ],
            elements: [
                id: int,
                dreamteam_count: int,
                element_type: int,
                event_points: int,
                first_name: str,
                second_name: str,
                web_name: str,
                cost_change_start: int,
                cost_change_event: int,
                form: str,
                in_dreamteam: bool,
                now_cost: int,
                points_per_game: str,
                selected_by_percent: str,
                team: int,
                team_code: int,
                total_points: int,
                transfers_in_event: int,
                transfers_out_event: int,
                value_form: str,
                value_season: str,
                minutes: int,
                goals_scored: int,
                assists: int,
                clean_sheets: int,
                goals_conceded: int,
                own_goals: int,
                penalties_saved: int,
                penalties_missed: int,
                yellow_cards: int,
                red_cards: int,
                saves: int,
                bonus: int,
                bps: int,
                <irrelevant fields omitted>
            ],
            element_types: [
                {
                    id: int,
                    plural_name: str,
                    plural_name_short: str,
                    singular_name: str,
                    singular_name_short: str,
                    <irrelevant fields omitted>
                },
                ...
            ],
            element_stats: {
                <irrelevant fields omitted>
            }
        }
    
    Returns:
        dict -- JSON object obtained from the URL.
    """
    return _get_from_url(BASE_URL + "bootstrap-static")


@st.cache(persist=True)
def get_entry_json(entry_id):
    """Returns JSON data for the given team (entry).

    Data is structured as follows:
        {
            id: int,
            started_event: int,
            favourite_team: int,
            name: str,
            player_first_name: str,
            player_last_name: str,
            player_region_id: int,
            player_region_name: str,
            player_region_iso_code_short: str,
            summary_overall_points: int,
            summary_overall_rank: int,
            summary_event_points: int,
            summary_event_rank: int,
            current_event: int,
            last_deadline_bank: int,
            last_deadline_value: int,
            last_deadline_total_transfers: int,
            leagues: {
                classic: [
                    {
                        id: int,
                        name: str,
                        short_name: str,
                        start_event: int,
                        entry_rank: int,
                        entry_last_rank: int,
                        <irrelevant fields omitted>
                    },
                    ...
                ],
                h2h: [
                    {
                        id: int,
                        name: str,
                        short_name: str,
                        start_event: int,
                        entry_rank: int,
                        entry_last_rank: int,
                        <irrelevant fields omitted>
                    },
                    ...
                ],
                cup: {
                    matches: list,
                    <irrelevant fields omitted>
                }
            },
            <irrelevant fields omitted>
        }

    Arguments:
        entry_id {int} -- The Entry ID.
    
    Returns:
        dict -- JSON object obtained from the URL.
    """
    return _get_from_url(BASE_URL + f"entry/{entry_id}")


@st.cache(persist=True)
def get_element_json(element_id):
    """Returns JSON data for the given element.

    Data is structured as follows:
        {
            fixtures: [
                {
                    id: int,
                    code: int,
                    team_h: int,
                    team_a: int,
                    event: int,
                    event_name: str,
                    is_home: bool,
                    difficulty: int,
                    <irrelevant fields omitted>
                },
                ...
            ],
            history: [
                {
                    element: int,
                    fixture: int,
                    opponent_team: int,
                    total_points: int,
                    was_home: bool,
                    team_h_score: int,
                    team_a_score: int,
                    round: int,
                    minutes: int,
                    goals_scored: int,
                    assists: int,
                    clean_sheets: int,
                    goals_conceded: int,
                    own_goals: int,
                    penalties_saved: int,
                    penalties_missed: int,
                    yellow_cards: int,
                    red_cards: int,
                    saves: int,
                    bonus: int,
                    bps: int,
                    influence: str,
                    creativity: str,
                    threat: str,
                    ict_index: str,
                    value: int,
                    transfers_balance: int,
                    selected: int,
                    transfers_in: int,
                    transfers_out: int
                },
                ...
            ],
            history_past: [
                {
                    <irrelevant fields omitted>
                },
                ...
            ]
        }

    Arguments:
        element_id {int} -- The Element ID.
    
    Returns:
        dict -- JSON object obtained from the URL.
    """
    return _get_from_url(BASE_URL + f"element-summary/{element_id}")


@st.cache(persist=True)
def get_league_json(league_id):
    """Returns JSON data for the given league.

    Data is structured as follows:
        {
            league: {
                id: int,
                name: str,
                start_event: int,
                <irrelevant fields omitted>
            },
            new_entries: {
                has_next: bool,
                page: int,
                results: list
            },
            standings: {
                has_next: bool,
                page: int,
                results: [
                    {
                        id: int,
                        division: int,
                        entry: int,
                        player_name: str,
                        rank: int,
                        last_rank: int,
                        rank_sort: int,
                        total: int,
                        entry_name: str,
                        matches_played: int,
                        matches_won: int,
                        matches_drawn: int,
                        matches_lost: int,
                        points_for: int
                    },
                    ...
                ]
            }
        }

    Arguments:
        league_id {int} -- The League ID.
    
    Returns:
        dict -- JSON object obtained from the URL.
    """
    return _get_from_url(
        BASE_URL + f"leagues-h2h/{league_id}/standings"
    )


@st.cache(persist=True)
def get_league_matches_json(league_id):
    """Returns JSON data for the given league's matches.

    Data is structured as follows:
        {
            has_next: bool,
            page: int,
            results: [
                {
                    id: int,
                    entry_1_entry: int,
                    entry_1_name: str,
                    entry_1_player_name: str,
                    entry_1_points: int,
                    entry_1_win: int,
                    entry_1_draw: int,
                    entry_1_loss: int,
                    entry_1_total: int,
                    entry_2_entry: int,
                    entry_2_name: str,
                    entry_2_player_name: str,
                    entry_2_points: int,
                    entry_2_win: int,
                    entry_2_draw: int,
                    entry_2_loss: int,
                    entry_2_total: int,
                    is_knockout: bool,
                    winner: int/null,
                    seed_value: int/null,
                    event: int,
                    tiebreak: bool/null
                },
                ...
            ]
        }

    Arguments:
        league_id {int} -- The League ID.
    
    Returns:
        dict -- JSON object obtained from the URL.
    """
    return _get_from_url(
        BASE_URL + f"leagues-h2h-matches/league/{league_id}"
    )


@st.cache(persist=True)
def get_entry_event_picks_json(entry_id, event_id):
    """Returns JSON data containing the team (picks) for a given manager
    (entry) and gameweek (event).

    Data is structured as follows:
        {
            active_chip: str/null,
            automatic_subs: list,
            entry_history: {
                event: int,
                points: int,
                total_points: int,
                rank: int,
                rank_sort: int,
                overall_rank: int,
                bank: int,
                value: int,
                event_transfers: int,
                event_transfers_cost: int,
                points_on_bench: int
            },
            picks: [
                {
                    element: int,
                    position: int,
                    multiplier: int,
                    is_captain: bool,
                    is_vice_captain: bool
                }, ...
            ]
        }

    Arguments:
        entry_id {int} -- The Entry ID.
        event_id {int} -- The Event ID for the Gameweek.
    
    Returns:
        dict -- JSON object obtained from the URL.
    """
    return _get_from_url(
        BASE_URL + f"entry/{entry_id}/event/{event_id}/picks"
    )


@st.cache(persist=True)
def get_entry_history_json(entry_id):
    """Returns JSON data containing the history for a given manager (entry).

    Data is structured as follows:
        {
            chips: [
                {
                    name: str,
                    time: str,
                    event: int
                }
            ]
            current: [
                {
                    event: int,
                    points: int,
                    total_points: int,
                    rank: int,
                    rank_sort: int,
                    overall_rank: int,
                    bank: int,
                    value: int,
                    event_transfers: int,
                    event_transfers_cost: int,
                    points_on_bench: int
                }, ...
            ],
            past: [
                {
                    season_name: str,
                    total_points: int,
                    rank: int
                }
            ]
        }

    Arguments:
        entry_id {int} -- The Entry ID.
        event_id {int} -- The Event ID for the Gameweek.
    
    Returns:
        dict -- JSON object obtained from the URL.
    """
    return _get_from_url(
        BASE_URL + f"entry/{entry_id}/event/{event_id}/picks"
    )
