import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import random
import os

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Weather Forecast & Alert System",
    page_icon="🌦",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

html, body, [class*="css"] {
    background-color: #050816;
    color: white;
    font-family: 'Segoe UI';
}

/* Sidebar */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg,#050b1c,#081225);
    border-right: 1px solid #00d9ff;
}

/* Title */

.main-title {
    font-size: 58px;
    font-weight: bold;
    color: #00d9ff;
    text-shadow: 0 0 20px rgba(0,217,255,0.6);
}

.ai-title {
    color: #ff2d75;
}

.sub-title {
    color: #ffd000;
    font-size: 22px;
    letter-spacing: 2px;
}

/* Cards */

.glass-card {
    background: rgba(8,15,30,0.92);
    border: 1px solid rgba(0,217,255,0.25);
    border-radius: 22px;
    padding: 25px;
    box-shadow: 0 0 30px rgba(0,217,255,0.15);
    margin-bottom: 20px;
}

/* Metrics */

.metric-card {
    background: rgba(8,15,30,0.95);
    border: 1px solid rgba(0,217,255,0.2);
    border-radius: 18px;
    padding: 18px;
    text-align: center;
    box-shadow: 0 0 18px rgba(0,217,255,0.08);
}

.metric-value {
    font-size: 30px;
    font-weight: bold;
    color: #00d9ff;
}

.metric-label {
    color: #cccccc;
    font-size: 14px;
}

/* Forecast Cards */

.forecast-card {
    background: rgba(8,15,30,0.92);
    border: 1px solid rgba(0,217,255,0.2);
    border-radius: 18px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 0 18px rgba(0,217,255,0.08);
    transition: 0.3s;
}

.forecast-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 0 28px rgba(0,217,255,0.25);
}

/* Alerts */

.alert-box {
    background: rgba(255,140,0,0.08);
    border: 2px solid orange;
    border-radius: 18px;
    padding: 20px;
    margin-top: 15px;
    box-shadow: 0 0 22px rgba(255,140,0,0.35);
}

/* Prediction Box */

.ai-box {
    background: rgba(255,45,117,0.08);
    border: 2px solid #ff2d75;
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0 0 25px rgba(255,45,117,0.3);
}

/* Buttons */

