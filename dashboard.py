import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
import os

FILE = "log.csv"

st.set_page_config(layout="wide")
st.title("Execution Discipline Dashboard")

# ---------------- SIDEBAR INPUT ----------------

st.sidebar.header("Log Today")

deep = st.sidebar.number_input("Deep Work Blocks", min_value=0, step=1)
escapes = st.sidebar.number_input("Escapes", min_value=0, step=1)
urges = st.sidebar.number_input("Urges Resisted", min_value=0, step=1)
output = st.sidebar.number_input("Output Count", min_value=0, step=1)
hours = st.sidebar.number_input("Study Hours", min_value=0.0, step=0.5)

if st.sidebar.button("Submit Entry"):
    today = datetime.now().strftime("%Y-%m-%d")

    new_data = pd.DataFrame(
        [[today, deep, escapes, urges, output, hours]],
        columns=[
            "date",
            "deep_blocks",
            "escapes",
            "urges_resisted",
            "output",
            "study_hours"
        ],
    )

    if os.path.exists(FILE):
        new_data.to_csv(FILE, mode="a", header=False, index=False)
    else:
        new_data.to_csv(FILE, index=False)

    st.sidebar.success("Entry Logged Successfully")

# ---------------- LOAD DATA ----------------

if os.path.exists(FILE):
    df = pd.read_csv(FILE)

    if not df.empty:

        df.columns = df.columns.str.strip()

        # Handle old schema safely
        if "study_minutes" in df.columns:
            df["study_hours"] = df["study_minutes"] / 60
            df.drop(columns=["study_minutes"], inplace=True)

        if "study_hours" not in df.columns:
            df["study_hours"] = 0.0

        df["study_hours"] = pd.to_numeric(df["study_hours"], errors="coerce").fillna(0)

        df["date"] = pd.to_datetime(df["date"])
        df = df.sort_values("date")

        # ---------------- ANALYTICS (LAST 7 DAYS) ----------------

        last7 = df.tail(7)

        avg_deep = last7["deep_blocks"].mean()
        avg_escapes = last7["escapes"].mean()
        avg_urges = last7["urges_resisted"].mean()

        if len(last7) >= 2:
            x = np.arange(len(last7))
            y = (last7["deep_blocks"] * 3
                 + last7["urges_resisted"] * 2
                 + last7["output"]
                 - last7["escapes"] * 3).values
            slope = np.polyfit(x, y, 1)[0]
        else:
            slope = 0

        variance = last7["deep_blocks"].std()

        # ---------------- LEVEL ENGINE ----------------

        if avg_deep < 1:
            level = 1
        elif avg_deep < 2:
            level = 3
        elif avg_deep >= 2 and avg_escapes > 3:
            level = 4
        elif avg_deep >= 3 and avg_escapes <= 3:
            level = 5
        elif avg_deep >= 3 and avg_urges > avg_escapes:
            level = 6
        elif avg_deep >= 4 and slope > 0:
            level = 7
        elif avg_deep >= 4 and slope > 0.5 and variance < 1:
            level = 8
        else:
            level = 4

        # ---------------- DIAGNOSIS ----------------

        if slope < 0:
            diagnosis = "Performance Declining – Avoidance Increasing"
        elif avg_escapes > 4:
            diagnosis = "High Escape Frequency – Discomfort Avoidance"
        elif variance and variance > 2:
            diagnosis = "High Variance – Inconsistent Discipline"
        elif slope > 0 and avg_deep >= 3:
            diagnosis = "Stable Growth – Execution Improving"
        else:
            diagnosis = "Structured but Fragile – Stabilize Consistency"

        # ---------------- PROGRESS ----------------

        days_completed = len(df)
        progress_percent = min((days_completed / 30) * 100, 100)

        st.subheader("30-Day Commitment Progress")
        st.progress(progress_percent / 100)
        st.write(f"Days Completed: {days_completed} / 30")
        st.write(f"Current Execution Level: {level}")
        st.write(f"Diagnosis: {diagnosis}")

        # ---------------- LEVEL BREAKDOWN ----------------

        st.write("## Execution Levels Overview")
        st.markdown("""
**Level 1 – Chaos:** No structure, no consistency.  
**Level 2 – Reactive:** High escape, emotional execution.  
**Level 3 – Inconsistent:** Some effort, unstable pattern.  
**Level 4 – Structured but Fragile:** Basic routine, relapse risk present.  
**Level 5 – Stable Execution:** Consistent 3+ deep blocks.  
**Level 6 – Self-Correcting:** Urges resisted > escapes regularly.  
**Level 7 – High Performer:** Strong upward trend, disciplined output.  
**Level 8 – Elite Discipline:** Low variance, high consistency, strong control.
""")

        # ---------------- FULL 30-DAY PLAN ----------------

        st.write("## 30-Day Execution Plan")

        st.markdown("""
### Phase 1 (Days 1–7) – Stabilization
**Do:**
- Minimum 2 deep blocks daily  
- Log every single day  
- Track escape triggers  

**Avoid:**
- System redesign  
- Productivity binge  
- Extreme restriction  

**Learn:**
- Sit with discomfort without escape  

---

### Phase 2 (Days 8–15) – Structure
**Do:**
- 3 deep blocks average  
- Define tasks before starting  
- Reduce escape count  

**Avoid:**
- Random browsing  
- Vague sessions  

**Learn:**
- Clarity reduces drift  

---

### Phase 3 (Days 16–23) – Control
**Do:**
- Urges resisted > escapes  
- Maintain positive slope  
- Analyze weak days calmly  

**Avoid:**
- Emotional collapse  
- Overcorrection  

**Learn:**
- Recovery without relapse  

---

### Phase 4 (Days 24–30) – Execution Upgrade
**Do:**
- 4 deep blocks on peak days  
- Maintain low variance  
- Increase measurable output  

**Avoid:**
- Tool upgrades  
- Structural changes  

**Learn:**
- Boredom tolerance = execution power
""")

        # ---------------- GRAPHS ----------------

        last30 = df.tail(30).reset_index(drop=True)
        day_index = np.arange(1, len(last30) + 1)

        st.subheader("Last 30 Days (Day Index View)")

        col1, col2 = st.columns(2)

        with col1:
            fig1 = plt.figure(figsize=(6,4))
            plt.plot(day_index, last30["deep_blocks"], marker="o")
            plt.xticks(day_index)
            plt.title("Deep Work Blocks")
            plt.xlabel("Day")
            plt.ylabel("Blocks")
            plt.tight_layout()
            st.pyplot(fig1)

            fig2 = plt.figure(figsize=(6,4))
            plt.plot(day_index, last30["escapes"], marker="o")
            plt.xticks(day_index)
            plt.title("Escapes")
            plt.xlabel("Day")
            plt.ylabel("Count")
            plt.tight_layout()
            st.pyplot(fig2)

        with col2:
            fig3 = plt.figure(figsize=(6,4))
            plt.plot(day_index, last30["urges_resisted"], marker="o")
            plt.xticks(day_index)
            plt.title("Urges Resisted")
            plt.xlabel("Day")
            plt.ylabel("Count")
            plt.tight_layout()
            st.pyplot(fig3)

            fig4 = plt.figure(figsize=(6,4))
            plt.plot(day_index, last30["study_hours"], marker="o")
            plt.xticks(day_index)
            plt.title("Study Hours")
            plt.xlabel("Day")
            plt.ylabel("Hours")
            plt.tight_layout()
            st.pyplot(fig4)

    else:
        st.info("No data yet. Add your first entry.")

else:
    st.info("No log file found. Add your first entry.")