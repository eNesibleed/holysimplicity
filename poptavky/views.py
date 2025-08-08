from django.shortcuts import render
from rest_framework import viewsets
from .models import Poptavka
from .serializers import PoptavkaSerializer
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import json

# API endpoint pro správu poptávek (např. v admin rozhraní nebo testování)
class PoptavkaViewSet(viewsets.ModelViewSet):
    queryset = Poptavka.objects.all().order_by('-datum')
    serializer_class = PoptavkaSerializer

# Vlastní endpoint pro příjem poptávky a odeslání e-mailu
@csrf_exempt
def odeslat_poptavku(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email')
            zprava = data.get('zprava')

            if not email or not zprava:
                return JsonResponse({'error': 'Chybí e-mail nebo zpráva.'}, status=400)

            send_mail(
                subject='Nová poptávka z webu HOLYSIMPLICITY',
                message=f"Email: {email}\n\nZpráva:\n{zprava}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=['holysimplicity-poptavky@seznam.cz'],
                fail_silently=False,
            )

            return JsonResponse({'success': 'Zpráva byla úspěšně odeslána.'})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Neplatný JSON.'}, status=400)
        except Exception as e:
            return JsonResponse({'error': f'Nastala chyba při odesílání e-mailu: {str(e)}'}, status=500)

    return JsonResponse({'error': 'Pouze metoda POST je povolena.'}, status=405)
