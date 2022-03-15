from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    weight = models.FloatField()
    price = models.PositiveIntegerField()
    is_stock = models.BooleanField(default=True)
    valid_until = models.DateField()
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    @property
    def filtered_reviews(self):
        return self.reviews.filter(stars__gte=4)

    @property
    def reviews_count(self):
        return self.reviews.filtered_reviews.count()

    @property
    def rating(self):
        reviews = self.filtered_reviews
        count = reviews.count()
        # if count == 0:
        #     return 0
        sum_ = 0
        for i in reviews:
            sum_ += i.stars
        try:
            return sum_ / count
        except ZeroDivisionError:
            return 0


CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
)


class Review(models.Model):
    text = models.TextField()
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True,
                                related_name='reviews')
    stars = models.IntegerField(default=1, choices=CHOICES)

    def __str__(self):
        return self.text
