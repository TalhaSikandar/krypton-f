# from django.contrib.auth.models import Group, User, Permission
# from django.contrib.contenttypes.models import ContentType
#
# # Create pre-defined groups for clarity (optional)
# kadmin_group, created = Group.objects.get_or_create(name="KAdmin")
# kmanager_group, created = Group.objects.get_or_create(name="KManager")
#
# # Assign permissions to groups based on their role
# from stores.models import Store
# def perm_stores():
#     content_type = ContentType.objects.get_for_model(Store)
#     store_permissions = Permission.objects.filter(content_type=content_type)
#
#     for perm in store_permissions:
#         if perm.codename == "view_store":
#             kadmin_group.permissions.add(perm)
#             kmanager_group.permissions.add(perm)
#         elif perm.codename == "change_store":
#             kadmin_group.permissions.add(perm)
#             kmanager_group.permissions.add(perm)
#         else:
#             kadmin_group.permissions.add(perm) # Gave no permission to the kmanager
#
#
# from warehouses.models import Warehouse
# def perm_warehouses():
#     content_type = ContentType.objects.get_for_model(Warehouse)
#     warehouse_permissions = Permission.objects.filter(content_type=content_type)
#
#     for perm in warehouse_permissions:
#         kadmin_group.permissions.add(perm) # Gave permissions to only Admin
#
#
# from raw_materials.models import Rawmaterial
# def perm_warehouses():
#     content_type = ContentType.objects.get_for_model(Rawmaterial)
#     rawmaterial_permissions = Permission.objects.filter(content_type=content_type)
#
#     for perm in rawmaterial_permissions:
#         kadmin_group.permissions.add(perm) # Gave permissions to only Admin
#
#
# # user = User.objects.get(username="test")
# # user.groups.add(author_group)  # Add the user to the Author group
# #
# # user = get_object_or_404(User, pk=user.id)
# #
# # print(user.has_perm("blog.delete_post")) # => False
# # print(user.has_perm("blog.change_post")) # => False
# # print(user.has_perm("blog.view_post")) # => True
# # print(user.has_perm("blog.add_post")) # => True
