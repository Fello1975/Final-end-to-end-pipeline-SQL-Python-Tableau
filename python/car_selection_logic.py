import sqlite3
import pandas as pd

# Path to the SQLite database file
db_path = "data/modified_cars_data.db"
try:
    # Create a connection to the SQLite database
    conn = sqlite3.connect(db_path)

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

    # Display the result
    print(selected_cars_df)

except sqlite3.OperationalError as e:
    print(f"Error: {e}")

