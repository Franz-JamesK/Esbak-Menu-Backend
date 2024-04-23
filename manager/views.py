from django.forms import ValidationError
from django.http import JsonResponse
from rest_framework import generics
from .models import Manager
from .serializers import ManagerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from .validators import validate_password
from django.core.exceptions import ObjectDoesNotExist
from manager.models import Manager  # Import the Manager model
from django.contrib.auth import get_user_model
from rest_framework import status
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from .validators import validate_password
from django.contrib.auth.hashers import make_password
from .models import Food, Drinks

@api_view(['POST'])
def ManagerRegistration(request):
    if request.method == 'POST':
        employee_number = request.data.get('employee_number')
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return JsonResponse({'message': 'Missing data in the request.'}, status=400)

        try:
            validate_password(password)
        except ValidationError as e:
            return JsonResponse({'message': str(e)}, status=400)

        # Check if a user with the email already exists
        existing_user = Manager.objects.filter(email=email).first()
        if existing_user:
            return JsonResponse({'message': 'User with this email already exists.'}, status=400)

        # Create a new user instance but don't save it to the database yet
        user = Manager.objects.create_user_with_token(employee_number, email, password)
        user.set_password(password)  # Set the hashed password

        # Save the user to the database
        user.save()
        return JsonResponse({'message': 'User registered successfully'}, status=201)


@api_view(['POST'])
def ManagerLogin(request):
    user_model = get_user_model()

    # Validate request data
    if 'employee_number' not in request.data or 'password' not in request.data:
        return Response({'message': 'Please provide both employee number and password'},
                        status=status.HTTP_400_BAD_REQUEST)

    employee_number = request.data['employee_number']
    password = request.data['password']
    user = user_model.objects.filter(employee_number=employee_number).first()

    if user and user.check_password(password):
        # Successful login
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
    else:
        # Invalid login credentials
        return Response({'message': 'Invalid employee number or password'}, status=status.HTTP_401_UNAUTHORIZED)
@csrf_exempt
@api_view(['POST'])
def add_food(request):
    if request.method == 'POST':
        name = request.data.get('name')
        description = request.data.get('description')
        price = request.data.get('price')

        if not name or not description or not price:
            return JsonResponse({'message': 'Missing data in the request. Ensure name, description, and price are provided.'}, status=400)

        food = Food.objects.create(name=name, description=description, price=price)
        food.save()

        return JsonResponse({'message': 'Food added successfully'}, status=201)

    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@csrf_exempt
@api_view(['POST'])
def add_drinks(request):
    if request.method == 'POST':
        name = request.data.get('name')
        description = request.data.get('description')
        price = request.data.get('price')

        if not name or not description or not price:
            return JsonResponse({'message': 'Missing data in the request. Ensure name, description, and price are provided.'}, status=400)

        drinks = Drinks.objects.create(name=name, description=description, price=price)
        drinks.save()

        return JsonResponse({'message': 'Drinks added successfully'}, status=201)

    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)