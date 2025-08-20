from mongodb_utils import get_mongodb_client

if __name__ == "__main__":
    try:
        client = get_mongodb_client()
        database = client.get_database("marketplace")
        collection = database.get_collection("categories")
        # database = client["marketplace"]
        # collection = database["categories"]

        query = {"categoryType": "ANTIQUES_ART"}
        document = collection.find_one(query)

        print(document)

        client.close()
    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)
