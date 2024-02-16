from django.db import models

class Module(models.Model):
    name = models.CharField(
        verbose_name = 'Nombre del Modulo',
        max_length= 30)
    description = models.CharField(
        verbose_name = 'Descripcion del Modulo',
        max_length = 100)
    
    def _str_(self):
        return self.name
    
    class Meta:
        verbose_name = 'modulo'
        verbose_name_plural = 'modulos'
    



class Question(models.Model):
    module = models.ForeignKey(Module, on_delete = models.CASCADE)
    question_text = models.CharField (
        null = True, blank = True,
        verbose_name ='Texto de la pregunta',
            max_length=255)
    image_text = models.ImageField(
    null = True, blank = True,
            verbose_name ='imagen de la pregunta',
            upload_to='image')
    aswer1 = models.CharField(
            verbose_name ='Respuesta A', 
            max_length= 150)
    
    aswer2 = models.CharField(
        verbose_name ='Respuesta B', 
        max_length= 150)
    aswer3 = models.CharField(
        null = True, blank = True,
        verbose_name ='Respuesta C', 
        max_length= 150)
    aswer4 = models.CharField(
        null = True, blank = True,
        verbose_name ='Respuesta D', 
        max_length= 150)
    correct = models.CharField(
        verbose_name ='Respuesta correcta',
        max_length= 5)
    
    def _str_ (self):
        return f"{self.module} + Pregunta  {self.id}"
    

    class Meta:
        verbose_name = 'pregunta'
        verbose_name_plural = 'preguntas'



