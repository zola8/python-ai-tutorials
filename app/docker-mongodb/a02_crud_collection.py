from mongodb_utils import get_mongodb_client

if __name__ == "__main__":
    try:
        client = get_mongodb_client()
        database = client["test_db"]

        database.create_collection("example_collection")
        database.create_collection("example_collection_2")

        collection_list = database.list_collections()
        for c in collection_list:
            print(c)
            collection = database[c['name']]
            collection.drop()

        print("Collections were dropped.")
        client.close()
    except Exception as e:
        raise Exception("Unable to find the document due to the following error: ", e)
