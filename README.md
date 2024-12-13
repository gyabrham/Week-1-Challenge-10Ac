# Financial News Sentiment and Stock Price Correlation Analysis

## Introduction
Nova Financial Solutions aims to enhance its predictive analytics capabilities by analyzing financial news sentiment and its correlation with stock market movements. This project focuses on performing sentiment analysis on financial news headlines and establishing correlations between news sentiment and stock price movements.

## Dataset Overview
### Financial News and Stock Price Integration Dataset (FNSPID)
- **headline**: Title of the news article.
- **url**: Link to the full news article.
- **publisher**: Author/creator of the article.
- **date**: Publication date and time (UTC-4).
- **stock**: Stock ticker symbol (e.g., AAPL: Apple).

## Methodology
### Data Understanding
- Loaded and explored the dataset to understand its structure and content.

### Exploratory Data Analysis (EDA)
#### Descriptive Statistics
- Calculated basic statistics for headline lengths.
- Counted the number of articles per publisher.
- Analyzed publication dates for trends.

#### Text Analysis
- Performed sentiment analysis on headlines.
- Conducted topic modeling to identify common themes.

#### Time Series Analysis
- Examined publication frequency over time.
- Analyzed specific publishing times.

#### Publisher Analysis
- Identified top contributors to the news feed.

### Statistical Correlation Analysis
- Merged sentiment scores with stock price data.
- Established statistical correlations between news sentiment and stock price movements.

## Python Code Implementation
### Setup and Installation
1. **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```
2. **Activate the virtual environment:**
    - On Windows:
        ```bash
        .\venv\Scripts\Activate.ps1
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
3. **Install required packages:**
    ```bash
    pip install -r requirements.txt
    ```

### Requirements
Create a `requirements.txt` file with the following contents:
```plaintext
yfinance
TA-Lib
pandas
matplotlib
plotly
pyfolio-reloaded
zipline-reloaded
