from pathlib import Path
import json
import pickle
import joblib
import pandas as pd
import numpy as np
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent

# ---------- Config & Style ----------
st.set_page_config(
    page_title="IBM HR — Job Satisfaction & Performance AI",
    page_icon="🏢",
    layout="centered"
)

LABEL_MAP = {
    1: "ระดับ 1: ต่ำ (Low)",
    2: "ระดับ 2: ปานกลาง (Medium)",
    3: "ระดับ 3: สูง (High)",
    4: "ระดับ 4: สูงมาก (Very High)"
}

FEATURES = ["JobLevel", "Age", "MonthlyIncome", "YearsAtCompany"]

# ---------- Model Loaders ----------
@st.cache_resource
def load_all_models():
    models = {}
    
    # 1. Decision Tree
    dt_path = BASE_DIR / "ibm_hr_job_satisfaction_tree.joblib"
    if dt_path.exists():
        try:
            models["Decision Tree (max_depth=3)"] = {
                "model": joblib.load(dt_path),
                "type": "tree",
                "desc": "โมเดลต้นไม้ตัดสินใจ (Explainable Rules)"
            }
        except Exception as e:
            pass

    # 2. SVM
    svm_path = BASE_DIR / "ibm_hr_job_satisfaction_svm.joblib"
    scaler_path = BASE_DIR / "ibm_hr_job_satisfaction_scaler.joblib"
    if svm_path.exists() and scaler_path.exists():
        try:
            models["Support Vector Machine (SVM RBF)"] = {
                "model": joblib.load(svm_path),
                "scaler": joblib.load(scaler_path),
                "type": "svm",
                "desc": "โมเดล SVM Kernel RBF พร้อม StandardScaler"
            }
        except Exception as e:
            pass

    # 3. Naive Bayes
    nb_path = BASE_DIR / "hr_GaussianNB.pkl"
    if nb_path.exists():
        try:
            with open(nb_path, "rb") as f:
                models["Naive Bayes (GaussianNB)"] = {
                    "model": pickle.load(f),
                    "type": "nb",
                    "desc": "โมเดลสถิติความน่าจะเป็นตามทฤษฎีเบย์ส"
                }
        except Exception as e:
            pass

    # 4. Neural Network (MLP)
    mlp_path = BASE_DIR / "ibm_hr_job_satisfaction_mlp.keras"
    if mlp_path.exists():
        try:
            import tensorflow as tf
            models["Neural Network (Deep MLP)"] = {
                "model": tf.keras.models.load_model(mlp_path),
                "type": "keras",
                "desc": "โครงข่ายประสาทเทียม Dense Layers (Keras)"
            }
        except Exception:
            pass

    return models

models_dict = load_all_models()

# ---------- Header ----------
st.title("🏢 IBM HR Analytics — Job Satisfaction AI")
st.markdown(
    "**ระบบปัญญาประดิษฐ์จำแนกระดับความพึงพอใจในการทำงานของพนักงาน**  \n"
    "*306-23-06 ปัญญาประดิษฐ์เพื่อธุรกิจดิจิทัล · มหาวิทยาลัยเทคโนโลยีราชมงคลสุวรรณภูมิ*"
)

# ---------- Model Selector ----------
available_model_names = list(models_dict.keys())
if not available_model_names:
    st.error("ไม่พบไฟล์โมเดลในโฟลเดอร์ กรุณาตรวจสอบไฟล์ .joblib / .pkl")
    st.stop()

selected_model_name = st.selectbox(
    "🤖 เลือกโมเดล AI ที่ต้องการใช้งานในการทำนาย:",
    options=available_model_names,
    index=0
)
model_info = models_dict[selected_model_name]
st.info(f"💡 {model_info['desc']}")

# ---------- Input Features ----------
st.subheader("📋 ระบุข้อมูลคุณลักษณะของพนักงาน")
col1, col2 = st.columns(2)

with col1:
    job_level = st.selectbox(
        "ระดับตำแหน่งงาน (JobLevel)",
        options=[1, 2, 3, 4, 5],
        index=0,
        help="1 = ระดับเริ่มต้น ... 5 = ระดับผู้บริหารระดับสูง"
    )
    age = st.slider("อายุ (Age)", min_value=18, max_value=60, value=35)

with col2:
    monthly_income = st.number_input(
        "เงินเดือนรายเดือน (MonthlyIncome)",
        min_value=1000,
        max_value=20000,
        value=5000,
        step=500
    )
    years_at_company = st.slider(
        "อายุงานกับบริษัท (YearsAtCompany)",
        min_value=0,
        max_value=40,
        value=5
    )

input_df = pd.DataFrame([{
    "JobLevel": job_level,
    "Age": age,
    "MonthlyIncome": monthly_income,
    "YearsAtCompany": years_at_company,
}])[FEATURES]

