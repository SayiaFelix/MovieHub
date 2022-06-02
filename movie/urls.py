from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', include('youtube.urls')),
]

admin.site.site_header= "Sir LoRa Movie Administration"
admin.site.site_title="SiR LoRa"
admin.site.index_title="Welcome to Sir LoRa Movie administration"