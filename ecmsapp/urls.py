from django.urls import path
from ecmsapp import views
from .Code import Accounts,Cleaning,Enviroments,Houses,Payments,Renter,Reports,Transactions


urlpatterns = [
    path('', views.index, name='index'),

    path('login/', Accounts.login, name='login'),
    path('register/', Accounts.register, name='register'),
    path('forgot/', Accounts.forgot, name='forgot'),
    path('staffs/', Accounts.staffs, name='staffs'),

    path('fetch_data/',Houses.fetch_data, name='fetch_data'),


    #region Environment

    path('house/', Houses.house, name='house'),
    path('createHouse/', Houses.createHouse, name='createHouse'),
    path('updateHouse/', Houses.update_house, name='updateHouse'),
    path('deleteHouse/', Houses.delete_house, name='deleteHouse'),




    path('Renter/', Renter.renter, name='Renter'),
    path('updateRenter/', Renter.update_renter, name='updateRenter'),


    path('Enviroment/', Enviroments.enviroment, name='Enviroment'),

    #endregion





    path('cleaning/', Cleaning.cleaning, name='cleaning'),
    
    path('reports/', Reports.reports, name='reports'),
    path('Payment_Method/', Payments.Payment_Method, name='Payment_Method'),
    path('Transaction/', Transactions.Transaction, name='Transaction'),
    path('Reports2/', Reports.Reports2, name='Reports2'),
]