from django.urls import path
from sampleapp import views

urlpatterns=[
    path("",views.home,name="home"),
    path("studentregister",views.studentregister,name="studentregister"),
    path("teacherregister",views.teacherregister,name="teacherregister"),
    path("logins",views.logins,name="logins"),
    path("adminhome",views.adminhome,name="adminhome"),
    path("teacherhome",views.teacherhome,name="teacherhome"),
    path("studenthome",views.studenthome,name="studenthome"),
    path("view_student_admin",views.view_student_admin,name="view_student_admin"),
    path("view_teacher",views.view_teacher,name="view_teacher"),
    path("logouts",views.logouts,name="logouts"),
    path("updateteacher/<int:id>",views.updateteacher,name="updateteacher"),
    path("editteacher",views.editteacher,name="editteacher"),
    path("tdelete/<int:id>",views.tdelete,name="tdelete"),
    path("delete/<int:id>",views.delete,name="delete"),
    path("view_student_teacher",views.view_student_teacher,name="view_student_teacher"),
    path("approve_student/<int:id>",views.approve_student,name="approve_student"),
    path("editstudent",views.editstudent,name="editstudent"),
    path("view_student",views.view_student,name="view_student"),
    path("updatestudent/<int:id>",views.updatestudent,name="updatestudent"),
   
    path("Trainercreate/create/",views.Trainercreate.as_view(),name="Trainercreate"),
    path("Trainercreate/",views.Trainerlist.as_view(),name="Trainerlist"),
    path("Trainercreate/<int:pk>",views.Trainerdetail.as_view(),name="trainerdetail"),
    path("Trainercreate/<int:pk>/update",views.Trainerupdate.as_view(),name="trainerupdate"),
    path("Trainercreate/<int:pk>/delete",views.Trainerdelete.as_view(),name="trainerdelete"),
    
    path('Bookss/create/',views.book_create_view,name="book_create_view"),
    path('Bookss/',views.book_list_view,name="book_list"),
    path('Bookss/<int:pk>',views.book_detail_view,name="book_detail"),
    path('Bookss/<int:pk>/update',views.book_update_view,name="book_update"),
    path('Bookss/<int:pk>/delete',views.book_delete_view,name="book_delete"),
    path("index",views.index,name="index"),
    # path()
]