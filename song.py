# Write your code here!
class Song:
    def __init__(self, name, artist, length):
        """
        Inicializa los atributos de la canción.
        """
        self.name = name
        self.artist = artist
        self.length = length

    def get_length_in_seconds(self):
        """
        Convierte la duración de minutos (float) a segundos.
        1 minuto = 60 segundos.
        """
        return self.length * 60