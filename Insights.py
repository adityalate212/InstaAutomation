# Import required libraries
from google.oauth2 import service_account
from googleapiclient.discovery import build
import pandas as pd
import matplotlib.pyplot as plt

# Define API credentials and properties
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
KEY_FILE_LOCATION = '<path_to_credentials_file>'
VIEW_ID = '<view_id>'
METRICS = [{'expression': 'ga:pageviews'}]
DIMENSIONS = [{'name': 'ga:date'}]
START_DATE = '30daysAgo'
END_DATE = 'today'

# Authenticate with the Google Analytics API
credentials = service_account.Credentials.from_service_account_file(
    KEY_FILE_LOCATION, scopes=SCOPES)
analytics = build('analyticsreporting', 'v4', credentials=credentials)

# Query the Google Analytics API for traffic data
response = analytics.reports().batchGet(
    body={
        'reportRequests': [{
            'viewId': VIEW_ID,
            'dateRanges': [{'startDate': START_DATE, 'endDate': END_DATE}],
            'metrics': METRICS,
            'dimensions': DIMENSIONS
        }]
    }
).execute()

# Extract data from the API response and transform it into a pandas dataframe
data = []
for report in response.get('reports', []):
    rows = report.get('data', {}).get('rows', [])
    for row in rows:
        date = row.get('dimensions', [])[0]
        pageviews = int(row.get('metrics', [])[0]['values'][0])
        data.append({
            'date': date,
            'pageviews': pageviews
        })

df = pd.DataFrame(data)

# Convert date string to datetime object and set it as the index
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
df.set_index('date', inplace=True)

# Plot the data in a line graph using Matplotlib
plt.plot(df.index, df['pageviews'])
plt.xlabel('Date')
plt.ylabel('Pageviews')
plt.title('One Piece Astrology Website Traffic')
plt.show()
