import sqlite3
from pathlib import Path

import pandas as pd

# Path to the SQLite database file (relative to repo root)
db_path = "data/modified_cars_data.db"

# Optional: export the final 14-car selection for easy sharing / Tableau reconnects
export_csv_path = "data/final_selected_14.csv"
try:
    # Create a connection to the SQLite database
    # (Resolve to an absolute path so the script works no matter where it's launched from.)
    repo_root = Path(__file__).resolve().parents[1]
    resolved_db_path = (repo_root / db_path).resolve()
    conn = sqlite3.connect(str(resolved_db_path))

    # Load the entire cars_data table into a DataFrame
    df = pd.read_sql_query("SELECT * FROM cars_data", conn)

    # Close the database connection
    conn.close()

    # Filter data to get the top models for each manufacturer
    manufacturers = ['HYUNDAI', 'TOYOTA', 'MERCEDES-BENZ', 'FORD', 'CHEVROLET', 'BMW', 'LEXUS', 'HONDA', 'NISSAN', 'VOLKSWAGEN']
    selected_cars = []

    # Loop through each manufacturer to find the top models
    for manufacturer in manufacturers:
        # Filter rows for the current manufacturer
        manufacturer_df = df[df['Manufacturer'] == manufacturer]

        # Group by Model and Prod._year, then count total cars for each group
        top_models = manufacturer_df.groupby(['Model', 'Prod._year']).size().reset_index(name='total_cars')

        # Sort by total_cars in descending order to get top models
        top_models = top_models.sort_values(by='total_cars', ascending=False)

        # Determine the number of top models to select based on the manufacturer
        if manufacturer == 'HYUNDAI':
            top_n = 3
        elif manufacturer == 'TOYOTA':
            top_n = 2
        elif manufacturer == 'MERCEDES-BENZ':
            top_n = 2
        else:
            top_n = 1

        # Select the top models based on the defined number
        top_models = top_models.head(top_n)

        # For each selected model, find the exact car(s) in the original DataFrame
        for _, row in top_models.iterrows():
            model, year = row['Model'], row['Prod._year']
            filtered_cars = manufacturer_df[(manufacturer_df['Model'] == model) & (manufacturer_df['Prod._year'] == year)]

            # Apply the price filter to ensure cars are sellable for middle-class individuals (max price $20,000)
            filtered_cars = filtered_cars[filtered_cars['Price'] <= 20000]

            # If no cars meet the price condition, continue to the next model
            if filtered_cars.empty:
                continue

            # Sort by criteria: Mileage (ascending), Production Year (descending), Airbags (descending), Price (ascending)
            filtered_cars = filtered_cars.sort_values(by=['Mileage', 'Prod._year', 'Airbags', 'Price'], ascending=[True, False, False, True])

            # Select the best car based on the sorting criteria and get its ID
            selected_car_id = filtered_cars.iloc[0]['ID']  # Assuming 'ID' is the unique identifier column
            selected_cars.append({
                'Manufacturer': manufacturer,
                'Model': model,
                'Prod._year': year,
                'Mileage': filtered_cars.iloc[0]['Mileage'],
                'Airbags': filtered_cars.iloc[0]['Airbags'],
                'Price': filtered_cars.iloc[0]['Price'],
                'ID': selected_car_id
            })

    # Convert the list of selected cars to a DataFrame for easier viewing
    selected_cars_df = pd.DataFrame(selected_cars)

    # Friendly formatting for display (does not change the underlying data)
    if not selected_cars_df.empty and "Price" in selected_cars_df.columns:
        selected_cars_df["Price_fmt"] = selected_cars_df["Price"].apply(
            lambda x: f"${x:,.0f}" if pd.notna(x) else x
        )

    # Export a CSV copy (handy for Tableau and for GitHub viewers)
    export_path = (repo_root / export_csv_path).resolve()
    export_path.parent.mkdir(parents=True, exist_ok=True)
    selected_cars_df.to_csv(export_path, index=False)

    # Display the result
    print(selected_cars_df)
    print(f"\nSaved: {export_path}")

    # Quick data-quality flags (informational only)
    if not selected_cars_df.empty and "Price" in selected_cars_df.columns:
        suspicious = selected_cars_df[(selected_cars_df["Price"] < 1000) | (selected_cars_df["Price"] > 200000)]
        if not suspicious.empty:
            print("\nNote: Some selected rows have unusually low/high 'Price' values.")
            print("This may be due to how the source dataset encodes price for certain listings.")
            print("If you want, we can add a cleaning rule (e.g., exclude prices < 1000) — but that will change the final 14 cars.")

except sqlite3.OperationalError as e:
    print(f"Error: {e}")


