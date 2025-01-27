from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import ( HomePageView, AboutPageView, ContactPageView, CategoryListView, CategoryDetailView, CategoryCreateView, CategoryUpdateView, CategoryDeleteView,
    PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView,
    CommentListView, CommentDetailView, CommentCreateView, CommentUpdateView, CommentDeleteView,
    AlertListView, AlertDetailView, AlertCreateView, AlertUpdateView, AlertDeleteView,

)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),

    # Category URLs
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    # Post URLs
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/create/', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Comment URLs
    path('comments/', CommentListView.as_view(), name='comment_list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    path('comments/<int:pk>/detail/', CommentDetailView.as_view(), name='comment_detail'),
    path('comments/create/<int:pk>/', CommentCreateView.as_view(), name='comment_create'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),

    # Alert URLs
    path('alerts/', AlertListView.as_view(), name='alert_list'),
    path('alerts/<int:pk>/', AlertDetailView.as_view(), name='alert_detail'),
    path('alerts/create/', AlertCreateView.as_view(), name='alert_create'),
    path('alerts/<int:pk>/update/', AlertUpdateView.as_view(), name='alert_update'),
    path('alerts/<int:pk>/delete/', AlertDeleteView.as_view(), name='alert_delete'),

    # account_profile URLs

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)