.stButton > button {
    background: linear-gradient(90deg,#00d9ff,#0072ff);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px 24px;
    font-weight: bold;
}

/* Inputs */

.stTextInput input {
    background-color: #0a1428;
    color: white;
    border: 1px solid #00d9ff;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown("# ⚙ WEATHER CONTROL PANEL")

city = st.sidebar.selectbox(
    "🌍 SELECT CITY",
    [
        "Pune",
        "Mumbai",
        "Delhi",
        "Bangalore",
        "Hyderabad",
        "Chennai",
        "Kolkata"
    ]
)

st.sidebar.markdown("---")

st.sidebar.markdown("## 🎛 MANUAL WEATHER INPUT")

manual_temp = st.sidebar.slider(
    "🌡 Temperature (°C)",
    10,
    50,
    34
)

manual_humidity = st.sidebar.slider(
    "💧 Humidity (%)",
    20,
    100,
    78
)

manual_wind = st.sidebar.slider(
    "💨 Wind Speed (km/h)",
    0,
    100,
    15
)

manual_pressure = st.sidebar.slider(
    "📊 Pressure (hPa)",
    900,
    1100,
    1012
)

weather_condition = st.sidebar.selectbox(
    "⛅ Weather Condition",
    [
        "Clear",
        "Clouds",
        "Rain",
        "Storm",
        "Mist"
    ]
)

# =========================================================
# SIMULATED WEATHER DATA
# =========================================================

forecast_dates = [
    "Mon",
    "Tue",
    "Wed",
    "Thu",
    "Fri"
]

forecast_temps = [
    manual_temp + random.randint(-3, 3)
    for _ in range(5)
]

forecast_humidity = [
    manual_humidity + random.randint(-5, 5)
    for _ in range(5)
]

# =========================================================
# HEADER
# =========================================================

st.markdown(f"""
<div class='main-title'>
WEATHER<span class='ai-title'>AI</span>
</div>

<div class='sub-title'>
FORECAST & ALERT APPLICATION
</div>
""", unsafe_allow_html=True)

st.write("INDUSTRY LEVEL WEATHER MONITORING • ALERT SYSTEM • FORECAST ANALYTICS")

# =========================================================
# MAIN WEATHER CARD
# =========================================================

st.markdown(f"""
<div class='glass-card'>

<h1>{city}, INDIA</h1>

<h1 style='font-size:85px;color:#00d9ff;'>{manual_temp}°C</h1>

<h2>{weather_condition}</h2>

<h4>Feels Like {manual_temp + 2}°C</h4>

</div>
""", unsafe_allow_html=True)

# =========================================================
# METRICS
# =========================================================

m1, m2, m3, m4 = st.columns(4)

metrics = [
    ("Humidity", f"{manual_humidity}%"),
    ("Wind Speed", f"{manual_wind} km/h"),
    ("Pressure", f"{manual_pressure} hPa"),
    ("Visibility", "8 km")
]

metric_cols = [m1, m2, m3, m4]

for col, metric in zip(metric_cols, metrics):

    with col:

        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-value'>{metric[1]}</div>
            <div class='metric-label'>{metric[0]}</div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# ALERTS
# =========================================================

alerts = []

if manual_temp > 35:
    alerts.append("🔥 HIGH TEMPERATURE ALERT")

if manual_humidity > 80:
    alerts.append("💧 HIGH HUMIDITY ALERT")

if weather_condition == "Rain":
    alerts.append("🌧 RAIN ALERT")

if weather_condition == "Storm":
    alerts.append("⛈ STORM WARNING")

if manual_wind > 50:
    alerts.append("💨 HIGH WIND ALERT")

st.markdown("## ⚠ WEATHER ALERTS")

if alerts:

    for alert in alerts:

        st.markdown(f"""
        <div class='alert-box'>
            <h2>{alert}</h2>
            <h4>AI detected abnormal weather conditions.</h4>
        </div>
        """, unsafe_allow_html=True)

else:

    st.success("No dangerous weather conditions detected.")

# =========================================================
# AI PREDICTION
# =========================================================

prediction = "Weather conditions are stable."

if manual_temp > 38:
    prediction = "Possible heatwave conditions expected."

elif manual_humidity > 85:
    prediction = "High probability of rainfall."

elif manual_wind > 60:
    prediction = "Strong wind conditions may affect travel."

st.markdown("## 🤖 AI WEATHER PREDICTION")

st.markdown(f"""
<div class='ai-box'>

<h2>{prediction}</h2>

<h4>Generated using weather trend analysis.</h4>

</div>
""", unsafe_allow_html=True)

# =========================================================
# FORECAST CARDS
# =========================================================

st.markdown("## 📅 5-DAY FORECAST")

forecast_cols = st.columns(5)

for i in range(5):

    with forecast_cols[i]:

        st.markdown(f"""
        <div class='forecast-card'>

        <h3>{forecast_dates[i]}</h3>

        <h1 style='color:#ff2d75'>
        {forecast_temps[i]}°C
        </h1>

        <h4>{weather_condition}</h4>

        <p>{forecast_humidity[i]}% Humidity</p>

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# TEMPERATURE GRAPH
# =========================================================

g1, g2 = st.columns(2)

with g1:

    st.markdown("## 📈 TEMPERATURE ANALYSIS")

    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=forecast_dates,
        y=forecast_temps,
        mode='lines+markers',
        line=dict(
            color='#00d9ff',
            width=4
        )
    ))

    fig.update_layout(
        paper_bgcolor='#050816',
        plot_bgcolor='#050816',
        font=dict(color='white'),
        height=420
    )

    st.plotly_chart(fig, use_container_width=True)

# =========================================================
# HUMIDITY GRAPH
# =========================================================

with g2:

    st.markdown("## 💧 HUMIDITY ANALYSIS")

    fig2 = px.bar(
        x=forecast_dates,
        y=forecast_humidity
    )

    fig2.update_layout(
        paper_bgcolor='#050816',
        plot_bgcolor='#050816',
        font=dict(color='white'),
        height=420
    )

    st.plotly_chart(fig2, use_container_width=True)

# =========================================================
# CITY-WISE COMPARISON
# =========================================================

st.markdown("## 🌍 CITY-WISE WEATHER DISTRIBUTION")

city_data = pd.DataFrame({
    "City": [
        "Pune",
        "Mumbai",
        "Delhi",
        "Bangalore",
        "Hyderabad",
        "Chennai"
    ],
    "Temperature": [
        34,
        32,
        39,
        28,
        35,
        33
    ],
    "Humidity": [
        80,
        85,
        45,
        70,
        60,
        88
    ]
})

c1, c2 = st.columns(2)

with c1:

    city_temp_fig = px.bar(
        city_data,
        x="City",
        y="Temperature",
        title="City Temperature Distribution"
    )

    city_temp_fig.update_layout(
        paper_bgcolor='#050816',
        plot_bgcolor='#050816',
        font=dict(color='white'),
        height=420
    )

    st.plotly_chart(city_temp_fig, use_container_width=True)

with c2:

    humidity_fig = px.pie(
        city_data,
        names="City",
        values="Humidity",
        title="Humidity Distribution"
    )

    humidity_fig.update_layout(
        paper_bgcolor='#050816',
        font=dict(color='white'),
        height=420
    )

    st.plotly_chart(humidity_fig, use_container_width=True)

# =========================================================
# WEATHER ANALYTICS
# =========================================================

st.markdown("## 📊 WEATHER ANALYTICS")

a1, a2, a3, a4 = st.columns(4)

analytics = [
    ("MAX TEMP", f"{max(forecast_temps)}°C"),
    ("MIN TEMP", f"{min(forecast_temps)}°C"),
    ("AVG HUMIDITY", f"{sum(forecast_humidity)/5:.1f}%"),
    ("WIND SPEED", f"{manual_wind} km/h")
]

analytics_cols = [a1, a2, a3, a4]

for col, item in zip(analytics_cols, analytics):

    with col:

        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-value'>{item[1]}</div>
            <div class='metric-label'>{item[0]}</div>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# SAVE REPORT
# =========================================================

report_df = pd.DataFrame({
    "Day": forecast_dates,
    "Temperature": forecast_temps,
    "Humidity": forecast_humidity
})

os.makedirs("reports", exist_ok=True)

report_path = f"reports/{city}_weather_report.csv"

report_df.to_csv(report_path, index=False)

st.success(f"Forecast report saved successfully → {report_path}")

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.write(
    "Weather Forecast & Alert Application • Built using Python, Streamlit, Pandas & Plotly"
)