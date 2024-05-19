from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#
# class CustomUserManager(BaseUserManager):
#     def create_user(self, username, password=None, **extra_fields):
#         if not username:
#             raise ValueError('The Username field must be set')
#         user = self.model(username=username, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, username, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#
#         return self.create_user(username, password, **extra_fields)
#
# class CustomUser(AbstractBaseUser):
#     username = models.CharField(max_length=150, unique=True)
#     address = models.CharField(max_length=255)
#     company_code = models.CharField(max_length=10, unique=True)
#
#     objects = CustomUserManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['address', 'company_code']
#
#     def __str__(self):
#         return self.username
#

from django.contrib.auth.models import AbstractUser
from companies.models import Company

class CustomUser(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True, help_text="Your Company", related_name="users")
    profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True, null=True) #needs pillow to work
    USERNAME_FIELD = 'email'

    ADMIN = 1
    MANAGER = 2
    class Types(models.TextChoices):
            ADMIN = "ADMIN", "Admin"
            MANAGER = "MANAGER", "Manager"
    role = models.CharField(default=Types.MANAGER, max_length=10, choices=Types.choices, blank=False, null=False, help_text="Your role in the Company")
    # REQUIRED_FIELDS = ['user_name', 'company_code', 'role']
    REQUIRED_FIELDS = ['username', 'role']
    # REQUIRED_FIELDS = ['role']

    def get_profile_picture(self):
        if self.profile_picture:
            self.profile_picture = self.make_profile_picture(self.profile_picture)
            return 'http://127.0.0.1:8000' + self.profile_picture.url
        return ''

    def make_profile_picture(self, image, size=(150, 150)):
        """
        Resizes and converts the profile picture to RGB format for consistency.

        Args:
            image: The profile picture as a Django File object or a file path string.
            size: The desired size of the resized image as a tuple (width, height).

        Returns:
            A BytesIO object containing the resized and converted image data.
        """
        from PIL import Image
        from io import BytesIO
        try:
            # Handle Django File objects and file paths
            if hasattr(image, 'read'):  # Check if it's a Django File object
                image_data = image.read()
            else:
                with open(image, 'rb') as f:
                    image_data = f.read()

            # Open the image using Pillow
            pp = Image.open(BytesIO(image_data))

            # Convert to RGB mode (optional, but recommended for consistency)
            pp = pp.convert('RGB')

            # Resize the image
            pp.thumbnail(size, Image.ANTIALIAS)  # Use ANTIALIAS for smoother resizing

            # Create a BytesIO object to store the resized image data
            output = BytesIO()
            pp.save(output, format='JPEG')  # Save as JPEG by default
            output.seek(0)

            return output

        except Exception as e:
            print(f"Error processing profile picture: {e}")
            return None  # Or return a default image path/data if desired

        def get_absolute_url(self):
            """Returns the URL to access a particular instance of MyModelName."""
            return reverse('model-detail-view', args=[str(self.id)])
