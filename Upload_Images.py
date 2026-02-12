#!/usr/bin/env python3

from datetime import date
import requests
import os
import time
from Utils.ParsingDescription import parse_description
from reports import generate_report

def Upload_image_to_server(folder_path, server_url):
    if not os.path.exists(folder_path):
        print(f"❌ Error: The folder {folder_path} does not exist.")
        return
    table_rows = [["Fruit Name", "Weight", "Status Message"]]
    for filename in os.listdir(folder_path):
        # 1. Process text files first
        if filename.lower().endswith('.txt'):
            txt_path = os.path.join(folder_path, filename)
            
            # 2. Parse the description to get fruit_info
            fruit_info = parse_description(txt_path)
            
            # 3. Find the matching image (e.g., apple.txt -> apple.jpg)
            image_name = filename.replace('.txt', '.jpg')
            image_path = os.path.join(folder_path, image_name)
            
            # 4. If the image exists, upload both together
            if os.path.exists(image_path):
                with open(image_path, 'rb') as f:
                    response = requests.post(
                        server_url, 
                        files={'file': f}, 
                        data=fruit_info # fruit_info is now guaranteed to exist!
                    )
                    
                    if response.status_code == 200:
                        print(f"✅ Successfully uploaded {image_name}")
                        table_rows.append([
                    fruit_info['name'], 
                    f"{fruit_info['weight']} lbs", 
                    "Uploaded Successfully"
                ])
                    else:
                        table_rows.append([
                    fruit_info['name'], 
                    f"{fruit_info['weight']} lbs", 
                    "Failed to Upload"
                ])
                        print(f"❌ Failed to upload {image_name}: {response.text}")
                
                print("Waiting for 3 seconds...")
                time.sleep(3)
            else:
                print(f"⚠️ Warning: Found {filename} but no matching image {image_name}")
    today = date.today().strftime("%B %d, %Y")
    generate_report(
        "/tmp/processed.pdf", 
        f"Processed Update on {today}", 
        table_rows
    )
if __name__ == "__main__":
    # Correct path to your folder
    target_folder = 'Fruit_Images' 
    url = 'http://localhost:5000/upload-fruit'
    
    # Call the function
    Upload_image_to_server(target_folder, url)