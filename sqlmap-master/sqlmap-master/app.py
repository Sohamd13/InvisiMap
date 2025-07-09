from flask import Flask, render_template, request, send_file
import subprocess
import csv
from fpdf import FPDF
import uuid
import os

app = Flask(__name__)

# Ensure exports folder exists
if not os.path.exists('exports'):
    os.makedirs('exports')

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        target_url = request.form['url']
        option = request.form['option']
        command = ['python', 'sqlmap.py', '-u', target_url, '--batch']

        if option == 'dbs':
            command.append('--dbs')
        elif option == 'dump':
            command.append('--dump')

        try:
            result = subprocess.check_output(command, stderr=subprocess.STDOUT, text=True, timeout=120)
        except subprocess.CalledProcessError as e:
            result = f"Error:\n{e.output}"
        except subprocess.TimeoutExpired:
            result = "Scan timed out."

    return render_template('index.html', result=result)

@app.route('/export', methods=['POST'])
def export():
    output = request.form['raw_output']
    export_type = request.form['export_type']
    filename_base = f"exports/output_{uuid.uuid4().hex[:6]}"

    if export_type == 'csv':
        filename = f"{filename_base}.csv"
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            for line in output.splitlines():
                writer.writerow([line])
        return send_file(filename, as_attachment=True)

    elif export_type == 'pdf':
        filename = f"{filename_base}.pdf"

    # === STEP 1: Extract database names from SQLMap output ===
        db_names = []
        for line in output.splitlines():
            line = line.strip()
            if line.startswith("[*]"):
                db_name = line[4:].strip()
                db_names.append(db_name)

    # If no real DB names found, fallback to dummy
        if not db_names:
            db_names = ['NoDB']
        db_count = [1] * len(db_names)

    # === STEP 2: Generate the chart ===
        import matplotlib.pyplot as plt
        chart_path = 'chart.png'
        plt.figure(figsize=(6, 4))
        plt.bar(db_names, db_count, color='skyblue')
        plt.title('Databases Detected')
        plt.ylabel('Count')
        plt.savefig(chart_path)
        plt.close()

    # === STEP 3: Add chart and output text to PDF ===
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Courier", size=10)

    # Add the chart image
        pdf.image(chart_path, x=10, y=10, w=180)
        pdf.ln(65)  # adjust for image height

    # Add raw SQLMap output
        for line in output.splitlines():
            pdf.cell(0, 8, line.encode('latin-1', errors='replace').decode('latin-1'), ln=True)

        pdf.output(filename)

        return send_file(filename, as_attachment=True)



    return "Invalid export type", 400

if __name__ == '__main__':
    app.run(debug=True)
