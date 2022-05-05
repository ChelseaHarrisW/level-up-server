class GameTypeView(ViewSet):
    """Level up game types"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        game_type = GameType.objects.get(pk=pk)
        serializer = GameTypeSerializer(game_type, context={'request': request})
        return Response(serializer.data)
        

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        game_types = GameType.objects.all()
        serializer = GameTypeSerializer(
            game_types, many=True, context={'request': request})
        return Response(serializer.data)

    def update(self, request, pk):
        """Handle PUT requests to get all game types

        Returns:
            Response -- 204
        """
        game_type = GameType.objects.get(pk=pk)
        game_type.label = request.data['label']
        game.save()
		
        return Response({}, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
	"""Handle DELETE requests to get all game types

        Returns:
            Response -- 204
        """
	game_type = GameType.objects.get(pk=pk)
	game_type.delete()

	return Response({}, status=status.HTTP_204_NO_CONTENT)
