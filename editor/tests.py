from django.test import TestCase

from rest_framework.test import APIRequestFactory
from django.urls import reverse

import json

from . import models
from . import viewset


reqFactory = APIRequestFactory()


class AuthorTest(TestCase):
    def test_receive(self):
        payload = 'not_existedUsername'

        req = reqFactory.get('')

        author_detail = viewset.AuthorViewset.as_view({'get': 'retrieve'})

        response = author_detail(req, pk=payload)

        self.assertEqual(response.status_code, 404)

    def test_create_new(self):
        payload = {
            'nick_name': 'test_user'
        }

        req = reqFactory.post('', data=payload)

        author_create = viewset.AuthorViewset.as_view({'post': 'create'})

        response = author_create(req)

        self.assertEqual(response.status_code, 201)
        self.assertTrue(models.Author.objects.filter(pk=response.data['id']).exists())
        self.assertTrue('id' in response.data)
        self.assertEqual(response.data['nick_name'], payload['nick_name'])

    def test_check_existing(self):
        payload = 'test_user'

        instance = models.Author(nick_name=payload)
        instance.save()

        req = reqFactory.get('')

        author_detail = viewset.UserViewset.as_view({'get': 'retrieve'})

        response = author_detail(req, nick_name=payload)

        self.assertEqual(response.status_code, 200)

    def test_create_with_long_name(self):
        payload = {
            'nick_name': 'a' * 41
        }
        req = reqFactory.post('', data=payload)

        author_create = viewset.AuthorViewset.as_view({'post': 'create'})

        response = author_create(req)

        self.assertEqual(response.status_code, 400)


class Editor(TestCase):
    @classmethod
    def setUpTestData(cls):
        nick_name = 'test_user'
        author = models.Author(nick_name=nick_name)
        author.save()

        cls.user = author

        cls.emptyDrawing = {
            "author": author.id,
            "title": "test example",
            "description": "some description",
            "data": {
                "file": "\n  CWRITER301151911312D                              "
                        "\nCreated with ChemWriter - http://chemwriter.com"
                        "\n  0  0  0  0  0  0  0  0  0  0999 V2000"
                        "\nM  END"
            }
        }

    def test_create(self):
        payload = self.emptyDrawing.copy()

        req = reqFactory.post('', data=payload, format='json')
        drawing_create = viewset.ViewDrawingViewset.as_view({'post': 'create'})
        response = drawing_create(req)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['author_name'], self.user.nick_name)
        self.assertTrue(models.Drawing.objects.filter(pk=response.data['id']).exists())
        self.assertTrue('file' in response.data['data'])

    def test_partial_filled_req(self):
        payload = self.emptyDrawing.copy()
        payload.pop('author')
        req = reqFactory.post('', data=payload, format='json')
        drawing_create = viewset.ViewDrawingViewset.as_view({'post': 'create'})
        response = drawing_create(req)

        self.assertEqual(response.status_code, 400)
        self.assertTrue('author' in response.data)

    def test_load_drawings(self):
        drawing_data = self.emptyDrawing.copy()
        drawing_data['author_id'] = drawing_data.pop('author')
        instance = models.Drawing(**drawing_data)
        instance.save()

        req = reqFactory.get('')
        drawing_detail = viewset.ViewDrawingViewset.as_view({'get': 'retrieve'})

        response = drawing_detail(req, pk=instance.id)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('title' in response.data)
        self.assertTrue('description' in response.data)
        self.assertTrue('author_name' in response.data)
        self.assertTrue('file' in response.data['data'])


# class Comment(TestCase):
#     def test_create_comment_partial_req(self):
#         pass
#
#     def test_create_comment(self):
#         pass
#
#     def test_create_comment_for_not_existed(self):
#         pass

