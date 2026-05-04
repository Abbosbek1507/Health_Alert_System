# Project Title: Health Alert Automation System

**Group Members (Group 9):**
*   Abdulaziz Abdumalikov - Logic Designer
*   Iskandar Husainov - CircuitVerse Designer
*   Abbosbek Abdumuminov - Python Developer & Documentation Lead
*   Temur Kadirov - Presenter
*   Lazizbek Sattorov - Team Member

**Course:** EEE120 Digital Design Fundamentals  
**Instructor:** Dr.Rajan  

### Problem Statement:
Hospitals and at-home patients need an automated way to evaluate multiple vital signs instantly. We are solving the problem of manual health monitoring by designing a system that automatically detects if a patient is in a critical condition (needs a doctor) or a warning condition (needs monitoring) based on 4 key symptoms.

### Inputs:
*   **A:** Severe Symptoms (1 = Yes, 0 = No)
*   **B:** High Temperature (1 = Yes, 0 = No)
*   **C:** Low Oxygen Level (1 = Yes, 0 = No)
*   **D:** High Heart Rate (1 = Yes, 0 = No)

### Outputs:
*   **Y1:** Seek Medical Help (Triggers if the patient is critical)
*   **Y0:** Monitor (Triggers if the patient needs observation but is not critical)

### Digital Logic Explanation:
Our circuit is purely combinational and uses 5 logic gates (2 AND, 2 OR, 1 NOT). 
*   **Logic for Y1 (Seek Help):** A patient needs immediate help if they have low oxygen (`C`) OR if they have both severe symptoms AND a high temperature (`A AND B`). Boolean formula: `Y1 = (A AND B) OR C`
*   **Logic for Y0 (Monitor):** A patient should be monitored if they DO NOT need immediate help (`NOT Y1`) BUT they have a high temperature OR high heart rate (`B OR D`). Boolean formula: `Y0 = NOT(Y1) AND (B OR D)`

### CircuitVerse Link:
Please see the `circuitverse_link.txt` file in the repository or click [here](https://circuitverse.org/simulator/edit/health-alert-system).

### Python Program Explanation:
The Python program implements the exact digital logic designed in CircuitVerse. It features a console-based menu system that allows users to either manually input patient data (`1` or `0`) to receive a health status or automatically generate the full 16-row Truth Table to verify the logic.

### How AI/LLM was used:
*   **NotebookLM:** Used by our presenter to organize our project data, synthesize the truth tables and logic rules, and quickly generate a structured slide deck for our final presentation.
*   **ChatGPT/LLM:** Used by our Python Developer to assist in structuring the Python code into a neat menu-driven application and formatting this `README.md` file according to the strict canvas rubric. *All group members reviewed the AI-generated code, verified it matches our manual Truth Table, and understand the logic perfectly.*

### How to Run the Python Code:
1. Make sure Python 3.x is installed on your machine.
2. Open terminal or command prompt.
3. Navigate to the `src` folder of this repository.
4. Run the command: `python main.py`
5. Follow the interactive menu on the screen.

### Screenshots & Demo Video:
*   **Circuit Design:** `/screenshots/circuit_design.png` shows our working CircuitVerse logic gate layout.
*   **Python Output:** `/screenshots/python_output.png` shows the Python console output verifying our Truth Table.
*   **Demo Video:** A short video demonstrating the working simulation can be viewed via the cloud link provided in the `demo_video_link.txt` file in this repository.

### Future Improvements:
In the future, we could add **Sequential Logic** (like a D Flip-Flop or Memory Bit) to store the patient's previous state. This would allow the system to trigger an alarm if a patient's condition *changes* from "Monitor" to "Seek Help" over time.