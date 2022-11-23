import streamlit as st
from pathlib import Path
import pandas as pd

# def main():

def increment():
    st.session_state.ctr += 1

def decrement():
    if st.session_state.ctr > 0:
        st.session_state.ctr -= 1

try:
    if 'ctr' not in st.session_state:
        st.session_state.ctr = 0


    data_root = Path(r"\\nasal01\data-r\Projects\611-CT.2169_SMARTLADLEGATE")
    path = st.text_input('Enter tha path to the data', value=data_root, key='input')
    path = Path(path)

    if not path.exists():
        st.write('Path does not exist')


    plots = list((path / "output").glob("**/*seg*.html"))

    df = pd.DataFrame(columns=["schmelze", "date" , "path"])
    intercheck_plts = []
    for p in plots:
        if "intercheck" in str(p):
            intercheck_plts.append(p)
            split = p.stem.split("_")
            date = split[0] + "_" + split[1]
            schmelze_nr = split[2]
            df = pd.concat([df, pd.DataFrame({"schmelze": [schmelze_nr], "date": [date], "path": [p]})])

    df.reset_index(inplace=True)

    idx = 0

    if st.button("Next"):
        increment()

    if st.button("Previous"):
        decrement()


    idx = st.slider("select schmelze", 0, len(intercheck_plts)-1, st.session_state.ctr)
    st.write("You selected:", df.loc[idx, "schmelze"])
    st.components.v1.html(open(df.loc[idx, "path"], 'r', encoding='utf-8').read(), height=800)

    # try:
    #     st.components.v1.html(open(data_root /"output" / "intercheck" / "20221016_2255_force_vs_n_uses_2070.html" , 'r', encoding='utf-8').read(), height=800)
    # except:
    #     st.write("no max force plot")
    #     pass

    comb_plots = list((path / "output" / "intercheck" / "open_forces").glob("*.html"))
    combs = []

    st.write("open forces")
    st.write(f"number of plots: {len(comb_plots)}")

    # df2 = pd.DataFrame(columns=["set_id", "date" , "path"])
    # for p in comb_plots:

    #     comb_plots.append(p)
    #     split = p.stem.split("_")
    #     date = split[0] + "_" + split[1]
    #     schmelze_nr = split[3]
    #     df2 = pd.concat([df2, pd.DataFrame({"set_id": [schmelze_nr], "date": [date], "path": [p]})])

    # st.write("for done")

    # df2.reset_index(inplace=True)
    idx_comb = 0
    idx_comb = st.slider("select set_id", 0, len(comb_plots)-1,idx_comb)

    p = comb_plots[idx_comb]
    split = p.stem.split("_")
    date = split[0] + "_" + split[1]
    set_id = split[3]
    st.write("You selected:", set_id, "set_id")
    # st.components.v1.html(open(df2.loc[idx_comb, "path"], 'r', encoding='utf-8').read(), height=800)
    st.components.v1.html(open(comb_plots[idx_comb], 'r', encoding='utf-8').read(), height=800)
except Exception as ex:
    st.write("something went wrong")
    st.write(ex)


# if __name__ == "__main__":

#     data_root = Path(r"\\nasal01\data-r\Projects\611-CT.2169_SMARTLADLEGATE")
    # main()
