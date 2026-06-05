import streamlit as st
import pandas as pd
import joblib

model = joblib.load("model/Best_model.pkl")
scaler = joblib.load("model/scaler.pkl")

st.set_page_config(
    page_title="Mobile Price Classification",
    page_icon="📱",
    layout="wide"
)

st.title("📱 Mobile Price Classification")

st.markdown("""
Predict the price category of a mobile phone based on its specifications.

### Price Categories
- 🟢 Low Cost (0)
- 🔵 Medium Cost (1)
- 🟠 High Cost (2)
- 🔴 Very High Cost (3)
""")

col1, col2 = st.columns(2)

with col1:

    battery_power = st.number_input(
        "Battery Power (mAh) : Imp feature",
        min_value=500,
        max_value=2500,
        value=1000
    )

    blue = st.selectbox(
        "Bluetooth Support",
        ["No", "Yes"]
    )

    clock_speed = st.number_input(
        "Clock Speed (GHz)",
        min_value=0.5,
        max_value=5.0,
        value=2.0
    )

    dual_sim = st.selectbox(
        "Dual SIM Support",
        ["No", "Yes"]
    )

    fc = st.number_input(
        "Front Camera (MP)",
        min_value=0,
        max_value=30,
        value=5
    )

    four_g = st.selectbox(
        "4G Support",
        ["No", "Yes"]
    )

    int_memory = st.number_input(
        "Internal Memory (GB)",
        min_value=2,
        max_value=256,
        value=64
    )

    m_dep = st.number_input(
        "Mobile Depth (cm)",
        min_value=0.1,
        max_value=1.0,
        value=0.5
    )

    mobile_wt = st.number_input(
        "Mobile Weight (grams)",
        min_value=80,
        max_value=250,
        value=150
    )

    n_cores = st.number_input(
        "Processor Cores",
        min_value=1,
        max_value=8,
        value=4
    )

with col2:

    pc = st.number_input(
        "Primary Camera (MP)",
        min_value=0,
        max_value=50,
        value=12
    )

    px_height = st.number_input(
        "Pixel Resolution Height(imp feature)",
        min_value=0,
        max_value=3000,
        value=1000
    )

    px_width = st.number_input(
        "Pixel Resolution Width(imp feature)",
        min_value=0,
        max_value=3000,
        value=1500
    )

    ram = st.number_input(
        "RAM (MB) : Imp feature",
        min_value=256,
        max_value=8000,
        value=4000
    )

    sc_h = st.number_input(
        "Screen Height (cm)",
        min_value=5,
        max_value=30,
        value=15
    )

    sc_w = st.number_input(
        "Screen Width (cm)",
        min_value=0,
        max_value=20,
        value=8
    )

    talk_time = st.number_input(
        "Talk Time (hours)",
        min_value=2,
        max_value=30,
        value=10
    )

    three_g = st.selectbox(
        "3G Support",
        ["No", "Yes"]
    )

    touch_screen = st.selectbox(
        "Touch Screen",
        ["No", "Yes"]
    )

    wifi = st.selectbox(
        "WiFi Support",
        ["No", "Yes"]
    )



blue = 1 if blue == "Yes" else 0
dual_sim = 1 if dual_sim == "Yes" else 0
four_g = 1 if four_g == "Yes" else 0
three_g = 1 if three_g == "Yes" else 0
touch_screen = 1 if touch_screen == "Yes" else 0
wifi = 1 if wifi == "Yes" else 0

if st.button("🔍 Predict Price Category"):

    input_data = pd.DataFrame([[
        battery_power,
        blue,
        clock_speed,
        dual_sim,
        fc,
        four_g,
        int_memory,
        m_dep,
        mobile_wt,
        n_cores,
        pc,
        px_height,
        px_width,
        ram,
        sc_h,
        sc_w,
        talk_time,
        three_g,
        touch_screen,
        wifi
    ]], columns=[
        'battery_power',
        'blue',
        'clock_speed',
        'dual_sim',
        'fc',
        'four_g',
        'int_memory',
        'm_dep',
        'mobile_wt',
        'n_cores',
        'pc',
        'px_height',
        'px_width',
        'ram',
        'sc_h',
        'sc_w',
        'talk_time',
        'three_g',
        'touch_screen',
        'wifi'
    ])

    # Scale Data
    scaled_data = scaler.transform(input_data)

    # Prediction
    prediction = model.predict(scaled_data)[0]

    # Probability
    probabilities = model.predict_proba(scaled_data)[0]

    labels = {
        0: "🟢 Low Cost",
        1: "🔵 Medium Cost",
        2: "🟠 High Cost",
        3: "🔴 Very High Cost"
    }

    st.success(f"Predicted Category: {labels[prediction]}")

    st.subheader("Prediction Probabilities")

    prob_df = pd.DataFrame({
        "Price Category": list(labels.values()),
        "Probability": probabilities
    })

    st.dataframe(prob_df)

    st.bar_chart(
        prob_df.set_index("Price Category")
    )