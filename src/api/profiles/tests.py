from os.path import abspath, join, dirname
from shutil import rmtree
from tempfile import mkdtemp

from django.core.files.storage import FileSystemStorage
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.test.utils import override_settings

from rest_framework.test import APITestCase

from .models import Project

User = get_user_model()


class ProfileProjectsTestCase(APITestCase):
    def setUp(self):
        self.photo_path = join(abspath(dirname(__file__)), 'test-photo.png')

        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

        p = Project(profile=user.profile, description='non-awesome project')
        p.save()
        self.project_to_update = Project.objects.get(description='non-awesome project')

        logged_in = self.client.login(username='testuser', password='12345')
        
        self.media_folder = mkdtemp()
        

    def tearDown(self):
        rmtree(self.media_folder)

    def test_post_project(self):
        with open(self.photo_path, 'rb') as photo:
            project_payload = {
            'description': 'awesome project here',
            'photo': photo,
            'github_link': 'https://github.com/coretabs-academy/awesome-project',
            'live_demo_link': 'https://github.com/coretabs-academy/demo-link'
            }

            with override_settings(MEDIA_ROOT=self.media_folder):
                response = self.client.post(reverse('my_profile_projects'), project_payload, format='multipart')
                self.assertEqual(response.status_code, 201)

    def test_put_project(self):
        with open(self.photo_path, 'rb') as photo:
            project_payload = {
            'description': 'awesome project here',
            'photo': photo,
            'github_link': 'https://github.com/coretabs-academy/awesome-project',
            'live_demo_link': 'https://github.com/coretabs-academy/demo-link'
            }
            import json
            with override_settings(MEDIA_ROOT=self.media_folder):
                response = self.client.patch(reverse('my_profile_projects_update_delete', args=(self.project_to_update.id,)), 
                                             project_payload,
                                             format='multipart')
                self.assertEqual(response.status_code, 200)
                self.assertEqual(Project.objects.get(id=self.project_to_update.id).description, 'awesome project here')

    def test_delete_project(self):
        response = self.client.delete(reverse('my_profile_projects_update_delete', args=(self.project_to_update.id,)))
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Project.objects.filter(id=self.project_to_update.id).first(), None)