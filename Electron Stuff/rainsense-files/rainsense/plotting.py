import matplotlib.pyplot as plt

def plot_rainwater_results(harvestable, annual_rainfall_mm, roof_area, tank_size=1000):
    tank_fill = min(harvestable, tank_size)
    recharge = max(0, harvestable - tank_size)

    categories = ['Tank Storage', 'Groundwater Recharge']
    values = [tank_fill, recharge]

    plt.figure(figsize=(7,5))
    bars = plt.bar(categories, values, color=['steelblue', 'seagreen'], alpha=0.8)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, height + 100, f"{height:.0f} L",
                 ha='center', va='bottom', fontsize=10, fontweight='bold')

    plt.title(f"Rainwater Harvesting Potential\nRainfall: {annual_rainfall_mm:.1f} mm | Roof Area: {roof_area} m²",
              fontsize=12, fontweight='bold')
    plt.ylabel("Water (Liters)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()


def plot_monthly_rainfall(df, state, district):
    record = df[(df["STATE_UT_NAME"].str.lower() == state.lower()) &
                (df["DISTRICT"].str.lower() == district.lower())]

    if record.empty:
        return None

    months = ["JAN","FEB","MAR","APR","MAY","JUN",
              "JUL","AUG","SEP","OCT","NOV","DEC"]
    values = [float(record[m].values[0]) for m in months]

    plt.figure(figsize=(10,6))
    plt.bar(months, values, color="skyblue")
    plt.title(f"Monthly Average Rainfall in {district}, {state}")
    plt.ylabel("Rainfall (mm)")
    plt.show()
