from rest_framework.response import Response
from .serializers import ArticleSerializer
from rest_framework.decorators import api_view
from .models import Article

# Create your views here.
@api_view(('GET','POST'))
def index(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        # article = Article()
        # article.title = request.POST.get('title','')
        # article.content = request.POST.get('content','')
        # article.save()
        serializer = ArticleSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)