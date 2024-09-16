import joblib
import scapy.all as scapy
import pandas as pd
from utils import extract_features_from_packet
'''
# Load the pre-trained model
model = joblib.load('models/ml_model.pkl')

def classify_packet(packet):
    features = extract_features_from_packet(packet)  # Custom function to extract relevant features from the packet
    features = pd.DataFrame([features])  # Convert to DataFrame for prediction
    result = model.predict(features)
    return "Attack Detected" if result == 1 else "Normal Traffic"
'''
def packet_sniffer(packet):
    #classification = classify_packet(packet)
    #print(f"Packet: {packet.summary()}, Classification: {classification}")
    
    # Log detected attacks
    #if classification == "Attack Detected":
    with open('logs/capture.pcap', 'a') as log_file:
        log_file.write(f"{packet}\n")

if __name__ == "__main__":
    print("Starting network traffic monitoring...")
    scapy.sniff(prn=packet_sniffer, store=False)  # Start sniffing live traffic
