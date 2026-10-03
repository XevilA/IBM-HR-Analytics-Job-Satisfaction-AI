# 🧠 ระบบปัญญาประดิษฐ์เพื่อการวิเคราะห์ความพึงพอใจและอัตราการคงอยู่ของบุคลากร
## AI-Driven Employee Job Satisfaction & Retention Intelligence System

[![Course](https://img.shields.io/badge/รายวิชา-ปัญญาประดิษฐ์เพื่อธุรกิจดิจิทัล-12203A.svg)](https://github.com/XevilA/IBM-HR-Analytics-Job-Satisfaction-AI)
[![Semester](https://img.shields.io/badge/ภาคการศึกษา-1%2F2569-0C7C6B.svg)](https://github.com/XevilA/IBM-HR-Analytics-Job-Satisfaction-AI)
[![Team](https://img.shields.io/badge/กลุ่มโครงงาน-TEAM--99-3B5BA5.svg)](https://github.com/XevilA/IBM-HR-Analytics-Job-Satisfaction-AI)
[![Demo](https://img.shields.io/badge/ทดลองใช้งาน-Interactive%20Web%20App-FF4B4B.svg)](https://001-009-016-ib5byag38gdzr4kmjilx2h.streamlit.app/)

---

## 📌 บทสรุปสำหรับผู้บริหารและผู้ใช้งานทั่วไป (Executive Summary)

ในยุคดิจิทัล **"บุคลากร" คือสินทรัพย์ที่มีมูลค่าสูงสุดขององค์กร** แต่ปัญหาคลาสสิกที่ฝ่ายทรัพยากรบุคคล (HR) และผู้บริหารต้องเผชิญอยู่เสมอคือ **"พนักงานที่กำลังหมดไฟหรือไม่มีความสุขมักไม่แสดงออก"** และมักจะรู้ตัวอีกทีเมื่อพนักงานยื่นใบลาออกแล้ว การทำแบบประเมินความพึงพอใจประจำปียังใช้เวลามาก และพนักงานมักไม่กล้าตอบตามความเป็นจริง

โครงงานนี้จึงได้พัฒนา **ระบบปัญญาประดิษฐ์ (AI) ช่วยคัดกรองระดับความพึงพอใจในการทำงานของพนักงานล่วงหน้า** โดยนำข้อมูลพื้นฐานการทำงานที่องค์กรมีอยู่แล้ว (เช่น ฐานเงินเดือน, ประสบการณ์ทำงาน, สภาพแวดล้อม, ตำแหน่งงาน) มาประมวลผลเพื่อทำนายระดับความสุขในการทำงาน 4 ระดับ เพื่อให้ทีม HR สามารถเข้าไปดูแลและรักษาพนักงานที่มีความเสี่ยงได้ทันท่วงทีก่อนเกิดการลาออกจริง

```
[ ข้อมูลพนักงานในระบบ HR ] ──▶ [ ระบบวิเคราะห์ปัญญาประดิษฐ์ (AI) ] ──▶ [ ผลประเมินความสุข 4 ระดับ + สัญญาณเตือนล่วงหน้า ]
```

---

## 🎯 ปัญหาจริงในองค์กรและประโยชน์ที่ได้รับ (Business Challenge & Value)

| ปัญหาเดิมในองค์กร (Traditional Pain Points) | สิ่งที่ระบบ AI เข้ามาช่วยแก้ปัญหา (AI Solution) |
| :--- | :--- |
| **ดูแลคนไม่ทัน:** บริษัทมีพนักงานหลายร้อยหลายพันคน HR ไม่สามารถพูดคุยอย่างลึกซึ้งได้ทุกคนในแต่ละเดือน | **ระบบคัดกรองอัตโนมัติ:** วิเคราะห์พนักงานทั้งบริษัทได้ในเสี้ยววินาที จัดกลุ่มคนที่ต้องการความช่วยเหลือเร่งด่วน |
| **รู้ช้าเกินไป:** พนักงานสะสมความไม่พอใจทีละน้อย จนถึงจุดตัดสินใจลาออกจึงยื่นเอกสาร | **ตรวจพบสัญญาณล่วงหน้า:** ประเมินแนวโน้มความพึงพอใจ ช่วยให้ผู้จัดการเข้าพูดคุยปรับปรุงงานได้ก่อนพนักงานจะหมดใจ |
| **แบบสอบถามไม่สะท้อนความจริง:** พนักงานกังวลเรื่องผลประเมิน จึงมักตอบแบบสอบถามระดับคะแนนกลางๆ | **ประเมินจากพฤติกรรมและข้อมูลจริง:** ใช้งานข้อมูลลักษณะงาน ประสบการณ์ และสภาพแวดล้อมที่เป็นกลาง |

---

## 💡 ข้อค้นพบสำคัญจากข้อมูลที่ผู้บริหารควรรู้ (Key Business Insights)

จากการนำข้อมูลพนักงานของ IBM HR Analytics (จำนวน 1,470 คน) มาวิเคราะห์ผ่านกระบวนการ Data Science พบข้อเท็จจริงสำคัญดังนี้:

1. **เงินเดือนและตำแหน่งไม่ได้การันตีความสุขเสมอไป:**  
   พนักงานที่มีเงินเดือนสูงหรือตำแหน่งงานสูง มีสัดส่วนระดับความพึงพอใจกระจายตัวใกล้เคียงกับพนักงานทั่วไป การเพิ่มค่าตอบแทนเพียงอย่างเดียวจึงไม่ใช่วิธีแก้ปัญหาความผูกพันในองค์กรที่เบ็ดเสร็จ
2. **ความพึงพอใจเป็นตัวทำนาย "การลาออก" ที่แม่นยำที่สุด:**  
   * กลุ่มพนักงานที่มีความพึงพอใจระดับต่ำสุด (ระดับ 1) มีอัตราการลาออกสูงถึง **22.8%**
   * ขณะที่กลุ่มพนักงานที่มีความพึงพอใจสูงสุด (ระดับ 4) มีอัตราการลาออกเพียง **11.3%**  
   *(ต่างกันมากถึง **2 เท่าตัว** ยืนยันว่าการดูแลความพึงพอใจช่วยลดต้นทุนการสรรหาพนักงานใหม่ได้อย่างมีนัยสำคัญ)*

---

## 🧠 ทำความรู้จัก 4 โมเดล AI ที่พัฒนาขึ้น (The 4 AI Models Explained)

โครงการนี้ได้ทดลองสร้างและเปรียบเทียบโมเดล AI หลากหลายรูปแบบ เพื่อให้ตอบโจทย์การใช้งานของธุรกิจจริง:

```mermaid
graph TD
    A["ชุดข้อมูลพนักงาน HR"] --> B["Decision Tree<br>(ผู้เชี่ยวชาญชี้แจงเหตุผล)"]
    A --> C["Naive Bayes<br>(ผู้คำนวณสถิติแม่นยำสูงสุด)"]
    A --> D["Support Vector Machine<br>(ผู้คัดแยกกรณีซับซ้อน)"]
    A --> E["Neural Network<br>(สมองกลรองรับสเกลใหญ่)"]
    B --> F["ระบบแสดงผลแบบ Interactive ให้ HR ใช้งาน"]
    C --> F
    D --> F
    E --> F
```

1. **Decision Tree (AI แบบโครงสร้างต้นไม้ตัดสินใจ - White-Box AI):**  
   * **บทบาท:** เหมาะที่สุดสำหรับผู้บริหารที่ต้องการ **"ความโปร่งใสและอธิบายเหตุผลได้ 100%"** โมเดลจะแจกแจงเกณฑ์เป็นข้อๆ เหมือน Flowchart เช่น ดูจากระดับรายได้และช่วงอายุ
   * **ผลความแม่นยำ:** 27.55% (สอดคล้องตามที่นำเสนอในสไลด์ของกลุ่ม)
2. **Naive Bayes (AI แบบคำนวณความน่าจะเป็น):**  
   * **บทบาท:** ประมวลผลรวดเร็วมาก ให้คำตอบเป็นสัดส่วนเปอร์เซ็นต์ความน่าจะเป็นครบทั้ง 4 ระดับ เหมาะกับการทำ Dashboard มอนิเตอร์แบบ Real-time
   * **ผลความแม่นยำ:** **31.29% (มีความแม่นยำสูงสุดในการทดสอบครั้งนี้)**
3. **Support Vector Machine - SVM (AI แบบแบ่งขอบเขตพื้นที่):**  
   * **บทบาท:** เก่งในการหาเส้นแบ่งความสัมพันธ์ที่ซับซ้อน ไม่แปรปรวนง่ายตามสัญญาณรบกวนของข้อมูล
   * **ผลความแม่นยำ:** 25.85%
4. **Deep Neural Network - MLP (โครงข่ายประสาทเทียมจำลองสมองมนุษย์):**  
   * **บทบาท:** ออกแบบหลายชั้นโครงข่ายเพื่อเตรียมพร้อมสำหรับการขยายผล รองรับเมื่อองค์กรมีปริมาณข้อมูลพนักงานสะสมหลักหมื่นถึงหลักแสนคนในอนาคต
   * **ผลความแม่นยำ:** 28.91%

> *(หมายเหตุ: โจทย์นี้มี 4 ทางเลือก เกณฑ์มาตรฐานของการเดาสุ่มปกติจะอยู่ที่ 25.00% ดังนั้นทุกโมเดลที่พัฒนาขึ้นสามารถเรียนรู้รูปแบบข้อมูลได้สูงกว่าเกณฑ์สุ่มจริง)*

---

## 🖥️ วิธีการเปิดใช้งานและตรวจสอบชิ้นงาน (User & Reviewer Guide)

### 1. ทดลองใช้งานหน้าจอระบบจริง (Interactive Web Demo)
ผู้บริหารหรือผู้ใช้งานทั่วไปสามารถทดลองกรอกข้อมูลพนักงานเพื่อดูผลการประเมินได้ทันทีผ่านเว็บเบราว์เซอร์:
* 🌐 **ลิงก์ทดลองระบบ:** [คลิกเปิดระบบทดสอบออนไลน์ Streamlit](https://001-009-016-ib5byag38gdzr4kmjilx2h.streamlit.app/)
* หรือเปิดรันบนเครื่องคอมพิวเตอร์ของคุณด้วยคำสั่ง:
  ```bash
  pip install -r requirements.txt
  streamlit run app.py
  ```

### 2. เอกสารรายงานและสไลด์สรุปโครงงาน
* 📑 **สไลด์นำเสนอฉบับผู้บริหาร (PDF 11 สไลด์):** [คลิกดูเอกสารสไลด์นำเสนอ](AI_จำแนกระดับความพึงพอใจในการทำงานของพนักงาน.pdf)
* 📄 **รายงานใบงานตามรายวิชา (.doc):** บรรจุอยู่ในโฟลเดอร์ [`02_Assignment_Docs_Word/`](02_Assignment_Docs_Word/) ครบทั้ง 10 สัปดาห์ (ใบงานที่ 01 ถึง 11)

### 3. สมุดโค้ดการทดลองสำหรับนักพัฒนาและผู้ตรวจวิชาการ (Google Colab)
 อยู่ในโฟลเดอร์ [`01_Colab_Notebooks/`](01_Colab_Notebooks/) ซึ่งมีระบบ **Auto-Setup** ในตัว สามารถคลิกเปิดบน Google Colab ผ่านปุ่มด้านล่างได้ทันทีโดยไม่ต้องตั้งค่าใดๆ เพิ่มเติม:

| ลำดับงาน | ชื่อไฟล์ในระบบส่งงาน | หัวข้อการทดลอง | ลิงก์ตรงเปิด Google Colab |
|---|---|---|---|
| **รวมทุกงาน** | `ใบงานรวมโครงงาน -001,009,016.ipynb` | **Master Project (All-in-One ครบ 11 งาน)** | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/XevilA/IBM-HR-Analytics-Job-Satisfaction-AI/blob/main/01_Colab_Notebooks/%E0%B9%83%E0%B8%92%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%A3%E0%B8%A7%E0%B8%A1%E0%B9%82%E0%B8%84%E0%B8%A3%E0%B8%87%E0%B8%87%E0%B8%B2%E0%B8%99%20-001%2C009%2C016.ipynb) |
| **ใบงาน 01** | `ใบงานที่01 -001,009,016.ipynb` | การสำรวจและโหลดข้อมูลด้วย Pandas | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/XevilA/IBM-HR-Analytics-Job-Satisfaction-AI/blob/main/01_Colab_Notebooks/%E0%B9%83%E0%B8%92%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%8801%20-001%2C009%2C016.ipynb) |
| **ใบงาน 02** | `ใบงานที่02 -001,009,016.ipynb` | การกำหนดโจทย์และคลาสเป้าหมาย Machine Learning | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/XevilA/IBM-HR-Analytics-Job-Satisfaction-AI/blob/main/01_Colab_Notebooks/%E0%B9%83%E0%B8%92%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%8802%20-001%2C009%2C016.ipynb) |
| **ใบงาน 03** | `ใบงานที่03 -001,009,016.ipynb` | การทำความสะอาดและจัดเตรียมข้อมูล (Data Cleaning) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/XevilA/IBM-HR-Analytics-Job-Satisfaction-AI/blob/main/01_Colab_Notebooks/%E0%B9%83%E0%B8%92%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%8803%20-001%2C009%2C016.ipynb) |
| **ใบงาน 04** | `ใบงานที่04 -001,009,016.ipynb` | การวิเคราะห์ข้อมูลเชิงสำรวจ (Exploratory Data Analysis) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/XevilA/IBM-HR-Analytics-Job-Satisfaction-AI/blob/main/01_Colab_Notebooks/%E0%B9%83%E0%B8%92%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%8804%20-001%2C009%2C016.ipynb) |
| **ใบงาน 05** | `ใบงานที่05 -001,009,016.ipynb` | ต้นไม้ตัดสินใจ (Decision Tree Classifier) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/XevilA/IBM-HR-Analytics-Job-Satisfaction-AI/blob/main/01_Colab_Notebooks/%E0%B9%83%E0%B8%92%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%8805%20-001%2C009%2C016.ipynb) |
| **ใบงาน 06** | `ใบงานที่06 -001,009,016.ipynb` | โครงข่ายประสาทเทียม (Multi-Layer Perceptron - MLP) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/XevilA/IBM-HR-Analytics-Job-Satisfaction-AI/blob/main/01_Colab_Notebooks/%E0%B9%83%E0%B8%92%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%8806%20-001%2C009%2C016.ipynb) |
| **ใบงาน 07** | `ใบงานที่07 -001,009,016.ipynb` | ซัพพอร์ตเวกเตอร์แมชชีน (Support Vector Machine - SVM) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/XevilA/IBM-HR-Analytics-Job-Satisfaction-AI/blob/main/01_Colab_Notebooks/%E0%B9%83%E0%B8%92%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%8807%20-001%2C009%2C016.ipynb) |
| **ใบงาน 08** | `ใบงานที่08 -001,009,016.ipynb` | นาอีฟเบย์ส (Naive Bayes Classifier) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/XevilA/IBM-HR-Analytics-Job-Satisfaction-AI/blob/main/01_Colab_Notebooks/%E0%B9%83%E0%B8%92%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%8808%20-001%2C009%2C016.ipynb) |
| **ใบงาน 10** | `ใบงานที่10 -001,009,016.ipynb` | การคัดเลือกฟีเจอร์ด้วย Genetic Algorithm (GA) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/XevilA/IBM-HR-Analytics-Job-Satisfaction-AI/blob/main/01_Colab_Notebooks/%E0%B9%83%E0%B8%92%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%8810%20-001%2C009%2C016.ipynb) |
| **ใบงาน 11** | `ใบงานที่11 -001,009,016.ipynb` | การปรับแต่งและเปรียบเทียบโมเดลขั้นสุดท้าย | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/XevilA/IBM-HR-Analytics-Job-Satisfaction-AI/blob/main/01_Colab_Notebooks/%E0%B9%83%E0%B8%92%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%97%E0%B8%B5%E0%B9%8811%20-001%2C009%2C016.ipynb) |

---

## 👥 คณะผู้จัดทำ (Project Members)

**กลุ่มโครงงาน: TEAM-99**  
สาขาวิชาเทคโนโลยีธุรกิจดิจิทัล / วิทยาการคอมพิวเตอร์  
มหาวิทยาลัยเทคโนโลยีราชมงคลสุวรรณภูมิ (RMUTSB)

1. **น.ส.กมลวรรณ จันทร์ผึ้ง** (รหัสนักศึกษา: 001)
2. **น.ส.ชลดา อิศรเสนา ณ อยุธยา** (รหัสนักศึกษา: 009)
3. **น.ส.ณัฐพร เผือกผ่อง** (รหัสนักศึกษา: 016)

---
*เอกสารนี้จัดทำขึ้นเพื่อการศึกษาและการประยุกต์ใช้ปัญญาประดิษฐ์ในธุรกิจดิจิทัล ภาคการศึกษา 1/2569*
