from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist
from .models import Waiter
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from .models import Waiter
from .validators import validate_password

@csrf_exempt
@api_view(['POST'])
def register_waiter(request):
    if request.method == 'POST':
        data = request.data  # Use request.data for REST Framework requests
        employee_number = data.get('employee_number')
        email = data.get('email')
        password = data.get('password')

        print("Received employee_number:", employee_number)
        print("Received email:", email)
        print("Received password:", password)

        if not employee_number or not email or not password:
            return JsonResponse({'message': 'Missing data in the request.'}, status=400)

        try:
            validate_password(password)
        except ValidationError as e:
            return JsonResponse({'message': str(e)}, status=400)

        if Waiter.objects.filter(employee_number=employee_number).exists():
            return JsonResponse({'message': 'Waiter with this employee number already exists.'}, status=401)

        waiter = Waiter.objects.create_user(username=email, email=email, password=password, employee_number=employee_number)
        waiter.save()

        return JsonResponse({'message': 'Waiter registered successfully'}, status=201)
    else:
        return JsonResponse({'message': 'Method not allowed'}, status=405)


@csrf_exempt
@api_view(['POST'])
def login_waiter(request):
    if request.method == 'POST':
        data = request.data  # Use request.data for REST Framework requests
        employee_number = data.get('employee_number')
        password = data.get('password')

        # Check if employee_number or password is missing
        if not employee_number or not password:
            print("Missing employee_number or password")
            return JsonResponse({'message': 'Missing employee number or password'}, status=400)

        try:
            # Retrieve the waiter from the database using employee_number
            waiter = Waiter.objects.get(employee_number=employee_number)
            print("Retrieved waiter from database:", waiter)
        except ObjectDoesNotExist:
            print("Waiter not found in database")
            return JsonResponse({'message': 'Invalid employee number or password'}, status=401)

        # Check if the password matches
        if not waiter.check_password(password):
            print("Incorrect password")
            return JsonResponse({'message': 'Invalid employee number or password'}, status=401)

        print("Login successful")
        return JsonResponse({'message': 'Login successful'}, status=200)

    else:
        print("Received non-POST request")
        # Return a method not allowed error for non-POST requests
        return JsonResponse({'message': 'Method not allowed'}, status=405)
