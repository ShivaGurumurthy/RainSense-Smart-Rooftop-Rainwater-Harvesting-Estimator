import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from rainsense.data_loader import load_dataset
from rainsense.geo import get_district_state
from rainsense.estimation import estimate_rainwater, ROOF_MATERIAL_EFFICIENCY, STANDARD_ROOF_AREA, STANDARD_TANK_SIZE

df = load_dataset()

def main():
    # Read args from Electron
    locality = sys.stdin.readline().strip()
    material = sys.stdin.readline().strip()
    area = float(sys.stdin.readline().strip() or STANDARD_ROOF_AREA)

    district, state = get_district_state(locality)
    if not district or not state:
        print("Could not resolve locality.")
        return

    result = estimate_rainwater(df, state, district, area, material)
    if not result:
        print("Estimation failed.")
        return

    harvestable, annual_rainfall_mm, tank_fill, recharge = result
    print(f"Location: {district}, {state}")
    print(f"Annual Avg Rainfall: {annual_rainfall_mm:.2f} mm")
    print(f"Roof Area: {area} m²")
    print(f"Estimated Harvestable Rainwater: {harvestable/1000:.2f} KL")
    print(f"Tank Storage: {tank_fill/1000:.2f} KL")
    print(f"Groundwater Recharge: {recharge/1000:.2f} KL")

if __name__ == "__main__":
    main()