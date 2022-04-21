import json
from google.cloud import datastore


def readJsonFile():
    # Instantiates a client
    datastore_client = datastore.Client()

    with open("sustainable-people-2.json", "r") as read_file:
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
                if "name" in c:
                	contact["name"] = c["name"]
                if "real_name" in c:
                	contact["real_name"] = c["real_name"]
                if "team_id" in c:
                	contact["team_id"] = c["team_id"]
                if "time_zone" in c:
                	contact["time_zone"] = c["tz_label"]
                if "title" in c["profile"]:
                	contact["title"] = c["profile"]["title"]
                if "image_original" in c["profile"]:
                	contact["image_original"] = c["profile"]["image_original"]
                if "email" in c["profile"]:
                	contact["email"] = c["profile"]["email"]
                if "first_name" in c["profile"]:
                	contact["first_name"] = c["profile"]["first_name"]
                if "last_name" in c["profile"]:
                	contact["last_name"] = c["profile"]["last_name"]

                # Saves the entity
                datastore_client.put(contact)

                print(f"Saved {contact.key.name}: {contact['real_name']}")


if __name__ == "__main__":
    print('Loading json data into cloud...')
    readJsonFile()
    
    
