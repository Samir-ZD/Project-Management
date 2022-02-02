from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import User, Workspace, Tasks
from .serializers import UserSerializer, WorkspaceSerializer, TasksSerializer


#---------------------------------- GET REQUESTS ---------------------------------------------#
@api_view(['GET'])
def getData(request):
    """
    Returns all the data from the Db
    """
    user = User.objects.all()
    workspc = Workspace.objects.all()
    tasks = Tasks.objects.all()

    user_serializer = UserSerializer(user, many=True)
    workspc_serializer = WorkspaceSerializer(workspc, many=True)
    tasks_serializer = TasksSerializer(tasks, many=True)
    serializer = [user_serializer.data,
        workspc_serializer.data, tasks_serializer.data]
    return Response(serializer)


@api_view(['GET'])
def get_All_Users(request):
    """
    Returns all Users in Db
    """

    user = User.objects.all()
    user_serializer = UserSerializer(user, many=True)
    return Response(user_serializer.data)


@api_view(['GET'])
def get_All_Workspaces(request):
    """
    Returns all Workspaces in Db
    """

    workspace = Workspace.objects.all()
    wspc_serializer = WorkspaceSerializer(workspace, many=True)
    return Response(wspc_serializer.data)


@api_view(['GET'])
def get_All_Tasks(request):
    """
    Returns all Tasks in Db
    """
    tasks = Tasks.objects.all()
    tasks_serializer = TasksSerializer(tasks, many=True)
    return Response(tasks_serializer.data)


#---------------------------------- POST REQUESTS ---------------------------------------------#

@api_view(['POST'])
def createWorkspace(request):
    """
    Creates a new Workspace in Db
    """
    serializer = WorkspaceSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
