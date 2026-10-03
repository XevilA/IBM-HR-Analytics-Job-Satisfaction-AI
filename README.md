# 🧠 AI Multi-class Classification: Employee Job Satisfaction & Retention Analysis
### ระบบปัญญาประดิษฐ์จำแนกระดับความพึงพอใจในการทำงานและวิเคราะห์อัตราการคงอยู่ของบุคลากร

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.16%2B-orange.svg)](https://www.tensorflow.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.4%2B-F7931E.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io/)
[![Google Colab](https://img.shields.io/badge/Google%20Colab-GPU%20T4-F9AB00.svg)](https://colab.research.google.com/)

---

## 📌 ข้อมูลโครงงานและสมาชิกผู้จัดทำ (Project & Team Info)

* **รายวิชา:** 306-23-06 ปัญญาประดิษฐ์เพื่อธุรกิจดิจิทัล (Artificial Intelligence for Digital Business)
* **ภาคการศึกษา:** 1/2569 | มหาวิทยาลัยเทคโนโลยีราชมงคลสุวรรณภูมิ (RMUTSB)
* **รหัสกลุ่ม:** `TEAM-99`
* **สมาชิกในกลุ่ม:**
  1. 001 น.ส.กมลวรรณ จันทร์ผึ้ง
  2. 009 น.ส.ชลดา อิศรเสนา ณ อยุธยา
  3. 016 น.ส.ณัฐพร เผือกผ่อง

---

## 🎯 ที่มาและความสำคัญ (Business Problem & Objectives)

ความพึงพอใจในการทำงานของพนักงานเป็นปัจจัยชี้ขาดต่อความสำเร็จและอัตราการคงอยู่ของบุคลากร (Employee Retention) แต่ในองค์กรที่มีพนักงานจำนวนมาก ฝ่ายทรัพยากรบุคคล (HR) มักไม่สามารถรับรู้สัญญาณความไม่พอใจได้ทันท่วงทีจนกระทั่งพนักงานยื่นใบลาออก 

โครงงานนี้จึงพัฒนา **ระบบปัญญาประดิษฐ์แบบ Multi-class Classification** เพื่อประเมินระดับความพึงพอใจในการทำงานของพนักงาน (`JobSatisfaction`) แบ่งออกเป็น 4 ระดับ:
* **ระดับ 1:** พอใจน้อย (Low)
* **ระดับ 2:** ปานกลาง (Medium)
* **ระดับ 3:** พอใจมาก (High)
* **ระดับ 4:** พอใจมากที่สุด (Very High)

---

## 📊 ข้อมูลชุดทดลอง (Dataset Overview)

* **ชุดข้อมูล:** IBM HR Analytics Employee Attrition & Performance (`n = 1,470` แถว, `35` คอลัมน์)
* **การกระจายตัวของ Target (`JobSatisfaction`):**
  * ระดับ 1: 289 คน (19.7%)
  * ระดับ 2: 280 คน (19.0%)
  * ระดับ 3: 442 คน (30.1%)
  * ระดับ 4: 459 คน (31.2%)
* **เกณฑ์สุ่มเดาขั้นต่ำ (Baseline Threshold):** 25.00%
* **การแบ่งชุดข้อมูล:** Train 80% (1,176 คน) / Test 20% (294 คน) แบบ Stratified

---

## 🔬 ตารางสรุปผลลัพธ์การทดลองจริง (Experiment Results)

| ลำดับ | โมเดล (Model) | ไฮเปอร์พารามิเตอร์หลัก | Test Accuracy | จุดเด่นและการนำไปใช้ในธุรกิจ |
| :---: | :--- | :--- | :---: | :--- |
| **0** | **Dummy Baseline** | `most_frequent` | 25.00% | เกณฑ์มาตรฐานขั้นต่ำสำหรับการเดาสุ่ม |
| **1** | **Decision Tree** | `criterion='gini', max_depth=3` | **27.55%** (~27.6%) | **Explainable AI (White-box):** ตีความได้ชัดเจนที่สุด ปัจจัยสำคัญคือ MonthlyIncome (73.7%) และ Age (26.3%) |
| **2** | **Support Vector Machine (SVM)** | `kernel='rbf', C=1.0, StandardScaler` | **25.85%** | ความเสถียรสูง อาศัย 1,156 Support Vectors ในการกั้น Margin ขอบเขตไม่เชิงเส้น |
| **3** | **Naive Bayes (GaussianNB)** | `Gaussian Prior, 5 GA Features` | **31.29%** | **แม่นยำสูงสุด:** ให้ค่าความน่าจะเป็นครบทั้ง 4 คลาสอย่างสมดุล เหมาะกับ Real-time Scoring |
| **4** | **Deep Neural Network (MLP)** | `Dense(32-16-8-4), Dropout, GPU` | **28.91%** | จับมิติความซับซ้อนหลายชั้น รองรับการขยายสเกลเมื่อมีข้อมูลพนักงานระดับหมื่นคนขึ้นไป |

### 💡 ข้อค้นพบสำคัญเชิงธุรกิจ (Key Business Findings):
* ข้อมูล Demographic ทั่วไป (อายุ, เงินเดือน, ระดับตำแหน่ง) มีความสัมพันธ์โดยตรงกับระดับความพึงพอใจต่ำมาก ($r \approx -0.07$ ถึง $0.02$)
* **แต่ JobSatisfaction มีความสัมพันธ์ผกผันอย่างมีนัยสำคัญยิ่งยวดกับอัตราการลาออก (Attrition Rate):**
  * พนักงานกลุ่มพึงพอใจระดับ 1 (พอใจน้อย) มีอัตราการลาออกสูงถึง **22.8%**
  * พนักงานกลุ่มพึงพอใจระดับ 4 (พอใจมากที่สุด) มีอัตราการลาออกเพียง **11.3%**  
  *(ต่างกันถึง **2 เท่าตัว** พิสูจน์ว่าความพึงพอใจเป็นตัวพยากรณ์การลาออกล่วงหน้าที่แม่นยำ)*

---

## 📁 โครงสร้างไฟล์ใน Repository (Project Structure)

```text
├── 01_Colab_Notebooks/             # สมุดงาน Google Colab ครบทุกสัปดาห์ (พร้อม Auto-Setup)
│   ├── work01_Data_Loading_Pandas.ipynb
│   ├── work02_ML_Types_and_Target.ipynb
│   ├── work03_Data_Cleaning_and_Preprocessing.ipynb
│   ├── work04_Exploratory_Data_Analysis_EDA.ipynb
│   ├── work05_Decision_Tree.ipynb
│   ├── work06_Neural_Network_MLP.ipynb
│   ├── work07_Support_Vector_Machine_SVM.ipynb
│   ├── work08_Naive_Bayes.ipynb
│   ├── work10_Genetic_Algorithm_Feature_Selection.ipynb
│   ├── work11_Model_Optimization_and_Comparison.ipynb
│   └── work_all_in_one_master.ipynb # รวมทุกสัปดาห์ตั้งแต่ต้นจนจบในไฟล์เดียว
├── 02_Assignment_Docs_Word/        # เอกสารรายงานใบงานส่งอาจารย์ (.doc) ครบ 10 ใบงาน
│   ├── ใบงาน01_TEAM-99.doc ถึง ใบงาน11_TEAM-99.doc
├── 03_Trained_Models_and_Data/     # โมเดลที่เทรนสำเร็จ, ชุดข้อมูลสะอาด และกราฟสรุป
│   ├── clean.csv
│   ├── ibm_hr_job_satisfaction_tree.joblib
│   ├── ibm_hr_job_satisfaction_svm.joblib
│   ├── hr_GaussianNB.pkl
│   ├── ibm_hr_job_satisfaction_mlp.keras
│   └── job_satisfaction_model_decision.json
├── app.py                          # เว็บแอปพลิเคชัน Streamlit สำหรับทดสอบทำนาย
├── requirements.txt                # รายการไลบรารีที่จำเป็น
└── AI_จำแนกระดับความพึงพอใจในการทำงานของพนักงาน.pdf # สไลด์นำเสนอโครงงานฉบับสมบูรณ์ (11 สไลด์)
```

---

## 🚀 วิธีการติดตั้งและรันใช้งาน (Quick Start)

### 1. รันบน Google Colab:
* เปิดไฟล์ในโฟลเดอร์ `01_Colab_Notebooks/` ผ่าน Google Colab
* สามารถกด **Runtime $\rightarrow$ Run all** ได้ทันที โค้ดมีระบบ Auto-Setup ดาวน์โหลดชุดข้อมูลและสร้างโมเดลให้อัตโนมัติ

### 2. รันเว็บแอปจำลอง (Streamlit Web App) บนเครื่องของคุณ:
```bash
# โคลน Repository
git clone https://github.com/XevilA/IBM-HR-Analytics-Job-Satisfaction-AI.git
cd IBM-HR-Analytics-Job-Satisfaction-AI

# ติดตั้งไลบรารี
pip install -r requirements.txt

# สั่งรันแอป Streamlit
streamlit run app.py
```
แอปจะเปิดบนเบราว์เซอร์ที่ `http://localhost:8501` โดยสามารถเลือกเปรียบเทียบผลการทำนายได้ทั้ง 4 โมเดล (Decision Tree, SVM, Naive Bayes, Neural Network) แบบเรียลไทม์
