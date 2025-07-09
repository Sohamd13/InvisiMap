SQLMAP Web GUI – Enhanced Reporting Edition
-------------------------------------------

🛠 Built By: Soham Deshmukh
📅 Date: July 2025

🔗 Base Application:
This project is based on the open-source tool "sqlmap":
https://github.com/sqlmapproject/sqlmap

It uses the same core engine but wraps it in a more user-friendly interface for educational and practical use.

🎯 Key Modifications & Enhancements:
-------------------------------------
1. ✅ Created a Web-based GUI using Flask to run SQLMap via browser.
2. ✅ Added modern HTML/CSS interface to accept target URLs and options.
3. ✅ Captured SQLMap CLI output and displayed it in a user-friendly format.
4. ✅ Built a Visual Reporting Dashboard using Chart.js:
   - Shows a summary of detected databases via a bar chart.
5. ✅ Enabled Exporting of SQLMap results:
   - 📄 Export as CSV
   - 🧾 Export as PDF
6. ✅ Added Visual Summary to the PDF report:
   - Automatically generates a database count chart and embeds it in the PDF.
7. ✅ Ensured all inputs and outputs are encoded securely.
8. ✅ Auto-generates filenames using unique IDs.

🚀 How to Run:
--------------
1. Clone or extract the folder.
2. Install dependencies:
   pip install flask fpdf matplotlib pillow
3. Run the app:
   python app.py
4. Open your browser:
   http://127.0.0.1:5000
5. Submit a target (with URL params like ?id=1), run scan, view output.
6. Export results as CSV or PDF with chart summary.

⚠️ Disclaimer:
--------------
This tool is for educational and authorized testing only.
Do not use it against unauthorized or production systems.
You are responsible for all usage and legal compliance.

Created with ❤️ by Soham Deshmukh
