import streamlit as st
import geocoder


st.set_page_config(layout="wide")

if __name__ == "__main__":
    st.markdown(
        "<h1 style='text-align: center; color: green;'>Reverse Geocoding with MapBox</h1>",
        unsafe_allow_html=True,
    )

    st.write('Get the correct address according to the coordinates (latitude / longitude) by using the Reverse Geocoding API from MapBox.')

    col_11, col_12, col_2 = st.columns(3)
    latlng = [36.54085544, -4.619933495]
    with col_11:
        lat = st.text_input('Latitude: ', value="36.54085544")

    with col_12:
        lng = st.text_input('Longitude: ', value="-4.619933495")

    with col_2:
        get = st.button('Get the address')
        if get:
            try:
                g = geocoder.mapbox(latlng, method='reverse', key=st.secrets["MAPBOX_ACCESS_TOKEN"])
                st.success(g.json)
            except Exception as e:
                st.error(e)
