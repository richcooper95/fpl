import streamlit as st
import pandas as pd
import numpy as np
import functools

import fetch
import data
import error

def main():
    if st.sidebar.button("Refresh Data"):
        st.caching.clear_cache()

    league_id = st.sidebar.text_input("League ID", value="309333")
    try:
        league_id = int(league_id)
    except ValueError as exc:
        st.sidebar.error(
            f"Invalid League ID: {league_id}. Must be an integer."
        )
        raise st.StopException from exc

    try:
        league = data.H2HLeague.create(
            functools.partial(fetch.get_league_json, league_id)
        )
    except Exception as exc:
        st.error(f"Error obtaining league data: {exc}")
        raise st.StopException from exc

    st.title(f"FPL H2H Tool: {league.name}")
    
    st.header("Current Standings")
    st.dataframe(league.display_df)
    st.dataframe(league.standings_df)


if __name__ == "__main__":
    main()
