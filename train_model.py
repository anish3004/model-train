import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from snowflake_config import get_connection

conn = get_connection()
query = "SELECT * FROM CUSTOMER_FEATURES;"
df = pd.read_sql(query, conn)
conn.close()
                                                            
#  Create target label (active = 1, inactive = 0)
df['IS_ACTIVE'] = ((df['LOGIN_DAYS'] >= 3) & (df['TOTAL_TRANSACTIONS'] >= 10)).astype(int)

#  Drop non-numeric columns
df['LAST_LOGIN_DATE'] = pd.to_datetime(df['LAST_LOGIN_DATE'])
df['DAYS_SINCE_LAST_LOGIN'] = (pd.Timestamp.today() - df['LAST_LOGIN_DATE']).dt.days
df = df.drop(columns=['CUSTOMER_ID', 'LAST_LOGIN_DATE'])

#  Split dataset
X = df.drop(columns='IS_ACTIVE')
y = df['IS_ACTIVE']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

#  Train Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#  Evaluate model
y_pred = model.predict(X_test)
print("Classification Report:\n")
print(classification_report(y_test, y_pred))
