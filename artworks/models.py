from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=250)
    description = models.TextField(verbose_name='Описание')
    url = models.SlugField(max_length=180, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Категории"


class Technic(models.Model):
    name = models.CharField(verbose_name="Техника работы", max_length=250)
    description = models.TextField(verbose_name='Описание')
    url = models.SlugField(max_length=180, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Основная техника"


class Artists(models.Model):
    name = models.CharField(verbose_name="Имя", max_length=300)
    surname = models.CharField(verbose_name="Фамилия", max_length=300)
    patronymic = models.CharField(verbose_name="Отчество", max_length=300,blank=True)
    image = models.ImageField(verbose_name="Изображение", upload_to="artists/")
    location = models.CharField(verbose_name="Адрес", max_length=450)
    technic_favorite = models.ManyToManyField(Technic, verbose_name="Основная техника художника")
    # technic_favorite_addition = models.ForeignKey(Technic, verbose_name="Основная техника художника", on_delete=models.SET_NULL,
    #                                      null=True, default=None)
    age = models.PositiveSmallIntegerField(verbose_name="Возраст")
    description = models.TextField(verbose_name='Биография',max_length=500)
    education = models.TextField(verbose_name='Образование',max_length=250)
    facebook = models.CharField(verbose_name="Facebook", max_length=300, blank=True)
    instagram = models.CharField(verbose_name="Instagram", max_length=300, blank=True)
    site = models.CharField(verbose_name="Сайт", max_length=200, blank=True)
    nft_platform = models.CharField(verbose_name="Платформа NFT", max_length=300, blank=True)
    phone = models.CharField(verbose_name="Номер телефона", max_length=22)

    def __str__(self):
        return self.surname

    def get_full_name(self):
        return self.surname + " " + self.name

    def get_absolute_url(self):
        return reverse('artist_detail', kwargs={"slug":self.surname})


    class Meta:
        verbose_name_plural = "Авторы"



    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Художники"


class Artworks(models.Model):
    name = models.CharField(verbose_name="Название работы", max_length=250)
    description = models.TextField(verbose_name='Описание')
    poster = models.ImageField(verbose_name="Изображение", upload_to="artworks/normal/")
    quality_image = models.ImageField(verbose_name="Изображение-HD", upload_to="artworks/hd/")
    year = models.PositiveSmallIntegerField(verbose_name="Год создания")
    country = models.ForeignKey("Country", verbose_name="Страна", on_delete=models.SET_NULL,null=True)
    location = models.CharField(verbose_name="Месонахождение предмета", max_length=350)
    artist = models.ForeignKey(Artists, verbose_name="Автор", related_name="artwork_artist",on_delete=models.SET_NULL,
                                          null=True) #изменил foreighnkey
    owner = models.CharField(verbose_name="Владелец", max_length=300, blank=True)
    # category_paint = models.ManyToManyField(Technic, verbose_name="Техника", related_name="artwork_technic")
    category = models.ManyToManyField(Category, verbose_name="Категория")
    price = models.PositiveIntegerField(verbose_name="Цена", help_text="Укажите сумму в рублях", default=0)
    in_sale = models.BooleanField(verbose_name="В продаже",default=False)
    signature = models.CharField(verbose_name="Идентификация автора", max_length=300, help_text="Как и где автор оставил свою подпись")
    certificate_of_auth = models.CharField(verbose_name="Подтверждение подлинности", max_length=300, blank=True, help_text="Проверка галереей")
    frame = models.BooleanField(verbose_name="Наличие рамки", default=False)
    size = models.CharField(verbose_name="Размер предмета", max_length=350)
    tags = models.CharField(verbose_name="Теги", max_length=350, default='')
    url = models.SlugField(max_length=180, unique=True)
    draft = models.BooleanField(verbose_name="Черновик", default=False)

    def __str__(self):
        return self.name

    def get_comment(self):
        return self.comment_set.filter(parent__isnull=True)

    def get_absolute_url(self):
        return reverse("artwork_detail", kwargs={"slug":self.url})

    class Meta:
        verbose_name = "Работа"
        verbose_name_plural = "Работы"

class Raitingstar(models.Model):
    value = models.SmallIntegerField(verbose_name="Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"] #Сортировка по значению

class Raiting(models.Model):
    ip = models.CharField("IP-адрес", max_length=15)
    star = models.ForeignKey(Raitingstar, on_delete=models.CASCADE, verbose_name="звезда")
    artworks = models.ForeignKey(Artworks, on_delete=models.CASCADE, verbose_name="работа")

    def __str__(self):
        return f"{self.star} - {self.artworks}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class Comment(models.Model):
    email = models.EmailField()
    name = models.CharField(verbose_name="Имя", max_length=100)
    text = models.TextField(verbose_name="Сообщение", max_length=5000)
    parent = models.ForeignKey("self", verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    artworks = models.ForeignKey(Artworks, verbose_name="Работа", on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

class Country(models.Model):
    label_ru = models.CharField(verbose_name="Название на русском", max_length=140)
    label_en = models.CharField(verbose_name="Название на английском", max_length=140)
    domain = models.CharField(verbose_name="Домен", max_length=10, blank=True, null=True)

    def __str__(self):
        return self.label_ru

    class Meta:
        verbose_name = "Страна"
        verbose_name_plural = "Страны"

class Event(models.Model):
    poster = models.ImageField(verbose_name="Изображение", upload_to="artworks/event/")
    text = models.CharField(verbose_name="Имя", max_length=1000)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Анонс события"
        verbose_name_plural = "Анонсы"

