from django.db import models


class Products(models.Model):
    title = models.CharField("Название товара", max_length=17)
    img = models.ImageField("Фото", upload_to='products')
    description = models.CharField("Описание", blank=True, max_length=250)
    price = models.CharField("Цена", max_length=5)
    sale = models.CharField("Акция(если нет - оставить по умолчанию)", max_length=3, default="Нет")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
