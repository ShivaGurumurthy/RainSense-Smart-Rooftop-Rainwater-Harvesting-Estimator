from rainsense.data_loader import load_dataset
from rainsense.geo import get_district_state
from rainsense.estimation import estimate_rainwater, ROOF_MATERIAL_EFFICIENCY, STANDARD_ROOF_AREA, STANDARD_TANK_SIZE
from rainsense.plotting import plot_monthly_rainfall, plot_rainwater_results


# Load dataset once
df = load_dataset()

def main():
    locality = input("Enter your locality (e.g., Navi Mumbai, Whitefield, Adyar): ")
    district, state = get_district_state(locality)

    if district and state:
        print(f"Resolved locality → District: {district}, State: {state}")

        material = input(f"Enter roofing material {list(ROOF_MATERIAL_EFFICIENCY.keys())}: ")
        area = float(input(f"Enter roof area in m² (default {STANDARD_ROOF_AREA}): ") or STANDARD_ROOF_AREA)

        # Run estimation
        result = estimate_rainwater(df, state, district, area, material)

        if result:
            harvestable, annual_rainfall_mm, tank_fill, recharge = result

            # Show text results
            print(f"\n Location: {district}, {state}")
            print(f"Annual Avg Rainfall: {annual_rainfall_mm:.2f} mm")
            print(f"Roof Area: {area} m²")
            print(f"Estimated Harvestable Rainwater: {harvestable/1000:.2f} KL")
            print(f"Tank Storage: {tank_fill/1000:.2f} KL")
            print(f"Groundwater Recharge: {recharge/1000:.2f} KL")

            # Show plots
            plot_monthly_rainfall(df, state, district)
            plot_rainwater_results(harvestable, annual_rainfall_mm, area, tank_size=STANDARD_TANK_SIZE)

    else:
        print(" Could not resolve your locality. Try again with a nearby city/district.")


if __name__ == "__main__":
    main()
