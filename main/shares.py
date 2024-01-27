import requests
import zipfile
import io
import pandas as pd
import datetime
from main.models import Stock, Company

class StockData:
    """Service for getting stock bhavcopy"""
    
    @staticmethod
    def save_data(df, date):
        """Save data into database"""

        if df is None:
            return
        
        stock_list = []
        for index, row in df.iterrows():
            company, created = Company.objects.get_or_create(name=row['SC_NAME'])
            stock = Stock(
                company=company,
                date=date,
                open=row['OPEN'],
                close=row['CLOSE'],
                high=row['HIGH'],
                low=row['LOW'],
                last=row['LAST'],
                prev_close=row['PREVCLOSE'],
                no_trades=row['NO_TRADES'],
                no_of_shrs=row['NO_OF_SHRS'],
                net_turnover=row['NET_TURNOV']
            )
            stock_list.append(stock)
        
        Stock.objects.bulk_create(stock_list)

    @staticmethod
    def download_and_extract_zip(url, file_name):
        """Download and extract zip from bseindia and save them to csv file in extracted data folder"""

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, headers=headers, allow_redirects=True)

        
        if response.status_code == 200:
            with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
                # Assuming there is only one CSV file in the ZIP, get its name
                csv_file_name = zip_ref.namelist()[0]
                # Extract the CSV file from the ZIP
                with zip_ref.open(csv_file_name) as file:
                    # Read CSV file into a pandas DataFrame
                    df = pd.read_csv(file)
                    # write data to csv file and store in extracted_data foleder
                    df.to_csv(f'extracted_data/{file_name}')
                    return df       
        else:
            print(f"Failed to download ZIP file. Status code: {response.status_code}")
            return None

    @classmethod
    def refresh_data(cls):
        """Function fill update the data in database for last 50 days"""

        base_url = "https://www.bseindia.com/download/BhavCopy/Equity/"
        current_date = datetime.date.today()

        for i in range(50):
            if Stock.objects.filter(date=current_date).exists():
                current_date -= datetime.timedelta(days=1)
                continue
            print(f"Downloading data for {current_date}")
            date_str = current_date.strftime("%d%m%y")
            file_name = f"EQ{date_str}.CSV"
            stock_url = f"{base_url}EQ{date_str}_CSV.ZIP"
            df = cls.download_and_extract_zip(stock_url, file_name)
            cls.save_data(df, current_date)
            current_date -= datetime.timedelta(days=1)


