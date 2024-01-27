from .models import Stock, Company, FavouriteStock
import datetime
from .serializers import StockSerializer, CompanySerializer, FavouriStockSerializer
from rest_framework.authtoken.models import Token



class StockService:
    """Service class for Stock."""

    @classmethod
    def get_top_10_stock(cls):
        """
        Return a list of top 10 stocks.
        """
        date = Stock.objects.all().order_by('date').first().date
        print(date)
        data = Stock.objects.filter(date=date).order_by('-net_turnover')[:10]
        serializer = StockSerializer(data, many=True)
        return serializer.data
    
    @classmethod
    def get_stock_by_name(cls, name):
        """
        get stock by name
        """
        stocks = Company.objects.filter(name__contains=name)
        serializer = CompanySerializer(stocks, many=True)
        return serializer.data
    
    @classmethod
    def get_stock_price_history_list(cls, id):
        """
        Return a list of stock price history.
        """
        company = Company.objects.filter(id=id).first()
        if not company:
            return None
        
        stocks = Stock.objects.filter(company=id).order_by('-date')
        serializer = StockSerializer(stocks, many=True)
        return serializer.data
    
    @classmethod
    def add_stoks_to_favourite(cls, id, user):
        """
        Add stocks to favourite.
        """
        company = Company.objects.filter(id=id).first()
        if not company:
            return False, "Company does not exists"
        try: 
            print(FavouriteStock.objects.filter(user= user, stock= company).exists())
            if FavouriteStock.objects.filter(user= user, stock= company).exists():
                FavouriteStock.objects.filter(user= user, stock= company).delete()
                return True, "Stock Remove from favourite"
            
            FavouriteStock.objects.create(user= user, stock= company)
            return True, "Stock Added to favourite"
        except:
            return False, "There is some error"
    
    @classmethod
    def get_favourite_stocks(cls, user):
        """
        Get favourite stocks.
        """
        stocks = FavouriteStock.objects.filter(user=user)
        serializer = FavouriStockSerializer(stocks, many=True)
        return serializer.data  
    


class AuthService:
    """Service class for Auth."""
    @classmethod
    def generate_token(cls, user):
        """
        Generate token.
        """
        token, created = Token.objects.get_or_create(user=user)
        return token.key
        