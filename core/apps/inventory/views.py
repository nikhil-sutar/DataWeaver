from django.http import HttpResponse
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from apps.inventory.serializers import ItemSerializer
from apps.inventory.models import Item
from apps.inventory.filters import ItemFilter
from apps.inventory.utils.reports import generate_pdf_report, generate_excel_report
# Create your views here.
import logging

logger = logging.getLogger(__name__)

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    filterset_class = ItemFilter

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        logger.info(f"Item added: {serializer.data['name']}")

        return Response({
            "message":"Item added successfully.",
            "data":serializer.data
        },status=status.HTTP_201_CREATED) 
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial',False)
        instance = self.get_object()
        serializer = self.get_serializer(instance,data=request.data,partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        logger.info(f"Item updated: {instance.name}")

        return Response({
            "message":"Item updated successfully.",
            "data":serializer.data
        },status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        item_name = instance.name
        self.perform_destroy(instance)
        logger.info(f"Item deleted: {item_name}")
        
        return Response({
            "message":f"Item {item_name} deleted successfully."
        },status=status.HTTP_200_OK)
    
    @action(detail=False,methods=['get'],url_path='export/pdf')
    def export_pdf(self,request):
        items = self.filter_queryset(self.get_queryset())
        pdf_file = generate_pdf_report(items)

        response = HttpResponse(pdf_file,content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="items_report.pdf"'
        return response
    
    @action(detail=False, methods=['get'],url_path='export/excel')
    def export_excel(self, request):
        items = self.filter_queryset(self.get_queryset())
        excel_file = generate_excel_report(items)
        
        response = HttpResponse(
            excel_file,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename="items_report.xlsx"'
        return response
