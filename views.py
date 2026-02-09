from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser])
def upload_csv(request):
    file = request.FILES.get('file')

    if not file:
        return Response({"error": "No file uploaded"})

    return Response({"message": "File uploaded successfully"})
