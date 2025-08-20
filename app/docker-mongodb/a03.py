import mongodb_utils

client = mongodb_utils.get_mongodb_client()
print("DB Connected successfully!")

if __name__ == "__main__":
    # Access database and collection
    print(f"Database exists? ({'marketplace'}) --", mongodb_utils.is_database_exist(client, "marketplace"))
    print(f"Database exists? ({'test'}) --", mongodb_utils.is_database_exist(client, "test"))
    print()

    db = client["test"]
    print(f"Collection exists? ({'random_collection_name'}) --",
          mongodb_utils.is_collection_exist(db, "random_collection_name"))
    print()

    collection = db["customers"]

    # Insert a single document
    doc = {"name": "John", "address": "Highway 37"}
    result = collection.insert_one(doc)
    print("Inserted record ID:", result.inserted_id)

    # Insert multiple documents
    docs = [
        {"name": "Amy", "address": "Apple st 652"},
        {"name": "Hannah", "address": "Mountain 21"},
        {"name": "Michael", "address": "Valley 345"}
    ]
    result_many = collection.insert_many(docs)
    print("Inserted record IDs:", result_many.inserted_ids)

    print()
    print(f"Collection exists? ({'customers'}) --", mongodb_utils.is_collection_exist(db, "customers"))

    db.drop_collection("customers")
