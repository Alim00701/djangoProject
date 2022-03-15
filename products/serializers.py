from rest_framework import serializers
from products.models import Product, Brand, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text stars'.split()


class BrandSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = 'id name'.split()


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializers()
    # reviews = ReviewSerializer(many=True)
    reviews = serializers.SerializerMethodField()
    # reviews_count = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = 'id title price brand reviews_count rating'.split()

    def get_reviews(self, product):
        return ReviewSerializer(product.filtered_reviews, many=True).data

    # def get_reviews_count(self, product):
    #     return product.reviews.filter(stars__gte=4).count()
