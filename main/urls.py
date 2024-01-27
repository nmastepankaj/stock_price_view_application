from django.urls import path, include
from .views import StockViewSet, FavouriteStokViewset


urlpatterns = [
    path('get_top10_stocks', StockViewSet.as_view({"get": "get_top_10_stock"})),
    path('get_stock_by_name/<str:name>', StockViewSet.as_view({"get": "get_stock_by_name"})), 
    path('get_stock_price_history_list/<int:id>', StockViewSet.as_view({"get": "get_stock_price_history_list"})),  
    path('add_stocks_to_favourite/<int:id>', FavouriteStokViewset.as_view({"post": "add_stoks_to_favourite"})),
    path('get_favourite_stocks', FavouriteStokViewset.as_view({"get": "get_favourite_stocks"})),
]
