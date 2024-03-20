from django.http import JsonResponse
from .models import Match
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from docu.tokens import verifyToken
from transcendence.settings import SECRET_KEY

# Create your views here.
@csrf_exempt
def allMatchs(response):
    try:
        token = response.headers['Authorization']
        pref, token = token.split(' ')
        if (pref != 'Bearer'):
            return JsonResponse({'errormsg': 'Authorization Bearer not found'})
        token_data = verifyToken(token, SECRET_KEY)
        token_data_keys = [*token_data.keys()]
        print(token_data_keys)
        if token_data_keys.count('errormsg') > 0:
            return JsonResponse(token_data)
        if not token_data_keys.count('tokentype') > 0:
            return JsonResponse({'errormsg': 'Authorization token do not include tokentype'})
        if token_data['tokentype'] != 'access':
            return JsonResponse({'errormsg': 'Authorization access not found'})

        obj = Match.objects.first()
        ret = {'name': obj.name, 'id': obj.pk,
            'player1': obj.player1.__str__(), 'player2': obj.player2.__str__(), 
            'score1': obj.score1, 'score2': obj.score2,
            'start': obj.startDate }
        return JsonResponse(ret)
    except KeyError:
        return JsonResponse({'errormsg': 'Authorization not found Key Error'})
    except ValueError:
        return JsonResponse({'errormsg': 'Authorization not found Value Error'})
