import json
from google.cloud import datastore


def readJsonFile():
    # Instantiates a client
    datastore_client = datastore.Client()

    with open("sustainable-people.json", "r") as read_file:
        data = json.load(read_file)
        
        for c in data["results"]:

            if c["is_email_confirmed"]:
                # The kind for the new entity
                kind = "Contact"
                # The name/ID for the new entity
                name = c["id"]
                # The Cloud Datastore key for the new entity
                contact_key = datastore_client.key(kind, name)
                
                # # Prepares the new entity
                contact = datastore.Entity(key=contact_key)
                contact["name"] = c["name"]
                contact["real_name"] = c["real_name"]
                contact["team_id"] = c["team_id"]
                contact["time_zone"] = c["tz_label"]
                contact["title"] = c["profile"]["title"]
                # contact["image_original"] = c["profile"]["image_original"]
                contact["email"] = c["profile"]["email"]
                contact["first_name"] = c["profile"]["first_name"]
                contact["last_name"] = c["profile"]["last_name"]

                # Saves the entity
                datastore_client.put(contact)

                print(f"Saved {contact.key.name}: {contact['real_name']}")


if __name__ == "__main__":
    print('Loading json data into cloud...')
    readJsonFile()
    
    