from django.db import models

class ProjectMemory(models.Model):
    projectName = models.CharField(max_length=255)
    projectPath = models.CharField(max_length=1024)
    lastUpdated = models.DateTimeField(auto_now=True)
    memoryData = models.JSONField(default=dict)  # Store LLM-relevant data
    
    def __str__(self):
        return self.projectName
