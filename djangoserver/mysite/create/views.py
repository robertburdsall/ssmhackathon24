from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
import json

@method_decorator(csrf_exempt, name='dispatch')
class MyJsonView(View):

    def get( self, request):
        return HttpResponse("<h1>HAPPT</h1>")
    

    def post(self, request, *args, **kwargs):
        try:

            print(request.body)
            # get json data
            json_data = json.loads(request.body.decode('utf-8'))

            # extract
            location = json_data.get('location')
            payment = json_data.get('payment')
            time = json_data.get('time')
            orderLink = json_data.get('orderLink')
            personCount = json_data.get('personCount')
            hostName = json_data.get('hostName')

            print( hostName, personCount)
            # validation 
            if not (location and payment and time and orderLink and personCount and hostName):
                return JsonResponse({'message' : 'missing required information to create group!', 'status':'error'})
        

            return JsonResponse({'message': 'Group added successfully!', 'status': "ok"})
        
        except json.JSONDecodeError:
            return JsonResponse({'message': 'Invalid JSON data!', 'status': 'error'})
        except Exception as e:
            return JsonResponse({'message':'error: who knows', 'status':'error'})