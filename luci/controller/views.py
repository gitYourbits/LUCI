from rest_framework.decorators import api_view
from rest_framework.response import Response
from memory.models import ProjectMemory

@api_view(['POST'])
def getProject(request):
    project_name = request.data.get('projectName')

    try:
        project = ProjectMemory.objects.get(projectName=project_name)
        return Response({"projectPath": project.projectPath})
    except ProjectMemory.DoesNotExist:
        return Response(status=404)
