# Entry script that should call the reporting logic from lib/report_generator.py

# TODO: Import your report generator module
# from lib.report_generator import generate_csv_report

import csv
from datetime import datetime

filename = f"report_{datetime.now().strftime('%Y%m%d')}.csv"

def main():
    with open(filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Status"])
        writer.writerow([1, "Complete"])

print(f"Report saved as {filename}")

if __name__ == "__main__":
    main()
