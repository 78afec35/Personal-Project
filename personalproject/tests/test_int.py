# Import the necessary modules
import unittest
from flask import url_for
from flask_testing import TestCase
# import the app's classes and objects
from personalproject import app, db, models, forms, bcrypt
from personalproject.models import User, Post
from personalproject.forms import RegistrationForm, LoginForm, UpdateAccount, PostForm
# Create the base class
class TestBase(unittest.TestCase):

    def create_app(self):

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
                SECRET_KEY='TEST_SECRET_KEY',
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # Create table
        db.create_all()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class Tests(TestBase):
    
    def test_register(self):
        tester=app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertEqual(response.status_code,200)

    def test_register_functionality_gooddata(self):
        tester=app.test_client(self)
        response = tester.post('/register', data=dict(username="Admin1",
            email="testadmin@testadmin.com",
            password="passwordpassword",
            confirm_password="passwordpassword"), follow_redirects = True)
        self.assertIn(b'Login', response.data)

    def test_register_functionality_baddata(self):
        tester=app.test_client(self)
        response = tester.post('/register', data=dict(username="Adm", email="testadmin",password="password", confirm_password="passwordword"), follow_redirects = True)
        self.assertIn(b'Register', response.data)

    def test_login(self):
        tester=app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code,200)

    def test_login_fuctionality_baddata(self):
        tester=app.test_client(self)
        response = tester.post('/login', data=dict(email="testa=min@testadmin.com",password="passw0assword", remember=True), follow_redirects = True)
        self.assertIn(b'Login', response.data)


    def test_login_fuctionality_gooddata(self):
        tester=app.test_client(self)
        response = tester.post('/login', data=dict(email="testadmin@testadmin.com",password="passwordpassword", remember=True), follow_redirects = True)
        self.assertIn(b'Posts', response.data)


    
    def test_home(self):
        tester=app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code,200)
    
    def test_blog(self):
        tester=app.test_client(self)
        response = tester.get('/blog', content_type='html/text')
        self.assertEqual(response.status_code,200)
    
    def test_new_post(self):
        tester=app.test_client(self)
        response = tester.post('/new_post', data=dict(title="Testpost!",content="This is a test post!"), folow_redirects = True)
        self.assertIn(b'Testpost!', response.data)
    
    def test_blog_paginator(self):
        tester=app.test_client(self)
        response = tester.get('/blog?page=2', content_type='html/text')
        self.assertEqual(response.status_code,200)
    


if __name__ == '__main__':
    unittest.main()



# # Write a test class for testing that the home page loads but we are not able to run a get request for delete and update routes.
# class TestViews(TestBase):

#     def test_home_get(self):
#         response = self.client.get(url_for('home'))
#         self.assertEqual(response.status_code, 200)

# Test adding 
# class TestAdd(TestBase):
#     def test_add_post(self):
#         response = self.client.post(
#             url_for('home'),
#             data = dict(name="MrMan"),
#             follow_redirects=True
#         )
#         self.assertIn(b'MrMan',response.data)