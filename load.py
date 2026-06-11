# load_correct.py
# Purpose: Send cleaned data from Python to PostgreSQL

import pandas as pd
from sqlalchemy import create_engine
from logger_config import logger
import config

# Step 1: Read the cleaned CSV file
df = pd.read_csv('cleaned_ecommerce_data.csv')
print(f"Read {len(df)} rows from CSV")

# Step 2: Create a connection string (telling Python where PostgreSQL is)
# Format: postgresql://username:password@host:port/database_name

try:
	logger.info("loading successfully")
	connection_string = f"postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}:{config.DB_PORT}/{config.DB_NAME}"

# Step 3: Create an engine (this is like a bridge between Python and PostgreSQL)
	engine = create_engine(connection_string)

# Step 4: Send the DataFrame to PostgreSQL
# 'sales' = table name
# engine = the bridge
# if_exists='replace' = delete old table if exists, create new one
# index=False = don't save row numbers
	df.to_sql('sales', engine, if_exists='replace', index=False)
	
# Step 5: Close the connection
	engine.dispose()


except Exception as e:
	logger.error(f"loading failed:{e}")


