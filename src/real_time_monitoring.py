import scapy.all as scapy
import time
from collections import defaultdict

# Store extracted features for connections
connections = defaultdict(lambda: {
    'protocol_type': None,
    'src_bytes': 0,
    'dst_bytes': 0,
    'count': 0,
    'serror_rate': 0,   # Add more features here
    'rerror_rate': 0,
    'start_time': None
})

# Function to extract features from packet
def extract_features(packet):
    src_ip = packet[scapy.IP].src if scapy.IP in packet else None
    dst_ip = packet[scapy.IP].dst if scapy.IP in packet else None
    protocol = packet[scapy.IP].proto if scapy.IP in packet else None
    
    if src_ip and dst_ip:
        # Update connection features
        connection = connections[(src_ip, dst_ip)]
        connection['protocol_type'] = protocol
        connection['src_bytes'] += len(packet)
        connection['count'] += 1
        if connection['start_time'] is None:
            connection['start_time'] = time.time()
        
        # Compute additional features as required
        # Example: `serror_rate`, `rerror_rate`, etc.
        # These need to be computed over multiple packets
    
    return connection

# Sniffer callback function
def packet_sniffer(packet):
    connection_features = extract_features(packet)
    print(connection_features)

# Start sniffing
if __name__ == "__main__":
    print("Starting network traffic monitoring...")
    scapy.sniff(prn=packet_sniffer, store=False)
