from scapy.all import IP, TCP, UDP

def extract_features_from_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto
        
        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
        else:
            src_port = dst_port = 0
        
        packet_length = len(packet)
        
        # Create feature vector (you can extend this with more features)
        features = [src_ip, dst_ip, proto, src_port, dst_port, packet_length]
        return features
    return None

