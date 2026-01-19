-- Top 3 models for Hyundai
SELECT * FROM (
    SELECT 'HYUNDAI' AS Manufacturer, Model, "Prod._year", COUNT(*) AS total_cars
    FROM cars_data
    WHERE Manufacturer = 'HYUNDAI'
    GROUP BY Model, "Prod._year"
    ORDER BY total_cars DESC
    LIMIT 3
) AS hyundai_models

UNION ALL

-- Top 2 models for Toyota
SELECT * FROM (
    SELECT 'TOYOTA' AS Manufacturer, Model, "Prod._year", COUNT(*) AS total_cars
    FROM cars_data
    WHERE Manufacturer = 'TOYOTA'
    GROUP BY Model, "Prod._year"
    ORDER BY total_cars DESC
    LIMIT 2
) AS toyota_models

UNION ALL

-- Top 2 models for Mercedes-Benz
SELECT * FROM (
    SELECT 'MERCEDES-BENZ' AS Manufacturer, Model, "Prod._year", COUNT(*) AS total_cars
    FROM cars_data
    WHERE Manufacturer = 'MERCEDES-BENZ'
    GROUP BY Model, "Prod._year"
    ORDER BY total_cars DESC
    LIMIT 2
) AS mercedes_models

UNION ALL

-- Top 1 model for Ford
SELECT * FROM (
    SELECT 'FORD' AS Manufacturer, Model, "Prod._year", COUNT(*) AS total_cars
    FROM cars_data
    WHERE Manufacturer = 'FORD'
    GROUP BY Model, "Prod._year"
    ORDER BY total_cars DESC
    LIMIT 1
) AS ford_models

UNION ALL

-- Top 1 model for Chevrolet
SELECT * FROM (
    SELECT 'CHEVROLET' AS Manufacturer, Model, "Prod._year", COUNT(*) AS total_cars
    FROM cars_data
    WHERE Manufacturer = 'CHEVROLET'
    GROUP BY Model, "Prod._year"
    ORDER BY total_cars DESC
    LIMIT 1
) AS chevrolet_models

UNION ALL

-- Top 1 model for BMW
SELECT * FROM (
    SELECT 'BMW' AS Manufacturer, Model, "Prod._year", COUNT(*) AS total_cars
    FROM cars_data
    WHERE Manufacturer = 'BMW'
    GROUP BY Model, "Prod._year"
    ORDER BY total_cars DESC
    LIMIT 1
) AS bmw_models

UNION ALL

-- Top 1 model for Lexus
SELECT * FROM (
    SELECT 'LEXUS' AS Manufacturer, Model, "Prod._year", COUNT(*) AS total_cars
    FROM cars_data
    WHERE Manufacturer = 'LEXUS'
    GROUP BY Model, "Prod._year"
    ORDER BY total_cars DESC
    LIMIT 1
) AS lexus_models

UNION ALL

-- Top 1 model for Honda
SELECT * FROM (
    SELECT 'HONDA' AS Manufacturer, Model, "Prod._year", COUNT(*) AS total_cars
    FROM cars_data
    WHERE Manufacturer = 'HONDA'
    GROUP BY Model, "Prod._year"
    ORDER BY total_cars DESC
    LIMIT 1
) AS honda_models

UNION ALL

-- Top 1 model for Nissan
SELECT * FROM (
    SELECT 'NISSAN' AS Manufacturer, Model, "Prod._year", COUNT(*) AS total_cars
    FROM cars_data
    WHERE Manufacturer = 'NISSAN'
    GROUP BY Model, "Prod._year"
    ORDER BY total_cars DESC
    LIMIT 1
) AS nissan_models

UNION ALL

-- Top 1 model for Volkswagen
SELECT * FROM (
    SELECT 'VOLKSWAGEN' AS Manufacturer, Model, "Prod._year", COUNT(*) AS total_cars
    FROM cars_data
    WHERE Manufacturer = 'VOLKSWAGEN'
    GROUP BY Model, "Prod._year"
    ORDER BY total_cars DESC
    LIMIT 1
) AS volkswagen_models;

-- Optional: You can also apply an ORDER BY clause at the end if needed
-- ORDER BY total_cars DESC;