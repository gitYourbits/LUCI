from rest_framework.decorators import api_view
from rest_framework.response import Response
from .main import open_vscode

# @api_view(['POST'])
# def open_project(request):
#     project_path = request.data.get('projectPath')
#     result = open_vscode(project_path)
#     return Response(result)
