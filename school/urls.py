from django.urls import path
from rest_framework.routers import DefaultRouter
from school.apps import SchoolConfig
from school.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, PaymentCreateAPIView, PaymentUpdateAPIView, PaymentDestroyAPIView, \
    PaymentRetrieveAPIView, PaymentListAPIView

app_name = SchoolConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
    path('lesson/list/', LessonListAPIView.as_view(), name='lesson_list'),
    path('lesson/detail/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
    path('lesson/update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
    path('lesson/destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
]

urlpatterns += [
    path('lesson/payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('lesson/payment/list/', PaymentListAPIView.as_view(), name='payment_list'),
    path('lesson/payment/detail/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payment_detail'),
    path('lesson/payment/update/<int:pk>/', PaymentUpdateAPIView.as_view(), name='payment_update'),
    path('lesson/payment/destroy/<int:pk>/', PaymentDestroyAPIView.as_view(), name='payment_destroy'),

]

urlpatterns += router.urls
