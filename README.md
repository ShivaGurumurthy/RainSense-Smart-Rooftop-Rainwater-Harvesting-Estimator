# 🌧️ RainSense: Rooftop Rainwater Harvesting Estimator

RainSense is a **Python-based Command-Line Tool (CLI)** designed to estimate rooftop rainwater harvesting potential using real rainfall datasets.  
It simplifies the traditionally complex process of calculating harvestable water by combining **scientific accuracy**, **automation**, and **user-friendly outputs**.  

Whether for **households, institutions, or urban planning authorities**, RainSense provides a quick, reproducible, and scalable way to evaluate rainwater harvesting capacity.  

---

## ✨ Features
- 🔹 **Automated Estimation** – Calculates harvestable water with minimal user input.  
- 🔹 **Scientific Accuracy** – Incorporates rainfall data, roof efficiency, absorption, and transmission losses.  
- 🔹 **Data Integration** – Uses **NetCDF rainfall datasets** for reproducibility.  
- 🔹 **Scalability** – Works from **household-level** to **district-level** analysis.  
- 🔹 **Visualization** – Generates both **text-based** and **graphical outputs** (monthly/yearly).  
- 🔹 **Lightweight CLI** – No complicated setup, runs straight in the terminal.  

---

## 📊 System Architecture
```mermaid
flowchart LR
    A["User Input"] --> B["Geo Mapper"]
    B --> C["Rainfall Data"]
    A --> D["Estimation"]
    D --> E["Tank & Recharge"]
    C --> E
    E --> F["Visualization"]
    F --> G["CLI Output<br/>(Text/Graph)"]


⸻

🛠️ Implementation Overview

RainSense is built as a modular Python project with clear separation of concerns:
	•	data_loader.py → Loads and preprocesses rainfall data from NetCDF files.
	•	geo.py → Maps user-provided location (city/district/coordinates) to dataset indices.
	•	estimation.py → Applies harvesting formula with roof efficiency, loss factors, and absorption.
	•	plotting.py → Uses matplotlib to generate graphs of rainfall vs harvested water.
	•	main.py → Entry point for the CLI interface.
	•	requirements.txt → Lists dependencies (numpy, pandas, netCDF4, xarray, matplotlib, click, rich).
	•	setup.py → Installation and packaging script.

⸻

🚀 Installation

Clone the repository and set up the environment:

# Clone repo
git clone https://github.com/your-username/rainsense.git
cd rainsense

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

# Install dependencies
pip install -r requirements.txt


⸻

▶️ Usage

Run RainSense directly from the CLI:

python main.py --location "Chennai" --roof-area 120

Example Output (Text):

Estimated Harvest: 48,500 liters/year
Storage Tank Capacity: 40,000 liters
Overflow: 8,500 liters

Example Output (Graph):
	•	Monthly rainfall vs harvested water (bar/line chart).
	•	Tank storage and overflow visualization.

⸻

🎯 Goals
	•	Develop a Python CLI tool for RRWH estimation.
	•	Automate calculations with minimal user input.
	•	Integrate NetCDF rainfall datasets for reproducibility.
	•	Provide both text and graphical outputs.
	•	Scale seamlessly from individual rooftops to district-level planning.

⸻

📚 Literature Insights

Research consistently supports RRWH as a viable solution for sustainable urban water management.
Studies highlight its role in reducing reliance on traditional sources [1–4], cost-effectiveness [7], GIS-based mapping [13–14], and smart IoT-driven monitoring [15].

RainSense builds on these findings by offering a standardized, practical, and easily deployable solution.

⸻

🤝 Contributing

Contributions are welcome! 🚀
If you’d like to improve features, fix bugs, or enhance visualizations:
	1.	Fork the repo.
	2.	Create a feature branch.
	3.	Submit a pull request.

⸻

📄 License

This project is licensed under the MIT License – see the LICENSE file for details.

⸻

👨‍💻 Authors
	•	Shiva G (2023PECCS493)
	•	Sijo Santhosh (2023PECCS498)

Department of Computer Science and Engineering
Panimalar Engineering College, Chennai, India
