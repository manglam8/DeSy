import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Load the dataset with appropriate column names
def load_data(path):
    col_names = ["duration", "protocol_type", "service", "flag", "src_bytes",
                 "dst_bytes", "land", "wrong_fragment", "urgent", "hot", 
                 "num_failed_logins", "logged_in", "num_compromised", 
                 "root_shell", "su_attempted", "num_root", "num_file_creations", 
                 "num_shells", "num_access_files", "num_outbound_cmds", 
                 "is_host_login", "is_guest_login", "count", "srv_count", 
                 "serror_rate", "srv_serror_rate", "rerror_rate", "srv_rerror_rate", 
                 "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate", 
                 "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate", 
                 "dst_host_diff_srv_rate", "dst_host_same_src_port_rate", 
                 "dst_host_srv_diff_host_rate", "dst_host_serror_rate", 
                 "dst_host_srv_serror_rate", "dst_host_rerror_rate", 
                 "dst_host_srv_rerror_rate", "label", "level"]
    
    # Read the CSV file with no header and assign the column names
    df = pd.read_csv(path, header=None, names=col_names)
    return df

# Preprocessing the dataset
def preprocess_data(df):
    # Dropping the 'level' column as it's not needed for classification
    df = df.drop('level', axis=1)
    
    # Encode categorical variables
    df = pd.get_dummies(df, columns=['protocol_type', 'service', 'flag'], drop_first=True)
    
    # Feature scaling
    scaler = StandardScaler()
    features = df.drop(['label'], axis=1)
    scaled_features = scaler.fit_transform(features)
    
    # Label encoding: 1 for attacks, 0 for normal
    df['label'] = df['label'].apply(lambda x: 0 if x == 'normal' else 1)
    
    target = df['label']
    
    return scaled_features, target

def split_data(features, target):
    # Split dataset into training and test sets
    X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.3, random_state=42)
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    df = load_data('data/NSL-KDD-Dataset.csv')
    features, target = preprocess_data(df)
    X_train, X_test, y_train, y_test = split_data(features, target)
    print(f'Training data: {X_train.shape}, Test data: {X_test.shape}')

