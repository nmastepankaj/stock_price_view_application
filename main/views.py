from rest_framework import viewsets
from .services import StockService
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class StockViewSet(viewsets.ViewSet):
    """
    API endpoint that allows stocks to be viewed or edited.
    """
    
    def get_top_10_stock(self, request):
        """
        Return a list of top 10 stocks.
        """
        data = StockService.get_top_10_stock()
        return Response(data, status=HTTP_200_OK)

    def get_stock_by_name(self, request, name):
        """
        get stock by name
        """
        data = StockService.get_stock_by_name(name)
        if not data:
            return Response({"message": "No data found"}, status=HTTP_400_BAD_REQUEST)
        
        return Response(data, status=HTTP_200_OK)

    def get_stock_price_history_list(self, request, id):
        """
        Return a list of stock price history.
        """
        data = StockService.get_stock_price_history_list(id)
        if not data:
            return Response({"message": "No data found"}, status=HTTP_400_BAD_REQUEST)
        
        return Response(data, status=HTTP_200_OK)
    
class FavouriteStokViewset(viewsets.ViewSet):
    """
    Viewset for Favourite Stocks
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def add_stoks_to_favourite(self, request, id):
        """
        Add stock to favourite.
        """
        status, message = StockService.add_stoks_to_favourite(id, request.user)

        if not status:
            return Response({"message": "No data found"}, status=HTTP_400_BAD_REQUEST)
        
        data={"message": message}
        return Response(data, status=HTTP_200_OK)
        
    def get_favourite_stocks(self, request):
        """
        Return a list of favourite stocks.
        """
        data = StockService.get_favourite_stocks(request.user)
        if not data:
            return Response({"message": "No data found"}, status=HTTP_400_BAD_REQUEST)
        
        return Response(data, status=HTTP_200_OK)
