# Import necessary libraries
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
headlines = pd.read_csv("path/to/financial_news.csv")
stock_data = pd.read_csv("path/to/stock_data.csv")

# Data Understanding and Descriptive Statistics
headlines['headline_length'] = headlines['headline'].apply(len)
print(headlines['headline_length'].describe())

publisher_counts = headlines['publisher'].value_counts()
print(publisher_counts)

headlines['date'] = pd.to_datetime(headlines['date'])
headlines['date'].hist()
plt.title('Publication Dates Histogram')
plt.xlabel('Date')
plt.ylabel('Frequency')
plt.show()

# Sentiment Analysis
def get_sentiment(text):
    blob = TextBlob(text)
    return blob.sentiment.polarity

headlines['sentiment'] = headlines['headline'].apply(get_sentiment)
print(headlines[['headline', 'sentiment']])

# Plot sentiment distribution
sns.histplot(headlines['sentiment'], kde=True)
plt.title('Sentiment Score Distribution')
plt.xlabel('Sentiment Score')
plt.ylabel('Frequency')
plt.show()

# Correlation Analysis
combined_data = pd.merge(stock_data, headlines, on='stock', how='inner')
combined_data['date'] = pd.to_datetime(combined_data['date'])

correlation = combined_data.groupby('stock').apply(lambda x: x['sentiment'].corr(x['stock_price']))
print(correlation)

# Publisher Analysis
publisher_analysis = headlines['publisher'].value_counts()
print(publisher_analysis)

# Topic Modeling (Optional)
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation

count_vectorizer = CountVectorizer(max_df=0.95, min_df=2, stop_words='english')
dtm = count_vectorizer.fit_transform(headlines['headline'])

lda = LatentDirichletAllocation(n_components=10, random_state=42)
lda.fit(dtm)

for index, topic in enumerate(lda.components_):
    print(f"TOPIC #{index}")
    print([count_vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]])
