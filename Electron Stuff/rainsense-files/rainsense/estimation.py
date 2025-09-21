# Efficiency and constants
ROOF_MATERIAL_EFFICIENCY = {'concrete': 0.85, 'metal': 0.95, 'tile': 0.80}
PIPE_LOSS = 0.95
ABSORPTION_LOSS = 0.90
STANDARD_TANK_SIZE = 1000   # Liters
STANDARD_ROOF_AREA = 100    # m²

def estimate_rainwater(df, state, district, roof_area, material, tank_size=STANDARD_TANK_SIZE):
    """
    Estimate annual harvestable rainwater for given district & state.
    """
    record = df[(df["STATE_UT_NAME"].str.lower() == state.lower()) &
                (df["DISTRICT"].str.lower() == district.lower())]

    if record.empty:
        print(f"No rainfall data found for {district}, {state}.")
        return None

    annual_rainfall_mm = float(record["ANNUAL"].values[0])
    volume_liters = annual_rainfall_mm * roof_area

    efficiency = (ROOF_MATERIAL_EFFICIENCY[material] * PIPE_LOSS * ABSORPTION_LOSS)
    harvestable = volume_liters * efficiency

    tank_fill = min(harvestable, tank_size)
    recharge = max(0, harvestable - tank_size)

    return harvestable, annual_rainfall_mm, tank_fill, recharge
