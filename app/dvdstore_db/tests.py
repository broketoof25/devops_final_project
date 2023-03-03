from django.test import TestCase
from django.urls import reverse
from dvdstore_db.models import Movies
import pytest
# Create your tests here.
def test_homepage_access():
    url = reverse('home')
    assert url == "/"


