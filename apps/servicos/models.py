from django.db import models
import uuid


class Categoria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField('Categoria', max_length=30)
    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Categorias"


class Servico(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField('Servico', max_length=150)
    capa = models.ImageField(upload_to='servicos/imagens', default='servico_padrao.jpg')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='cat_servico')
    descricao = models.TextField('Descrição')
    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Serviços"


class Imagem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titulo = models.CharField('Imagem nome', max_length=15)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE, related_name='img_servico')
    imagem = models.ImageField(null=True, blank=True, upload_to='galeria/original')
    created_at = models.DateTimeField('Cadastrado em', auto_now_add=True)
    updated_at = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ["-created_at"]
        verbose_name_plural = "Imagens"

    # def save(self, *args, **kwargs):
    #     if self.image:
    #         small = rescale_image(self.image, width=100, height=100)
    #         self.image_small = SimpleUploadedFile(name, small_pic)
    #     super(Model, self).save(*args, **kwargs)