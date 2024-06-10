from django.http import JsonResponse
from django.shortcuts import render
from .models import Product
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



def get_products(request):
    if request.method =='GET':
        product = Product.objects.all()
        product_list = list(product.values())
        print(product.values())
        return JsonResponse({
            "message": "Get products route is active",
            "data" : product_list
            })
    else:
        return JsonResponse({"message": "Invalid method"}, status=405)
    
    
@csrf_exempt
def add_product(request):
    if request.method == "POST":
        json_data = request.body.decode("utf-8")
        data_dict = json.loads(json_data)
        Product.objects.create(
            name = data_dict["name"],
            image_url = data_dict["image_url"],
            description = data_dict["description"],
            type = data_dict["type"],
            brand = data_dict["brand"],
            price =data_dict["price"],
            available = data_dict["available"]
        )
        return JsonResponse({
            "message": "Post added succesfully"})
    else:
        return JsonResponse({"message": "Invalid method"}, status=405)
    
    
    
@csrf_exempt
def update_product(request, pk):
    if request.method == "PUT":
        json_data = request.body.decode("utf-8")
        data_dict = json.loads(json_data)
        product = Product.objects.get(pk=pk)
        product.name = data_dict["name"]
        product.image_url = data_dict["image_url"]
        product.description = data_dict["description"]
        product.type = data_dict["type"]
        product.brand = data_dict["brand"]
        product.price = data_dict["price"]
        product.available = data_dict["available"]
        product.save()
        return JsonResponse({"message": "Product updated successfully"})
    else:
        return JsonResponse({"message": "Invalid method"}, status=405)
    
    
@csrf_exempt
def delete_product(request, pk):
    if request.method == "DELETE":
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return JsonResponse({"message": "Product deleted successfully"})
        except Product.DoesNotExist:
            return JsonResponse({"message": "Product not found"}, status=404)
    else:
        return JsonResponse({"message": "Invalid method"}, status=405)
