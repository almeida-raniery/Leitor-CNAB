from django.contrib import admin
from django import forms
from django.urls import path
from django.shortcuts import render
from datetime import datetime

from transactions.models import Transaction
from transactions.serializers import TransactionSerializer

class CNABInportForm(forms.Form):
    cnab_file = forms.FileField()

class TransactionAdmin(admin.ModelAdmin):
    change_list_template = "transaction_change_list.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-cnab/', self.import_cnab),
        ]
        return my_urls + urls
    
    def import_cnab(self, request):
        if (request.method == "POST"):
            cnab_file = request.FILES["cnab_file"]
            self.read_cnab(cnab_file)

        form = CNABInportForm()
        payload = {"form": form}
        return render(
            request, "cnab_form.html", payload
        )
    
    def read_cnab(self, file):
        for chunk in file.chunks():
            lines = chunk.decode("utf-8").splitlines()

            for line in lines:
                line_data = {
                    "tr_type":line[0],
                    "date":line[1:9],
                    "value":line[9:19],
                    "cpf":line[19:30],
                    "card_number":line[30:42],
                    "time":line[42:48],
                    "owner":line[48:62],
                    "store":line[62:81],
                }

                line_data["value"] = int(line_data["value"])/100.0
                line_data["date"]  = datetime.strptime(line_data["date"], "%Y%m%d").strftime("%Y-%m-%d")
                line_data["time"]  = datetime.strptime(line_data["time"], "%H%M%S").strftime("%H:%M:%S")

                serializer = TransactionSerializer(data=line_data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
        

admin.site.register(Transaction, TransactionAdmin)