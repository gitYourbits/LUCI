from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ProjectMemory
from .serializers import ProjectMemorySerializer

@api_view(['POST'])
def update_memory(request):
    project_name = request.data.get('projectName')
    project_path = request.data.get('projectPath')
    memory_data = request.data.get('memoryData')

    project, created = ProjectMemory.objects.get_or_create(
        projectName=project_name, defaults={"projectPath": project_path}
    )
    project.memoryData.update(memory_data)
    project.save()

    serializer = ProjectMemorySerializer(project)
    return Response({"message": "Memory updated successfully!", "data": serializer.data})
