from django.urls import include, re_path

urlpatterns = [
    re_path(r"^", include("pinax.blog.urls", namespace="pinax_blog")),
    re_path(r"^ajax/images/", include("pinax.images.urls", namespace="pinax_images")),
]
