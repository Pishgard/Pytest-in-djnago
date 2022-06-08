from django.db import models


class Category(models.Model):
    name = models.CharField('نام دسته بندی', max_length=128, unique=True)

    created_at = models.DateTimeField('زمان ساخت', auto_now_add=True)
    updated_at = models.DateTimeField('تاریخ بروزرسانی', auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Product(models.Model):
    name = models.CharField('نام', max_length=10)
    description = models.TextField('توضیحات', blank=True)
    price = models.IntegerField('قیمت', default=0)
    image = models.ImageField('عکس', upload_to='product/%Y/%m/%d', null=True, blank=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE, blank=True, null=True,
                                 verbose_name='دسته بندی')

    created_at = models.DateTimeField('زمان ساخت', auto_now_add=True)
    updated_at = models.DateTimeField('تاریخ بروزرسانی', auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'