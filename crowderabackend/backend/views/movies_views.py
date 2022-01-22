from rest_framework.views import APIView
from backend import models
from backend.serializers import MovieSerializers
from rest_framework.response import Response

class GetMovies(APIView): 
    def get(self,request):
        movies=models.Movies.objects.all()
        response=MovieSerializers(movies,many=True)
        return Response(response.data)

class CreateMovies(APIView):
    def post(self,request):
        movie_request=request.data
        movie_data=MovieSerializers(data=movie_request)
        if movie_data.is_valid():
            movie_data.save()
            return Response({
                'msg':"recived"
            })
        else:
            print(movie_data.errors)
            return Response({'error':'product_data.errors'})
            
class getMovies(APIView):
    def get(self,request,pk):
        movies=models.Movies.objects.get(id=pk)
        response=MovieSerializers(movies,many=False)
        return Response(response.data)
        