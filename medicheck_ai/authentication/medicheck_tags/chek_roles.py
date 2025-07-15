# # your_app/templatetags/check_role.py

# from django import template

# register = template.Library()

# @register.simple_tag
# def user_role_checking(request, roles):
#     """
#     Usage: {% user_role_checking request 'Admin,Doctor' as allow %}
#     """
#     if request.user.is_authenticated:
#         allowed_roles = [r.strip() for r in roles.split(',')]
#         return request.user.role in allowed_roles
#     return False
