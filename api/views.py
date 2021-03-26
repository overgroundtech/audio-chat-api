from django.http import JsonResponse, HttpResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import VoiceGrant
from twilio.twiml.voice_response import VoiceResponse, Dial


def obtain_token(request):
    if request.method == "GET":
        voice_grant = VoiceGrant(
            outgoing_application_sid=settings.TWIML_APPLICATION_SID,
            incoming_allow=True,
        )
        access_token = AccessToken(
            settings.TWILIO_ACCOUNT_SID,
            settings.API_KEY,
            settings.API_SECRET,
        )
        access_token.add_grant(voice_grant)

        token = access_token.to_jwt()

        return JsonResponse({'token': token.decode('utf-8')})


@csrf_exempt
def conference_call(request):
    response = VoiceResponse()
    room_name = request.POST['roomName']
    dial = Dial()
    dial.conference(room_name)
    response.append(dial)
    return HttpResponse(response.to_xml(), content_type='text/xml')
