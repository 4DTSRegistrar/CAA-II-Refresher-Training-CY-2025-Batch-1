import pandas as pd
import qrcode
import os

# Load student data
df = pd.read_csv("certificates.csv")

# Ensure folder exists
if not os.path.exists("qr_codes"):
    os.makedirs("qr_codes")

# Generate QR per batch
batches = df['batch_id'].unique()

for batch in batches:
    # Correct repo name + id parameter
    url = f"https://4dtsregistrar.github.io/CAA-II-Refresher-Training-CY-2025-Batch-1/verify.html?id={batch}"
    img = qrcode.make(url)

    # Save file as qr_codes/<batch_id>.png
    img.save(f"qr_codes/{batch}.png")

    print(f"QR for {batch} generated: {url}")
