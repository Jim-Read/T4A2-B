import unittest                                                        
from main import create_app, db                                        
from models.Users import Users
                              

class TestProfiles(unittest.TestCase):                                     
    @classmethod
    def setUp(cls):                                                     
        cls.app = create_app()                                          
        cls.app_context = cls.app.app_context()                         
        cls.app_context.push()                                          
        cls.client = cls.app.test_client()                              
        db.create_all()                                                 
        runner = cls.app.test_cli_runner()
        runner.invoke(args=["db-custom", "seed"])                       

    @classmethod                                                        
    def tearDown(cls):                                                  
        db.session.remove()                                             
        db.drop_all()                                                   
        cls.app_context.pop()                                           

   
    def test_register_page(self):
        response = self.client.get("/signup")

        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)

    def test_login_page(self):
        response = self.client.get("/login")

        self.assertEqual(response.status_code, 200)