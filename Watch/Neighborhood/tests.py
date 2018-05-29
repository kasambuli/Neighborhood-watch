from django.test import TestCase
from .models import UserProfile,Business,Neighborhood

# Create your tests here.
class UserProfileTestClass(TestCase):
    '''
    Test case for the UserProfile class
    '''

    def setUp(self):
        '''
        Method that creates an instance of UserProfile class
        '''
        # Create a profile instance
        self.new_profile = UserProfile(name = 'flower',identification='35305834',location = 'Nairobi',avatar = 'avatar.jpeg')

    def test_instance(self):
        '''
        Test case to check if self.new_profile in an instance of UserProfile class
        '''
        self.assertTrue(isinstance(self.new_profile, UserProfile))

    def update_profile(self):
        '''
        Test case to update a user's profile
        '''
        self.new_profile.save_profile()
        profile_id = self.new_profile.id
        UserProfile.update_profile(id,"test")
        self.assertEqual(self.caption.caption,"test")

    def test_delete_profile(self):
        '''
        Test case to delete user profile
        '''
        self.profile.save_profile()
        self.profile.delete_profile()
        profiles = UserProfile.objects.all()
        self.assertTrue(len(profiles) == 0)

   
class NeighborhoodTestCase(TestCase):
    '''
    Test case for the Neighborhood class
    '''

    def setUp(self):
        '''
        Method that creates an instance of Neighborhood class
        '''
        # Create instance of Neighborhood class
        self.new_neighborhood = Neighborhood(name = 'miambani',location = 'Nairobi',occupant_count=1)

    def test_instance(self):
        '''
        Test case to check if self.new_neighborhood in an instance of Neighborhood class
        '''
        self.assertTrue(isinstance(self.new_neighborhood, Neighborhood))

    
    def test_update_neighborhood(self):
        '''
        Test case to update neighborhood details
        '''
        self.new_neighborhood.save_neighborhood()
        neighborhood_id = self.new_neighborhood.id
        Neighborhood.update_neighborhood(id, "test")
        self.assertEqual(self.neighborhood.neighborhood,"test")

    def test_delete_neighborhood(self):
        ''''
        Test to delete a neighborhood
        '''
        self.neighborhood.save_neighborhood()
        self.neighborhood.delete_neighborhood()
        hoods = Neighborhood.objects.all()
        self.assertTrue(len(hoods) == 0)

class BusinessTestCase(TestCase):
    '''
    Test case for the Business class
    '''

    def setUp(self):
        '''
        Method that creates an instance of Business class
        '''
        # Create a Business instance
        self.new_business = Business(name ='test',email = 'test@ms.com')

    def test_instance(self):
        '''
        Test case to check if self.new_business in an instance of Business class
        '''
        self.assertTrue(isinstance(self.new_business, Business))

    def test_update_business(self):
        '''
        Test case to update name of a business
        '''
        self.new_business.save_business()
        business_id = self.new_business.id
        Business.update_business(id, "test")
        self.assertEqual(self.business.business, "test")


    def test_delete_business(self):
        ''''
        Test to delete a business in an image
        '''
        self.business.save_business()
        self.business.delete_business()
        business = Business.objects.all()
        self.assertTrue(len(business) == 0)