with st.expander("🔎 ตรวจสอบข้อมูล Input Vector ที่ส่งเข้าสู่โมเดล"):
    st.dataframe(input_df, use_container_width=True)

# ---------- Predict Button ----------
st.divider()
if st.button("🔮 ทำนายระดับความพึงพอใจ", type="primary", use_container_width=True):
    m_type = model_info["type"]
    raw_model = model_info["model"]

    pred_label = 1
    proba_list = [0.25, 0.25, 0.25, 0.25]

    try:
        if m_type == "tree":
            pred_label = int(raw_model.predict(input_df)[0])
            proba_list = list(raw_model.predict_proba(input_df)[0])
        elif m_type == "svm":
            scaler = model_info["scaler"]
            scaled_input = scaler.transform(input_df)
            pred_label = int(raw_model.predict(scaled_input)[0])
            proba_list = list(raw_model.predict_proba(scaled_input)[0])
        elif m_type == "nb":
            pred_label = int(raw_model.predict(input_df)[0])
            proba_list = list(raw_model.predict_proba(input_df)[0])
        elif m_type == "keras":
            # MinMax approximate or direct
            norm_input = input_df.copy()
            norm_input["Age"] = (norm_input["Age"] - 18) / 42.0
            norm_input["MonthlyIncome"] = (norm_input["MonthlyIncome"] - 1000) / 19000.0
            norm_input["YearsAtCompany"] = norm_input["YearsAtCompany"] / 40.0
            norm_input["JobLevel"] = (norm_input["JobLevel"] - 1) / 4.0
            prob_raw = raw_model.predict(norm_input.values, verbose=0)[0]
            proba_list = list(prob_raw)
            pred_label = int(np.argmax(prob_raw)) + 1
    except Exception as e:
        st.warning(f"เกิดข้อผิดพลาดในการทำนายแบบละเอียด: {e}")
        pred_label = int(raw_model.predict(input_df)[0])

    st.success(f"### ผลการจำแนก: **{LABEL_MAP.get(pred_label, f'ระดับ {pred_label}')}**")

    st.write("📊 **สัดส่วนความน่าจะเป็นในแต่ละระดับ (Probability Distribution):**")
    prob_display = pd.DataFrame({
        "ระดับความพึงพอใจ": [LABEL_MAP[i] for i in [1, 2, 3, 4]],
        "ความน่าจะเป็น (%)": [round(float(p) * 100, 2) for p in proba_list]
    }).set_index("ระดับความพึงพอใจ")
    st.bar_chart(prob_display)

# ---------- Comparison Tab ----------
with st.expander("📈 ดูตารางเปรียบเทียบผลการทดลองของทุกโมเดลในโครงงาน"):
    st.markdown("""
    | โมเดล (Model) | สถาปัตยกรรม / พารามิเตอร์ | Train Acc | Test Acc | จุดเด่น |
    | :--- | :--- | :---: | :---: | :--- |
    | **Decision Tree** | `max_depth=3, gini` | ~85.5% (Attr) / 27.6% (Sat) | 27.6% | เข้าใจง่าย สามารถสร้างเป็นกฎเกณฑ์ทางธุรกิจได้ |
    | **SVM (RBF Kernel)** | `StandardScaler, C=1, gamma=scale` | ~84.0% | 25.9% | ทนทานต่อมิติข้อมูล และสร้างขอบเขต Margin เหมาะสม |
    | **Naive Bayes** | `GaussianNB` | ~31.5% | 31.3% | คำนวณรวดเร็ว อิงสถิติความน่าจะเป็นตามเงื่อนไข |
    | **Deep MLP (Keras)** | `Dense(32-16-8-4), 50 epochs` | ~28.0% | 25.2% | เรียนรู้ความสัมพันธ์เชิงลึก เหมาะกับข้อมูลขนาดใหญ่ |
    """)

# ---------- Footer ----------
st.divider()
st.markdown(
    "<div style='text-align: center; color: #666; font-size: 0.9em;'>"
    "<b>ผู้จัดทำ: TEAM-99</b><br>"
    "น.ส.กมลวรรณ จันทร์ผึ้ง รหัสนักศึกษา 001<br>"
    "น.ส.ชลดา อิศรเสนา ณ อยุธยา รหัสนักศึกษา 009<br>"
    "น.ส.ณัฐพร เผือกผ่อง รหัสนักศึกษา 016<br>"
    "<i>สาขาคอมพิวเตอร์ธุรกิจ / ปัญญาประดิษฐ์เพื่อธุรกิจดิจิทัล มทร.สุวรรณภูมิ</i>"
    "</div>",
    unsafe_allow_html=True
)
