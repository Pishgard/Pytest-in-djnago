from product.models import Category, Product
import pytest


def test_create_category(db):
    category = Category.objects.create(name="اپل")
    assert category.name == "اپل"


def test_update_category(db):
    category = Category.objects.create(name="اپل")
    category.name = "سامسونگ"
    category.save()
    category_from_db = Category.objects.get(name="سامسونگ")
    assert category_from_db.name == "سامسونگ"

##########################################################################################


@pytest.fixture
def category(db) -> Category:
    return Category.objects.create(name="موبایل")


def test_filter_category(category):
    assert Category.objects.filter(name="موبایل").exists()


def test_update_category2(category):
    category.name = "تبلت"
    category.save()
    category_from_db = Category.objects.get(name="تبلت")
    assert category_from_db.name == "تبلت"

##############################################################################################


@pytest.mark.django_db
def test_product_price():
    products = Product.objects.all()
    for product in products:
        assert product.price > 0