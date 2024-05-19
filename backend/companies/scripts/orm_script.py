import os
import django

# project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
# os.chdir(project_path)
# print(project_path)
# # Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")  # Replace 'your_project_name' with the actual name of your project
django.setup()

from companies.models import Company

# Create company instances
dell = Company.objects.create(company_name="Dell")
lenovo = Company.objects.create(company_name="Lenovo")
asus = Company.objects.create(company_name="ASUS")
hp = Company.objects.create(company_name="HP")

from accounts.models import CustomUser

user1 = CustomUser.objects.create_user(email="ali@krypton.com", username="ali", password="krypton", company=dell, role=CustomUser.Types.ADMIN)
user1 = CustomUser.objects.create_user(email="talha@krypton.com", username="talha", password="krypton", company=lenovo, role=CustomUser.Types.ADMIN)
user1 = CustomUser.objects.create_user(email="aizaz@krypton.com", username="aizaz", password="krypton", company=asus, role=CustomUser.Types.ADMIN)
user1 = CustomUser.objects.create_user(email="mahnoor@krypton.com", username="mahnoor", password="krypton", company=hp, role=CustomUser.Types.ADMIN)

from stores.models import Store

store1 = Store.objects.create(company=dell)
store1 = Store.objects.create(company=asus)
store1 = Store.objects.create(company=hp)
store1 = Store.objects.create(company=lenovo)



print("Companies created successfully!")
